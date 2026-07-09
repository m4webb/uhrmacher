#!/usr/bin/env python3
"""State-space verification for the winding room counterweight puzzle (v2, pull-chains).

Model: four 3-wide counterweights at two levels (rows E and I); each pokes into its outer
lane ('out') or the shared middle ('mid'); both weights of a level cannot be 'mid'
(jam). Chains are reusable, one per weight per direction, pulling costs an action.

Party analysis uses an occupancy abstraction (8 players ~ unlimited tokens).
Pair analysis (P7) is an exact two-actor search: Fritz and the golem are two
ordinary actors — both walk, both pull chains. No slips, no shoves, nothing special.

If the current arrangement fails P7, a placement search runs automatically.
"""
from collections import deque
from itertools import permutations

# --- Static layout: 9 cols x rows A..N ---
ROWS = "ABCDEFGHIJKLMN"
base = set()
for c in range(3, 8): base.add(f"N{c}")
for c in range(2, 9): base.add(f"M{c}")
for r in "DEFGHIJKL":
    for c in (2, 5, 8): base.add(f"{r}{c}")
base |= {"J3", "J4", "G6", "G7"}
for c in range(2, 6): base.add(f"C{c}")                    # backroom, bottom row
base.add("C8")                                             # east approach
for c in range(2, 6): base.add(f"A{c}"); base.add(f"B{c}") # backroom 4x3 (cols 2-5)
base |= {"A7", "B7", "A8", "B8"}                           # Fritz's corner (2x2 home)
START, GOAL, FRITZ, GOLEM = "N5", "A4", "A7", "G8"

LANE_CELL = {
    "Uw": {"out": "E2", "mid": "E5"}, "Ue": {"out": "E8", "mid": "E5"},
    "Lw": {"out": "I2", "mid": "I5"}, "Le": {"out": "I8", "mid": "I5"},
}
PARTNER = {"Uw": "Ue", "Ue": "Uw", "Lw": "Le", "Le": "Lw"}
ORDER = ("Uw", "Ue", "Lw", "Le")
INIT = ("out", "mid", "mid", "out")     # upper open EAST, lower open WEST
PARADE = ("mid", "out", "mid", "out")   # both levels open WEST (golem-seal config)

# --- Current chain arrangement: square -> (gear, direction) ---
CHAINS = {
    "G2": ("Lw", "out"), "G6": ("Lw", "mid"),
    "M3": ("Le", "mid"), "K2": ("Le", "out"),
    "B4": ("Uw", "mid"), "C3": ("Uw", "out"),
    "L2": ("Ue", "mid"), "C8": ("Ue", "out"),
}

def covered(cfg):
    return {LANE_CELL[g][p] for g, p in zip(ORDER, cfg)}

def walkable(cfg):
    return base - covered(cfg)

def neighbors(cell, w):
    r, c = cell[0], int(cell[1])
    for rr, cc in ((chr(ord(r)+1), c), (chr(ord(r)-1), c), (r, c+1), (r, c-1)):
        n = f"{rr}{cc}"
        if n in w: yield n

def closure(cells, w):
    seen = {c for c in cells if c in w}
    q = deque(seen)
    while q:
        for n in neighbors(q.popleft(), w):
            if n not in seen: seen.add(n); q.append(n)
    return frozenset(seen)

def pull(cfg, gear, direction):
    i = ORDER.index(gear)
    pos = cfg[i]
    if direction == "mid":
        if pos == "mid": return None
        if cfg[ORDER.index(PARTNER[gear])] == "mid": return None  # jam
        return cfg[:i] + ("mid",) + cfg[i+1:]
    if pos == "out": return None
    return cfg[:i] + ("out",) + cfg[i+1:]

# --- Party exploration (occupancy abstraction) ---
def explore(chains):
    w0 = walkable(INIT)
    occ0 = closure({START}, w0)
    start = (INIT, occ0)
    seen, paths, edges, pockets = {start}, {start: []}, {}, []
    q = deque([start])
    while q:
        state = q.popleft()
        cfg, occ = state
        succs = []
        for sq, (g, d) in chains.items():
            if sq not in occ: continue
            nc = pull(cfg, g, d)
            if nc is None: continue
            w = walkable(nc)
            nocc = closure(occ, w)
            main = closure({START}, w)
            stray = [c for c in nocc if c not in main]
            if stray: pockets.append((paths[state] + [sq], sorted(stray)[:4]))
            ns = (nc, nocc)
            succs.append(ns)
            if ns not in seen:
                seen.add(ns); paths[ns] = paths[state] + [sq]; q.append(ns)
        edges[state] = succs
    success = {s for s in seen if GOAL in s[1]}
    rev = {s: [] for s in seen}
    for s, outs in edges.items():
        for t in outs: rev[t].append(s)
    can_win = set(success)
    q = deque(success)
    while q:
        for p in rev[q.popleft()]:
            if p not in can_win: can_win.add(p); q.append(p)
    return dict(
        seen=seen, paths=paths, occ0=occ0, success=success,
        doomed=seen - can_win, pockets=pockets,
        min_win=min((paths[s] for s in success), key=len, default=None),
        parade=[paths[s] for s in seen if s[0] == PARADE and GOAL in s[1]],
    )

def first_effective(chains):
    occ0 = closure({START}, walkable(INIT))
    return sorted(sq for sq, (g, d) in chains.items()
                  if sq in occ0 and pull(INIT, g, d) is not None)

# --- P7: exact two-actor search. Two ordinary actors: both walk, both pull.
#     State carries an 'out' flag (set once both stand outside simultaneously)
#     so the same search answers both escape and full round-trip questions. ---
def _pair_search(chains, goal_fn, want_path=False):
    Wc, Mc = {}, {}
    def wm(cfg):
        if cfg not in Wc:
            Wc[cfg] = walkable(cfg)
            Mc[cfg] = closure({START}, Wc[cfg])
        return Wc[cfg], Mc[cfg]
    def canon(cfg, a, b, out):
        return (cfg, a, b, out) if a <= b else (cfg, b, a, out)
    start = canon(INIT, FRITZ, GOLEM, False)
    seen = {start}
    parent = {start: (None, None)}
    q = deque([start])
    while q:
        state = q.popleft()
        cfg, a, b, out = state
        w, main = wm(cfg)
        if goal_fn(cfg, a, b, out):
            if not want_path:
                return True
            pulls = []
            s = state
            while parent[s][0] is not None:
                s, ev = parent[s][0], parent[s][1]
                if ev: pulls.append(ev)
            return list(reversed(pulls))
        moves = []
        for me, other in ((a, b), (b, a)):
            for n in neighbors(me, w):
                moves.append((cfg, n, other, None))
            if me in chains:
                nc = pull(cfg, *chains[me])
                if nc is not None:
                    nw, _ = wm(nc)
                    oth = other
                    if oth not in nw:  # weight slid onto the other actor: step aside
                        opts = sorted(neighbors(oth, nw))
                        oth = opts[0] if opts else None
                    if oth is not None:
                        g, d = chains[me]
                        moves.append((nc, me, oth, f"{me} pulls {g}->{d}"))
        for ncfg, na, nb, ev in moves:
            _, nmain = wm(ncfg)
            nout = out or (na in nmain and nb in nmain)
            s = canon(ncfg, na, nb, nout)
            if s not in seen:
                seen.add(s)
                parent[s] = ((cfg, a, b, out) if (cfg, a, b, out) == canon(cfg, a, b, out)
                             else canon(cfg, a, b, out), ev)
                q.append(s)
    return None if want_path else False

def pair_out(chains, want_path=False):
    return _pair_search(chains, lambda cfg, a, b, out: out, want_path)

# P7b: full round trip — leave (both outside at once), then come home:
# maze back to the exact starting config with the pair at their start cells
def pair_roundtrip(chains, want_path=False):
    return _pair_search(chains,
                        lambda cfg, a, b, out: out and cfg == INIT and {a, b} == {FRITZ, GOLEM},
                        want_path)

def evaluate(chains, with_p7=True):
    fe = first_effective(chains)
    exp = explore(chains)
    w1 = walkable(pull(INIT, *chains[fe[0]])) if fe else None
    wp = walkable(PARADE)
    golem0 = closure({GOLEM}, walkable(INIT))
    res = dict(
        fe=fe, exp=exp,
        p1=(len(fe) == 1),
        p2=golem0.isdisjoint(exp["occ0"]),
        p2_guard=sorted(sq for sq in chains if sq in golem0),
        p3=(fe and fe[0] not in closure({START}, w1)),
        p4=(fe and not closure({GOLEM}, w1).isdisjoint(closure({START}, w1))),
        p5=bool(exp["parade"]),
        p5_seal=closure({GOLEM}, wp).isdisjoint(closure({START}, wp)),
        p7=pair_out(chains) if with_p7 else None,
    )
    res["p6"] = {}
    for gear in ORDER:
        sqs = [sq for sq, (g, d) in chains.items() if g == gear]
        res["p6"][gear] = not all(sq not in closure({START}, wp) for sq in sqs)
    return res

# --- Report for the current arrangement ---
r = evaluate(CHAINS)
exp = r["exp"]
print(f"explored states: {len(exp['seen'])}")
print(f"1. sealed at start: {GOAL not in exp['occ0']}")
print(f"2. minimum pulls to open a route: {exp['min_win'] and len(exp['min_win'])} via {exp['min_win']}")
print(f"3. doomed states: {len(exp['doomed'])}")
print(f"4. pocket events (recoverable): {len(exp['pockets'])}")
print("--- placement principles ---")
print(f"P1 unique effective first pull: {r['p1']} {r['fe']}")
print(f"P2 golem starts sealed away from party: {r['p2']} (cage guards chains: {r['p2_guard']})")
print(f"P3 first pull traps the puller: {r['p3']}")
print(f"P4 first pull releases the golem: {r['p4']}")
print(f"P5 parade reachable: {r['p5']}; parade seals golem: {r['p5_seal']}")
for gear, ok in r["p6"].items():
    print(f"P6 {gear} chains separated: {'ok' if ok else 'VIOLATION'}")
print(f"P7 Fritz+golem walk out in tandem (chains only, no cheats): {r['p7']}")
if r["p7"]:
    print(f"P7b full round trip (out, home again, maze re-armed to start): {pair_roundtrip(CHAINS)}")
    print(f"    escape pulls: {pair_out(CHAINS, want_path=True)}")

# --- Search: if P7 or the full round trip (P7b) fails, look for arrangements
#     that satisfy EVERYTHING. Beat-critical chains stay fixed (G2 first-pull
#     trap, C8 Fritz self-seal, M3/K2 lower-east pair); the other four move. ---
if not (r["p7"] and pair_roundtrip(CHAINS)):
    print("\n--- searching chain placements for escape + full round trip ---")
    FIXED = {"G2": ("Lw", "out"), "C8": ("Ue", "out"),
             "M3": ("Le", "mid"), "K2": ("Le", "out")}
    ROLES = [("Lw", "mid"), ("Ue", "mid"), ("Uw", "mid"), ("Uw", "out")]
    SPOTS = ["H5", "H8", "G7", "B2", "B4", "C3", "C5", "A8", "L2", "K8", "M7"]
    GEAR_ROW = {"Uw": "E", "Ue": "E", "Lw": "I", "Le": "I"}
    current_pos = {v: sq for sq, v in CHAINS.items()}
    solutions = []
    for combo in permutations(SPOTS, 4):
        if any(abs(ord(sq[0]) - ord(GEAR_ROW[role[0]])) < 2
               for sq, role in zip(combo, ROLES)):
            continue  # never right next to its own gear
        chains = dict(FIXED)
        for sq, role in zip(combo, ROLES):
            chains[sq] = role
        if len(chains) != 8: continue
        if first_effective(chains) != ["G2"]: continue
        e = evaluate(chains, with_p7=False)   # cheap criteria first
        if not (e["p1"] and e["p2"] and e["p3"] and e["p4"] and e["p5"]
                and e["p5_seal"] and all(e["p6"].values())): continue
        if e["exp"]["doomed"]: continue
        if e["exp"]["min_win"] is None: continue
        if not pair_out(chains): continue
        if not pair_roundtrip(chains): continue
        moved = sum(1 for sq, role in zip(combo, ROLES) if current_pos[role] != sq)
        solutions.append((moved, combo, chains))
    solutions.sort(key=lambda s: s[0])
    print(f"arrangements satisfying ALL criteria (incl. P7 + full round trip): {len(solutions)}")
    for moved, combo, _ in solutions[:8]:
        desc = ", ".join(f"{role[0]}->{role[1]}@{sq}" for role, sq in zip(ROLES, combo))
        print(f"  moved {moved} chains: {desc}")
    if solutions:
        best = solutions[0]
        print(f"\nbest candidate ({best[0]} chain(s) moved):")
        print(f"  escape pulls:     {pair_out(best[2], want_path=True)}")
        print(f"  round-trip pulls: {pair_roundtrip(best[2], want_path=True)}")

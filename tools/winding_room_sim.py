#!/usr/bin/env python3
"""State-space verification for the winding room counterweight puzzle (v3, six weights).

Model: six cast-iron PINECONE counterweights (3x3 footprint), one hanging above
each berth (E2/E5/E8 upper, I2/I5/I8 lower). At any moment exactly two per level
are down — four pinecones on the map, never more. Each pull-chain transfers load
between two berths of one level: the weight over one berth descends, the weight
over the other rises. A pull whose descending berth is already down grinds (jam).
Chains are reusable, one per berth-pair per direction, pulling costs an action.

(State-equivalent to the earlier four-traveling-weight model — states and pulls
map 1:1, so all previously verified properties carry over unchanged.)

Party analysis uses an occupancy abstraction (7 players ~ unlimited tokens).
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
base |= {"K3", "K4", "G6", "G7"}
for c in range(2, 6): base.add(f"C{c}")                    # backroom, bottom row
base.add("C8")                                             # east approach
for c in range(2, 6): base.add(f"A{c}"); base.add(f"B{c}") # backroom 4x3 (cols 2-5)
base |= {"A7", "B7", "A8", "B8"}                           # Fritz's corner (2x2 home)
START, GOAL, FRITZ, GOLEM = "N5", "A4", "A7", "G8"

BERTHS = ("E2", "E5", "E8", "I2", "I5", "I8")   # a weight hangs above each
INIT   = frozenset({"E2", "E5", "I5", "I8"})    # down at start: upper open EAST, lower open WEST
PARADE = frozenset({"E5", "E8", "I5", "I8"})    # both levels open WEST (golem-seal config)

# --- Current chain arrangement: square -> (descends onto, rises from) ---
CHAINS = {
    "G2": ("I2", "I5"), "G6": ("I5", "I2"),
    "M3": ("I5", "I8"), "K2": ("I8", "I5"),
    "B4": ("E5", "E2"), "C3": ("E2", "E5"),
    "L2": ("E5", "E8"), "C8": ("E8", "E5"),
}

def covered(cfg):
    # Each DOWN weight buries a 3x3 footprint centered on its berth.
    cells = set()
    for berth in cfg:
        r0, c0 = ROWS.index(berth[0]), int(berth[1])
        for dr in (-1, 0, 1):
            for dc in (-1, 0, 1):
                rr, cc = r0 + dr, c0 + dc
                if 0 <= rr < len(ROWS) and 1 <= cc <= 9:
                    cells.add(f"{ROWS[rr]}{cc}")
    return cells

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

def pull(cfg, dn, up):
    # Lower the weight over `dn`, raise the weight over `up`.
    # Grinds (None) if the descending berth is already down or the rising
    # berth is already up — the load has nowhere to transfer.
    if dn in cfg or up not in cfg: return None
    return frozenset(cfg - {up} | {dn})

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
        for sq, (dn, up) in chains.items():
            if sq not in occ: continue
            nc = pull(cfg, dn, up)
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
    return sorted(sq for sq, (dn, up) in chains.items()
                  if sq in occ0 and pull(INIT, dn, up) is not None)

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
                    if oth not in nw:  # weight descended onto the other actor: step aside
                        opts = sorted(neighbors(oth, nw))
                        oth = opts[0] if opts else None
                    if oth is not None:
                        dn, up = chains[me]
                        moves.append((nc, me, oth, f"{me} pulls (down {dn}, up {up})"))
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

def chain_pairs(chains):
    # Chains grouped by the berth-pair they operate (each pair has 2 chains,
    # one per direction).
    groups = {}
    for sq, (dn, up) in chains.items():
        groups.setdefault(frozenset((dn, up)), []).append(sq)
    return groups

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
    for pair, sqs in chain_pairs(chains).items():
        label = "-".join(sorted(pair))
        res["p6"][label] = not all(sq not in closure({START}, wp) for sq in sqs)
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
for label, ok in sorted(r["p6"].items()):
    print(f"P6 {label} chains separated: {'ok' if ok else 'VIOLATION'}")
print(f"P7 Fritz+golem walk out in tandem (chains only, no cheats): {r['p7']}")
if r["p7"]:
    print(f"P7b full round trip (out, home again, maze re-armed to start): {pair_roundtrip(CHAINS)}")
    print(f"    escape pulls: {pair_out(CHAINS, want_path=True)}")

# --- Search: if P7 or the full round trip (P7b) fails, look for arrangements
#     that satisfy EVERYTHING. Beat-critical chains stay fixed (G2 first-pull
#     trap, C8 Fritz self-seal, M3/K2 lower-east pair); the other four move. ---
if not (r["p7"] and pair_roundtrip(CHAINS)):
    print("\n--- searching chain placements for escape + full round trip ---")
    FIXED = {"G2": ("I2", "I5"), "C8": ("E8", "E5"),
             "M3": ("I5", "I8"), "K2": ("I8", "I5")}
    ROLES = [("I5", "I2"), ("E5", "E8"), ("E5", "E2"), ("E2", "E5")]
    SPOTS = ["H5", "H8", "G7", "B2", "B4", "C3", "C5", "A8", "L2", "K8", "M7"]
    current_pos = {v: sq for sq, v in CHAINS.items()}
    solutions = []
    for combo in permutations(SPOTS, 4):
        if any(abs(ord(sq[0]) - ord(role[0][0])) < 2
               for sq, role in zip(combo, ROLES)):
            continue  # never right next to the berths it works
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
        desc = ", ".join(f"down {role[0]} up {role[1]} @{sq}" for role, sq in zip(ROLES, combo))
        print(f"  moved {moved} chains: {desc}")
    if solutions:
        best = solutions[0]
        print(f"\nbest candidate ({best[0]} chain(s) moved):")
        print(f"  escape pulls:     {pair_out(best[2], want_path=True)}")
        print(f"  round-trip pulls: {pair_roundtrip(best[2], want_path=True)}")

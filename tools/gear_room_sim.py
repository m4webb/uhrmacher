#!/usr/bin/env python3
"""State-space verification for the gear room shunt puzzle.

Model: party members are abstract tokens (8 is plenty ~ unlimited). Occ = set of
squares some member could occupy. Pressing a plate requires its square to be in
Occ; the shunt then updates walkability and Occ re-closes under movement
(members standing in a closing gap dive to an adjacent open square).

Checks:
  1. No route to the cradle exists before any plate is pressed (forced engagement)
  2. Which plate sequences reach the cradle; minimum presses
  3. Wedge states (all effective plates spent, no route) -> Fritz moments
  4. No party member can ever be sealed in a pocket (every occupied square stays
     connected to staging or chamber)
  5. Golem repositioning distances between gap posts (guard coverage)
"""
from collections import deque

# --- Layout: 9 cols x 14 rows (A=back ... N=entrance) ---
base = set()
for c in range(3, 8): base.add(f"N{c}")            # staging (entrance row)
for c in range(2, 9): base.add(f"M{c}")            # staging (touches all lanes)
for r in "DEFGHIJKL":
    for c in (2, 5, 8): base.add(f"{r}{c}")        # three lanes
base |= {"J3", "J4", "G6", "G7"}                   # crossings (static)
for c in range(2, 9): base.add(f"C{c}")            # top corridor
for c in range(3, 8): base.add(f"A{c}"); base.add(f"B{c}")  # cradle chamber

GAPS = {"G1": "F2", "G2": "F5", "G3": "F8"}        # shunt gaps, all start CLOSED
PLATES = {                                          # name: (square, opens, closes)
    "P1": ("J2", "G3", "G2"),
    "P2": ("J5", "G1", "G3"),
    "P3": ("J8", "G2", "G1"),
    "P4": ("D2", None, "G3"),                       # lockout: close-only
    "P5": ("D8", None, "G1"),                       # lockout: close-only
}
START, GOAL = "N5", "A5"

def walkable(open_gaps):
    w = set(base)
    for g, cell in GAPS.items():
        if g not in open_gaps: w.discard(cell)
    return w

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

def bfs_dist(a, b, w):
    if a not in w or b not in w: return None
    dist, q = {a: 0}, deque([a])
    while q:
        x = q.popleft()
        if x == b: return dist[x]
        for n in neighbors(x, w):
            if n not in dist: dist[n] = dist[x] + 1; q.append(n)
    return None

# --- BFS over (spent plates, open gaps, occ) ---
w0 = walkable(frozenset())
occ0 = closure({START}, w0)
start = (frozenset(), frozenset(), occ0)

seen = {start}
q = deque([(start, [])])
state_paths = {start: []}
successes, wedges, pocket_violations = [], [], []
min_success = None

while q:
    (spent, open_gaps, occ), path = q.popleft()
    reached = GOAL in occ
    if reached:
        successes.append(path)
        if min_success is None:
            min_success = path
    pressable = [p for p, (cell, _, _) in PLATES.items() if p not in spent and cell in occ]
    if not pressable and not reached:
        wedges.append((path, open_gaps))
    for p in pressable:  # keep exploring past success — parties keep pressing
        cell, opens, closes = PLATES[p]
        new_open = (open_gaps | ({opens} if opens else set())) - {closes}
        w = walkable(new_open)
        new_occ = closure(occ, w)
        # pocket check: every occupied square must stay connected to staging or chamber
        anchors = closure({START, GOAL}, w)
        stranded = sorted(c for c in new_occ if c not in anchors)
        if stranded:
            pocket_violations.append((path + [p], stranded))
        s = (spent | {p}, new_open, new_occ)
        if s not in seen:
            seen.add(s)
            state_paths[s] = path + [p]
            q.append((s, path + [p]))

print(f"explored states: {len(seen)}")
print(f"1. route to cradle before any press: {GOAL in occ0}")
print(f"2. minimum presses to reach cradle: {len(min_success)} via {min_success}")
one_press = [p for p, (cell, opens, closes) in PLATES.items()
             if cell in occ0 and opens and GOAL in closure(occ0, walkable(frozenset({opens})))]
print(f"   single presses that open a route: {one_press}")
print(f"   total solved branches: {len(successes)}")
print(f"3. wedge states (Fritz moments): {len(wedges)}")
for path, gaps in wedges:
    print(f"   after {path} -> open gaps {sorted(gaps) or 'none'}")
seals = [path for (spent, open_gaps, occ), path in state_paths.items()
         if not open_gaps and GOAL in occ]
print(f"6. golem-seal states (all gaps closed, party at cradle): {len(seals)}")
for path in seals[:5]:
    print(f"   e.g. after {path}")
print(f"4. pocket violations (stranded members): {len(pocket_violations)}")
for path, cells in pocket_violations:
    print(f"   after {path}: {cells}")

# --- 5. Golem guard coverage: distance between gap posts, all gaps open ---
w_all = walkable(frozenset(GAPS))
print("5. golem repositioning distances (squares, speed 30 ft = 6/turn):")
for a, b in (("F2", "F5"), ("F5", "F8"), ("F2", "F8")):
    print(f"   {a} <-> {b}: {bfs_dist(a, b, w_all)}")

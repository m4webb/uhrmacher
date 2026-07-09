# Encounter — Gear Room

**Difficulty:** Hard by geometry, not by numbers. On paper the golem is Easy for 8 level 3 PCs (900 adjusted XP) — action economy would demolish it in an open room. The map is the difficulty: chokepoint lanes limit engagement to 1-2 PCs at a time, making the golem's ~34 avg DPR a real threat to whoever is exposed. No additional enemies needed.

**Target duration:** 2-3 rounds (if combat), shorter if resolved socially

---

## Enemies

### Gear Golem (Flesh Golem statblock, reskinned) — CR 5
| AC | HP | Speed | Attack | Damage | Save DC |
|----|-----|-------|--------|--------|---------|
| 9 | 127 | 30 ft | +7 to hit (x2) | 13 (2d8+4) bludgeoning + 4 (1d8) lightning per slam | — |

**Immunities:** Lightning, Poison; Charmed, Exhaustion, Frightened, Paralyzed, Petrified, Poisoned
**Aversion to Fire:** Fire damage → disadvantage on attacks/checks until end of next turn
**Berserk:** When bloodied, roll 1d6 at start of turn. On 6, attacks nearest creature. [TBD — does Fritz calm it? Does berserk change the social dynamic?]
**Lightning Absorption:** Regains HP equal to lightning damage taken
**Magic Resistance:** Advantage on saves vs. spells
**Immutable Form:** Can't be shapeshifted

---

## Social Resolution

Players can end this encounter without killing the golem:

| Approach | Mechanic | Notes |
|----------|----------|-------|
| Find Fritz | Perception DC 12 | Spot him hiding behind machinery |
| Persuade Fritz (help the tower) | Persuasion DC 12 | Tell him the Gear will help the tower — true, and he wants that |
| Deceive Fritz | Deception DC [TBD] | Lie about intentions |
| Intimidate Fritz | [TBD] | He's a child — this should work but feel bad |
| Calm the golem directly | [TBD — probably not possible without Fritz] | |

**If Fritz calls off the golem:** It stops immediately and stands down. Fritz watches warily but lets the party work.

**If Fritz learns they want to harm the tower:** Golem fights to the death. Fritz hides and won't call it off.

**If the golem goes berserk:** [TBD — Fritz may lose control. Could attack Fritz too, adding urgency to find the boy.]

---

## The Map — Chokepoint Lanes (decided)

Puzzle-map approach: the room itself limits how many PCs can face the golem.

- **Long rectangular room, 9 × 14 squares (45 × 70 ft)**; entrance at one end, mounting cradle at the far end (back)
- **Three main lanes** run the length of the room through the machinery, with a few cross-connections between them
- Lanes are 1 square wide (single file); the golem is Medium and fits in the lanes — it can chase, and only the front PC can engage it in a lane
- **Main mechanic: shunting carriages (decided).** Machinery never disappears — it shunts. Sections of gear train sit on sliding carriages; every trigger closes one gap and opens another (the metal has to go somewhere)
  - **Pressure plates** fire instantly when a creature enters the square; visible brass panels
  - **One-way:** each plate fires once, then locks (spent). The "undo" is a different plate elsewhere — teamwork by construction
  - **Tracing:** overhead drive chains link each plate to its carriage; action + easy Investigation to learn a plate's pairing before stepping on it (back-rank job)
  - **Caught in a closing gap:** DEX save, dive to adjacent open square; fail = 1d6 bludgeoning + prone
  - **Golem:** keyed to the tower — chooses whether stepping on a plate triggers it. Never damages machinery, so closed paths genuinely stop it (it can be cut off or trapped)
  - **Fritz's control panel:** rigged at the back of the room — he can fire any carriage remotely. Friendly Fritz = the maze opens; hostile Fritz = the maze fights you; also the DM fail-safe if the party spends all plates and wedges themselves (soft-lock pushes toward the social path, by design)
  - **Flavor:** maintenance interlocks — weight on a plate makes the tower reconfigure for "service access." The lanes are service galleries (the Tickwichtel's runs), never meant for people
- Dense machinery blocks ranged sightlines except along open lanes — no plinking from the entrance
- **No round-based timing effects** — that gimmick is reserved for Act III's rotating gear floor
- Players not facing the golem work the maze: climbing/squeezing through the works (Athletics/Acrobatics), scouting flanking routes, searching for Fritz

## Layout v1 (sim-verified — `tools/gear_room_sim.py`)

```
      1  2  3  4  5  6  7  8  9
  A   ▓  ▓  .  .  ◎  .  .  ▓  ▓     ◎ cradle (A5)
  B   ▓  ▓  .  .  .  f  ⌨  ▓  ▓     f Fritz camp · ⌨ control panel (B7)
  C   ▓  .  .  .  .  .  .  .  ▓     open cross-corridor
  D   ▓  P4 ▓  ▓  |  ▓  ▓  P5 ▓     lockout plates (close-only)
  E   ▓  |  ▓  ▓  |  ▓  ▓  |  ▓
  F   ▓  G1 ▓  ▓  G2 ▓  ▓  G3 ▓     shunt gaps — ALL START CLOSED
  G   ▓  |  ▓  ▓  |  .  .  |  ▓     G6-G7: center↔east crossing
  H   ▓  |  ▓  ▓  |  ▓  ▓  |  ▓
  I   ▓  |  ▓  ▓  |  ▓  ▓  |  ▓
  J   ▓  P1 .  .  P2 ▓  ▓  P3 ▓     J3-J4: west↔center crossing · entry plates
  K   ▓  |  ▓  ▓  |  ▓  ▓  |  ▓
  L   ▓  |  ▓  ▓  |  ▓  ▓  |  ▓
  M   ▓  .  .  .  .  .  .  .  ▓     staging (spans cols 2-8, touches all lanes)
  N   ▓  ▓  .  .  ▲  .  .  ▓  ▓     ▲ stairs from Clockhall
```

| Plate | Where | Opens | Closes | Note |
|---|---|---|---|---|
| P1 | J2 (west) | G3 (east) | G2 (center) | round-robin: serves another lane |
| P2 | J5 (center) | G1 (west) | G3 (east) | |
| P3 | J8 (east) | G2 (center) | G1 (west) | |
| P4 | D2 (west, deep) | — | G3 (east) | lockout (close-only), flavor: maintenance lockout |
| P5 | D8 (east, deep) | — | G1 (west) | lockout (close-only) |

**Sim findings:**
- No route exists before the first press (forced engagement); any single entry plate opens a route (progress guaranteed)
- No party member can ever be pocketed (all squares stay connected to staging or chamber)
- Full-party deadlock impossible; **stranded-rear wedges exist** (all gaps closed, part of party stuck below) — but lockout plates are only reachable from above, so any wedge means a vanguard is already at the back *with Fritz*. The Fritz moment happens by construction
- **Golem seal achievable in 2 presses** (e.g. P1 then P4: open east, run up, cross the C corridor, lock east behind you) — 11 distinct seal states
- Golem guard coverage is asymmetric: center↔east reposition = 5 squares (one turn at speed 30), west is 9-12 (two turns) — **west is the slow flank**, learnable by observant players

## Environment

- **Mounting cradle** — empty circular frame at the back of the room, where the Gear installs
- **Heavy gear trains** — fill the room, provide cover, climbable
- **Fritz's camp** — bedroll, crate, candle stub near the cradle
- **Weight chains** — hang from ceiling, could be interacted with [TBD — swing on them? Drop something?]
- **Low ceiling, vaulted** — underground, echoing

---

## End Conditions

1. **Golem defeated** — Fritz is terrified, may flee or surrender
2. **Fritz calls off golem** — Social resolution, golem stands down
3. **Party installs the Gear** — Regardless of how they dealt with Fritz/golem, the Gear clicks into the mounting cradle

---

## Open Questions

- [x] ~~Is the flesh golem statblock the right CR?~~ Resolved: keep the statblock as-is; difficulty comes from map geometry
- [x] ~~Should there be minor enemies to supplement the golem?~~ Resolved: no — chokepoint terrain replaces minions
- [ ] Lane layout — how many lanes, where they run, where the golem's wide lane sits
- [ ] Environmental triggers — which spots trigger what (paths closing, opening, other effects)
- [ ] What happens to Fritz after the encounter? Does he stay in the tower during Act III? Does he follow the party?
- [ ] Berserk mechanic — how does it interact with Fritz's control?
- [ ] Does killing the golem have narrative consequences (Fritz's only protector, the party just destroyed a child's companion)?

---

## DM Notes

- The golem hits hard (17 avg per slam, 34 per round with multiattack) — at level 3 HP pools that's potentially downing a PC in one round
- AC 9 means players almost never miss — the encounter is about HP attrition, not difficulty hitting
- Magic Resistance and immunities make it resistant to certain caster strategies
- Fire is the key weakness — fire damage gives it disadvantage on everything
- The real design intent is that this encounter has multiple valid solutions: fight, talk, sneak. Pure combat is the least interesting path.

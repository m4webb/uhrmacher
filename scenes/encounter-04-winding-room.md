# Encounter — Winding Room

**Difficulty:** Hard by geometry, not by numbers. On paper the golem is Easy for 7 level 3 PCs (900 adjusted XP) — action economy would demolish it in an open room. The map is the difficulty: chokepoint lanes limit engagement to 1-2 PCs at a time, making the golem's ~34 avg DPR a real threat to whoever is exposed. No additional enemies needed.

**Target duration:** 2-3 rounds (if combat), shorter if resolved socially

---

## Enemies

### Gear Golem (Flesh Golem statblock, reskinned) — CR 5
| AC | HP | Speed | Attack | Damage | Save DC |
|----|-----|-------|--------|--------|---------|
| 9 | 127 | 30 ft | +7 to hit (x2) | 13 (2d8+4) bludgeoning + 4 (1d8) lightning per slam | — |

**Start position:** G8 (east mid-band) — caged behind the counterweights at encounter start, released by the first effective chain pull.

**Immunities:** Lightning, Poison; Charmed, Exhaustion, Frightened, Paralyzed, Petrified, Poisoned
**Aversion to Fire:** Fire damage → disadvantage on attacks/checks until end of next turn
**Berserk:** When bloodied, roll 1d6 at start of its turn; on a 6 it goes berserk — it ignores Fritz's commands and attacks the nearest creature, *including Fritz*. Fritz can end it: he must reach the golem (through the fight) and spend his turn at it with the brass key — it calms on his next command, automatically. The rescue-the-boy beat.
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
| Deceive Fritz | Deception DC 14 | Lie about intentions — harder than the truth; his skepticism is his armor |
| Intimidate Fritz | Auto-success — no roll | Terrifying a child works. But the golem reads Fritz's fear as a threat and goes berserk immediately: intimidation is a trap option |
| Calm the golem directly | Not possible | Only Fritz (or holding his brass key) commands it — the social pressure points at the boy. Taking the key by force works, and feels like it |

**If Fritz calls off the golem:** It stops immediately and stands down. Fritz watches warily but lets the party work.

**If Fritz learns they want to harm the tower:** Golem fights to the death. Fritz hides and won't call it off.

**If the golem goes berserk:** it stops obeying and attacks the nearest creature — including Fritz. Only Fritz with the key, adjacent, spending his turn, can wind it back down. If Fritz is hiding, someone has to get the terrified boy to his rampaging protector.

---

## The Map — Chokepoint Lanes (decided)

Puzzle-map approach: the room itself limits how many PCs can face the golem.

- **Long rectangular room, 9 × 14 squares (45 × 70 ft)**; entrance at one end; back splits in two: west+center lanes feed the **4×3 backroom** (cols 2-5; the mounting cradle is a circular frame centered on the A/B–3/4 grid intersection), the east lane dead-ends in a **deserted corner where Fritz lives** — the two are walled off from each other, keeping the two-column machinery rhythm between lanes
- **Three main lanes** run the length of the room through the machinery, with two static crossings (K3-K4 west↔center, G6-G7 center↔east) — both placed where no pinecone footprint can ever reach them (same safety property as the chains)
- Lanes are 1 square wide (single file); the golem is Medium and fits in the lanes — it can chase, and only the front PC can engage it in a lane
- **Main mechanic: pinecone counterweights + pull-chains (decided, v3 — pinecones).**
  - **Six colossal cast-iron PINECONE counterweights** — the classic cuckoo-clock weight, scaled monstrous, **3×3 squares** each — hang from the winding chains, one above each berth (two levels, rows E and I). At any moment exactly two per level are down — **four pinecones on the map, never more**. Pulling a chain transfers the load: one weight descends as another rises
  - **A pull that would lower a weight already down (or raise one already up) grinds and jams** (the jam rule)
  - **Footprint:** 3×3 centered on the berth — it buries the lane cell plus the surrounding bays and lane segments. Sim-verified connectivity-equivalent to the earlier 3×1 slider model (all properties P1-P7b unchanged)
  - **Why pinecones:** real cuckoo clocks use cast-iron pinecone weights on chains — this room was always supposed to be this; and it keeps THE Gear (and its empty cradle) the only gear that matters here
  - **Invariant:** each level always has exactly one lane open. "Sealing" the maze means mismatching the levels, not closing everything
  - **Eight pull-chains** hang from the ceiling, scattered (never beside their own pinecone): one chain per pinecone per direction — no chain does double duty. Symbol convention: the arrow sits on the side the load travels toward (↓I5 lowers I5 from the east pair; I5↓ from the west). Pulling costs an **action**; chains are reusable (they grind or jam with audible flavor when the move is impossible)
  - **Tracing:** a chain's rigging runs up into the works; action + easy Investigation follows it to the pair of weights it works — which berth it lowers, which it raises (back-rank job)
  - **Caught under a descending pinecone:** DC 14 DEX save, dive to an adjacent open square; fail = 7 (2d6) bludgeoning + prone (a wonderful save to narrate) — matches the Act III door-slam peril
  - **Golem:** never damages machinery, so blocked lanes genuinely stop it — it reroutes or waits
  - **Only chains move the pinecones, and anyone can pull them** — players, Fritz, the golem. Fritz and the golem are ordinary actors: they walk and they pull. No special traversal for anybody
  - **The pair can leave AND fully re-arm (sim-verified, P7/P7b):** from the starting configuration, Fritz and the golem acting in tandem can walk out using only chain pulls (C8, B4, G2, C3, L2 — Fritz self-seals, the golem loops the maze and frees him), and on returning home the golem's final pull of **G6 — the chain at the crossing beside its post — restores the exact starting configuration around them.** The room is found sealed because the golem seals itself into its cage, every time they come home
  - **Fritz has no control panel.** His one lever is the C8 chain hanging beside his corner: he can pull it himself — sealing himself in and revealing the way to the cradle. The social path's payoff is Fritz choosing to do this
  - **Flavor:** the lanes are service galleries (the Tickwichtel's runs), never meant for people; the chains are the tower's winding rigging, and the pinecones they raise and lower are the clock's own drive weights — cast-iron pinecones, as on any honest cuckoo clock
- Dense machinery blocks ranged sightlines except along open lanes — no plinking from the entrance
- **No round-based timing effects** — that gimmick is reserved for Act III's rotating gear floor
- Players not facing the golem work the maze: tracing chains, relaying positions, climbing/squeezing through the works (Athletics/Acrobatics)

## Layout v3 — pinecones (sim-verified — `tools/winding_room_sim.py`, interactive: `tools/winding_room_sim.html`)

```
      1  2  3  4  5  6  7  8  9
  A   ▓  .  .◎ .  .  ▓  f  .  ▓     backroom 4×3 (cols 2-5) · ◎ cradle on the A/B–3/4 intersection
  B   ▓  .  .  ⛓  .  ▓  .  .  ▓     B4: E5↓ ↑E2 · f Fritz's camp (2×2 home, A7–B8, walled off at col 6)
  C   ▓  .  ⛓  .  .  ▓  ▓  ⛓  ▓     C3: ↓E2 ↑E5 · C8: E8↓ ↑E5 (Fritz's chain)
  D   ▓  |  ▓  ▓  |  ▓  ▓  |  ▓
  E   ▓  ◉  ▓  ▓  ◉  ▓  ▓  ◉  ▓     UPPER BERTHS (E2 · E5 · E8) — a weight above each; two of three down
  F   ▓  |  ▓  ▓  |  ▓  ▓  |  ▓
  G   ▓  ⛓  ▓  ▓  |  ⛓  .  Ⓖ  ▓     G2: ↓I2 ↑I5 · G6: I5↓ ↑I2 (re-arm) · G7 crossing · Ⓖ golem start (G8)
  H   ▓  |  ▓  ▓  |  ▓  ▓  |  ▓
  I   ▓  ◉  ▓  ▓  ◉  ▓  ▓  ◉  ▓     LOWER BERTHS (I2 · I5 · I8) — a weight above each; two of three down
  J   ▓  |  ▓  ▓  |  ▓  ▓  |  ▓
  K   ▓  ⛓  .  .  |  ▓  ▓  |  ▓     K2: I8↓ ↑I5 · K3-K4 crossing
  L   ▓  ⛓  ▓  ▓  |  ▓  ▓  |  ▓     L2: ↓E5 ↑E8
  M   ▓  .  ⛓  .  .  .  .  .  ▓     M3: ↓I5 ↑I8 · staging (spans cols 2-8)
  N   ▓  ▓  .  .  ▲  .  .  ▓  ▓     ▲ stairs from Clockhall
```

**Start:** weights down at E2, E5, I5, I8 (E8 and I2 up). Upper level open = east; lower open = west; no route — sealed. (Footprints are 3×3, but only the berth cells above are connectivity-relevant.)

| Chain | Hangs at | Weights | Effect when it fires |
|---|---|---|---|
| G2 | west gallery | ↓I2 ↑I5 | opens lower middle, closes lower west — **first effective pull: traps the puller in the gallery and releases the golem** |
| G6 | cage crossing, beside the golem's post | I5↓ ↑I2 | opens lower west, closes lower middle — the re-arm chain; pulling it from inside seals you into the cage |
| M3 | staging | ↓I5 ↑I8 | opens lower east, closes lower middle |
| K2 | west low | I8↓ ↑I5 | opens lower middle, closes lower east |
| B4 | backroom | E5↓ ↑E2 | opens upper west, closes upper middle — endgame control, part of the pair's exit route |
| C3 | backroom | ↓E2 ↑E5 | opens upper middle, closes upper west — endgame control |
| L2 | west low | ↓E5 ↑E8 | opens upper east, closes upper middle |
| C8 | east approach, Fritz's corner | E8↓ ↑E5 | opens upper middle, **seals E8 behind the puller** — critical path; Fritz can pull it himself |

**Verified properties** (all machine-checked in `tools/winding_room_sim.py`):
- Sealed at start; minimum 2 pulls to any route (`G2` → `C8`)
- Teaching funnel: exactly one effective first pull (`G2`); the rest grind or jam informatively
- Golem starts caged in the mid-band at G8 — a chain-less monster zone whose territory guards the critical C8 chain
- First pull traps its puller AND releases the golem, simultaneously
- Tolls: the critical-path pulls cost their pullers position (G2 → the gallery, C8 → Fritz's corner)
- Golem re-seal exists — the "west parade" victory: both levels open west, party walks past the caged golem
- Paired-chain separation: no weight-pair's two chains can be pocketed by a single seal — no unrecoverable states (0 doomed; 32 recoverable pocket events)
- **3×3 pinecone footprints verified connectivity-equivalent** to the slider model; crossings (K3-K4, G6-G7) and all eight chains sit outside every possible footprint
- **P7/P7b tandem commute with full re-arm:** Fritz + the golem can walk out using only chain pulls (5 pulls: C8, B4, G2, C3, L2) and return home, with the golem's final pull of G6 restoring the exact starting configuration — it seals itself into its cage; no special powers, fully self-consistent fiction

## Environment

- **Mounting cradle** — empty circular frame in the 4×3 backroom, centered on the A/B–3/4 grid intersection, where the Gear installs
- **Heavy gear trains** — fill the room, provide cover, climbable
- **Fritz's camp** — bedroll, crate, candle stub in the deserted east corner; his home is the 2×2 nook at A7–B8, walled off from the backroom by the col-6 machinery
- **Pull-chains** — the tower's maintenance rigging, hanging from the ceiling at the eight marked squares
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
- [x] ~~Lane layout~~ Resolved: Layout v2 above (three lanes, two gear tracks, split back)
- [x] ~~Environmental triggers~~ Resolved: sliding gears + eight pull-chains (v2)
- [x] ~~Can the golem pull chains?~~ Resolved: yes — chains are ordinary mechanisms and anyone can pull them, golem included. In practice the golem acts with/for Fritz; a hostile Fritz directing golem chain-pulls is the DM's "maze fights back" dial
- **Fritz after the encounter — depends on the party:** befriended, he trails them up and watches Act III from the landing hatch (the tower that healed him is at stake); frightened or fought, he hides below with the golem and is found in the epilogue. His presence at the finale mirrors how they treated him
- **Killing the golem:** no notated consequence — play Fritz's reaction in the moment (it is a child's only protector; let that land however the table earns it)

---

## Initiative

One roll for Fritz + the gear golem (they act together); the environment acts on initiative 20 (adventure-wide convention — use it for machinery beats, e.g. a counterweight groaning down after a chain pull).

---

## DM Notes

- The golem hits hard (17 avg per slam, 34 per round with multiattack) — at level 3 HP pools that's potentially downing a PC in one round
- AC 9 means players almost never miss — the encounter is about HP attrition, not difficulty hitting
- Magic Resistance and immunities make it resistant to certain caster strategies
- Fire is the key weakness — fire damage gives it disadvantage on everything
- The real design intent is that this encounter has multiple valid solutions: fight, talk, sneak. Pure combat is the least interesting path.

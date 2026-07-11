# Encounter — Cuckoo's Landing

**Difficulty:** Deadly (boss encounter)
**Target duration:** 5 rounds (ON/OFF/ON/OFF/ON)

---

## Enemies

### The Cuckoo (Custom Statblock) — [TBD CR]
| AC | HP | Attack | Damage |
|----|-----|--------|--------|
| 16 | ~110 | [TBD] | [TBD] |

**Restrained on the rod:** Attacks against it have advantage. Its attacks have disadvantage.
**The Cuckoo's Call:** 30 ft cone, DC 14 CON save. Fail: 3d8 thunder + poisoned until end of next turn (cancels restrained advantage). Save: half damage, no poisoned. Once per cycle.
**Emergency Venting:** Once, below half HP. 10 ft radius, DC 14 DEX save. Fail: 3d6 fire. Save: half. Melee punishment.
**Defensive Lockdown (optional):** AC +2 if going down too fast.

### Modron Reinforcements

| Wave | Cycle | Enemies | DPR | Notes |
|------|-------|---------|-----|-------|
| 1 | 1 (ON) | 4 monodrones | Low | Fly 30 ft, not affected by gear rotation. One-shot fodder. |
| 2 | 2 (ON) | 3 duodrones + 1 tridrone | ~25 | Ground only, rotate with gear. Multi-attack makes them sticky. |
| 3 | 3 (ON) | 2 tridrones + 2 quadrones | ~38 | Tridrones ground; quadrones fly 30 ft. Shortbows threaten backline. |

[TBD — need 2024 MM stat blocks for monodrone, duodrone, tridrone, quadrone]

---

## Round Structure

| Round | Phase | What Happens |
|-------|-------|--------------|
| Every | Init 20 | Gear floor rotates 90° CW. All ground creatures/players rotate with it. |
| 1 (ON) | Cuckoo's turn | Emerges from aperture. Knockdown in impact path (DEX save [TBD DC]). Wave 1 modrons burst out. Cuckoo's Call (cone). |
| 2 (OFF) | Cuckoo's turn | Retracts. Knockdown in path (DEX save). Hold-on window: DC 12 STR Athletics to ride into Mechanus. |
| 3 (ON) | Cuckoo's turn | Emerges again. Knockdown. Wave 2 modrons. Cuckoo's Call. |
| 4 (OFF) | Cuckoo's turn | Retracts. Knockdown. Hold-on window. |
| 5 (ON) | Cuckoo's turn | Emerges. Knockdown. Wave 3 modrons. Cuckoo's Call. Last chance. |

Players who beat the cuckoo's initiative can reposition after gear rotation but before emergence/blast.

---

## Battlefield

- **Floor:** Single large gear (25 ft radius). Rotates 90° CW at init 20.
- **Platform (fixed, north edge — does NOT rotate):** row A is a half-depth catwalk (2.5 ft deep) — creatures on it are squeezing (half speed, disadvantage on attacks, attacks against them have advantage). Corner blocks A/B 1-2 and 9-10 are full standing room, level with the gear. Hatch up from the Bellows Chamber at B2; the air riser surfaces at B1 and enters the tower at the A1 half-wall.
- **Doors:** two 10-ft leaves in the north wall (cols 4-7). They slam outward 180° when the cuckoo deploys — everything in the two 10-ft swing arcs (most of the platform) is at risk of the slam ([TBD] save/damage).
- **Aperture:** In the north wall behind the doors. The rod extends inward; the cuckoo perches at the gear hub.
- **Cone direction:** Fixed from center. Rotation shifts who's in the blast zone.
- **Center hazard:** Anyone in the center when cuckoo emerges → knockdown (DEX save).
- **Table procedure:** the platform sheet (doors closed) stays laid over row A all fight; the gear map rotates beneath it. On ON cycles set the ROD PIECE on top — its head is the open doorway (covers the closed doors) and its perch lands on the gear hub. Lift it off on OFF cycles.
- See `props/cuckoos_landing_guide.html` for visual layout (`props/cuckoos_landing_map.html` is the print battle map; `props/cuckoos_landing_overlay.html` is the platform sheet + rod piece).

---

## Riding the Cuckoo into Mechanus

- Players in melee range can grab on as cuckoo retracts: DC 12 STR (Athletics)
- Door blocked while cuckoo is extended — this is the only way through
- On Mechanus: DC 14 WIS save at start of each turn or lose action (move/bonus still available)
- Ride back out on next cycle
- If cuckoo dies while they're inside: door closes, party must figure out how to get them back

---

## End Conditions

**Victory:** Cuckoo destroyed before 3 full cycles. Contract null and void (Art. VI §6.3). Aperture closes. Modrons retreat immediately. Broken cuckoo remains.

**Defeat:** 3 cycles complete. Planar anchor established. Conformity permanent.

**Alternate path:** Players defend the cuckoo from hag coven + fey minions. Cuckoo completes 3 cycles. Contract fulfilled.

---

## Open Questions

- [ ] Full cuckoo custom statblock — attacks on its turn besides the Call? Or is the Call + knockdown + modron waves the entirety of its action?
- [ ] Knockdown DEX save DC — not specified in adventure summary
- [ ] Door-slam save/damage (the 180° swing over the platform) — numbers not set
- [ ] Monodrone/duodrone/tridrone/quadrone 2024 stat blocks needed
- [ ] What does "cuckoo destroyed" look like mechanically — reduced to 0 HP?
- [ ] Gear rotation — do flying creatures rotate? (Currently: no for flyers, yes for ground)
- [ ] How do players know the 3-cycle rule? Is it obvious? Does someone tell them? Does the contract mention it?
- [ ] Alternate path encounter (hag coven + fey minions) needs full design if we want it playable
- [ ] What happens to Pendel during Act III? Does he fight the players? Hesitate? Go fully rogue?

---

## DM Notes

- Initiative: Roll for cuckoo, modrons (one group), and PCs
- The cuckoo is primarily an objective/HP sponge — the modron waves are the real combat threat
- The rotating floor is the key tactical element: it constantly repositions everyone relative to the cone's fixed direction
- Players who figure out the rotation pattern can predict where the cone will hit and position accordingly
- The fight should feel frantic and mechanical — a machine to be dismantled, not a monster to be slain

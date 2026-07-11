# Encounter — Cuckoo's Landing

**Difficulty:** Deadly (boss encounter)
**Target duration:** 5 rounds (ON/OFF/ON/OFF/ON)

---

## Enemies

### The Cuckoo (Custom Statblock) — CR 3 (custom objective)
| AC | HP | Attack | Damage |
|----|-----|--------|--------|
| 16 | ~110 | none — see below | — |

**No attack actions.** The cuckoo's entire turn is: emerge/retract + knockdown + modron wave + the Call. It is an objective to destroy, not a duelist — the modron waves and the environment are the threat.
**Construct:** Immune to poison damage; immune to the poisoned, charmed, frightened, and exhaustion conditions. No damage resistances — its HP and the battlefield are its defense.

**Restrained on the rod:** Attacks against it have advantage. Its attacks have disadvantage.
**The Cuckoo's Call:** 30 ft cone, DC 14 CON save. Fail: 3d8 thunder + poisoned until end of next turn (cancels restrained advantage). Save: half damage, no poisoned. Once per cycle.
**Emergency Venting:** Once, below half HP. 10 ft radius, DC 14 DEX save. Fail: 3d6 fire. Save: half. Melee punishment.
**Defensive Lockdown (optional):** AC +2 if going down too fast.

### Modron Reinforcements

| Wave | Cycle | Enemies | DPR | Notes |
|------|-------|---------|-----|-------|
| 1 | 1 (ON) | 4 monodrones | ~26 | Fly 30 ft, not affected by gear rotation. One-shot fodder (5 HP) — but 2024 Gear attacks bite: real alpha-turn pressure. |
| 2 | 2 (ON) | 3 duodrones + 1 tridrone | ~25 | Ground only, rotate with gear. Multi-attack makes them sticky. |
| 3 | 3 (ON) | 2 tridrones + 2 quadrones | ~38 | Tridrones ground; quadrones fly 30 ft. Gears Launchers (320 ft) threaten backline. |

**Key stats (2024 Monster Manual, via Roll20 compendium):**

| Modron | AC | HP | Speed | Attack |
|--------|----|----|-------|--------|
| Monodrone (CR 1/8) | 15 | 5 | 30 ft, fly 30 ft | Gear +4, 6 (1d8+2) force — melee or ranged 120 ft |
| Duodrone (CR 1/4) | 15 | 11 | 30 ft | Multiattack ×2: Clockwork Blade +3, 4 (1d6+1) force — melee or ranged 30 ft |
| Tridrone (CR 1/2) | 15 | 16 | 30 ft | Multiattack ×3: Clockwork Spear +3, 4 (1d6+1) force — melee or ranged |
| Quadrone (CR 1) | 16 | 22 | 30 ft, fly 30 ft | Multiattack ×4: Slam or Gears Launcher +4, 4 (1d4+2) force — ranged 320 ft |

---

## Round Structure

| Round | Phase | What Happens |
|-------|-------|--------------|
| Every | Init 20 | Gear floor rotates 90° CW. Ground creatures rotate with it; flying creatures and the platform do NOT. |
| 1 (ON) | Cuckoo's turn | Emerges from aperture. Knockdown in impact path (DC 14 DEX). Wave 1 modrons burst out. Cuckoo's Call (cone). |
| 2 (OFF) | Cuckoo's turn | Retracts. Knockdown in path (DC 14 DEX). Hold-on window: DC 12 STR Athletics to ride into Mechanus. |
| 3 (ON) | Cuckoo's turn | Emerges again. Knockdown. Wave 2 modrons. Cuckoo's Call. |
| 4 (OFF) | Cuckoo's turn | Retracts. Knockdown. Hold-on window. |
| 5 (ON) | Cuckoo's turn | Emerges. Knockdown. Wave 3 modrons. Cuckoo's Call. Last chance. |

Players who beat the cuckoo's initiative can reposition after gear rotation but before emergence/blast.

---

## Battlefield

- **Floor:** Single large gear (25 ft radius). Rotates 90° CW at init 20.
- **Platform (fixed, north edge — does NOT rotate):** row A is a half-depth catwalk (2.5 ft deep) — creatures on it are squeezing (half speed, disadvantage on attacks, attacks against them have advantage). Corner blocks A/B 1-2 and 9-10 are full standing room, level with the gear. Hatch up from the Bellows Chamber at B2; the air riser surfaces at B1 and enters the tower at the A1 half-wall.
- **Doors:** two 10-ft leaves in the north wall (cols 4-7). They slam outward 180° when the cuckoo deploys — the swing tiles (A2-A9, B2-B9, C3-C4, C7-C8) join the impact path. **Door slam: DC 14 DEX; fail = 7 (2d6) bludgeoning and knocked prone, save = half and stay standing.**
- **Aperture:** In the north wall behind the doors. The rod extends inward; the cuckoo perches at the gear hub.
- **Cone direction:** Fixed from center. Rotation shifts who's in the blast zone.
- **Center hazard:** Anyone in the center when cuckoo emerges → knockdown (DC 14 DEX).
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

## Telegraphing the 3-Cycle Rule

Primary: the contract, Art. VI §6.3 — players who found and read it in the Study know the termination clause. Backup (DM's choice by table state): a conflicted Pendel states it during Act III, Linde spells it out if she's in play, or any other DM hint (e.g., a modron announcing "second emergence logged; one remains") — deliver it by the end of cycle 1 if nobody has connected it.

---

## End Conditions

**Victory:** Cuckoo destroyed (reduced to 0 HP) before 3 full cycles. Contract null and void (Art. VI §6.3). Aperture closes. Modrons retreat immediately. Broken cuckoo remains.

**Defeat:** 3 cycles complete. Planar anchor established. Conformity permanent.

**Alternate path (improv — deliberately undesigned):** Players defend the cuckoo from Linde's coven (3 moss women / green hag statblocks) + fey minions (blights, wolves) breaking in over 3 cycles. Cuckoo completes 3 cycles → contract fulfilled. Run from the adventure-summary balance notes: coven spells are the real threat, action economy favors the party 8:3, minions fill the gap.

---

## Open Questions


---

## Pendel During the Fight

Branches on how the party treated him in Act II:

- **Befriended / pushed rogue:** he sides with the party — stands clear of the fight but helps: calls the wave timings ("the next emergence comes NOW"), states the 3-cycle rule if they don't know it, shouts which duct the Call is charging from.
- **Neutral:** he freezes — torn between the contract and the doubt, he watches, pleads with both sides, and acts only at the very end (DM's choice of which way, based on the fight's final beat).
- **Antagonized:** he assists the modron waves — directing them, not attacking PCs himself; even hostile, Pendel does not personally fight.

---

## DM Notes

- Initiative: Roll for cuckoo, modrons (one group), and PCs
- The cuckoo is primarily an objective/HP sponge — the modron waves are the real combat threat
- The rotating floor is the key tactical element: it constantly repositions everyone relative to the cone's fixed direction
- Players who figure out the rotation pattern can predict where the cone will hit and position accordingly
- The fight should feel frantic and mechanical — a machine to be dismantled, not a monster to be slain

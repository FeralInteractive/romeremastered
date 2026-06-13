![Workshop_header_template](/Workshop_header_template.png)
# Battle AI Personalities — descr_battle_ai_personalities.txt

## Table Of Contents

* [1. Introduction](#1-introduction)
* [2. How the Battle AI Hierarchy Works](#2-how-the-battle-ai-hierarchy-works)
* [3. Priority Arrays — How They Work](#3-priority-arrays--how-they-work)
* [4. Tactics Constants](#4-tactics-constants)
* [5. Detachment Constants](#5-detachment-constants)
* [6. Objective Constants](#6-objective-constants)
* [7. Melee Manager Constants](#7-melee-manager-constants)
* [8. Miscellaneous Constants](#8-miscellaneous-constants)
* [9. Practical Tuning Guide](#9-practical-tuning-guide)
* [10. The Default Personality (full reference)](#10-the-default-personality-full-reference)
* [Related guides](#related-guides)

---

## 1. Introduction

`descr_battle_ai_personalities.txt` defines sets of constants that control how the AI behaves in 3D battles. Each named personality can be assigned to a faction in `descr_sm_factions.txt`.

All constants in this file were added in Rome Remastered 2.0.4 and do not exist in the original game.

> **Important:** These constants control which **orders** AI units are given — not how the pathfinding or movement is carried out. A unit given the same order will move the same way regardless of personality; only the decision to give that order changes.

> **What these constants do NOT affect:** Campaign map movement, diplomatic decisions, city construction, or recruitment. Those are controlled by `feral_descr_ai_personality.txt`.

---

## 2. How the Battle AI Hierarchy Works

The battle AI operates in a three-level hierarchy:

```
Objectives  →  Detachments  →  Tactics  →  Units
                                    ↓
                            Melee Manager (takes over once in combat)
```

**Objectives** are the highest-level battle goals. Examples: "attack the enemy", "defend this settlement", "scout", "sally out". Only objectives appropriate to the current battle type are active — an open-field battle will never activate siege objectives no matter how high their priority is set.

**Detachments** are created by objectives to carry out specific tasks. A single objective may create several detachments.

**Tactics** are created by detachments to issue orders to individual units. Tactics choose which units they want using an **auction system** (see Section 3).

**Melee Manager** operates separately from the hierarchy. Once units enter close combat, the Melee Manager seizes control and manages unit-vs-unit fighting, flanking, use of special abilities, and retreat decisions.

> The hierarchy means that tuning a tactic priority to zero will disable it globally, but many tactics are already only active in specific battle types. Verify the inline comment on each tactic before concluding it has no effect.

---

## 3. Priority Arrays — How They Work

Both the Tactics and the Melee Manager sections contain a `priority` array. These work differently depending on where they appear:

**Tactics `priority` array:** Values are used as **linear multipliers** on a dynamically calculated base priority. The AI selects tactics in priority order; higher-priority tactics get **first choice** of available units. A value of `0.0` disables the tactic entirely for all battle types. A value of `2.0` doubles the effective priority relative to a tactic at `1.0`.

**Objectives `priority` array:** Also linear multipliers, but objectives participate in an **auction** where each objective bids for units based on opportunity cost (the difference between its best and second-best unit option wins the auction). Scaling an objective to `0.0` disables it.

**Melee Manager `priority` array:** Multiplies calculated priorities for each micro-combat analyser. All are `1.0` by default, meaning no analyser is artificially preferred.

> Values in tactics priorities do **not** represent an absolute number of units. A high priority means the tactic gets first pick, not that more units will be devoted to it — the tactic itself decides how many units it needs.

> The `;;(unused)` comments in the file indicate tactics that exist in code but are never activated by the current battle AI. Setting their priority above `0.0` has no effect because they are never selected regardless of priority value.

---

## 4. Tactics Constants

These constants control distances, thresholds, and probabilities for specific tactical decisions.

### Engagement Distances

* `ai_threat_dist` — distance (metres) at which line defenders notice approaching enemies and begin reacting. Reducing this gives defenders less warning time; increasing it causes them to react to threats sooner.

### Siege Attack Tactics

* `assault_min_dock_distance` — minimum distance siege engines deploy from their target before firing.
* `assault_gate_distance` — distance in front of a gate where AI units form up before assaulting.
* `assault_wall_missile_penalty` — added to the score used to select which units assault gates and walls. **Higher values = missile units are less likely to be selected as assault troops.** At the default `1000.0`, missile units are strongly penalised and melee units are preferred.

### Attacking Battlegroups

* `atk_battlegroup_tracking_tolerance_sq` — distance (squared, metres²) an enemy must move before the AI recalculates unit positions. Default `900` = approximately 30 metres.
* `atk_battlegroup_outflank_distance` — how far from the target unit outflankers aim (metres). Default `150` = aim 150 metres to the side of the enemy unit.
* `atk_battlegroup_missile_react_dist` — how close an enemy must be before the AI reacts to missile fire by adjusting position.
* `atk_battlegroup_outflank_near_dist` — if the enemy is closer than this distance, the AI considers them too close to outflank.
* `atk_battlegroup_outflank_far_dist` — if the enemy is further than this distance, the AI considers them too far to outflank.
* `atk_battlegroup_outflank_prob` — probability (0–100) of attempting an outflanking manoeuvre per update cycle. Default `25` = 25% chance.

### Building Attack

* `atk_building_max_units` — maximum number of units simultaneously assigned to attacking buildings during siege.
* `atk_building_wall_bonus`, `atk_building_tower_bonus`, `atk_building_gate_house_bonus` — score bonuses added when selecting which structures to prioritise during siege attack. Higher = more likely to target that structure type.

### Settlement Capture

* `capt_plaza_link_defender_range` — how close enemies must be to gates or breaches before the AI tries to route around them rather than through them.
* `capt_plaza_gate_preference` — preference for reaching the plaza via a gate vs. breached walls. Higher = more likely to use gates.

### Crossing Defence

* `def_crossing_distance` — how far from the crossing the defensive line is formed.
* `def_crossing_block_distance` — how far back from the crossing a blocking unit stands when holding the exit.
* `def_crossing_formation_block` — formation block index used as the centre of the crossing defence (see formations text file).
* `def_crossing_cavalry_bonus`, `def_crossing_square_bonus`, `def_crossing_missile_bonus`, `def_crossing_phalanx_bonus` — score bonuses for selecting which unit type blocks the crossing. Higher = more likely to assign that unit type. Default preference order: phalanx > missile > square formation > cavalry.

### Junction Defence (Settlement)

* `def_junct_seperation` — distance between junction-defending units in a settlement.
* `def_junct_near_dist` — if a unit is already within this distance of its assigned junction, it is not ordered to move there.
* `def_junct_num_sectors` — the map is divided into this many equal-angle sectors centred on the plaza. The AI falls back on a sector-by-sector basis as enemies advance. Default `8` sectors.

### Breach Defence

* `def_breach_angle_thresh` — angle threshold (radians) before the AI orders units to face the breach again after being knocked aside.

### Line Defence

* `def_line_unformed_thresh_sq` — if a unit is further than this distance² from the defensive line, it moves in formation rather than unformed.
* `def_line_update_tick_time` — number of AI updates before flanking threats are re-evaluated.
* `def_line_threat_merge_dist` — how close enemy units need to be before they are considered a single threat group.
* `def_line_turn_thresh_rad` — how far the defensive line must rotate before units are repositioned.
* `def_line_power_thresh` — how much enemy group strength must change before a new target is chosen.

### Plaza Defence

* `def_plaza_wall_height` — units on walls are treated as being this many metres further from the plaza than units on the ground (for threat priority calculations).
* `def_plaza_order_tolerance` — a unit within this distance of its ordered destination is considered to have arrived.
* `def_plaza_min_size` — plazas smaller than this are treated as "small" and use different assignment logic.
* `def_plaza_minimum_assigned` — minimum number of units assigned to defend the plaza at all times. Note: this floor may not be reached if other tactics claim units first.
* `def_plaza_emergency_thresh` — if enemy strength in the plaza exceeds friendly strength by this ratio, all available units are recalled to the plaza. Default `8.0` = 8:1 enemy:friendly triggers emergency recall.

### Wall Defence

* `def_walls_refresh_time` — seconds between re-evaluation of enemy threats to the walls.
* `def_walls_group_merge_dist` — how close enemy units must be to be considered a single threat group.
* `def_walls_close_dist` — if two threats are within this distance, they are merged as the same threat.

### Outflanking

* `outflank_tolerance_sq` — distance² tolerance before an individual outflanker is ordered to a new position.

### Sally Out

* `sally_out_border` — distance from the settlement border that units aim for when queueing to leave.
* `sally_out_queue_spacing` — spacing between units in the queue to exit the settlement.

### Skirmishing

* `skirmish_ticks_to_shoot` — number of AI ticks missile troops will skirmish before being recalled. Default `1200` = approximately 2 minutes.

### Legacy Values

These are marked `[Legacy]` in the file. They exist for compatibility but are not used by the current AI:

* `atk_crossing_scan_range`, `atk_crossing_force_centre_formation_block`, `atk_crossing_assault_force_centre_formation_block`, `atk_crossing_reform_dist`

---

## 5. Detachment Constants

These constants define the thresholds used to classify how far a battle has progressed. The AI changes its behaviour as the battle advances through phases.

### Contact Thresholds

* `contact_dist` — distance (metres) within which units are considered "in contact".
* `close_approach_dist` — distance within which units are "close approach".
* `distant_approach_dist` — distance within which units are "distant approach".

### Battle Phase Thresholds

The AI tracks what phase the battle is in. Phase affects how freely units are committed:

* `engage_percent_general_melee` — percentage of units that must be in engaged/contact state before the battle is considered "general melee". At this phase the AI no longer holds units back. Default `80%`.
* `engage_percent_initial_assault` — percentage for "initial assault" phase (just before general melee). Default `30%`.
* `contact_percent_contact` — percentage for "contact" phase (units close but mostly not fighting). Default `50%`.

### Enemy Distance Classification

* `enemy_far_dist` — distance at which the enemy is "far away".
* `enemy_near_dist` — distance at which the enemy is "near".

### Formation Cohesion

* `in_position_radius` — units within this radius of their target position are considered to have arrived.
* `in_position_percent` — percentage of a formation that must be in position for the formation to be considered "in position". Default `85%`.

### Miscellaneous Detachment

* `reform_timeout` — AI ticks allowed for reforming before giving up. Default `300` ticks ≈ 30 seconds.
* `atk_battlegroup_multi_prob` — probability (0–100) of attacking from multiple sides simultaneously. Default `50` = 50% chance.
* `atk_settlement_give_up_time` — seconds of idling before the AI gives up on attacking a settlement.
* `def_settlement_assign_tick_period` — ticks between tactic reassignment when defending a settlement. Default `100` ≈ 10 seconds.

### Terrain Defence

* `def_terrain_threat_freq` — ticks between threat re-evaluation for terrain defence.
* `def_terrain_merge_dist` — distance within which enemy units are merged into a single threat group.
* `def_terrain_theat_radius_mult` — [Legacy] enemies within this multiplier × terrain radius are ignored.
* `def_terrain_merge_thresh_sq` — further merging threshold (distance²) for identified enemy groups.
* `def_terrain_mid_point_deviation` — how far a defensive line centre must move before repositioning.
* `def_terrain_length_deviation` — how much a defensive line must change in length before repositioning.
* `def_terrain_angle_deviation` — how much a defensive line must rotate (radians) before repositioning.

### Siege Coordination

* `settlement_link_exclude_range` — any building within this distance of a currently bombarded building is excluded from simultaneous attack.

---

## 6. Objective Constants

Objectives are the highest-level goals. The `priority` array (one entry per objective type) multiplies the dynamically calculated priority for each objective. All are `1.0` by default — a linear scale with no favouritism.

Other constants in this section:

* `high_priority`, `medium_priority`, `low_priority` — named priority tiers used when objectives calculate their bids. These are additive modifiers, not multipliers. Default values: 60, 40, 20.
* `backup_modifier` — extra priority added to objectives that need backup from other units.
* `minimum_priority`, `maximum_priority` — absolute bounds on any calculated priority value.
* `far_range`, `near_range` — distance thresholds used by objectives when estimating threat proximity.

**The 17 objective types** (in priority array order):

| Index | Objective | Notes |
|-------|-----------|-------|
| 0 | Invalid | (unused) |
| 1 | Move to point | General advance or initial deployment |
| 2 | Attack enemy battlegroup | Attack enemies outside settlement or past river defences |
| 3 | Defend terrain hill | May be an ambush if hidden |
| 4 | Defend terrain forest | May be an ambush if hidden |
| 5 | Defend terrain area | May be an ambush if hidden |
| 6 | Defend crossing | Defend each bridge before the attacker has crossed |
| 7 | Defend line | Defend a line |
| 8 | Scout | Move to improve visibility of enemy, or (AI cheat) advance toward hidden enemies |
| 9 | Withdraw | Move off the map when outnumbered |
| 10 | Defend settlement | One per settlement |
| 11 | Support defend settlement | Move reinforcements into a settlement |
| 12 | Attack settlement | One or more depending on simultaneous assault capacity |
| 13 | Skirmish | Against a specific enemy battlegroup |
| 14 | Bombard | Artillery only — attack a building |
| 15 | Attack model | Attack a specific model (gate, wall segment) |
| 16 | Sally out | Sally out from settlement |

---

## 7. Melee Manager Constants

The Melee Manager operates independently of the objective hierarchy. Once units enter close combat, it takes direct control of micro decisions.

### Timing and Proximity

* `update_time` — seconds between Melee Manager updates.
* `engagement_min_proximity_count` — minimum number of nearby enemy soldiers for the situation to be considered a real engagement (not just near-misses).
* `inner_threat_zone_dist_sq` — distance² within which any enemy is an immediate threat and will be attacked. Default `1600` = 40-metre radius.
* `max_engage_dist` — enemies beyond this distance are not considered valid targets. Default `180` metres.

### Strength Modifiers

When calculating whether a unit has enough strength to engage, different unit types have their effective strength adjusted:

* `melee_str_mod` — melee unit strength multiplier. Default `0.7`.
* `missile_str_mod` — missile unit strength multiplier. Default `0.3` (missile units are assumed weaker in melee).
* `rout_str_mod` — routing/fleeing unit strength multiplier. Default `0.25`.

### Fulfilment (Commitment Thresholds)

"Fulfilment" is the theoretical ratio of enemy deaths to friendly deaths. A value of `1.7` means the AI expects to kill 1.7 enemy soldiers for every one of its own lost.

The AI only commits to an attack when it estimates the fulfilment will meet the minimum threshold. It stops requesting more units once the ideal threshold is reached.

* `melee_atk_min_fulfillment` — minimum fulfilment before the AI will begin an attack. Default `0.75`.
* `melee_atk_max_fulfillment` — if fulfilment exceeds this, no more units are added. Default `2.5`.
* `melee_atk_ideal_fulfillment` — target fulfilment the AI aims for when assigning units. Default `1.7`.
* `missile_ideal_fulfillment` — target fulfilment for missile engagements. Default `1.0`.
* `outflank_ideal_fulfillment` — target fulfilment for outflanking actions. Default `1.0`.
* `street_atk_ideal_fulfillment` — target for street-fighting in settlements. Default `1.7`.
* `wall_atk_ideal_fulfillment` — target for attacking walls. Default `1.7`.
* `wall_def_ideal_fulfillment` — target for defending walls. Default `1.7`.

> To make the AI more aggressive and willing to attack at a disadvantage, reduce `melee_atk_min_fulfillment`. To make it more cautious and wait for better odds, raise it toward `1.0` or above.

### Warcry

* `melee_atk_warcry_dist` — distance before attacking units trigger a warcry. Default `60` metres.

### Outflanking (Melee Manager)

* `outflank_close_dist` — if the outflank target is closer than this, outflank priority is reduced.
* `outflank_dist` — distance from the target that outflankers aim for.
* `outflank_waypoint_dist` — distance of the waypoint used when a direct route is blocked.

### Special Abilities

* `special_ability_enter_dist` — distance at which the AI activates formation abilities such as schiltrom.

### Override Levels

When multiple Melee Manager objectives want to force a unit into an action simultaneously, the one with the higher override level wins. In the event of a tie, the objective listed earlier in the array wins.

Default override levels (higher = wins ties):

| Index | Analyser | Override Level |
|-------|----------|---------------|
| 0 | Attack | 1 |
| 1 | Rolling attack | 0 |
| 2 | Outflank | 0 |
| 3 | Missile | 0 |
| 4 | Retreat | 2 |
| 5 | Attack brace | 3 |
| 6 | Special ability | 4 |
| 7 | Collect artillery | 0 |
| 8 | Wall attack | 0 |
| 9 | Wall defend | 0 |
| 10 | Street attack | 0 |

Special ability (override 4) beats all others by default. Retreat (2) and attack brace (3) override basic attack (1). All other analysers are equal-priority and resolved by list order.

---

## 8. Miscellaneous Constants

These constants control skirmisher group behaviour — missile units that harass enemies at range and withdraw when threatened.

* `skirmish_grp_move_thresh_sq` — distance² tolerance before the skirmisher group is ordered to move.
* `skirmish_grp_orientation_thresh` — angle tolerance (radians) before the skirmisher group turns.
* `skirmish_grp_by_pass_dist` — distance at which the skirmisher group stops moving and begins shooting.
* `skirmish_grp_hover_range_sq` — range² that skirmishers maintain from the enemy while hovering.
* `skirmish_grp_shoot_range` — effective shooting range (metres) for skirmisher groups.

---

## 9. Practical Tuning Guide

### Making the AI more aggressive in open-field battles

* Raise `atk_battlegroup_outflank_prob` (try `50`) to make flanking more frequent.
* Raise `atk_battlegroup_multi_prob` (try `70`) for more multi-angle attacks.
* Lower `melee_atk_min_fulfillment` (try `0.5`) so the AI commits at a relative disadvantage.
* Lower `engage_percent_general_melee` (try `50`) so the AI transitions to all-out attack sooner.

### Making the AI more aggressive in sieges

* Increase the `Assault gate` and `Assault wall ladders` priorities in the tactics `priority` array relative to `Sap`. Sap is passive (waiting for tunnel completion); raising gate assault makes the AI prefer direct attacks.
* Increase `atk_building_gate_house_bonus` to make the AI prioritise gatehouse capture.
* Reduce `def_plaza_emergency_thresh` to make defending garrisons retreat to the plaza later (and fight harder at walls).

### Making wall defenders more responsive

* Lower `def_walls_refresh_time` (try `5.0`) so the AI reassesses wall threats more often.
* Lower `def_line_update_tick_time` (try `3`) for faster flank threat reassessment.

### Making the AI hold positions longer before retreating

* Raise `melee_atk_min_fulfillment` — the AI will not start fighting until it has more favourable odds.
* Raise `engage_percent_general_melee` (try `90`) so the AI continues holding back units even late into the battle.

### Increasing skirmisher effectiveness

* Increase `skirmish_ticks_to_shoot` to keep missile units skirmishing longer.
* Increase `skirmish_grp_hover_range_sq` to keep skirmishers at a safer distance.
* Raise the `Skirmish` tactic priority (default `100.0`) relative to other tactics.

### Tuning siege defender behaviour

* `def_plaza_minimum_assigned` — increase to always keep more units at the plaza.
* `def_plaza_emergency_thresh` — lower (e.g. `4.0`) so emergency recall triggers sooner.
* `def_junct_num_sectors` — reduce to consolidate defence at fewer points.

> **Note on priority values:** Tactic priorities are relative to each other within each group. The absolute values matter less than the ratios. `Skirmish : 100` and `Attack enemy battlegroup : 1` means the AI strongly prefers skirmishing. If you set `Attack enemy battlegroup : 50`, the ratio is now 2:1, making the AI much more willing to commit to direct attack.

---

## 10. The Default Personality (full reference)

The complete default personality as shipped with Rome Remastered. All other named personalities in the file override only the values they need to change; unspecified values inherit these defaults.

```
"battle personalities":
[
	"default_personality":
	{
		;;The AI operates with a hierarchy of systems. 
		;;At the highest level, objectives are assigned based on their priority and if they are appropriate for the type of battle.
		;;Each objective creates a certain amount of detachments based on what it needs to do.
		;;Each detachment creates tactics that will order the units around.
		;;When changing priorities, note that only specific objectives/detachments/tactics are chosen depending on the type of battle. So, for example, if we are in an open field battle, no matter how high you set the priority of "Assault gate", that tactic will never be run if there aren't any gates. 
		"tactics":
		{
			"ai_threat_dist" : 33.1,										;;The distance at which line defenders will notice enemies.

			"assault_min_dock_distance" : 20.0,								;;Minimum distance the siege engies deploy from their target
			"assault_gate_distance" : 50.0,									;;Distance in-front of gates AI units go to
			"assault_wall_missile_penalty" : 1000.0,						;;Penalty given when deciding which units should assault gates/walls/buildings. Higher -> Less likely to pick missile units

			"atk_battlegroup_tracking_tolerance_sq" : 900.0,				;;Distance an enemy needs to move before positions are re-calculated
			"atk_battlegroup_outflank_distance" : 150.0,					;;Distance away from the unit that outflankers aim for.(e.g. they aim for 150m to the left of the unit)
			"atk_battlegroup_missile_react_dist" : 180.0,					;;How close an enemy must be in order for us to react to them firing at us.
			"atk_battlegroup_outflank_near_dist" : 150.0,					;;When the enemy is too close to outflank
			"atk_battlegroup_outflank_far_dist" : 400.0,					;;When the enemy is too far to outflank
			"atk_battlegroup_outflank_prob" : 25,							;;Probability of outflanking(out of 100)

			"atk_building_max_units" : 1,									;;Maximum number of units assigned to attacking the buildings

			;;Preference for attacking walls. Higher -> More likely to attack walls
			"atk_building_wall_bonus" : 500.0,								;;For walls
			"atk_building_tower_bonus" : 100.0,								;;For towers
			"atk_building_gate_house_bonus" : 200.0,						;;For gate houses

			"capt_plaza_link_defender_range" : 36.0,						;;How close enemies have to be to gates/breaches in order for this task to try and avoid them.
			"capt_plaza_gate_preference" : 5.0,								;;Preference for reaching the plaza via a gate. Higher -> More likely to go via a gate

			"def_crossing_distance" : 0.0,									;;Distance away from crossing that defensive line is formed
			"def_crossing_block_distance" : 16.0,							;;Distance away from crossing that defensive line, which is behind a unit blocking the crossing,is formed.
			"def_crossing_formation_block" : 0,								;;Index of formation block(see formations text file) that is the centre

			;;Preferences for which unit should be assigned to block the crossing.
			"def_crossing_cavalry_bonus" : 1.0,								;;For melee cavalry units
			"def_crossing_square_bonus"  : 2.0,								;;For units that form in a rectangle
			"def_crossing_missile_bonus" : 3.0,								;;For missile units
			"def_crossing_phalanx_bonus" : 4.0,								;;For phalanx

			"def_junct_seperation" : 20.0,									;;The distance between defending points when defending cities
			"def_junct_near_dist" : 20.0,									;;The distance at which a unit is considered to be close enough to the junction that it's not worth ordering them there
			"def_junct_num_sectors" : 8,									;;The AI divides the map into sectors of equal angle centred at the plaza.
																			;;The enemy's progress is measured in each sector and the AI will fall back on a sector-by-sector basis.

			"def_breach_angle_thresh" : 0.15,								;;The angle threshold for when the AI orders units to face the breach again

			"def_line_unformed_thresh_sq" : 2500.0,							;;If we are further than this distance from the line we are defending, move formed instead of unformed
			"def_line_update_tick_time" : 7,								;;Number of updates before the AI reconsiders threats to the flanks.
			"def_line_threat_merge_dist" : 30.0,							;;How close enemy units need to be in order to consider them part of the same group
			"def_line_turn_thresh_rad" : 0.9,								;;How far(in radians) the line  needs to turn before we adjust our  position.
			"def_line_power_thresh" : 200.0,								;;How much the power of enemy groups needs to change before we choose a new target

			"def_plaza_wall_height" : 1.5,									;;Units on walls are considered 1.5m further away from the plaza than units on the ground.
			"def_plaza_order_tolerance" : 10.0,								;;Tolerance for how close a unit can be to their destination and still be considered at that location.
			"def_plaza_min_size": 40.0,										;;Any plaza smaller than this will be considered "small"
			"def_plaza_minimum_assigned" : 1,								;;Minimum number of units we will assign to defend plaza. Note: This number may not be reached if other tactics/melee manager take the units first.
			"def_plaza_emergency_thresh" : 8.0,								;;If we are outnumbered 8 to 1 in the plaza(in terms of strength) then call all units to the plaza(emergency mode)

			"def_walls_refresh_time" : 10.0,								;;Time in seconds between each consideration of enemy threats
			"def_walls_group_merge_dist" : 80.0,							;;How close enemy units need to be in order to consider them part of the same group
			"def_walls_close_dist" : 160.0,									;;If two threats are this close together, merge them as the same threat.

			"outflank_tolerance_sq" : 1600.0,								;;Tolerance for individual outflankers moving to a new destination

			"sally_out_border" : 50.0,										;;Distance away from the settlement border that our armies will try to aim for.
			"sally_out_queue_spacing" : 30.0,								;;Spacing between our units when queueing to leave the settlement.

			"skirmish_ticks_to_shoot" : 1200,								;;2 minutes of shooting before we stop.

			"atk_crossing_scan_range" : 50.0,								;;[Legacy]How far to scan forward when searching for a crossing to attack
			"atk_crossing_force_centre_formation_block" : 0,				;;[Legacy]Index of formation block(see formations text file) that is the centre
			"atk_crossing_assault_force_centre_formation_block" : 0,		;;[Legacy]Index of formation block(see formations text file) that is the centre
			"atk_crossing_reform_dist": 20.0,								;;[Legacy]Distance away from crossing that we reform at.

			;; Depening on the type of battle, the AI will select a pool of tactics to use from the list below.
			;; Tactics are ordered by their priority, then they each take it in turns to take as many units as they want.
			;; Increasing priority doesn't mean more units will be assigned to that tactic, just that it will get first choice.
			"priority":
			[
				0.0, 			;;Reinforcement						- contains units which are too far away from the other tactics to be useful
				1.0,			;;Move to point						- move the unit groups under the tactics control to a specified position
				0.0,			;;Withdraw							- (unused) withdraw the units to a specified position
				0.0,			;;Scout								- (unused) move the units in an attempt to establish more information about the enemy
				0.0,			;;Support group						- (unused) hang around until the AI gives us something more useful to do
				1.0,			;;Attack enemy battlegroup			- track the enemy battlegroup and attack it
				1.0,			;;Defend line						- move to a terrain feature and defend a line along it
				1.0,			;;Defend terrain support			- move around freely to assist units that are defending a terrain spot.
				1.0,			;;Defend crossing					- move to and defend a river crossing
				1.0,			;;Block crossing					- move to and defend a river crossing, blocking the exit
				0.0,			;;Assault crossing					- (unused) assault a river crossing that is being defended
				0.0,			;;Seize crossing					- (unused) cross an undefended river crossing
				
				100.0,			;;Skirmish							- missile troops distracting the enemy, ready to withdraw
				100.0,			;;Outflank							- outflank the enemy with a single body of troops
				80.0,			;;Double envelopment				- outflank the enemy with two bodies of troops
				80.0,			;;Stop and shoot					- stop the units moving and use missile troops to shoot
				60.0,			;;Warcry							- stop the unit moving and do a warcry, then advance into combat

				;; siege attack tactics

				1.0,			;;Attack building					- either use melee troops to attack a building, or artillery to bombard a wall or building
				1.0,			;;Assault gate						- use troops equipped with a ram to assault a gate
				1.0,			;;Assault wall ladders				- use troops equipped with ladders to assault the walls
				1.0,			;;Assault wall siege tower			- use troops equipped with siege towers to assault the walls
				2.0,			;;Sap								- make use of sap points
				3.0,			;;Capture plaza						- capture plaza and take the settlement
				4.0,			;;Capture buildings					- capture important buildings (gatehouses and arrow towers)
				5.0,			;;General attack settlement			- reserved for general unit when attacking a settlement
				0.0,			;;Attack settlement surplus			- any units that haven't been given the above siege tactics

				;; siege defend tactics

				3.0,			;;Defend walls						- move units up onto the walls of the settlement to defend them
				2.0,			;;Defend breaches					- defend the breaches that the enemy has created in the settlement walls
				1.0,			;;Defend junctions					- defend junctions between the enemy and the plaza
				4.0,			;;Defend plaza						- defend the plaza
				5.0,			;;General defend settlement			- reserved for general unit when defending a settlement
				0.0,			;;Defend settlement surplus			- any units that haven't been given the above siege tactics
				1.0,			;;Support defend settlement			- reinforcements defending the settlement
				0.0,			;;Support defend settlement surplus	- all other reinforcements defending the settlement

				;;sally out tactics

				1.0,			;;Sally out							- order units outside of the settlement in a queue
				0.0,			;;Sally out surplus					- all other units in a sally out battle
			],
		},
		"detachment":
		{
			"contact_dist" : 120.0,											;;How close units need to be for them to be considered in "contact"
			"close_approach_dist" : 230.0,									;;How close units need to be for them to be considered in "close approach"
			"distant_approach_dist" : 500.0,								;;How close units need to be for them to be considered in "distant approach"

			"engage_percent_general_melee" : 80,							;;Required percentage of units in engaged/contact for the AI to consider the battle to have advanced to "general melee". This is the phase of the battle where all the units are fighting in melee and the AI will not hold back as much.
			"engage_percent_initial_assault" : 30,							;;Required percentage of units in engaged/contact for the AI to consider the battle to have advanced to "Initial assault". This is the phase right before "general melee"
			"contact_percent_contact" : 50,									;;Required percentage of units in contact for the AI to consider the battle to have advanced to "Contact". This is the first phase where the units are close but mostly not fighting.

			"enemy_far_dist" : 200.0,										;;The distance at which the enemy is considered far away
			"enemy_near_dist" : 100.0,										;;The distance at which the enemy is considered near

			"in_position_radius" : 40.0,									;;Units within this radius of their target positon are assumed to be there. We assume that unit group marching will keep us in formation so only want units to be considered out of formation if the group is scattered.
			"in_position_percent" : 85.0,									;;If this percentage of a formation is in position, then the formation is considered to be in position

			"reform_timeout" : 300,											;;Time to allow for reforming before giving up in ai ticks (30 secs)

			"atk_battlegroup_multi_prob" : 50,								;;Probability that we attack the enemy from multiple sides(2 or 3)

			"atk_settlement_give_up_time" : 15.0,							;;Time spent idle before giving up on attacking a settlement.(15 secs)

			"def_settlement_assign_tick_period" : 100,						;;Number of ticks between reassignment of tactics when defending a settlement(10 secs)

			"def_terrain_threat_freq" : 10,									;;Number of ticks between re-evaluation of threats to the terrain.
			"def_terrain_merge_dist" : 20.0,								;;How close enemy units need to be in order to consider them part of the same group
			"def_terrain_theat_radius_mult" : 4.5,							;;[Legacy]Enemies within 4.5 times the radius of the terrain feature will be ignored.
			"def_terrain_merge_thresh_sq" : 2500.0,							;;Once enemy groups are identified, they are further merged if their centres are within this distance.
			"def_terrain_mid_point_deviation" : 20.0,						;;How far a defensive line needs to move before the AI will re-position.
			"def_terrain_length_deviation" : 50.0,							;;How much a defensive line must change in length before the AI will re-position.
			"def_terrain_angle_deviation" : 0.523599,						;;How far a defensive line needs to turn before the AI will re-position.

			"settlement_link_exclude_range" : 200.0,						;;Do not attack any building that is within this distance of a building being bombarded with siege equipment.

			;; Note: Detachments don't have a priority system.
		},
		"objectives":
		{
			"high_priority" : 60,											;;Number considered to be a large amount of priority
			"medium_priority" : 40,											;;Number considered to be a medium amount of priority
			"low_priority" : 20,											;;Number considered to be a small amount of priority
			"backup_modifier" : 20,											;;Extra priority given for objectives that need backup
			"minimum_priority" : 1,
			"maximum_priority" : 5000,

			"far_range": 200.0,												;;The distance at which the enemy is considered far away
			"near_range": 100.0,											;;The distance at which the enemy is considered near

			;; Objectives assign detachments, and detachments assign tactics, which then order the units. 
			;; The AI will select a few objectives depending on the type of battle, then each will take part in an auction where they bid on the units they want.
			;; The unit with the highest opportunity cost(difference between best and second best objective) will be the winner of the auction and get assigned to it's best objective.
			;; Priorities are calculated dynamically based on various factors of the battlefield, so the values in the list below will simply scale the calculated priority linearly.
			"priority":
			[
				1.0, 			;;Invalid							- (unused)
				1.0,			;;Move to point						- move to a point on the map: cause a general advance on the enemy base while scouting or gather up initial units for deployment
				1.0,			;;Attack enemy battlegroup			- attack an enemy battlegroup: attack any enemy battlegroup outside the castle, attack the enemy's main body, or attack any enemy battlegroup which has crossed a river and made it past the river defences
				
				1.0,			;;Defend terrain hill				- defend a hidden or hill line. May be an ambush (if hidden)
				1.0,			;;Defend terrain forest				- defend a forest. May be an ambush (if hidden)
				1.0,			;;Defend terrain area				- defend an area. May be an ambush (if hidden)
				1.0,			;;Defend crossing					- defend each bridge if the attacker hasn't yet crossed it
				1.0,			;;Defend line						- defend a line
				
				1.0,			;;Scout								- look for the enemy: go to a point on the map to try to improve visibility of enemy units or, (CHEATING) move towards a hidden enemy unit, to advance the game.
				1.0,			;;Withdraw							- when we're outnumbered, move off the map
				
				1.0,			;;Defend settlement					- defend a settlement - one per settlement
				1.0,			;;Support defend settlement			- support defend settlement objective my moving refinforcements into settlement
				
				1.0,			;;Attack settlement					- one or more, depending on how many simultaneous assaults we can carry out
				1.0,			;;Skirmish							- against a specific enemy battlegroup
				1.0,			;;Bombard							- for artillery only - attack something, which could be a building
				1.0,			;;Attack model						- attack a specified model on the map, for instance a gate or castle wall
				1.0,			;;Sally out							- sally out
			],
		},
		;;AI units are controlled by the objective-detachment-tactic hierarchy for the big picture stuff.
		;;But the micro interactions are controlled by the melee manager, which will seize control of the units once they enter combat.
		"melee_manager":
		{
			"update_time" : 3,												;;Time(in seconds) between updates of the melee manager.
			"engagement_min_proximity_count" : 4,							;;Minimum number of enemy men that must in close proximity to consider this an engagement
			"inner_threat_zone_dist_sq" : 1600.0,							;;Units will try and attack any enemy that is within this distance.
			"max_engage_dist" : 180.0,										;;Enemies further than this will not be considered viable targets.
			
			;;When considering the strength of enemy units, these modifiers are multiplied to their base strength.
			"melee_str_mod" : 0.7,
			"missile_str_mod" : 0.3,
			"rout_str_mod" : 0.25,

			"melee_atk_warcry_dist" : 60.0,									;;Distance before we start a warcry
			;;Fulfillment refers to the theoretical total enemy soldier deaths per friendly soldier. Positive means a win for us.
			;;Different melee manager objectives require this number to different amounts. Most objectives want this number to be at 1.7 and will request units until this is met.
			
			"melee_atk_min_fulfillment" : 0.75,
			"melee_atk_max_fulfillment" : 2.5,
			"melee_atk_ideal_fulfillment" : 1.7,
			"melee_atk_rolling_atk_thresh" : 0.261799,						;;[Legacy]

			"missile_min_armour_mod" : 0.7,									;;[Legacy]
			"missile_max_armour_mod" : 1.5,									;;[Legacy]
			"missile_ideal_fulfillment" : 1.0,

			"outflank_close_dist" : 50.0,									;;If the enemy we are outflanking is closer than 50m then we reduce the priority to do this.
			"outflank_dist" : 20.0,											;;Distance away from the unit that outflankers aim for.(e.g. they aim for 20m to the left of the unit)
			"outflank_waypoint_dist" : 70.0,								;;Sometimes we need to go via a waypoint to outflank the unit, this is the distance that waypoint will be from the unit.
			"outflank_ideal_fulfillment" : 1.0,								

			"special_ability_enter_dist" : 200.0,							;;Distance before we enter schiltrom

			"street_atk_ideal_fulfillment" : 1.7,							

			"wall_atk_ideal_fulfillment" : 1.7,
			"wall_def_ideal_fulfillment" : 1.7,

			;;Override levels - if multiple melee manager objectives want to force a unit to do something, then the one with the higher override level will take precedence.(Must be positive whole numbers)
			;;In the event of a tie, elements higher on the list get precedence.
			"override_levels":
			[
				1, 				;;Attack
				0,				;;Rolling attack
				0,				;;Outflank
				
				0,				;;Missile
				2,				;;Retreat
				3,				;;Attack brace
				4,				;;Special ability
				0,				;;Collect artillery
				
				0,				;;Wall attack
				0,				;;Wall defend

				0,				;;Street attack
			],

			;; Similar auction system to objectives. These constants scale the priority linearly.
			"priority":
			[
				1.0, 			;;Attack
				1.0,			;;Rolling attack
				1.0,			;;Outflank
				
				1.0,			;;Missile
				1.0,			;;Retreat
				1.0,			;;Attack brace
				1.0,			;;Special ability
				1.0,			;;Collect artillery
				
				1.0,			;;Wall attack
				1.0,			;;Wall defend

				1.0,			;;Street attack
			],
		},
		"misc" :
		{
			"skirmish_grp_move_thresh_sq" : 400.0,							;;Distance tolerance before we move the skirmisher.
			"skirmish_grp_orientation_thresh" : 0.349066,					;;Angle tolerance before we move the skirmisher.
			"skirmish_grp_by_pass_dist" : 200.0,							;;Distance at which we stop and shoot
			"skirmish_grp_hover_range_sq" : 32400.0,						;;Range we hover at
			"skirmish_grp_shoot_range" : 120.0,								;;Shooting range
		},
	},
],
```

---

## Related guides

* [feral_descr_ai_personality.txt](/documentation/data_file_guides/feral_descr_ai_personality.md) — campaign AI: recruitment priorities, building priorities, diplomatic behaviour, and faction personality assignment
* [How the AI Conducts Diplomacy](/documentation/feature_guides/AI_Diplomacy.md) — how diplomatic personality values translate to AI decision-making

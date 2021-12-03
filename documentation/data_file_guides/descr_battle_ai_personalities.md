![Workshop_header_template](/Workshop_header_template.png)
# descr_battle_ai_personalities

## Table Of Contents

   * [Introduction](#introduction)
   * [Default Battle AI Personality](#default-battle-ai-personality)

## Introduction

With the introduction of this file the AI personalities inside 3D battles are now moddable. These constants can be assigned on a per-faction basis in `descr_sm_factions.txt`.

This file contains all constants used by the AI. These values affect which orders the units are given, but **not the pathfinding/way the orders are carried out**. Descriptions are from the perspective of the AI, so the "enemy" is likely the player, and "us" refers to the AI.

The file is fully documented and should be self explanatory. See below for a copy of the files contents including comments.

All of these features are new to Rome Remastered as of 2.0.4.

## Default Battle AI Personality

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
],```
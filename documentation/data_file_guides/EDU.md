![Workshop_header_template](/Workshop_header_template.png)
# export_descr_unit

## Table Of Contents

* [Introduction](#introduction)
* [EDU Breakdown](#edu-breakdown)
   * [Example of a complete unit definition](#example-of-a-complete-unit-definition)
   * [type](#type)
   * [dictionary](#dictionary)
   * [category](#category)
   * [class](#class)
   * [voice_type](#voice_type)
   * [soldier](#soldier)
   * [mount](#mount)
   * [mount_effect](#mount_effect)
   * [officer](#officer)
   * [animal](#animal)
   * [engine](#engine)
   * [ship](#ship)
   * [attributes](#attributes)
   * [formation](#formation)
   * [stat_health](#stat_health)
   * [stat_pri](#stat_pri)
   * [wpn_attributes](#wpn_attributes)
   * [stat_sec](#stat_sec)
   * [stat_pri_armour](#stat_pri_armour)
   * [stat_sec_armour](#stat_sec_armour)
   * [stat_heat](#stat_heat)
   * [stat_ground](#stat_ground)
   * [stat_mental](#stat_mental)
   * [stat_charge_dist](#stat_charge_dist)
   * [stat_fire_delay](#stat_fire_delay)
   * [stat_food](#stat_food)
   * [stat_cost](#stat_cost)
   * [recruit_priority_offset (New for RR)](#recruit_priority_offset)
   * [ownership](#ownership)
* [Useful Formulae](#useful-formulae)
   * [Chance_to_kill (melee):](#chance_to_kill-melee)
   * [Chance_to_kill (missile):](#chance_to_kill-missile)

## Introduction

This guide has been written based on the format first created by Aradan on the [TWC forums](https://www.twcenter.net/forums/showthread.php?111344-The-Complete-EDU-Guide). With his permission we have created this new updated version.

We actively encourage modders to update this document with useful information and we can merge in any changes so this document can be the main resource for editing the EDU in Rome Remastered.


## EDU Breakdown

The file contains the entries for all the units in the game; the limit has been raised from the original games 500 unit maximum to practically unlimited. The order the units are arranged in is not specified, but the format each entry is coded in, is of course strictly specified. Here we will use a single, generic entry as an example, break it to its separate lines and then analyse each line individually, and then break it down to its entries when needed.
Note that certain lines may be missing depending on the type of the unit.

NOTE: Attributes for ROME REMASTERED contain some addional attributes over the original release. See attributes section for more details.

### Example of a complete unit definition

```
type             barb peltast gaul
dictionary       barb_peltast_gaul      ; Skirmisher Warband
category         infantry
class            missile
voice_type       Light_1
voice_indexes    0 1 2
soldier          barb_peltast_gaul, 40, 0, 0.9
mount_effect     elephant +6, chariot +6
attributes       sea_faring, hide_improved_forest, hide_long_grass
formation        1.6, 2, 3.2, 4, 3, square
stat_health      1, 0
stat_pri         9, 4, javelin, 50, 6, thrown, archery, piercing, spear, 25 ,1
stat_pri_attr    thrown
stat_sec         6, 4, no, 0, 0, melee, simple, piercing, knife, 25 ,1
stat_sec_attr    no
stat_pri_armour  0, 1, 2, flesh
stat_sec_armour  0, 0, flesh
stat_heat        2
stat_ground      2, -2, 3, 2
stat_mental      4, low, untrained
stat_charge_dist 30
stat_fire_delay  0
stat_food        60, 300
stat_cost        1, 220, 130, 30, 40, 220
ownership        gauls
ethnicity gauls, Central_Gaul, don't_allow_mixed, don't_allow_regional, don't_allow_custom
tattoo_color blue
rebalance_statblock
soldier          barb_peltast_gaul, 40, 0, 0.9
mount_effect     elephant +6, chariot +6
attributes       sea_faring, hide_improved_forest, hide_long_grass
formation        1.6, 2, 3.2, 4, 3, square
stat_health      1, 0
stat_pri         9, 4, javelin, 65, 6, thrown, archery, piercing, spear, 25 ,0.75
stat_pri_attr    thrown
stat_sec         6, 4, no, 0, 0, melee, simple, piercing, knife, 25 ,1
stat_sec_attr    no
stat_pri_armour  0, 1, 2, flesh
stat_sec_armour  0, 0, flesh
stat_heat        2
stat_ground      2, -2, 3, 2
stat_mental      4, low, untrained
stat_charge_dist 30
stat_fire_delay  0
stat_food        60, 300
stat_cost        1, 220, 130, 30, 40, 220
```
---
### type

```Code: type             unit_type```

The type name which is referenced in the recruitment lines of *export_descr_buildings.txt*, the starting armies of *descr_strat.txt*, the visual attributes for units in the *descr_model_battle.txt* and the armies of *descr_battle.txt* for historical battles.

**Allowed Variables**

Any string including spaces

eg. ```type             barb peltast gaul```

---

### dictionary

```Code: dictionary       unit_dictionary_tag```

References the export_units.txt entries for the on-screen name, description and short description of the unit. Also references the unit and unit info card names in the UI folder.

**Allowed Variables**

Any string no spaces allowed

eg. ```dictionary       barb_peltast_gaul      ; Skirmisher Warband```

---

### category

```Code: category         unit_category```

Internal unit category for nature of unit (references sound files and triggers bracketed category mouseover text in battles along with class entry) It is also used (along with other factors including class) by the AI during campaign mode in order to decide which units to train. Also used (along with class occasionaly) in by descr_formations_ai.txt and descr_formations.txt, as labels for unit placement. Can be infantry, cavalry, siege, handler or ship. In the custom-battle selection screen infantry units will appear first, then cavalry and then siege.

**Allowed Variables**

Any of the following variables:

```
infantry
cavalry
siege
handler
ship
```

eg. ```category         infantry```

---

### class

```Code: class            unit_class```

References sound files and triggers bracketed category mouseover text in battles (along with category entry) It is also used (along with other factors including category) by the AI during campaign mode in order to decide which units to train. Also used (along with category) in by descr_formations_ai.txt and descr_formations.txt, as labels for unit placement. Can be light, heavy, spearmen or missile. Also "skirmish", but it is not used at all in vanilla (will be tested and updated). In the custom-battle selection screen light units will appear first, followed by spearmen, then heavy and finally missile (after being sorted by category) and then units are sorted by EDU order of appearence.

**Allowed Variables**

Any of the following variables:

```
light
heavy
spearmen
missile
skirmish - (**TODO: More detail needed**)
```

eg. ```class            missile```

---

### voice_type

```Code: voice_type       voice```

References the sound bank category for the unit's voice.

**Allowed Variables**

Any of the following variables:

```(**TODO: More detail needed**)```

eg. ```voice_type       Light_1```

(**TODO: More detail needed**) - Need to add extra info on voice_indexes

---

### soldier

```Code: soldier          unit_model, soldiers, extras, mass (,radius,height)```

Details of unit models.

* **unit_model** : Unit's model type as referenced in descr_model_battle.txt. Note that the skeleton scale and its associated animations in the DMB file both significantly affect the combat effectiveness and thus value of the unit. This is done mainly in three ways:
  * The unit model's scale improves combat effectiveness as it gets bigger. A way to balance this (though not perfectly safe) is through the hidden parameter 'height' that lies in the soldier line. [see below]
  * The unit skeleton attack animations also improve unit effectiveness as they get faster. The way to counter this effect is the min_delay_between_attacks stat, which lies in the stat_pri line [see below]
  * The unit skeleton animations also help combat effectiveness, when they have big(ger) impact deltas. The way to counter this is through lethality [see related information]
* **soldiers** : Number of unit's soldiers in medium unit-size settings. Can't be lower than 6 or higher than 60. General units have a max of 31 men.
* **extras** : Number of animals attached to unit again in medium unit-size settings.
* **mass** : Collision mass of the unit. Units with big mass values can "push" their enemies harder and break through enemy lines easier and also hold against enemy pushing better. The mass ratio is not fixed, in that a 1-mass soldier will push a 0.1-mass enemy much easier than a 10-mass soldier would push a 1-mass enemy. In the case of mounted units this stat is of no importance, as it is the mount's mass that's taken into account (see descr_mount.txt).
  * **radius** (may not be visible) : (**TODO: More detail needed**) Hidden attribute radius of the unit. The default value is 0.4. It's the area surrounding each single soldier that he "occupies" as the engine perceives it (not visually that is). Small radius makes a unit fight better, in that it allows soldiers to fight more closely to each other, resulting in more men of the small-radius unit fighting against fewer of the enemy one's.
  * **height** (may not be visible) : (**TODO: More detail needed**) Hidden attribute height of the unit. The default value is 1.7. It represents the height of the unit's soldiers (again not visually). Little is known concerning the exact way that height functions, but it is known that the higher it's value, the weaker the unit.

  **Allowed Variables**

  * See above for details on the various variables required

  eg. ```soldier          barb_peltast_gaul, 40, 0, 0.9```

---

### mount

```Code: mount            mount```

Type of mount used (if any) by the unit. The mount's stats are in the *descr_mount.txt* in the data folder. Mounted units with ridden mounts (horsemen) get an average of +8 against all infantry, varying from case to case according to specific stats of units each time.

**Allowed Variables**

 * See above for details on the various variables required

eg.
```
mount            medium horse
mount_effect     elephant -8, camel -4
```

(**TODO: More detail needed**)

---

### mount_effect

```Code: mount_effect     mount_effect(s)```

Unit's bonuses against mounted units (if any). There can be bonuses against horses, elephants, chariots and camels.The bonus may be against an entire class of mounts (eg elephants) in which case it's applied versus all of the types of the class or against only a specific type, but type-bonus stacks with class-bonus. They are applied directly and stack with any other bonuses, like ones derived from spear attributes. Note that these are modifiers to the unit's attack and that they will be applied to a secondary weapon too if one exists, but they do not affect missile weapons at all. Max number of valid mount effects is 3, extra will be ignored.

**Allowed Variables**

 * See above for details on the various variables required

eg. ```soldier          barb_peltast_gaul, 40, 0, 0.9```

(**TODO: More detail needed**)

---

### officer

```Code: officer          officer_model(s)```

Unit officers' model type as referenced in *descr_model_battle.txt*. Up to nine (**increased from three in 2.0.4**) officer lines may exist per unit, but note that officers may not be assigned to elephants or chariots.

**Allowed Variables**

 * See above for details on the various variables required

eg. ```officer          barb_standard```

(**TODO: More detail needed**)

---

### animal

```Code: animal           animal```

Type of animal used (if any) by the unit. References descr_animals.txt, but here it's coded in plural form. **Only one of animal, ship and engine lines may be used at a time.**

**Allowed Variables**

 * See above for details on the various variables required

eg. ```animal           wardog```

 (**TODO: More detail needed**)

---

### engine

```Code: engine           engine```

Type of engine used (if any) by the unit. References *descr_engines.txt*. **Only one of animal, ship and engine lines may be used at a time.**

**Allowed Variables**

 * See above for details on the various variables required

eg. ```engine           ballista```

---

### ship

```Code: ship           ship```

Type of ship used (if any) by the unit. References *descr_ship.txt*. **Only one of animal, ship and engine lines may be used at a time**.

**Allowed Variables**

 * See above for details on the various variables required

eg. ```ship             light warship```

---
### attributes


```Code: attributes       unit_attribute(s)```

The unit's attributes. The complete list is:

 * **sea_faring**: unit can board ships
 * **Stealth Attributes**: defines where the unit can hide. If absent, it means that the unit won't be able to hide at all.
	 * **hide_forest**: Basic ability to hide in forests
	 * **hide_improved_forest**: Improved ability to hide in forests
	 * **hide_long_grass** Can hide in long grass
	 * **hide_anywhere**:  "hide_anywhere" includes all the above abilities.
 * **can_sap**: unit can dig tunnels under walls during assaults using sap points
 * **Frighten Ability** unit causes fear to certain nearby units of the specified type. Both combined means the unit frightens all enemy (generals included)
 	* **frighten_foot**: demoralises nearby infantry units (not ones with javelins, though)
 	* **frighten_mounted**: frightens nearby cavalry and elephant units
 * **can_run_amok**: unit may go out of control when riders lose control of animals (usually when the unit's casualty ratio is high and the morale low or when being attacked with fire)
 * **general_unit**: unit can be used for a named character's bodyguard (note that this now also sets the bodyguard for recruitable generals of which there can be multiple instances of this attribute in the same faction though the first instance will always be the family-member bodyguard). Note also that the AI will never recruit units with the general_unit attribute.
 * **general_unit_upgrade "major_event"**: New for 2.0.4 - Unit can be used as upgraded bodyguard for named characters, after the a major_event (eg Marius' reforms) are triggered. A unit with this attribute must be listed in the file after the regular bodyguard unit. 
 * **cantabrian_circle**: unit has this special ability. More information about the feature can be found on the [Battle and Campaign Formulae](/documentation/feature_guides/Battle_and_Campaign_Formulae.md) page.
 * **no_custom**: unit is not available in custom battles
 * **command**: unit carries a legionary eagle, and gives morale bonus to nearby units (not the unit itself). Also can trigger lost/captured eagle news events. More information about the feature can be found on the [Battle and Campaign Formulae](/documentation/feature_guides/Battle_and_Campaign_Formulae.md) page.
 * **screeching_women**: unit has this special ability, which reduces the morale of nearby enemy units. More information about the feature can be found on the [Battle and Campaign Formulae](/documentation/feature_guides/Battle_and_Campaign_Formulae.md) page.
 * **mercenary_unit**: unit is a mercenary unit available for hire to all factions in certain regions. It also prevents a unit from replenishing losses after battle, forces it to use the 'merc' texture and sprite lines in DMB for all its faction owners and the text-tag 'Varies' instead of the unit recruitment cost on the unit info card. In Alexander mercenaries can be faction-specific (availability set in descr_mercenaries.txt).
 * **Hardiness**: reduces the speed at which stamina is depleted and also increases its regeneration rate. **NOTE**: These modifiers can be stacked to make additional levels of hardiness as needed.
	 * **hardy**: -2 fatigue modifier
	 * ***very_hardy**: -4 fatigue modifier
	 * **extremely_hardy** - NEW RR ATTRIBUTE (2.0.4): -8 fatigue modifier
	* **inexhaustible** - NEW RR ATTRIBUTE (2.0.2): Disables stamina for this unit without going into arcade mode.
 * **warcry**: More information about the feature can be found on the [Battle and Campaign Formulae](/documentation/feature_guides/Battle_and_Campaign_Formulae.md) page.
 * **druid**: More information about the feature can be found on the [Battle and Campaign Formulae](/documentation/feature_guides/Battle_and_Campaign_Formulae.md) page.
 * **power_charge**: increases the time during which a unit is 'charging' (as opposed to being 'in melee'), therefore extending the period during which the unit receives its charge-bonus.
 * **can_swim (RR 2.0.2 and later added support to base Rome)**: unit can swim rivers in battle mode (or walk in the case of some units).
 * **is_peasant (RR 2.0.2 and later added support to base Rome)**: 80% chance that it will be dropped from the selection list when generating a rebel garrison and they also count for half their numbers when suppressing unrest when garrisoned.
 * **can_horde (RR 2.0.2 and later added support to base Rome)**: unit can be part of a horde when one is created, and may be disbanded if a horde army decides to settle
 * **legionary_name (RR 2.0.2 and later added support to base Rome)**: assign a legionary name (based on region) and number to the recruited unit. The legionary element of the name is hardcoded.
 * **infinite_ammo** - NEW RR ATTRIBUTE (2.0.2): Allows a unit to have infinite ammo without going into arcade mode.
 * **non_scaling** - NEW RR ATTRIBUTE (2.0.4): Unit size unaffected by unit scale, allows creation of fixed number units for example a hero unit or supplies?

**Allowed Variables**

 * See above for details on the various variables available.

eg. ```attributes       sea_faring, hide_improved_forest, hide_long_grass```

—
### formation


```Code: formation        hor-cl-spacing, ver-cl-spacing, hor-ls-spacing, ver-ls-spacing, ranks, formation(s)```

The details of the unit's default formation:

* **horizontal close spacing**: Side-to-side distance between soldiers in close formation in metres
* **vertical close spacing**: Front to back distance between soldiers in close formation in metres
* **horizontal loose spacing**: Side-to-side distance between soldiers in loose formation in metres
* **vertical loose spacing**: Front-to-back distance between soldiers in loose formation in metres
* **ranks**: Default number of the unit's ranks (depth of its formation)
* **formation(s)**: Available formations of the unit. Can be one or two of the following:
  * **square** (normal)
  * **wedge** (*1* attack bonus)
  * **phalanx** (unbeatable from the front, very weak from sides and rear)
  * **testudo** (weak in melee, good against missiles)
  * **horde** (good vs missiles, bad in melee)
  * **schiltrom** (*2* - immobile, but excellent vs mounts)
  * **shield_wall** (*2* - melee bonus from the front, weak from rear and sides).

  ***Note 1***: Certain formations are used only for certain unit types (eg wedge only for cavalry).
  ***Note 2***: Sciltrom and Shield Wall are both now supported in the base game.

—-
### stat_health

```Code: stat_health      hp, hp_extra```

Details of the unit's hitpoints.

* **hp**: Hit points of the regular soldiers of the unit. Max value is 15, as everything higher will still be considered 15.
* **hp_extra**: Hit points of animals of the unit. Note that ridden horses are not assigned separate hitpoints. Max value is 15, as everything higher will still be considered 15.

**Note**: Even though `hp_extra` is ignored during battle-map mode for non-animal units, it is actually taken into account for auto-resolve for all units which can assist when modding auto complete stats.

—-
### stat_pri

```Code: stat_pri         atk, chrg, msl_type, msl_rng, msl_ammo, wpn_type, wpn_tech, dmg_type, snd_type, min_delay, lethality```

The unit's offensive stats.

* **attack**: Attack rating of the unit's primary weapon (if unit has missiles, those are its primary weapons). Note that 'Easy' difficulty level gives the AI a -4 attack; 'Medium' offers no advantages/penalties; 'Hard' grants the AI a +4 attack bonus and 'Very Hard' grants the AI a +7 attack bonus. Max value for attack is 63. Anything higher will still be considered 63.
* **charge**: Charge bonus of the primary weapon, added to the unit's attack when charging. As charge is slowed down and unit gets into 'proper' melee, the bonus stops being applied. Min value is 1 and max charge bonus value is 63, as everything higher will be considered 63. Missile units should have this equal to their desired secondary weapon charge bonus, as to not confuse players, since the charge bonus used by the engine will be the one of the melee weapon, while the one displayed on the unit card will be the missile weapon's.
* **missile_type**: Missile type used by the unit. Can be one of the projectiles defined in the descr_projectile_new.txt.
* **missile_range**: Max range of the unit's missile weapon. The max limit is determined by the specific missile type's velocity and min_angle, max_angle. Anything higher than this max value will be reduced to it. (see descr_projectile_new.txt) Min value is 20 (javelins).
* **missile_ammo**: Ammunition per unit's soldier. Minimum value is 2 (0 is of course acceptable as well).
* **weapon_type**: Unit's weapon type. Can be: melee, thrown, missile or siege_missile.
* **weapon_tech**: Unit weapon's tech type. Can be: simple, other, blade, archery or siege.
* **damage_type**: **Todo**
* **sound_type**: Sound type when the unit's weapon hits. Can be one of: none, knife, mace, club, axe, sword, or spear (ref: descr_sounds_weapons.txt).
* **min_delay**: Minimum delay between weapon attacks, measured in 1/10 of seconds. It is the minimum time allowed between the beginning of an attacking animation and the beginning of the next one. It only applies to foot melee skeletons.
* **lethality**: Percentile chance of a soldier to kill an enemy (assuming his strike has found its target). The higher the lethality, the more the kills and the less the knock-downs/knock-backs during a battle. Greatly affects the speed at which melee battles are resolved, since higher lethality means less missed hits and greater casualties in short time. It is not used in ranged combat.

—-
### wpn_attributes

```Code: stat_pri_attr    wpn_attributes```

Attributes of the unit's primary weapon. The complete list is:

* **ap**: armour piercing. Attacks take into account only half of the defender's armour value (not defence or shield). Results are rounded up.
* **bp**: body piercing. Missile can pass through men and hit those behind.
* **prec**: Missile weapon is only thrown just before charging into combat, though a unit may expend all its ammo if on 'fire at will' mode and the human player has not targeted an enemy unit.
* **thrown**: Missiles have a big bonus against elephant and chariot units, as they get stronger with every HP of the target. Also, the delay between volleys is reduced by 20%. Only missile units should use this and only for their missile weapons!
* **launching**: attack may throw target men into the air.
* **area**: attack affects an area (and everyone within it), not just one man.
* **long_pike**: Use very long pikes. Phalanx capable units only. Removed in BI.
* **short_pike**: Use shorter than normal spears. Can be used with phalanx ability or without it. The unit is still considered as infantry (and not spearmen). Grants a bonus of 8 versus mounted units, but due to the qualities of the formation (spacing, cohesion, etc) it seems that it roughly gets an extra -1 versus everyone. It also seems that short_pike overrides light_spear and spear, so that when the two are combined spear/light_spear is ignored, though due to it's own qualities it does slightly affect combat, depending on the units involved. Additionally, short_pike is required for units using the 'schiltrom' formation, because when in schiltrom and without short_pike, the soldiers will very rarely attack enemies.
* **spear_bonus_x**: 'x' may be any even number between 4 and 12 inclusive. Must be accompanied by spear or light_spear attributes, otherwise it has no effect. It offers a bonus to attack vs mounts which stacks with the default bonuses of these two attributes.
* **light_spear**: Gives default bonus of +8 to defence vs cavalry, and penalty of -4 to defence vs. infantry. Offers less pushing power than spear.
* **spear**: Gives default bonus of +8 to attack vs cavalry, and penalty of -4 to attack vs. infantry. Offers more pushing power than light_spear. Units with "spear" attribute tend to lose cohesion and break lines (due to the extreme pushing power) with undesired results, so use is advised only with cohesive formations/attributes like short_pike, shield_wall, phalanx etc.

—-
### stat_sec

```Code: stat_sec         same as stat_pri```
```Code: stat_sec_attr    same as stat_pri_attr```

Same for the unit's secondary weapon as the primary (c.f.). Certain units like elephants, handlers, chariots and siege-machines use this line for the stats of the animals/engines.

**NOTE**:Let it be noted that the upgrades of the secondary weapon are bugged, in that only the primary weapon tech is taken into account when upgraded. Any change applied to it will also be applied to the secondary weapon, regardless of the weapon_tech of the latter. Also, units with secondary weapons will use that to charge, and once in proper melee will switch back to their primary (units classified as spearmen will keep using their sec if enemy gets very close).

—-
### stat_pri_armour

```Code: stat_pri_armour  armour, def_skill, shield, sound```

The unit's defensive stats.

* **armour**: Unit's armour value. Taken into account in all occasions (soldier attacked from any direction, melee and ranged). It measures the amount of protection a soldier's armour offers. Max value is 63 and everything higher will be considered 63.
* **def_skill**: Unit's defensive skill, taken into account only in melee and only against attacks from the front or the right side. It doesn't affect defence against missiles. It represents a soldier's ability to parry(rather than block) and dodge strikes. Max value is 63 and everything higher will be considered 63.
* **shield** : Unit's shield value, taken into account against both ranged and melee attacks, but only when they come from the front or the left side. Against missiles from the front it offers twice the protection it's value suggests. Measures the blocking capabilities of a unit's shield. Max value is 31 and everything higher will be considered 31.
* **sound**: Sound played when unit gets hit. Can be: flesh, leather, or metal.

——
### stat_sec_armour

```Code: stat_sec_armour  same as stat_pri_armour(no shield)```

Same as stat_pri_armour. The stats of the unit's animals' or vehicles' defences.

**Note**: Ridden horses do not have a separate defence, and that if a vehicle/animal's defence skill is set to 0, its HP are considered to be 1. Of course there is no shield entry.

——
### stat_heat

```Code: stat_heat        heat_penalty```

Fatigue penalties applied to the unit due to heat. It measures how fast will its fatigue be depleted and how slowly it will regenerate. Ranges from -2 to 5, with 5 issuing the greatest penalty for the unit. The hotter the climate (aka the greater the climate_heat value of the map), where the battle takes place, the more important it becomes. In mild climates (low climate_heat of the map), it makes little to no difference.

—-

### stat_ground

```Code: stat_ground      scrub_mdf, sand_mdf, forest_mdf, snow_mdf```

Combat modifiers applied to unit only when it fights on the respective specified ground type. Positive numbers are bonuses, negative are penalties. They range from 8 to -8 and they have a 1 to 1 point relationship with attack.
 * **scrub_modifier**: self-explanatory (it's quite tricky to know for sure when you are fighting on scrub)
* **sand_modifier**: self-explanatory
* **forest_modifier**: self-explanatory
* **snow_modifier**: self-explanatory

—-
### stat_mental

```Code: stat_mental      morale,discipline,training```

Details of the unit's mentality.

* **morale**: Unit's morale or else how easy is for a unit to lose heart and flee the battle. The greater the value, the less likely the unit will rout. Note that morale bonuses from buildings in campaign mode are bugged and do not work. The following tags are attached by hardcode to morale values: 1-2 -> 'Poor morale', 8-11 -> 'Good morale', 12+ -> 'Excellent morale'
* **discipline**: Unit's discipline level, which determines the amount of morale lost when morale shocks occur (death of general, flanked, etc). Can be low, normal, disciplined, impetuous or berserker. Disciplined units are harder to lose morale. Berserker units can (obviously) go berserk and impetuous units may charge without orders.
* **training**: Unit's training level, which affects how tidy its formation is. Can be untrained, trained or highly_trained. Untrained units will have the most disorderly formations.

——

### stat_charge_dist

```Code: stat_charge_dist charge_distance```

Determines the distance from target at which a unit will begin charging (start it's charging animation that is) in metres.

—-
### stat_fire_delay

```Code: stat_fire_delay  fire_delay```

The extra delay, over that imposed by animation, between the unit's volleys. Vanilla has them all 0.

**Todo** According to some mods like Darth's, setting values like -50000 or 5000 depending on unit type improves combat function and solves the foot-missile-bug, but these haven't been confirmed by FATW or by any other major mod. Testing suggests that setting this value to anything else than 0, breaks cavalry charges, as it causes the riders to not always lower their spears when charging, even when the charge is made properly.

### stat_food

```Code: stat_food        ?, another_?```

**Todo** Unused?

—-
### stat_cost

```Code: stat_cost        turns,recruit,upkeep,wpn_upg,arm_upg,cb_cost```

Details of a units recruitment stats.

* **turns**: Amount of turns needed to train the unit. Max value is 244, anything higher will be ingored.
* **recruit**: Cost to train the unit. Also affects the retraining cost.
* **upkeep**: Price paid every turn for the upkeep of the unit.
* **weapon_upgrade**: Cost to upgrade the unit's weapons (both campaign and custom battles). Affects the retraining cost.
* **armour_upgrade**: Cost to upgrade the unit's armour (both campaign and custom battles). Affects the retraining cost.
* **custom_battle_cost**: Cost to include the unit in your army in custom battles.

—-
### recruit_priority_offset

```Code: recruit_priority_offset [100]```

Newly added in 2.0.4 - In the EDU, you can now put `recruit_priority_offset` followed by a value after `stat_cost`. The value will be the % bias towards recruiting that unit. E.G. `recruit_priority_offset 100` means that unit is twice as likely to be recruited.

——
### ownership

```Code: ownership        faction(s)```

Factions that can recruit the unit in custom battles (assuming no_custom attribute absent) and in campaign (assuming a recruitment line exists in export_descr_buildings.txt). Also allows for unit to be open to bribery to the specific factions.

—-

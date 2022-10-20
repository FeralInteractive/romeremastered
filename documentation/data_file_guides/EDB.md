![Workshop_header_template](/Workshop_header_template.png)
# export_descr_buildings

## Table Of Contents

* [Introduction](#introduction)
* [Hidden resources (Moved to descr_sm_resources.txt)](#hidden-resources-moved-to-descr_sm_resourcestxt)
* [Example format](#example-format)
   * [building](#building)
   * [icon](#icon)
   * [levels](#levels)
   * [levels_specific_building](#levels_specific_building)
      * [Full List of Requirements](#full-list-of-requirements)
   * [capability](#capability)
      * [capability requirements](#capability-requirements)
      * [Faction_Capability](#faction_capability)
   * [construction, cost, settlement_min &amp; upgrades](#construction-cost-settlement_min--upgrades)
* [Notes and additional information](#notes-and-additional-information)
   * [Note on Barbarian Building Trees](#note-on-barbarian-building-trees)
   * [Note on Building Names &amp; Descriptions](#note-on-building-names--descriptions)
   * [Note on Multiple Temples &amp; Indestructability of Buildings](#note-on-multiple-temples--indestructability-of-buildings)
   * [Note on Associated Files](#note-on-associated-files)
   * [Tools &amp; Other Resources](#tools--other-resources)

## Introduction

This guide is influenced by the guide created by Dol Guldur on the [TW Org forums](https://forums.totalwar.org/vb/showthread.php/50439-Guide-The-Complete-EDB-Guide-%28WIP%29). We thank Dol Guldur, Aradan and all other contributors to the original game guide.

We actively encourage modders to update this document with useful information and we can merge in any changes so this document can be the main resource for editing the EDU in Rome Remastered.

| Limit Type | Original Rome Limit | Rome Remastered Limit Resolution | Status | Notes |
|-|:-:|:-:|:-:|-|
| Overall building tree number | 64 | _Virtually Unlimited*_ | `2.0.4` | |
| Levels per building tree | 9 | _Virtually Unlimited*_ | `2.0.4` | |
| Hidden resources | 64 | _Virtually Unlimited*_ | `2.0.2` | |
| Unit buildable per city | 32 | _Virtually Unlimited*_ | `2.0.4` | |

 _*'Virtually Unlimited'_ allows for a theoretical value of `4294967296` entries.

## Building Classifiction Options

With the chnages to buildking limits and features in 2.0.4 you can now have custom building classifications. This tells the game which category of the building browser to use.

The can be added inside `building` and before first `levels` and is explained in more detail at the top of the EDB file.

```
; classification option (inside `building` and before first `levels`)
; Example:
;	 classification core|defence|military|trade|water|culture|religious (deprecated, but recognised:fortification|infrastructure|other)
; This tells the game which category of the building browser to use.
; RomeHD has subtly different classifications than the original, so note the deprecated classifications, they wont work anymore.
; If no classification is specified, the game will guess based on the building name, which works for all the unmodded buildings.
; Automatic classification:
;   core_building
;	   core
;   defenses
;	   defence
;   barracks|equestrian|missiles|smith|despotic_law
;	   military
;   market|port_buildings|hinterland_*|caravans
;	   trade
;   health
;	   water
;   academic|amphitheatres|theatres|taverns
;	   culture
;   temple_*|christian_acedemic
;	   religious
; Explicit classification overrides the automatic classification, so if you don't like the above classifications, you can overule them.
```

## Building Exclusivity

In the original game some features like temples had a hard coded exclusivity feature so if you built one type of temple the others are no longer avaialble. This has been extracted into the EDB file so any buildings can have exclusivity rules and you can have multiple different groups of exclusivity for diferenmt groups if you so wish.

The temples in the base game now use this feature. Near the top of the EDB you will see this section where you can add in as many custom tags as you want, these form the basis of the groups. You can then use these tags in the conditions using the `no_building_tagged` condition.

```
;;exclusivity tags, used for the "no_building_tagged" condition
tags
{
	temple
}
```

You could then add this check to a temple in the following manner:

```
building temple_of_battle
{
	tag temple
	icon religion
	levels temple_of_battle_shrine temple_of_battle_temple temple_of_battle_large_temple temple_of_battle_awesome_temple temple_of_battle_pantheon 
	{
		temple_of_battle_shrine requires no_building_tagged temple queued 
		{
```

However to make a feature like this clearer for users you'll want to combine it with the feature below (Custom Strings for conditions) that allows you to display custom strings to the player so they get told exactly what the buildoing conditions are. 

## Custom Strings for conditions

This feature allows you to create custom strings that you can then have display in the building info panels and tooltips. You can give multiple conditions a string (or allow conditions with normally no string to display one).

You can define multiple alias' items for multiple buildings without limits. Below contains an example of how the feature is used to display a custom string telling users that they need to destroy and existing temple before they can build one from a different branch.

```
;;alises, give multiple conditions a string (or allow conditions with normally no string to display one)
; alias roman_marian_reforms_triggered
; {
; 	requires factions { roman, } and major_event "marian_reforms"
;
; 	display_string roman_marian_reforms ;;gets a string from expanded_bi
; 	;; if display_string isn't included it will just display the strings for the events normally
; }

alias no_other_temple
{
	requires no_building_tagged temple queued

	display_string SMT_TECH_TREE_THREAD_REQUIRES_TEMPLE_DESTRUCTION
}
```

You then add the `display_string` to the `expanded_bi.txt` file in the `data/text/` file path.

```{SMT_TECH_TREE_THREAD_REQUIRES_TEMPLE_DESTRUCTION}	Building this item requires the destruction of an existing religious building```

You can then use this tag and the alias later in the EDU to make sure not only are temples excluisve so you can only build one but platyers also have a message in the building info and tooltips explaining how it works. This string is hooked into the localisation system so can also be fully localised.

```
building temple_of_battle
{
	tag temple
	icon religion
	levels temple_of_battle_shrine temple_of_battle_temple temple_of_battle_large_temple temple_of_battle_awesome_temple temple_of_battle_pantheon 
	{
		temple_of_battle_shrine requires factions { dacia, thrace, } and no_other_temple 
		{
```

## Hidden resources (Moved to descr_sm_resources.txt)

The declaration of hidden resources is now done in the [descr_sm_resources.txt](/documentation/data_file_guides/descr_sm_resources.md) file. The maximum number of resources is practially unlimited and you can also have more control over the resouyrce types. You can also use hidden reosurces inside scripting. See link above for more details on resources.

## Building Tree format

Each building tree is made up of nested elements. They are arranged in the folowing format

* `building` (name of a series of buildings)
 * `icon` (define icon used by building browser for this building tree)
 * `levels` (define the levels and names of the buildings in this series)
   * `levels_specific_building` (each level named in the above line has it's own subsection)
     * `capability` (what capabilities this specific level of building has)
     * `construction` (turns needed to construct)
     * `cost` (cost in dinarii to purchase)
     * `settlement_min` (minimum settlment level required to construct)
     * `upgrades` (does it upgrade an existing level or building defined by `levels_specific_building` )

You will then find listed in the EDB file the building tree for each building type complete with a block of code for each building. You may have virtually unlimited trees and levels (buildings) each though spread over a maximum of 5 (see note) settlement levels (though buildings attached to villages will not show up on the building browser).

NOTE: This number can be increased beyond 5 but it will break the visuals in the building browser and is not recommended.     

## Example format

```
building missiles
{
	icon ranged
	levels practice_field archery_range catapult_range siege_engineer 
	{
		practice_field requires factions { barbarian, carthaginian, eastern, parthia, egyptian, greek, roman, } 
		{
			capability
			{
				recruit "carthaginian peltast"  0
				recruit "barb peltast gaul"  0
				recruit "barb peltast german"  0
				recruit "barb slinger briton"  0
				recruit "barb archer dacian"  0
				recruit "barb archer scythian"  0
				recruit "carthaginian peltast"  0
				recruit "carthaginian archer"  0
				recruit "east peltast"  0
				recruit "east slinger"  0
				recruit "egyptian peltast"  0
				recruit "egyptian slingers"  0
				recruit "greek peltast"  0
				recruit "roman velite"  0  requires not major_event "marian_reforms" 
				recruit "roman light infantry auxillia"  0  requires major_event "marian_reforms" 
			}
			construction  3 
			cost  1200 
			settlement_min large_town
			upgrades
			{
				archery_range
			}
		}
```

### building
**building** - This is the building type. In a mod you can give this any custom name you wish as long as you don't include spaces. With RR (2.0.4) there is no practical limit on the number of buildings (previously 64).

```
building missiles
{
```

**NOTE:** Originally you could only can designate your own names for the building type should you wish to not make them universally available to all factions/cultures. However, core_buildings (aka government buildings), walls and hinterland buildings (roads, mines, and farms) could not be factionally or culturally designated (though some of their levels may be excluded from certain cultures/factions).

With the update to 2.0.4 this has been alters - Additional details and examples will be added in the future. (TODO)

### icon
**icon** - This tells the game which category of the building browser to use.

```
    icon ranged
```

Possible options allowed are:

```
; classification option (inside `building` and before first `levels`)
; Example:
;	 classification core|defence|military|trade|water|culture|religious (deprecated, but recognised:fortification|infrastructure|other)
; This tells the game which category of the building browser to use.
; RomeHD has subtly different classifications than the original, so note the deprecated classifications, they wont work anymore.
; If no classification is specified, the game will guess based on the building name, which works for all the unmodded buildings.
; Automatic classification:
;   core_building
;	   core
;   defenses
;	   defence
;   barracks|equestrian|missiles|smith|despotic_law
;	   military
;   market|port_buildings|hinterland_*|caravans
;	   trade
;   health
;	   water
;   academic|amphitheatres|theatres|taverns
;	   culture
;   temple_*|christian_acedemic
;	   religious
; Explicit classification overrides the automatic classification, so if you don't like the above classifications, you can overule them.

```

### levels
 Now the levels of the building type are listed (space-delimited & as of 2.0.4 unlimited).

```
    levels practice_field archery_range catapult_range siege_engineer
    {
```  

### levels_specific_building

The tree then lists a block of code for each building (`practice_field`). Continuing from our example above we will look at the first level of the "building missiles" tree, the `practice_field`:

**IMPORTANT**: As part of the culture improvements to culture functionality and limits in the 2.0.4 patch the culture previously called `ct_carthage` has been renamed to `carthaginian`. You will need to update any older mods with this new culture when using 2.0.4 or later.

```
practice_field requires factions { barbarian, carthaginian, eastern, parthia, egyptian, greek, roman, }
{
  ```
  
The first line states the conditions necessary to be satisfied in order for the building to be available for construction. 

All factions reside within the 6 named cultures (which are now fully moddable), and so this particular building can be built by all factions in the base game. Any combination of factions/cultures can be listed. 

Both visible and hidden resources can be used as requirements as may "building_present_min_level x y" where x is the building type and y the level of that building type. This latter simply requires a certain minimum level of building of a building type to be present in that settlement before the practice_field can become available for construction. The connector "and" can be used to compound requirements, for example:

```
practice_field requires factions { barbarian, roman, } and resource iron and hidden_resource woodland and building_present_min_level market trader
{
```
**NOTE** If you are wanting to make more complex requirements the parsing logic is as follows:

```Negation binds to the nearest term, the binary ops bind right-associative, so 'not A and B or not C and D' is '(not A) and (B or ((not C) and D))'.

No parenthesis is supported - probably won't be needed, such terms can just be expanded anyway.```

#### Full List of Conditions

* `resource` - See [descr_sm_resources.txt](/documentation/data_file_guides/descr_sm_resources.md) file
* `hidden_resource` - See [descr_sm_resources.txt](/documentation/data_file_guides/descr_sm_resources.md) file
* `building_present <building name> [queued] [factionwide]` - checks if a building exists at any level. **2.0.4 Feature**: The game now supports:
	 * `queued` - will also check the building queue not just constructed buildings
	 * `factionwide` - will check for the existence of a building across all settlments controlled by the faction allowing for buildings that can only be built once per faction.
* `building_present_min_level <building name> <level> [queued] [factionwide]` - checks if the building exists at at least the specified level. **2.0.4 Feature**: The game now supports:
	 * `queued` - will also check the building queue not just constructed buildings
	 * `factionwide` - will check for the existence of a building across all settlments controlled by the faction allowing for buildings that can only be built once per faction.
* `marian_reforms` - **FEATURE REMOVED AND REPLACED IN 2.0.4**
* `major_event "<event name>"` - checks if the given major event has triggered for this faction. As major events are now moddable and you can have multiple events this command replaces the hard coded `marian_reforms` conditions
* `factions { <all/culture/faction name>, }` - checks if the settlement is controlled by a given faction.  **2.0.4 Feature**: The game now supports:
	 * `culture` - you can use any custom culture for the checks
	 * `all` - you can use all if you just want it to be true for all factions 
* `port` - This returns true in coastal areas with ports assigned (i.e. in `map_regions.tga`). It can be used as a condition for buildings and capabilities, including units.
* `is_player` **2.0.2 Feature**: Allows you to use the `requires` function to state if a building is availble for only the player or only the AI factions. This will allow for the creation of special buildings that mods can use to assist the AI factions, or provide depth to the human player experience without overly complicating the AI build trees.
* `is_toggled "<toggle name>"` **2.0.2 Feature**: checks if the given gameplay toggle is turned on. This allows you to unlock items based on any of the classic/remastered toggle settings.
* diplomacy <allied/protector/protectorate/same_superfaction/at_war> <faction name> - checks the relationship of the settlement's owner with the given faction
* `building_factions { <all/culture/faction name>, }` **2.0.4 Feature**: checks if the building was built by a given faction. This allows modders to restrict units or building recuitment based on the faction that built the building instead of the faction that controls the building. This will allow factions to have the ability to recuit certain units via conquest only and not via construction.
* `capability <capability name> <number>` **2.0.4 Feature**: checks if the settlement has a capability of at least that amount. This allows you to conditionalise items being available based on settlment capabilties like public order etc 
* `resource <resource name> [factionwide]` **2.0.4 Feature**: checks if the settlement has that resource can also use `factionwide` as a check to check if the resource is found withing the empire.
* `no_building_tagged <tag name> [queued] [factionwide]` **2.0.4 Feature**: As explained in more detail in the prior section (TODO link) this checks that no building with this tag exists (lower levels of this building within the same settlement are not counted). This is used in the base game to restricty temples to only one type. This feature also supports the following optional items:
	 * `queued` - will also check the building queue not just constructed buildings
	 * `factionwide` - will check for the existence of a building across all settlments 
* `religion <religion name> <comparison operator (i.e. >=)> <number>` **2.0.4 Feature**: checks how much influence a religion has in this settlement.
* `majority_religion <religion name>` **2.0.4 Feature**: checks if the religion is the majority (highest influence) religion in the settlement
* `official_religion` <religion name> **2.0.4 Feature**: checks if the religion is the official religion in the settlement



**NOTE:**
* The connectors "or" and "not" can also be used in addition to "and". X represents a faction, culture, a list of the same - or all ("all,").
* **2.0.4 Feature**: All of the above can be used as capability requirements too - using the building_present/building_present_min_level for recruitment lines as will no longer cause a CTD when the player uses the right-click feature added in later versions of RTW.


### capability

The Capability section lists the capabilities (i.e. the recruitment capability and building effects) of any given settlement which contains this building. The pool of potential requirements that can be attached to both recruitment and effect lines are basically the same as those used for the building's construction requirement (see above).

```
capability
{
recruit "carthaginian peltast" 0 requires factions { spain, }
recruit "barb peltast gaul" 0 requires factions { gauls, }
recruit "barb peltast german" 0 requires factions { germans, }
recruit "barb slinger briton" 0 requires factions { britons, }
recruit "barb archer dacian" 0 requires factions { dacia, }
recruit "barb archer scythian" 0 requires factions { scythia, }
recruit "carthaginian peltast" 0 requires factions { carthage, }
recruit "carthaginian archer" 0 requires factions { numidia, }
recruit "east peltast" 0 requires factions { armenia, pontus, }
recruit "east slinger" 0 requires factions { parthia, }
recruit "egyptian peltast" 0 requires factions { egyptian, }
recruit "egyptian slingers" 0 requires factions { egyptian, }
recruit "greek peltast" 0 requires factions { greek, }
recruit "roman velite" 0 requires factions { roman, }
recruit "roman light infantry auxillia" 0 requires factions { roman, } and hidden_resource gondor
recruits_morale_bonus bonus 1 requires factions { dacia, }
}
```

**Note:**
* The "0" listed with recruits refers to the level of Experience the unit begins with when first recruited. It can of course be any number between 0 and 9.

#### capability requirements

Full List of Building Effects

 * `population_growth_bonus`: Pop. growth 1-25 (0.5-12.5%)
 * `population_loyalty_bonus`: Unused has no functionality
 * `population_health_bonus`: public health 1-x (5-x%)
 * `trade_base_income_bonus`: Increases trade goods) 1-5 (1-5) - adds 10% to base value of land trade & sea exports
 * `trade_level_bonus` **2.0.4 Feature**: Affects land trade only (previously non-functional in original game)
 * `trade_fleet` - adds additional overseas trade routes
 * `taxable_income_bonus`: Boosts tax income by stated percentage;1-100 (1%-100%)
 * `mine_resource` - generates income from mining
 * `farming_level`: Plus 0.5% pop. growth and plus 80 income (average harvest) per point - equivalent to base farm level in `descr_regions.txt`) 1-5 (1-5)
 * `road_level` - upgrades roads
 * `gate_strength` - upgrades gates
 * `gate_defences` - adds burning oil if >0
 * `wall_level` - upgrades walls
 * `tower_level` - ballista towers if >1, arrow towers else
 * `armour`: Armour upgrade 1 (1)
 * `stage_games` - allows staging games
 * `stage_races` - allows staging races
 * `fire_risk` aka `population_fire_risk_bonus`: Unused has no functionality
 * `weapon_simple` - provides weapon upgrades
 * `weapon_missile` - provides weapon upgrades
 * `weapon_bladed` - provides weapon upgrades
 * `weapon_siege` - provides weapon upgrades
 * `weapon_other` - provides weapon upgrades
 * `upgrade_bodyguard` - unused
 * `recruits_morale_bonus` **2.0.4 Feature**: Increases morale of units recruited 1-4 (1-4) (previously non-functional in original game)
 * `recruits_exp_bonus`:  Upgrades XP of units recruited 1-5 (1-5)
 * `happiness_bonus`: Public order due to happiness 1-x (5-x%)
 * `law_bonus`: Public order bonus due to law 1-x (5-x%)
 * `construction_cost_bonus_military` - building cost reduction
 * `construction_cost_bonus_religious` - building cost reduction
 * `construction_cost_bonus_defensive` - building cost reduction
 * `construction_cost_bonus_other` - building cost reduction
 * `construction_time_bonus_military` - building time reduction
 * `construction_time_bonus_religious` - building time reduction
 * `construction_time_bonus_defensive` - building time reduction
 * `construction_time_bonus_other` - building time reduction
 * `extra_recruitment_points` - additional recruitment points
 * `extra_construction_points` - additional construction points
 * `recruit` - allows recruiting units
 * `agent` - allows recruiting agents
 * `religious_belief` - increases religious conversion
 * `religious_order` - suppresses religious unrest
 * `agent_limit_settlement` - sets the amount of a given agent type that can be recruited here (bonus does not work with this)
 * `dummy` - does nothing, but allows specifying a string



Full List of Building Effects 2.0.2

* `weapon_simple` (upgrades melee (light) weapons) 1 (1)
* `weapon_bladed` (upgrades bladed (heavy) weapons) 1 (1)
* `weapon_missile` (upgrades missile weapons) 1-5 (1-5)
* `weapon_siege` (upgrades siege weapons) *
* `weapons_other` (?) *
* `upgrade_bodyguard` (improves general's bodyguard) ? * (comes into effect only after Marian Reforms)
* `trade_fleet` (trade fleets) 1-3 (1-3) [5]
* `mine_resource` (income from mining) 1-4 (1-4) [5] - values above 4 also work and create greater income
* `road_level` (improved roads and trade) 0-2 (0-2) [5]
* `gate_strength` (gates) 1-2 (reinforced, iron-bound)[1] [see also 4]
* `gate_defences` (gate defence) 0 (scorched sand/boiling oil)[2] [see also 4]
* `tower_level` (towers) 1-2 (arrow, ballista)[3] [see also 4]
* `wall_level` (walls) 0-4 (palisade, wooden, stone, large stone, epic stone) [4]
* `stage_games` (allows gladiatorial games) 1-3 (1-3) [5]
* `stage_races` (allows races) 1-2 (1-2) [5]
* `religious_belief` [pagan/zoroastrian/christianity] 1-x (5-x%)
* `construction_cost_bonus_military` (percentile cost reduction for recruitment buildings) 1-100 (1-100%)
* `construction_cost_bonus_religious` (percentile cost reduction for temples) 1-100 (1-100%)
* `construction_cost_bonus_defensive` (percentile cost reduction for walls) 1-100 (1-100%)
* `construction_cost_bonus_other` (percentile cost reduction for civil buildings but applies to all buildings except religious ones) 1-100 (1-100%)
* `construction_time_bonus_military` (percentile time reduction for constructing recruitment buildings but does not seem to work) 1-100 (1-100%)
* `construction_time_bonus_religious` (percentile time reduction for constructing temples) 1-100 (1-100%)
* `construction_time_bonus_defensive` (percentile time reduction for constructing walls) 1-100 (1-100%)
* `construction_time_bonus_other` (percentile time reduction for constructing civil buildings but also applies to all buildings except religious ones) 1-100 (1-100%)
* `extra_recruitment_points [bonus]` - **NEW for RR** Allows you to give addional recuitment points to a settlment via a building modifier. You can define the bonus in terms of turns.
* `extra_construction_points [bonus]` - **NEW for RR** Allows you to give addional construction points to a settlment via a building modifier. You can define the bonus in terms of turns.

**Notes on above list...**

* [1] wooden are default though not explicitly stated
* [2] does not appear to work; stone walls of any kind come with scorched sand/boiling oil
* [3] default towers are watchtowers though not explicitly stated
* [4] defensive capabilities seems to come with the wall_level regardless of what value they are given! See note below.
* [5] see Quietus's A Comprehensive Rome: Total War Guide (Tools & Other Resources) at the end of this Guide.
* \* untested or unknown use

These investigatiosn are from modders testing the original game, this document will be updated as we get reports of ther behaviour in ROME REMASTERED.

**Notes on format...**

Effects containing the "`_bonus`" element in their name should be coded with a stand-alone "`bonus`" added before the integer even when there is a "bonus" in the effect's name itself. E.G. `population_growth_bonus` bonus 1. However, `population_growth_bonus` bonus +1 also works. Sometimes omitting the "`bonus`" does work but can cause problems - for example, the building scroll may not display the actual bonus (even though it works), and no negative number can be introduced because the engine looks for either an integer (not a number with a "+" or "-" before it in this case) or the word "`bonus`".

In the original file `farming_level`, `armour` and the various weapon effects sometimes carry the stand-alone "`bonus`" and sometimes do not. It would seem that the cumulative and desired effect would necessitate "`bonus`" in each usage, but I do not know why this is not the case in the original file. "Armour 1" (for example) seems to ensure the armour attribute of the unit is 1 above the EDU-stated armour but is not cumulative (however, it does not seem to reduce higher armour so it is not setting the armour variable to "1"). So it also seems sensible to always use the "bonus" before integers for this grouping of effects.

`Trade_fleet`, `mine_resource`, `road_level`, and the `games`, `races` and the four `defensive effects` carry no stand-alone "`bonus`" in the EDB file.

These investigatiosn are from modders testing the original game, this document will be updated as we get reports of ther behaviour in ROME REMASTERED.

**Negative effects...**

`population_growth_bonus` bonus -5 displayed the expected -2.5 in the building scroll but seemed not to affect the settlement population growth indicator on the settlement scroll. The same seems true for law_bonus and happiness_bonus. Religious_belief , however, does seem to work in the negative (this needs more testing). The general principle in actual terms is that a negative will only deduct from a positive; so a settlement with 15% law will drop to 0% law when a negative bonus of -20% is applied and not -5%.

Interestingly, giving negative bonuses to upgrades (in the format `weapon_bladed` bonus -1 for example) removes the unit with that weapon technology from being able to be recruited but is still listed as available in the relevant building scroll. A building that negates the negative bonus will restore the unit's availability for recruitment.

Notes on (hardcoded?) defensive effects...

The following defensive buildings (walls) seem to entail the following effects:

* Palisade - wooden gate - arrow towers
* Wooden wall - reinforced gate - arrow towers
* Stone wall - reinforced gate - arrow towers (incendiary ability) - boiling oil
* Large stone wall - iron gates - arrow towers (incendiary ability) - boiling oil
* Epic stone wall - iron gates - ballista towers (incendiary ability) - boiling oil

These investigatiosn are from modders testing the original game, this document will be updated as we get reports of ther behaviour in ROME REMASTERED.

#### Faction_Capability

These are similar to capabilties except they are applied faction-wide rather than just in one settlement (regional). For example, inserting:

faction_capability
{
construction_time_bonus_defensive bonus 50 requires factions { parthia, }
}
after the Capabilty block of a building (and before the construction line) will, when such a building is built by Parthia, reduce building times of defensive structures (i.e. walls) by half in all Parthian settlements.


### construction, cost, settlement_min & upgrades

The end of each building block comprises the construction time (in turns), the cost, the minimum level of settlement necessary for the building in question to be built, and upgrades (if any). Note that the latter is quite correct to be in the plural - you can list more than one upgrade (top-level buildings should of course have no upgrade listed). Upgrades, can also take conditionals.

```
construction 3
cost 1200
settlement_min large_town
upgrades
{
archery_range
}
}
```

You will find "plugins" at the very end of the building trees - to learn more about these, see Squid's Complete Guide to Plugins here: https://forums.totalwar.org/vb/showthread.php?t=101525

## Notes and additional information

There are a few special cases and other useful links associated with the EDB, you can f

### Note on Barbarian Building Trees

With ROME REMASTERED you can now add 4th and 5th tier buildings to barbarian factions in the original game without any issues or bugs.

### Note on Building Names & Descriptions

The names and textual descriptions of all buildings (inc. the universal ones such as core_buildings) can all be specified per faction (as can building requirements, capabilities and faction capabilities of course). I have written a tutorial on this at https://forums.totalwar.org/vb/showp...2&postcount=56

### Note on Multiple Temples & Indestructability of Buildings

Although some modders have reported that it is the initial prefix of the temple buildings (levels) that allows these buildings to be built in the same settlement as temples, my own research shows that removing the prefix in just the tree name will bring the same result (but without having to change all the other files associated with advice, traits, ancillaries, sound etc.)

Following this same logic we can now add the "hinterland_" prefix to building tree names to make previously destructible buildings indestructible - that is, it will disable the hammer button in the building scroll.

### Note on Associated Files

`data\export_buildings.txt`

This file lists the in-game textual description of the building name, the building description, and a short version of the building description. It should match the code name in the EDB. This file also contains the "`_name`" elements which provide the text for the building thread summaries (i.e. the text for each building type in the in-game Building Browser).

`data\text\export_descr_buildings_enums.txt`

This file enumerates the tags for the textual descriptions of the building names and descriptions (long and short). It seems to be an obsolete file.

`data\descr_ui_buildings.txt`

A number of lines in this file take on the following format:

* temple_of_battle_shrine shrine
* temple_of_battle_temple temple
* temple_of_battle_large_temple large_temple
* temple_of_battle_awesome_temple awesome_temple
* temple_of_battle_pantheon pantheon
* temple_of_farming_shrine shrine

These entries give the game an alternative name to look for when loading a building graphic. This means you can have multiple custom buildings but have them all share a similar image in game. For example if you had modded the game to have seperate barracks for each of the barb factions called brit_barracks, gaul_barracks etc, instead of having a separate graphic for each one you could write

* brit_barracks barracks
* gaul_barracks barracks

### Tools & Other Resources

Below are some links and resources from the original Rome Total War that should be broadly similar to the edits required in ROME REMASTERED. They might not be 100% identical but they are a useful resource for more complex tasks.

* [Quietus's A Comprehensive Rome: Total War Guide (visit Economic section to read how buildings affect trade)](https://forums.totalwar.org/vb/showthread.php?t=45315)
* [Aradan's The Complete EDU Guide](https://forums.totalwar.org/vb/showthread.php?t=88859)

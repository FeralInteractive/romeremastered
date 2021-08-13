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
| Overall building tree number | 64 | **TBC** | `Targeted 2.0.3` | |
| Levels per building tree | 9 | **TBC** | `Targeted 2.0.3` | |
| Hidden resources | 64 | _Virtually Unlimited*_ | `2.0.2` | |
| Unit buildable per city | 32 | **TBC** | `Targeted 2.0.3` | |

 _*'Virtually Unlimited'_ allows for a theoretical value of `4294967296` entries.

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

You will then find listed in the EDB file the building tree for each building type complete with a block of code for each building. You may have up to 64 such trees with a maximum of 9 levels (buildings) each though spread over a maximum of 5 settlement levels (though buildings attached to villages will not show up on the building browser).     

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
                recruit "carthaginian peltast"  0  requires factions { spain, }
                recruit "barb peltast gaul"  0  requires factions { gauls, }
                recruit "barb peltast german"  0  requires factions { germans, }
                recruit "barb slinger briton"  0  requires factions { britons, }
                recruit "barb archer dacian"  0  requires factions { dacia, }
                recruit "barb archer scythian"  0  requires factions { scythia, }
                recruit "carthaginian peltast"  0  requires factions { carthage, }
                recruit "carthaginian archer"  0  requires factions { numidia, }
                recruit "east peltast"  0  requires factions { armenia, pontus, }
                recruit "east slinger"  0  requires factions { parthia, }
                recruit "egyptian peltast"  0  requires factions { egyptian, }
                recruit "egyptian slingers"  0  requires factions { egyptian, }
                recruit "greek peltast"  0  requires factions { greek, }
                recruit "roman velite"  0  requires factions { roman, }  and not marian_reforms
                recruit "roman light infantry auxillia"  0  requires factions { roman, }  and marian_reforms
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
**building** - This is the building type. In a mod you can give this any custom name you wish as long as you don't include spaces. You can have a maximum of 64 bulding types in total.
```
building missiles
{
```

**NOTE:** You can designate your own names for the building type should you wish to not make them universally available to all factions/cultures. However, core_buildings (aka government buildings), walls and hinterland buildings (roads, mines, and farms) cannot be factionally or culturally designated (though some of their levels may be excluded from certain cultures/factions).

### icon
**icon** - This tells the game which category of the building browser to use.
```
    icon ranged
```

Possible options allowed are:

```
; This tells the game which category of the building browser to use.
; RomeHD has subtly different classifications than the original, so note the deprecated classifications, they wont work anymore.
; If no classification is specified, the game will guess based on the building name, which works for all the unmodded buildings.
; Automatic classification:
;   core_building
;       core
;   defenses
;       defence
;   barracks|equestrian|missiles|smith|despotic_law
;       military
;   market|port_buildings|hinterland_*|caravans
;       trade
;   health
;       water
;   academic|amphitheatres|theatres|taverns
;       culture
;   temple_*|christian_acedemic
;       religious
; Explicit classification overrides the automatic classification, so if you don't like the above classifications, you can overule them.

```

### levels
 Now the levels of the building type are listed (space-delimited & maximum of 9).

```
    levels practice_field archery_range catapult_range siege_engineer
    {
```  

**NOTE:** You can designate your own names for the building type should you wish to not make them universally available to all factions/cultures. However, core_buildings (aka government buildings), walls and hinterland buildings (roads, mines, and farms) cannot be factionally or culturally designated (though some of their levels may be excluded from certain cultures/factions).

For example, you could have:

Code:
```
building missiles_roman
{
levels practice_field archery_range catapult_range siege_engineer
{
```
Which of course could be used to specify a purely roman tree of such buildings. Remember not to change the names of the levels (though you may choose to not use some or allow only certain roman factions their use).

### levels_specific_building

The tree then lists a block of code for each building (`practice_field`). Continuing from our example above we will look at the first level of the "building missiles" tree, the practice_field:

```
practice_field requires factions { barbarian, ct_carthage, eastern, parthia, egyptian, greek, roman, }
{
  ```
The first line states the requirements necessary to be satisfied in order for the building to be available for construction. All factions reside within the 6 hard-coded cultures, and so this particular building can be built by all factions. Any combination of factions/cultures can be listed. Both visible and hidden resources can be used as requirements as may "building_present_min_level x y" where x is the building type and y the level of that building type. This latter simply requires a certain minimum level of building of a building type to be present in that settlement before the practice_field can become available for construction. The connector "and" can be used to compound requirements, for example:

```
practice_field requires factions { barbarian, roman, } and resource iron and hidden_resource woodland and building_present_min_level market trader
{
```

#### Full List of Requirements

* `resource` - See [descr_sm_resources.txt](/documentation/data_file_guides/descr_sm_resources.md) file
* `hidden_resource` - See [descr_sm_resources.txt](/documentation/data_file_guides/descr_sm_resources.md) file
* `building_present` - Checks for the existance of ther building type at *any* level.
* `building_present_min_level` - hecks for the existance of ther building type at the specified level or higher
* `marian_reforms` - Checks if the marion reforms have triggered
* `factions { x, }` - Checks for specific factions
* `port` - This returns true in coastal areas with ports assigned (i.e. in map_regions.tga). It can be used as a condition for buildings and capabilities, including units.
* `currency_fixed` is tied to the BI debased currency event can be disabled via a classic/remastered toggle
* `remastered_only` is tied to the "settlement condition" classic/remastered toggle
* `tavern_bonus` is tied to the "tavern changes" classic/remastered toggle
* ```is_player``` - Allows you to use the ```requires``` function to state if a building is availble for only the player or only the AI factions. This will allow for the creation of special buildings that mods can use to assist the AI factions, or provide depth to the human player experience without overly complicating the AI build trees.

**NOTE:**
* The connectors "or" and "not" can also be used in addition to "and". X represents a faction, culture, a list of the same - or all ("all,").
* Not conditionals (even if true) and positive conditionals that result false seem to break the culture/faction for the slave faction if those buildings are placed at game start - see this thread: https://forums.totalwar.org/vb/showthread.php?t=81322
* All of the above can be used as capability requirements too though the building_present/building_present_min_level should not be used for recruitment lines as it will cause a CTD when the player uses the right-click feature added in later versions of RTW.


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
* If you use the marian_reform requirement then it has been reported that it needs to go at the end.
* The "0" listed with recruits refers to the level of Experience the unit begins with when first recruited. It can of course be any number between 0 and 9.

#### capability requirements

Full List of Building Effects

* `happiness_bonus` (public order due to happiness) 1-x (5-x%)
* `population_growth_bonus` (pop. growth) 1-25 (0.5-12.5%)
* `law_bonus` (public order bonus due to law) 1-x (5-x%)
* `population_health_bonus` (public health) 1-x (5-x%)
* `trade_base_income_bonus` (increases trade goods) 1-5 (1-5) [5] - adds 10% to base value of land trade & sea exports
* `farming_level` (farms) (plus 0.5% pop. growth and plus 80 income (average harvest) per point;equivalent to base farm level in descr_regions.txt) 1-5 (1-5) [5]
* `population_fire_risk_bonus` (reduces risk of fire) * (might function as "fire_risk", if it works at all)
* `taxable_income_bonus` (tax income bonus) boosts tax income by stated percentage;1-100 (1%-100%)
* `trade_level_bonus` (increase in trade) - affects land trade only (not confirmed to work - needs testing)
* `population_loyalty_bonus` (public order) - does not appear to work
* `recruits_morale_bonus` (increases morale of units recruited) 1-4 (1-4) (does not seem to work though)
* `recruits_exp_bonus` (upgrades XP of units recruited) 1-5 (1-5)
* `armour` (armour upgrade) 1 (1)
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
* `construction_cost_bonus_military` (percentile cost reduction for recruitment buildings but does not seem to work) 1-100 (1-100%)
* `construction_cost_bonus_religious` (percentile cost reduction for temples) 1-100 (1-100%)
* `construction_cost_bonus_defensive` (percentile cost reduction for walls) 1-100 (1-100%)
* `construction_cost_bonus_other` (percentile cost reduction for civil buildings but seems to apply to all buildings except religious ones) 1-100 (1-100%)
* `construction_time_bonus_military` (percentile time reduction for constructing recruitment buildings but does not seem to work) 1-100 (1-100%)
* `construction_time_bonus_religious` (percentile time reduction for constructing temples) 1-100 (1-100%)
* `construction_time_bonus_defensive` (percentile time reduction for constructing walls) 1-100 (1-100%)
* `construction_time_bonus_other` (percentile time reduction for constructing civil buildings but also seems to apply to all buildings except religious ones) 1-100 (1-100%)
* ```extra_recruitment_points [bonus]``` - **NEW for RR** Allows you to give addional recuitment points to a settlment via a building modifier. You can define the bonus in terms of turns.
* ```extra_construction_points [bonus]``` - **NEW for RR** Allows you to give addional construction points to a settlment via a building modifier. You can define the bonus in terms of turns.

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

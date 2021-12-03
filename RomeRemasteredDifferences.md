![Workshop_header_template](/Workshop_header_template.png)
# Differences & New Features

Feral have updated & rewritten parts of the game engine to lift limits and add new functionality. The lists and tables below show the original limits and any changes or new features that have now been added to Rome Remastered.

## Table Of Contents

* [New Features](#new-features)
   * [Custom Campaigns](#custom-campaigns)
   * [Combined Features Mode](#combined-features-mode)
   * [Disable Rebel merchants](#disable-rebel-merchants)
   * [Reputational and Faction Relationships](#reputational-and-faction-relationships)
   * [Scripting - Expanded functionality and support for running in background](#scripting---expanded-functionality-and-support-for-running-in-background)
   * [Expanded Logging](#expanded-logging)
   * [New Unit Abilities (EDU)](#new-unit-abilities-edu)
   * [New Building Abilities (EDB)](#new-building-abilities-edb)
   * [Moddable Graphics Settings](#moddable-graphics-settings)
      * [Graphics Options](#graphics-options)
      * [Tone Map Definitions](#tone-map-definitions)
      * [Grass settings](#grass-settings)
   * [AI Personalities](#ai-personalities)
   * [Portait Matching Visuals](#portait-matching-visuals)
   * [Classic Remaster Ruleset Toggles](#classic-remaster-ruleset-toggles)
   * [Scripting](#scripting)
* [Game Engine Limits](#game-engine-limits)
   * [Miscellaneous Hardcodes](#miscellaneous-hardcodes)
   * [export_descr_ancillaries.txt](#export_descr_ancillariestxt)
   * [export_descr_buildings.txt](#export_descr_buildingstxt)
   * [export_descr_character_trait.txt](#export_descr_character_traittxt)
   * [export_descr_unit.txt](#export_descr_unittxt)
   * [descr_terrain.txt](#descr_terraintxt)
   * [map_regions.tga](#map_regionstga)
   * [descr_model_Battle.txt](#descr_model_battletxt)
   * [descr_mount.txt](#descr_mounttxt)
   * [descr_daytype.txt](#descr_daytypetxt)
   * [descr_animals.txt](#descr_animalstxt)
   * [descr_aerial_map_bases.txt](#descr_aerial_map_basestxt)
   * [descr_grass.txt](#descr_grasstxt)
   * [descr_particle.txt](#descr_particletxt)
   * [descr_water.txt](#descr_watertxt)
   * [descr_engines.txt](#descr_enginestxt)
   * [descr_ship.txt](#descr_shiptxt)

## New Features

### Custom Campaigns

You can now define a new campaign list, allowing you to define new campaigns and enable/disable important features for them individually. This is controlled inside [descr_campaigns.txt](/documentation/data_file_guides/descr_campaigns.md).

### Combined Features Mode

Mods for Rome Remastered can now access all of the features available in Barbarian Invasion & Alexander. Most of the features are data driven but Loyalty & Religion need to be toggled on using the toggles found inside [descr_campaigns.txt](/documentation/data_file_guides/descr_campaigns.md).

### Disable Rebel merchants

You can specifically disable Rebel Merchants but allow you to have merchants for all factions. This is controlled inside [descr_campaigns.txt](/documentation/data_file_guides/descr_campaigns.md)

### Reputational and Faction Relationships

You can now modify the reputational bonuses your faction gains or loses due to their actions. Previously, the bonuses where more limited and could not be modded. This is now controlled inside [feral_descr_reputations_and_relations.txt](/documentation/data_file_guides/feral_descr_reputations_and_relations.md).  

### Scripting - Expanded functionality and support for running in background

You can now setup your mod to automatically load a background script when your mod loads, allowing you to add more immersion to your mod and avoid users having to manually trigger scripts using workarounds like the `show me how` button. We also added the abilitiy to store persistent variables inside the save game so that you can track script progression between play sessions, plus the ability destroy buildings and rename settlments inside a script. You can find a quick guide to scripting [here](/documentation/scripts/Scripts.md).

### Expanded Logging

We have added two detailed logging modes for modders that will provide additional warnings. These will dump out progress messages as well as warnings and errors but can help when debugging more complex changes. You can find a quick guide to logging [here](/documentation/feature_guides/logging/logging.md).

### New Unit Abilities (EDU)
When defining units we have added two new features in order to grant more flexibility, allowing for more potential within a modded unit.

The ```attributes``` field for units now supports two new features:

* ```infinite_ammo``` - Allows a unit to have infinite ammo without going into arcade mode.
* ```inexhaustible``` - Disables stamina for this unit without going into arcade mode.

This is controlled inside [EDU](/documentation/data_file_guides/EDU.md).

### New Building Abilities (EDB)
When defining units we have added a feature that grants more flexibility for buildings, allowing for more potential within complex mods.

* ```is_player``` - Allows you to use the ```requires``` function to state if a building is availble for only the player or only the AI factions. This will allow for the creation of special buildings that mods can use to assist the AI factions, or provide depth to the human player experience without overly complicating the AI build trees.
* ```extra_recruitment_points [bonus]``` - Allows you to give addional recuitment points to a settlment via a building modifier. You can define the bonus in terms of turns.
* ```extra_construction_points [bonus]``` - Allows you to give addional construction points to a settlment via a building modifier. You can define the bonus in terms of turns.

This is controlled inside [EDB](/documentation/data_file_guides/EDB.md).

### Moddable Graphics Settings

The graphics have a number of new moddable files that allow you to alter the visuals in a number of ways. Below is a list of the files that allow you to modify the graphics options and visuals.

#### Graphics Options
The graphic settings are now moddable through a json file mod. This will allow you to change the settings in the graphics menus to have different limits. For example, you could expand the grass draw distance beyond the current limits. You can find a quick guide to graphics options [here](/documentation/feature_guides/graphics_options.md).

#### Tone Map Definitions
* [feral_descr_tonemap_lut.txt](/documentation/data_file_guides/feral_descr_tonemap_lut.md)

#### Grass settings
* [feral_descr_grass_textures.txt](/documentation/data_file_guides/feral_descr_grass_textures.md)
* [feral_descr_grass_usage.txt](/documentation/data_file_guides/feral_descr_grass_usage.md)

### AI Personalities
The AI personality system in Rome Remastered can now be modded so the behaviour of the different personality profiles is now possible. This is controlled inside [feral_descr_ai_personality.txt](/documentation/data_file_guides/feral_descr_ai_personality.md).

### Portait Matching Visuals
* [feral_descr_portraits_variation.txt](/documentation/data_file_guides/feral_descr_portraits_variation.md)

### String overrides

Some of the text displayed in game isn't read from data/text folders but uses the Feral overrides method. You can find out more about these strings [here](/documentation/data_file_guides/string_overrides.md).

### Classic Remaster Ruleset Toggles
You can find out more about toggles [here](/documentation/data_file_guides/toggles.md).

### Scripting
Scripting has been extended in Rome Remastered with logging, modded background support, persistent counters, plus addional commands, conditions and events. You can find out more about this feature [here](/documentation/scripts/Scripts.md).

</br>

## Game Engine Limits

### Miscellaneous Hardcodes

| Limit Type | Original Rome Limit | Rome Remastered Limit Resolution | Status | Notes |
|-|:-:|:-:|:-:|-|
| Number of Factions | 21 | _Virtually Unlimited*_ | `2.0.4` | |
| Cultures | 7 | _Virtually Unlimited*_ | `2.0.4` | N/A |
| Religion count | 3 |_Virtually Unlimited*_ | `2.0.4` |  |
| Polygon limit | 20,000 faces | 20,000 faces |  | |

</br>

### export_descr_ancillaries.txt

| Limit Type | Original Rome Limit | Rome Remastered Limit Resolution | Status | Notes |
|-|:-:|:-:|:-:|-|
| ExcludedAncillaries | 3 | **TBC** | `To Investigate for 2.0.4` | |

</br>

### export_descr_buildings.txt

| Limit Type | Original Rome Limit | Rome Remastered Limit Resolution | Status | Notes |
|-|:-:|:-:|:-:|-|
| Overall building tree number | 64 |_Virtually Unlimited*_| `2.0.4` | |
| Levels per building tree | 9 | 9 | `2.0.4` | |
| Hidden resources | 64 | _Virtually Unlimited*_ | `2.0.2` | |
| Unit buildable per city | 32 | _Virtually Unlimited*_ | `2.0.4` | |

</br>

### export_descr_character_trait.txt

| Limit Type | Original Rome Limit | Rome Remastered Limit Resolution | Status | Notes |
|-|:-:|:-:|:-:|-|
| Levels per trait | 9 | 9| `2.0.0` | |
| Points required for a threshold | 600 | 600 | `2.0.0` | |
| Points assignable per trigger | 100 | 100 | `2.0.0` | |

</br>

### export_descr_unit.txt

| Limit Type | Original Rome Limit | Rome Remastered Limit Resolution | Status | Notes |
|-|:-:|:-:|:-:|-|
| Overal unit number | 500 | Max: _Virtually Unlimited*_| `2.0.2` | |
| Units per faction | Min: 1 </br> Max: 100 | Min: 1 </br> Max: _Virtually Unlimited*_ | `2.0.2` | |
| Soldiers per unit | Min: 12 </br> Max: 60 | Added `Extreme` unit size  | `2.0.0` | Extreme allows 300 soldiers per unit vs Original's 240 limit.  |
| Extras per unit | Min: 2 | Min: 2 | `2.0.0` | 0 is also acceptable if there are none |
| Officers per unit | Min: 0 </br> Max: 3 | Min: 0 </br> Max: 3 | `2.0.0` | |
| Collision mass | 100 | 100| `2.0.0` | |
| Mount effects per units | 3 | 3 | `2.0.0` | |
| Number of formations | Min: 1 </br> Max: 2 | Min: 1 </br> Max: 2 | `2.0.0` | |
| Hitpoints | Min: 1 </br> Max: 15 | Min: 1 </br> Max: 15 | `2.0.0` | Any extra is considered as 15 by the game. |
| Attack factor | Min: 1 </br> Max: 63 | Min: 1 </br> Max: 63 | `2.0.0` | |
| Charge bonus | Min: 0 </br> Max: 63 | Min: 0 </br> Max: 6 | `2.0.0` | |
| Missile range | Min: 20 |  Min: 20 | `2.0.0` | The maximum varies dependng on the projectile type. This maximum range is set by the velocity in `descr_projectile_new.txt`. A higher velocity means further range. |
| Missile Ammunition | Min: 2 |  Min: 2 | `2.0.0` | If there is no missile, 0 is acceptable. '2.0.2' 'infinite_ammo' |
| Armour factor | Min: 0 </br> Max: 63 | Min: 0 </br> Max: 63 | `2.0.0`| |
| Defensive skill factor | Min: 0 </br> Max: 63 | Min: 0 </br> Max: 63 | `2.0.0` |  Any extra is considered as 63 by the game |
| Shield factor |  Min: 0 </br> Max: 31 | Min: 0 </br> Max: 31 | `2.0.0` | Any extra is considered as 31 by the game. |
| Base morale | Min: 0 </br> Max: 128 | **TBC** | `2.0.0` | Any extra is considered as 128 by the game.  |
| Turns to build | Min: 1 </br> Max: 244 | Min: 1 </br> Max: 244 | `2.0.0' | Any extra is considered as 244 by the game. |
| Animals | Min: 0 </br> Max: 3 | Min: 0 </br> Max: 3 | `2.0.0` | |

</br>

### descr_terrain.txt

| Limit Type | Original Rome Limit | Rome Remastered Limit Resolution | Status | Notes |
|-|:-:|:-:|:-:|-|
| Max Width | 500 | 500 | `2.0.0` | |
| Max Height | 500 | 500 | `2.0.0` | |

</br>

### map_regions.tga

| Limit Type | Original Rome Limit | Rome Remastered Limit Resolution | Status | Notes |
|-|:-:|:-:|:-:|-|
| Number of provinces | 200 | 16581372 | `2.0.2` | |
| Number of landmasses | 20 | 20 | `2.0.2` | |

</br>

### descr_model_Battle.txt

| Limit Type | Original Rome Limit | Rome Remastered Limit Resolution | Status | Notes |
|-|:-:|:-:|:-:|-|
| Model Entries | 256 (512 Alex) | _Virtually Unlimited*_ | `2.0.2` | |

</br>

 ### descr_mount.txt

| Limit Type | Original Rome Limit | Rome Remastered Limit Resolution | Status | Notes |
|-|:-:|:-:|:-:|-|
| Mount Entries | 100 | _Virtually Unlimited*_ | `2.0.2` | |

</br>

 ### descr_daytype.txt

| Limit Type | Original Rome Limit | Rome Remastered Limit Resolution | Status | Notes |
|-|:-:|:-:|:-:|-|
| | 128 | | _Virtually Unlimited*_ | `2.0.2` | |

</br>

 ### descr_animals.txt

| Limit Type | Original Rome Limit | Rome Remastered Limit Resolution | Status | Notes |
|-|:-:|:-:|:-:|-|
| | 100 | _Virtually Unlimited*_ | `2.0.2` | Defines types of animals handlers can use|

</br>

 ### descr_aerial_map_bases.txt

| Limit Type | Original Rome Limit | Rome Remastered Limit Resolution | Status | Notes |
|-|:-:|:-:|:-:|-|
| | 100 | _Virtually Unlimited*_ | `2.0.2` ||

</br>

 ### descr_grass.txt

| Limit Type | Original Rome Limit | Rome Remastered Limit Resolution | Status | Notes |
|-|:-:|:-:|:-:|-|
| | 256 | _Virtually Unlimited*_ | `2.0.2` | |

</br>

 ### descr_particle.txt

| Limit Type | Original Rome Limit | Rome Remastered Limit Resolution | Status | Notes |
|-|:-:|:-:|:-:|-|
| | 256 | _Virtually Unlimited*_ | `2.0.2` | |

</br>

 ### descr_water.txt

| Limit Type | Original Rome Limit | Rome Remastered Limit Resolution | Status | Notes |
|-|:-:|:-:|:-:|-|
| | 80 | _Virtually Unlimited*_ | `2.0.2` | |

</br>

 ### descr_engines.txt

| Limit Type | Original Rome Limit | Rome Remastered Limit Resolution | Status | Notes |
|-|:-:|:-:|:-:|-|
| Number of Siege Engines | 128 | _Virtually Unlimited*_ | `2.0.2` | |

</br>

 ### descr_ship.txt

| Limit Type | Original Rome Limit | Rome Remastered Limit Resolution | Status | Notes |
|-|:-:|:-:|:-:|-|
| Number of ships | 100 | _Virtually Unlimited*_ | `2.0.2` | |

 _*'Virtually Unlimited'_ allows for a theoretical value of `4294967296` entries.

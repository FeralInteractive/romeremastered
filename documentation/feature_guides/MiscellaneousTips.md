![Workshop_header_template](/Workshop_header_template.png)
# Miscellaneous Hints and Tips

## Table Of Contents

   * [Introduction](#introduction)
   * [Disaster Values](#disaster-values)
   * [read_no_endian error](#read_no_endian-error)
   * [CA_RAND_MAX Values](#ca_rand_max-values)
   * [export_descr_character_traits](#export_descr_character_traits)
   * [descr_quick_battle_locations](#descr_quick_battle_locations)
   * [Unexpected in condition parsing error](#unexpected-in-condition-parsing-error)
   * [descr_fog_params](#descr_fog_params)
   * [ambient_settlements](#ambient_settlements)
   * [Output Variables To Log](#output-variables-to-log)
   * [Volcano](#volcano)
   
## Introduction

This page is a collection of hints and tips that don't otherwise fit into their own page but could be useful to players and modders alike.


## Swap Merge & Sort Behaviour

In Rome Remastered you can sort your units on the campaign map into the orders you like, this is then remembered when you enter and leave battles meaning you can organise your armies as you recuit them on the map.

There are buttons in the UI to auto sort and auto merge units in your armies on the bottom of the screen.

![AutoMerge_Autosort](/documentation/feature_guides/images/AutoMerge_Autosort.jpg)

By default dragging will reorder units and you can use ctrl and drag to manually merge units. You can however swap this behaviour around inside the preferences folder if you prefer.

 1. Open the Pre-Game Options Panel and go to the Support tab
 2. Click on the `Open Preferences Folder` button.
![SupportOpenPreferences](/documentation/feature_guides/images/SupportOpenPreferences.jpg)
 3. Quick the launcher using the `Quit` button
 4. Now open the `Preferences Data` file from the `Total War ROME REMASTERED` in a text editor.
 5. Search for the line with `CtrlToMerge`. Edit the line so the value is `0` instead of `1`. Afterwards it should look like the line in point 6 below. 
 6. `<value name="CtrlToMerge" type="integer">0</value>`
 7. Save the file and restart the game. You can now merge by default and hold down ctrl if you want to reorder.

## Disaster Values

The maximum values for disasters and disaster events are technically unlimited but the engine will cap the max value to the following limits when triggering them in game.

* Earthquake 9
* Flood 9
* Volcano 9
* Storm 13

## read_no_endian error

```read_no_endian(&data, sizeof(T)) Failed``` 

This error implies that the system that's reading the file has hit EoF (End Of File)  where it wasn't expecting it. i.e. the game was expecting the file to be longer than it actually was. You should check the file for any missing for incorrectly formatted items. In some cases adding an extra empty line at the end of the file can fix some parsing errors.

## CA_RAND_MAX Values

The CA_RAND_MAX value matches the minimum guaranteed value of RAND_MAX by the c++ spec. This is 32767. The random number genertor is using LFSR.

## export_descr_character_traits

Sometimes you can get errors that a token is not recognised in your traits file. This can be caused by a typo in the trait capitalisation.

```Script Error in Q:\Feral\Users\Default\AppData\Local\Mods\My Mods\example_mod/data/export_descr_character_traits.txt, at line 8046, column 15. Condition parser doesn't recognise this token: Battleodds```

Remember that Triggers are CaseSensitive so `BattleOdds` and `Battleodds` are not the same trigger so make sure you don't have differnt capitalisation in different places. That all need to be the same including the case.

## descr_quick_battle_locations

descr_quick_battle_locations.txt has a list of coordinates used in the quick battles option. This was hard coded in the original game but broken out into a text file for RR. The coordinate values have a 1:1 relationship with the pixel location on the ground_types.tga map files for your mod.

## Unexpected in condition parsing error

`Unexpected in condition parsing:` is exclusively used when the game is expecting an "and" or "or" usually on the line listed in the error log.

## descr_fog_params

This allows you to alter the dynamic behavour of fog, some minor items to note.

* `fog`, `static_fog` or `dynamic_fog`, all need to be present
* `fog_main_layer_height` is also typo'd in the code, you need to use `m_fog_main_layer_height` instead.

Dynamic Fog Default values include:

* `Scaling = 500`
* `wanted particles = 4`
* `spawn interval = 0.17`
* `constrast power = 0.96`

![fog_defaults.png](/documentation/feature_guides/images/fog_defaults.png)

## ambient_settlements

Below is a quick memory dump of some useful information for people wanting to mod this area of the game.

The game will usually attempt to place **up to** 5 randomly selected items from each type (except farms, number of which depends on fertility of the tile). The `always` tage forces the game to always attempt to place a given entry at the end of the placing function.

For farms, the number placed depends on the fertility of the tile and if it is cultivated. In addition when you place a farm, it also places a random number of children too so cultivated mid fertility will try and place 5-10 children aroud the farm using the following logic:

```
               | Not cultivated          | Cultivated
---------------+-------------------------+--------------------------
Low fertility  | no farms                | 1-3 farms, 0-5 children
---------------+-------------------------+--------------------------
Mid fertility  | 0-1 farms, 0-2 children | 3-6 farms, 5-10 children
---------------+-------------------------+--------------------------
High fertility | 0-2 farms, 0-4 children | 6-10 farms, 10-15 children
```

For other ambient items the following addional limitations are present.

* `Watchtower` is just 1, (if the tile has a watchtower)
* `forestry` is unused
* `mines` is unused
* `natural` is just straight 0-5 dice roll 
* `monuments` is just straight 0-5 dice roll 
* `ruins` is just straight 0-5 dice roll 
* `ancient battlefield` is 1, if the location is the site of a famous battle (has a crossed swords icon on the campaign map)

## Output Variables To Log

If you want to dump a variables values to the log for debugging you can use something in the following format.

`console_command check_persistent_var <variable name>`

You should avoid using the `script_log` command as that dumps to stdout not the log file.

## Volcano

You can trigger volcanos inside a script using the command `console_command event volcano <x> <y>`

The volcano will start smoking then the command is triggered then erupt the following turn.

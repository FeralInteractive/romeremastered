![Workshop_header_template](/Workshop_header_template.png)
# Scripts

# Table Of Contents

   * [Introduction](#introduction)
   * [Background Script Setup](#background-script-setup)
   * [Enable Script Logging](#enable-script-logging)
   * [Triggers, conditions, events &amp; commands](#triggers-conditions-events--commands)
      * [Events](#events)
      * [New conditions](#new-conditions)
      * [New commands](#new-commands)
   * [RomeShell Commands List](#romeshell-commands-list)

## Introduction
Rome Remastered supports the same scripting langauge as the original Rome Total War however script support has been extended so a mod can now run a background script.

## Background Script Setup

1. Create the following file inside your mod, you can use a copy the file from game data as a starting point. `data/world/maps/campaign/imperial_campaign/descr_strat.txt`
2. At the bottom of the `descr_strat.txt` file add in the name of your custom script.
3. Create a script txt file in the following location `data/world/maps/campaign/imperial_campaign/` and make sure it matches the the file name listed in point 2.

## Enable Script Logging

When scripting you can get errors and items not triggering that need to be debugged. To assist with this we have a seperate verbose script logging mode. You need to add the string `verbose_script_logging` to the advanced options (see screenshot).

![Script Logging](/documentation/feature_guides/scripts/script_logging.jpg)

Once enabled you will find an extra file in the following location:

`/VFS/Local/Rome/logs/scripting_log.txt`

This option can be combined with other options like `enable_logging`. Please be aware the verbose script logging is **very** verbose. This is great for debugging issues line by line but the text file will start to get quite large if you play for an extended time and/or have complex scripts.

## Triggers, conditions, events & commands

When the game is launched the game will generate 3 files inside `/VFS/Local/Rome/documentation` these will document the following available commands, conditions and events you can use in scripts.  

* [docudemon_events.txt](/documentation/feature_guides/scripts/docudemon_events.txt)
* [docudemon_conditions.txt](/documentation/feature_guides/scripts/docudemon_conditions.txt)
* [docudemon_commands.txt](/documentation/feature_guides/scripts/docudemon_commands.txt)

These three files are similar to the ones you may have seen for the original game but do contain some new commands. A list of the new items can be seen below but refer to the full documenation files for further details.

There are also the following UI elements and console commands that can be used, files listing all of the individual commands and elements are linked below:

* [available_ui_elements_strat.txt](/documentation/feature_guides/scripts/available_ui_elements_strat.txt)
* [available_ui_elements_battle.txt](/documentation/feature_guides/scripts/available_ui_elements_battle.txt)
* [console_commands.txt](/documentation/feature_guides/scripts/console_commands.txt)

Items below `highlighted` are potentially very useful to complex modding scripts.

### New Events

In total around 100 new events have been added to the dictionary for the Remaster. The majority of the new commands are linked to the ability to track user interaction with the game related to the in campaign tutorial system.

However there are a few new events that have been added to improve modding control and support new features these include:

 * `TakeOffice` - Supports new senate modding capabilities
 * `LeaveOffice` - Supports new senate modding capabilities
 * `NewTurnStart` - Allows scripts to trigger at the beginning of a turn
 * `ScriptPromptCallback` - A script prompt has received player input
 * `FactionDestroyed` - Allows scripts to react to when a faction is destroyed
 
You can find out more details of all the new features on the [Scripts Events ](/documentation/feature_guides/scripts/Scripts_events.md) page.


### New conditions

In total just over 50 new conditions have been added to the dictionary for the Remaster. The majority of these new commands are aimed to improve modding control of the game play and support new features the highlights include:

 * Diplomatic status - Check diplomatic status between two factions
 	* `IsAlly` 
 	* `IsProtectorate`
 	* `IsProtector`
 	* `IsSameSuperfaction`
 	* `at_war`
 * Settlement Checks - Check the status of a settlement or region.
 	* `IsCapital` - Is this settlement the faction capital
 	* `I_SettlementOwnerCulture` - Is this settlement controlled by a faction with this culture?
 	* `I_SettlementLevel` - Is this settlement at this level?
 	* `SettlementCapabilityLevel` - Test to see if the settlement has a capability at a particular level
    * `SettlementOrderLevel` - Test to see if the settlements order factor is at a particular level
    * `HomeSettlementBuildingExists` - Test to see if the home settlement of the triggering character has a building at a particular level
    * `HasResource` - Does the region have this resource?
    * `SettlementRevoltingFrom` - Used with revolt faction spawning script ability
 * Character Checks - Check details of a specific character   
    * `CharacterName` - Checks for a given characters name
 	* `DistanceCapital` - Does the characters distance to the faction capital exceed the given threshold?
 	* `I_CharacterNameNearTile` - Is a particular character near a particular tile?
 	* `HasOffice` - Checks if a character holds a senate office
 * `FactionIsAlive` - Checks if the given faction is alive
 * `MajorEventActive` - Supports new multiple major event feature (marian reforms etc).
 * `I_CompareCounter` - Compare a script counter to a value
 * `LangIs` - Test game language, can use to warn players if language is unsupported in mod.

You can find out more details of all the new features on the [Scripts Conditions ](/documentation/feature_guides/scripts/Scripts_conditions.md) page.


### New commands

In total around 100 new events have been added to the dictionary for the Remaster. The majority of the new commands are linked to the ability to track user interaction with the game related to the in campaign tutorial system.

However there are a few new events that have been added to improve modding control and support new features these include:

 * `message_prompt` - Creates a new news message with a simple yes/no prompt and will pass the users responce back to the game for processing.
 * Senate - The senate(s) can now be modded so has the following commands
 	* `override_superfaction_popularity` - Disable normal superfaction popularity processing so that it can be controlled by a script
 	* `set_faction_senate_standing` - Set the senate standing of a given faction
 	* `set_faction_people_standing` - Set the senate standing of a given faction
 * Scripting Features
 	* `declare_persistent_counter` - declare a counter that will be persistent between saves (these counters are stored inside the players save game)
 	* `break` - immediately exit the current scope
 	* `return` - return a value from the script and terminate, used for faction spawn scripts
 	* `counter_operation` - Sets the result counter to the result of the expression.
 	* `store_counter` - Stores a counter with the label specified
 	* `retrieve_counter` - Extacts a counter with the given label
 	* `for_each` - Iterate through all instances of a certain type within a given scope
 	* `goto` - jump to a place in the script marked by a label
 	* `set_label` - Set a label that can be jumped to with a Goto statement
 	* `if_not` - conditions to satisfy to execute the scope
 	* `script_log` - logs a message to the log file (if enabled)
 	* `while_not` - start a while not loop
 * Control Ambient Objects on Campaign Map
 	* `set_ao_visible` - Control a specific object
 	* `set_all_ao_visible` - Toggle all ambient objects
 * Regional and Settlement Commands
 	* `add_religion` - Add commitment to a given religion into a region
 	* `add_hidden_resource` - add a hidden resource to a given region
	* `create_mercenary_pool` - Create a mercenary pool
 	* `destroy_building` - destroy a building in a settlement
 	* `move_to_settlement` - Moves the camera position to a settlement
	* `remove_hidden_resource` - remove a hidden resource to a given region
	* `rename_settlement_in_region` - rename a settlement to a given name
 * `spawn_character_child` - Spawns a new character with given parameters and a given father
 * `trigger_marriage_proposal` - Triggers a marriage proposal for a player
 
 You can find out more details of all the new features on the [Scripts Commands ](/documentation/feature_guides/scripts/Scripts_commands.md) page.

## RomeShell Commands List

We output the commands for RomeShell into a docudemon file. When the game is launched the game will generate the file in your `/VFS/Local/Rome/documentation` folder.

You can find a copy of the file on the [RomeShell ](/documentation/feature_guides/scripts/docudemon_romeshell.txt) page.

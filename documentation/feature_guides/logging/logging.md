![Workshop_header_template](/Workshop_header_template.png)
# logging

# Table Of Contents

## Introduction
Rome Remastered supports extended logging compared the original game with a number of new options allowing you to enable addional logs for various aspects of the game.

## Enable detailed logging

To assist debugging mods we now have the option to save logging to a text file. THis text file not only contains errors and warnings but also also success/failure output to help modders track not only what went wrong but what the game was going prior to the issue.

You need to add the string `enable_logging` to the advanced options (see screenshot).

![Script Logging](/documentation/feature_guides/logging/enable_logging.jpg)

Once enabled you will find an extra file in the following location:

`/VFS/Local/Rome/logs/message_log.txt`

This option can be combined with other options like `enable_logging`.

### Example of log contents

Below is a snippet from a log generated when running the Example Mod.

```
region 'Baetica' has no specified legionary name
loading world map file 'Q:\Feral\Users\Default\AppData\Local\Mods\My Mods/ExampleMod/data/world/maps/base/map.rwm'...
finished

setting capital(Arretium:7ff19d36f400:romans_julii) for faction(romans_julii)
attaching region Etruria(48) to faction(romans_julii), giving them 5 triumph points
Created a port in region 48, faction 'romans_julii'

attaching region Umbria(51) to faction(romans_julii), giving them 10 triumph points
New Character - Faction(romans_julii) named character(Flavius Julius)
Flavius Julius(7ff1ff0bc1d0) has gained a new trait(Factionleader)(level-Faction Leader)
```

## Enable error dialog for detailed logging

This mode is similar to the original games -show_err dialog but it displays the extended errors & warnings from the new `enable_logging` system. This enhanced mode should display more useful errors and warnings.

You need to add the string `enable_dialogs` to the advanced options (see screenshot).

![Script Logging](/documentation/feature_guides/logging/enable_dialogs.jpg)

**NOTE** As this mod enables a lot of the original internal warnings from the game engine there are some warnings that can be ignored and exist in the unmodded base game.

## Enable script specific logging

When scripting you can get errors and items not triggering that need to be debugged. To assist with this we have a seperate verbose script logging mode. You need to add the string `verbose_script_logging` to the advanced options (see screenshot).

![Script Logging](/documentation/feature_guides/scripts/script_logging.jpg)

Once enabled you will find an extra file in the following location:

`/VFS/Local/Rome/logs/scripting_log.txt`

This option can be combined with other options like `enable_logging`. Please be aware the verbose script logging is **very** verbose. This is great for debugging issues line by line but the text file will start to get quite large if you play for an extended time and/or have complex scripts.

## Enable original error dialog

The original game would display an error dialog when the game engine encountered certain error messages. You can use this original error dialog in ROME REMASTERED as well.

You need to add the string `-show_err` to the advanced options (see screenshot).

![Script Logging](/documentation/feature_guides/logging/show_err.jpg)

**NOTE:** With the existence of the newer more detailed modding this function is no longer as useful to debugging modding so we reccomend using `enable_dialogs` if you wish to get pop-up dialogs. However for a more detailed debug option the logging to text file in `enable_logging` and `verbose_script_logging` will usually be your best option.

## Enable Battle Mode Unit Info

We have added a debug dialog to allow you to click on any unit in a 3D battle and get information on what assets the unit is using. This can help debug visual issues when adding in new or modifying existing units.

1. You need to open the preferences folder for ROME REMASTERED
2. Make sure the game is NOT running
3. Open the file called `Preferences Data` using a text editor
4. Search for the line that contains: `<value name="EnableBattleModelInfo" type="integer">0</value>`
5. Edit the `0` to a `1` so the line looks like this:                         `<value name="EnableBattleModelInfo" type="integer">1</value>`
6. Save the file.

Now when you are in a 3D battle if you `shift + click` on a unit you will get a dialog appear with the following information:

* Unit: UI String Name
* Battle Models:
  * Soldier: unit_name
  * Model: model
  * Texture: texture_name
* Ethnic variations
  * Skin offsets
  * Hair colours
  * Hair Styles
  * Beard Styles
  * Face Indexes

![Dialog](/documentation/feature_guides/logging/model_info_dialog.jpg)  

All this information is related to the offsets and definitions referenced in the [character guide](/documentation/techart_guides/Characters.md) and the  [DMB guide](documentation/data_file_guides/DMB.md).

## Enable Battle Mode Building Info 

We have added a debug dialog to allow you to hover over on any building in a 3D battle and get information on what assets the building is using. This can help debug visual issues when adding in new or modifying existing buildings. You need to add the string `-building_debug_info` to the advanced options (see screenshot).



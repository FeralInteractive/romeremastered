![Workshop_header_template](/Workshop_header_template.png)
# Launch Options - Logging & Debugging Tools

## Table Of Contents

   * [Table Of Contents](#table-of-contents)
   * [Introduction](#introduction)
   * [Enable detailed logging](#enable-detailed-logging)
      * [Example of log contents](#example-of-log-contents)
      * [Campaign AI Log contents](#campaign-ai-log-contents)
   * [Enable error dialog for detailed logging](#enable-error-dialog-for-detailed-logging)
   * [Enable script specific logging](#enable-script-specific-logging)
   * [Enable original error dialog](#enable-original-error-dialog)
   * [Enable Battle Mode Unit Info](#enable-battle-mode-unit-info)
   * [Enable Battle Mode Building Info](#enable-battle-mode-building-info)
   * [Enable option to log end-of-turn settlement religious conversion](#enable-option-to-log-end-of-turn-settlement-religious-conversion)
      * [Example of log contents](#example-of-log-contents-1)

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

### Campaign AI Log contents

When you enabled logging a second file alomgside `message_log.txt` will also start to be updated called `campaign_ai_log.txt` this file will contain information about what each faction AI is doing for their turn. It is extremely verbose but will provide information about their decision making process. You can use this to help you balance campaign AI in a little more detail as you can see what their decision makng process is and perhaps how to alter it by changing their AI personalities and other variables like victory conditions & scripting bonuses.

Below is a snippet from a log generated when running the the base game.

```AI: ========================================================================================
AI: 				start 'egypt' for year -270, season summer
AI: ========================================================================================


AI: ltgd: Update enemies of egypt
AI: finance: est income 11872, est maintenance 6628, est outgoings 7139 -- spending max 5000, spending norm 2500; balance AFB_EARN_MASSES, state AFS_ROLLING_IN_IT
AI: ltgd: defend (frontline 1.0, free 10277.999616, product 1.539092) vs fac 'seleucid': not at war, neither at war elsewhere >> ALD_DEFEND_NORMAL.
AI: ltgd: defend (frontline 89.272728, free 1.233113, product 2.158267) vs fac 'numidia': not at war, neither at war elsewhere >> ALD_DEFEND_NORMAL.
AI: ltgd: 'egypt' against 'seleucid', his frontline: 1, our frontline: 1
AI: ltgd: 'egypt' against 'seleucid', frontline balance: 1.0, production balance: 1.539092
AI: ltgd: 'egypt' invade 'seleucid', not at war, good production against strongest neighbour >> ALI_START_PLAN (200).
AI: ltgd: 'egypt' against 'numidia', his frontline: 66, our frontline: 5892
AI: ltgd: 'egypt' against 'numidia', frontline balance: 89.272728, production balance: 2.158267
AI: ltgd: 'egypt' invade 'numidia', not at war, superior frontline and overall >> ALI_INVADE_IMMEDIATE (500).
AI: ltgd: 'egypt' invade 'slave', since they have a neighbouring region >> ALI_INVADE_OPPORTUNISTIC (850).
AI: ltgd: number of invasion targets: 3```


## Enable error dialog for detailed logging

This mode is similar to the original games `-show_err` dialog but it displays the extended errors & warnings from the new `enable_logging` system. This enhanced mode should display more useful errors and warnings.

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

We have added a debug dialog to allow you to **shift + left click** on any unit in a 3D battle and get information on what assets the unit is using. This can help debug visual issues when adding in new or modifying existing units.

You need to add the string `battle_model_info` to the advanced options (see screenshot). This option can be combined with other options like `enable_logging`. 

![Script Logging](/documentation/feature_guides/logging/battle_model_info.jpg)

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

All this information is related to the offsets and definitions referenced in the [character guide](/documentation/techart_guides/Characters.md) and the [DMB guide](documentation/data_file_guides/DMB.md).

## Enable Battle Mode Building Info

We have added a debug dialog to allow you to **hover over** any building in a 3D battle and get information on what assets the unit is using. This can help debug visual issues when adding in new or modifying existing buildings.

You need to add the string `building_debug_info` to the advanced options (see screenshot). This option can be combined with other options like `enable_logging`. 

![Building Tooltip](/documentation/feature_guides/logging/building_debug_info.png)

## Enable option to log end-of-turn settlement religious conversion

This option provides detailed information on how end of turn settlement is working and can help modders turn how their religions are setup.

Add `log_conversion_calc` command line option to log end-of-turn settlement religious conversion to the command line, this option requires `enable_logging` to be active.

![log_conversion_calc](/documentation/feature_guides/logging/log_conversion_calc.jpg)  

### Example of log contents

```
Doing per turn religion update for region Scythia
{
  Dominant religion is tengrism

  Current profile:
   - hellenism        (current influence  5%) (conversion  0%)
   - paganism         (current influence 10%) (conversion 10%)
   - zoroastrianism   (current influence  0%) (conversion  0%)
   - daharmic         (current influence  0%) (conversion  0%)
   - tengrism         (current influence 85%) (conversion  5%)

  religion paganism has the highest conversion rate
  {
    Conversion strength over tengrism is 5% (10% - 5%)
    Meaning 4% (85 * .05) of the population gets converted

    Conversion strength over hellenism is 10% (10% - 0%)
    Meaning 1% (5 * .10) of the population gets converted
  }

  New profile:
   - hellenism        (new influence  4%)
   - paganism         (new influence 15%)
   - zoroastrianism   (new influence  0%)
   - daharmic         (new influence  0%)
   - tengrism         (new influence 81%)


  Dominant religion is now tengrism

}
```

## Enable option to log mismatches models

You need to add the string `report_model_mismatches` to the advanced options.

Be warned this will add 300+ lines of mismatches that in most cases aren't always useful when modding as some of these warnings are non-fatal and none issue. However can be useful in some cases.

## Enable option to log verbose skeleton & animation pack logs

You need to add the string `verbose_skeletons` to the advanced options.

Generates verbose skeleton & animation pack logs only needed when modding skeleton and animations.

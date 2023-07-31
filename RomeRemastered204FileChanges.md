![Workshop_header_template](/Workshop_header_template.png)
# 2.0.4 Data File Changes

## Table Of Contents

   * [Introduction](#introduction)
   * [New Files added](#new-files-added)
      * [data_controlled_features.json](#data_controlled_featuresjson)
      * [data_controlled_variables.json](#data_controlled_variablesjson)
      * [descr_battle_ai_personalities.txt](#descr_battle_ai_personalitiestxt)
      * [descr_diplomacy_comments.txt](#descr_diplomacy_commentstxt)
      * [descr_namelists.txt](#descr_nameliststxt)
      * [descr_sm_ambient_objects.txt](#descr_sm_ambient_objectstxt)
      * [descr_sm_faction_logos.txt](#descr_sm_faction_logostxt)
      * [descr_sm_icon_models.txt](#descr_sm_icon_modelstxt)
      * [descr_sm_major_events.txt](#descr_sm_major_eventstxt)
         * [major_event_scripts](#major_event_scripts)
            * [marian_reforms_trigger.txt](#marian_reforms_triggertxt)
      * [ui folder](#ui-folder)
         * [building_icons](#building_icons)
         * [buttons](#buttons)
         * [faction_icons](#faction_icons)
      * [ui_overrides folder](#ui_overrides-folder)
         * [ui_overrides - menu folder](#ui_overrides---menu-folder)
   * [Files Modified](#files-modified)
      * [descr_cultures.txt](#descr_culturestxt)
      * [descr_engines.txt](#descr_enginestxt)
      * [descr_event_enums.txt](#descr_event_enumstxt)
      * [descr_event_images.txt](#descr_event_imagestxt)
      * [descr_font_db.txt](#descr_font_dbtxt)
      * [descr_model_battle.txt](#descr_model_battletxt)
      * [descr_model_mount.txt](#descr_model_mounttxt)
      * [descr_namelists.txt](#descr_nameliststxt-1)
      * [descr_senate.txt](#descr_senatetxt)
      * [descr_settlement_plan.txt](#descr_settlement_plantxt)
      * [descr_sm_factions.txt](#descr_sm_factionstxt)
      * [descr_standards.txt](#descr_standardstxt)
      * [descr_time_of_day.txt](#descr_time_of_daytxt)
      * [export_descr_buildings.txt](#export_descr_buildingstxt)
      * [export_descr_character_traits.txt](#export_descr_character_traitstxt)
      * [export_descr_unit.txt](#export_descr_unittxt)
      * [items folder](#items-folder)
      * [models_building folder](#models_building-folder)
      * [models_engine folder](#models_engine-folder)
      * [settlement_plans folder](#settlement_plans-folder)
         * [Custom Campaign Map models (settlements and ports)](#custom-campaign-map-models-settlements-and-ports)
         * [Updated Ground &amp; Street Plans](#updated-ground--street-plans)
      * [sounds folder](#sounds-folder)
      * [string_overrides](#string_overrides)
      * [terrain folder](#terrain-folder)
      * [text folder](#text-folder)
         * [event_titles.txt](#event_titlestxt)
         * [expanded_bi.txt](#expanded_bitxt)
         * [quotes.txt](#quotestxt)
         * [strat.txt](#strattxt)
      * [toggles](#toggles)
         * [battle.txt](#battletxt)
         * [campaign.txt](#campaigntxt)
      * [ui_overrides folder](#ui_overrides-folder-1)
      * [world folder](#world-folder)
         * [custom battles](#custom-battles)
         * [camapaign](#camapaign)
   * [Files Deleted](#files-deleted)
      * [loadingscreen/symbols](#loadingscreensymbols)
      * [original_overrides](#original_overrides)

## Introduction

This page lists the key changes between 2.0.3 and 2.0.4. With all the major changes and links to relavant files as appropriate.

## New Files added

### data_controlled_features.json

Provides modding access to a number of modding specific features.

See [data_controlled_features.md](/documentation/data_file_guides/data_controlled_features.md) for more information.

### data_controlled_variables.json

Contains variables controlled by `data_controlled_features.json` See [data_controlled_features.md](/documentation/data_file_guides/data_controlled_features.md) for more information.

### descr_battle_ai_personalities.txt

With the introduction of this file the AI personalities inside 3D battles are now moddable. This file contains all constants used by the AI. These values affect which orders the units are given, but **not the pathfinding/way the orders are carried out**. 

See [descr_battle_ai_personalities.md](/documentation/data_file_guides/descr_battle_ai_personalities.md) for more information.

### descr_diplomacy_comments.txt

This file was added to support additional factions and cultures with custom diplomacy options if modders want. This is optional.

```
;;diplomacy comment DB

;;format is as follows

; comment <comment type>
; {
; 	<key in diplomacy.txt> (next bit is optional, equivalent to (from all, to all) if not specified)
;	{
;		from <faction type/culture/all> [, <faction type/culture/all>]
;		to <faction type/culture/all>
;	}
; }
```
### descr_namelists.txt

New way of organising names to allow for easier assigning.

```
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; Names Database Entries
;;
;; Holds non-localised Latin names for settlements and characters.  These are arranged on
;; a per faction basis.
;;
;; Entries are specified by the following syntax:
;;
;; faction: <faction name>
;;	settlements
;;		<settlement names list>
;;	characters
;;		<character names list>
;;
;; faction ... etc
```

### descr_sm_ambient_objects.txt

It allows you to add ambient objects (wth optional sounds) to the campaign map. You can also define if they are impassable or not. Given you can turn these on and off using a script ambient objects are not just decorative they could be used to block and unblock areas of the map via scripted events 

See [descr_sm_ambient_objects.md](/documentation/data_file_guides/descr_sm_ambient_objects.md) for more information on how these work.

### descr_sm_faction_logos.txt

Used to define the indexes for the logos referenced in `descr_sm_factions`. The order in this file is used to generate the index number used in the `descr_sm_factions` file

### descr_sm_icon_models.txt

The generic info icons/models above settlements have been moved out of `descr_cultures` and into this file.

### descr_sm_major_events.txt

Contains the marian reforms as the example of how the new major events can be defined. The file is fully documented and should be self explanatory.

```
;;if you want to enable/disable a particular event, do
; set_major_event_enabled <trigger name>, false

;;also note that the message uses the marian reforms message as a base, in case you were wondering

"major events":
[
	"marian_reforms":
	{
		;;which factions should get notifications about this
		"affects": [ "all", ],
		
		;;should this event be tracked globally or individually for each affected faction
		;;(if false, notifications will only be sent to the faction that meets the condition)
		"global": true,

		;;when general units are assigned to this event, should it take priority over general units assigned to other events with lower priorities
		;;the default general units have a priority of 0, so make sure to set that
		"priority": 100,
	
		;;settings for when the event is activated
		"activation":
		{
			;;script for the trigger conditions for this event
			;;NOTE: if individual is true, this will be triggered from a faction scope, otherwise it won't be scoped at all
			"trigger conditions": "major_event_scripts/marian_reforms_trigger.txt",
			
			;;when this triggers, switch these units to those units
			"unit switches":
			{
				;;bodyguard swaps
				"barb chieftain cavalry early dacian": "barb chieftain cavalry dacian",
				"barb chieftain cavalry early gaul": "barb chieftain cavalry gaul",
				"barb chieftain cavalry early german": "barb chieftain cavalry german",
				"barb chieftain cavalry early scythian": "barb scythian general scythian",
				"carthaginian general's cavalry early": "carthaginian general's cavalry",
				"egyptian general's bodyguard early": "egyptian general's bodyguard",
				"greek general's guard cavalry early": "greek general's guard cavalry",
				"thracian bodyguard early": "thracian bodyguard",
				"roman generals guard cavalry early": "roman generals guard cavalry",
			},
			
			;;should we also use a large panel in addition to a news message
			;;also triggers the near victory music
			"use big panel": true,
			
			;;title and body, as defined in text/major_events.txt
			"title":	"SMT_A_NEW_MAN__GAIUS_MARIUS_TITLE",
			"body":		"SMT_A_NEW_MAN__GAIUS_MARIUS_BODY",
			
			;;image, as redirected per-culture in ui/<culture name>/eventpics
			"image":	"marian_reform",
		},
		;;settings for when the event is deactivated (needs to be activated first ofc)
		"deactivation":
		{
		},
	},
],
```

#### major_event_scripts

This folder contains all of the trigger files for major events. In the original game this only contains the Marian reforms but in mods you can add as many major events as you like.

##### marian_reforms_trigger.txt

This is a simple script per 

```script
	;;check every settlement in the world
	for_each settlement in world
		if		HasResource italy						;;has the italy hidden resource
			&&	I_SettlementLevel local >= huge_city	;;is a huge city
			&&	I_SettlementOwnerCulture local == roman	;;the owner is roman
			&&	not SettlementName Rome					;;the settlement isn't rome
			
			return true ;;trigger marian reforms
		end_if
	end_for

	return false ;;don't trigger marian reforms
end_script```

### feral_descr_movement_multipliers.txt

### feral_descr_truesky.txt

### major_events.txt

Inside the `/text` folder there is a new text file to store strings for Major events. Mods can use this file when adding new events or modifying the existing events.

You will also find localised versions in the folder for localising the mod.

```{SMT_A_NEW_MAN__GAIUS_MARIUS_TITLE}	A New Man: Gaius Marius
{SMT_A_NEW_MAN__GAIUS_MARIUS_BODY}	Gaius Marius has proposed a series of laws that allow the proletariat to join his reorganised Roman army. In return for many years of military service every soldier will be given land as a kind of pension. This reform is passed in the people's assembly without the approval of the Senate. It's a certainty that such popular - and populist - appeal will do Marius no favours in the long run!\n\nThe troop types available for recruitment now reflect the structure of this new professional army. Check the recruitment scroll to view the details.
```

### ui folder

With the ability to mod and add new factions, building types and religions the UI elements for all 3 are now stored in the following location for ease of modding.

#### building_icons

These are the tag icons used on the building browser and overlayed on top of building cards showing the player the type of building. These can be modified or added to as needed.

See [EDB.md](/documentation/data_file_guides/EDB.md) for more information on how to link to these images.

#### buttons

These are the icons used for different religions in the game. These can be modified or added to as needed.

You can look at the Religion example mod [here](/example_mods/ExampleMods.md) to see how to link these images to the rest of the religion files.

#### faction_icons

These are the icons used for different factions in the game. These can be modified or added to as needed.

You can look at the Faction example mod [here](/example_mods/ExampleMods.md) to see how to link these images to the rest of the faction files.

### ui_overrides folder

This folder contains .pos layout files for the game UI, the following new files have been added to add support for new large info panel feature:

* campaignuicentralagentinfo.pos
* campaignuicentralbuildinginfo.pos
* campaignuiunitinfolarge.pos

#### ui_overrides - menu folder

 * dialog_generic_confrm_large.xml - Generic confirm panel xml file
 * menu_colours.json - You can now define all the main menu colours with hex values.

## Files Modified

### descr_cultures.txt

Mods using the old format files will stull work but will put warnings in the logs. However it's best to update to the new format as the new format apart from allowing unlimited cultures also allows you to define the following:

 * unrest factors - Squalor, Over-crowding, distance from capital
 * settlement upgrade levels - Population requirements, over crowding values etc
 * custom settlement models per settlement, custom fort and watchtower models as well 
 
See comments inside the _desc_cultures.txt_ file for more details.
 
 ### descr_engines.txt
 
 Minor edits to specific seige equipment to improve path finding.

### descr_event_enums.txt

Add the following 3 items into the events file:

* roman_empire_unstable_currency
* roman_empire_stable_currency
* script_prompt

The first two are used for the debased currency penalty in BI and the final one is used for the new `script_prompt` news article modding feature.

You can look at the `script_prompt` example mod [here](/example_mods/ExampleMods.md) to see how you can use this new event. 

### descr_event_images.txt

Updated the logic in the file to deal with the newly added support for additional religions, multiple super factions, emergent factions and the new `script_prompt` feature.

### descr_font_db.txt

Added new font sizes for additional formatting options inside .cas files.

* cinzel_lrg
* cinzel_lrg_bold
* cinzel_huge
* cinzel_huge_bold
* verdana_sml_med
* verdana_sml_med_bold
* cinzel_sml_med
* cinzel_sml_med_bold

### descr_model_battle.txt

* Disable the following items as they are unique so don't need a default mapping.
  * `data/animals/textures/mount_elephant_african_cataphract_base_default.tga`
  * `data/animals/textures/mount_camel_cataphract_base_default.tga`
  * `data/animals/textures/mount_horse_cataphract_base_default.tga`
  
### descr_model_mount.txt

 Minor edits to chariots hit boxes to improve path finding.
 
### descr_namelists.txt

This file is no longer used by the game and has been superseded by `descr_namelists.txt` 

### descr_senate.txt

Updated the senate file as this needs to be set per-faction now as we can now have multiple senate files.

See [descr_senate.txt](/example_mods/super_faction/data/descr_senate.txt) example mod for more information.

### descr_settlement_plan.txt

Add a way to specify tags instead of buildings tags. Allows for more flexible systems with buildings while making sure they still appear correctly in the building plans. So:

```
buildings
			{
				temple_of_battle temple_of_battle_shrine
			}
			
```
			
becomes:

```
buildings
			{
				none
			}
			;; JNF 2021-11-02 - Add a way to specify tags instead of buildings
			tags
			{
				;;so this represents any building tagged as a "temple" at level >= 0
				temple 0
			}
```

For more examples see the new file inside game data.

### descr_sm_factions.txt

The faction system has been reformatted to make for easier and more flexible modding but the old format is still usable with a few small edits.

```
;;Old style preserved, only difference is:

; standard_index
; logo_index
; small_logo_index

;;Needs to be replaced with:

; standard_index
; rebel_standard_index
; logo_index
; rebel_logo_index
```

However we suggest you update your mod to the new format as it exposes new features like faction groups, namelists, ai personalities and family trees.

See [descr_sm_factions.md](/documentation/data_file_guides/descr_sm_factions.md) for more information.

### descr_standards.txt

Extra comment showing what banners are normal and which are used for rebels.

### descr_time_of_day.txt

Minor tweaks to time of day for various maps plus added an info header below if modders want to add their own maps and time rules.

```
;;Format:
;;map_name
;;{
;;	season
;;  {
;;		time_name time_of_day_24h
;;		...
;;	}
;;	...
;;}
;;If a map is not specified, "default_times" is used instead.
```
### export_descr_buildings.txt

This file has been updated to support the new limits and also compliment the new features in the building browser and other areas of the game like scripting, negative bonuses and UI.

The new system uses exclusivity tags so you can have exclusive buildings, custom strings and more complex requirements.  

See [export_descr_buildings.md](/documentation/data_file_guides/EDB.md) for more information.

### export_descr_character_traits.txt

Updated traits for senate/super faction roles now that you can have multiple custom super factions in a mod.

### export_descr_unit.txt

 * Add support for `recruit_priority_offset` a % modifier for AI recruitment priority (optional). 
 * Replaced all instances of `general_unit_upgrade` with `general_unit_upgrade "marian_reforms"`, so we can specify multiple general unit upgrades.

See [export_descr_unit.md](/documentation/data_file_guides/EDU.md) for more information.

### items folder

A few items have been updated to fix minor issues

### models_building folder

A few cas files have been updated to fix minor issues

### models_engine folder

The tort ram has been updated

### settlement_plans folder


#### Custom Campaign Map models (settlements and ports)

All settlement plans now allow for specific settlement models on the campaign map, this includes the port model if applicable. These can also be customised per settlement upgrade level. See example of a huge city below.


```
{

;; JNF 2021-09-06 - Define model as part of plans now - allows for specific settlement models
;; and generally makes the code logistics more straightforward
strat
{
	buildings		data/models_strat/residences/roman_huge_city_buildings.CAS
	default_base	settlement_roman_level_6

	;;walls and base map overrides
	fortifications
	{
		wooden_pallisade
		{
			model	data/models_strat/residences/roman_huge_city_wall_1.CAS
			base	settlement_roman_walled_level_6
		}
		wooden_wall
		{
			model	data/models_strat/residences/roman_huge_city_wall_2.CAS
			base	settlement_roman_walled_level_6
		}
		stone_wall
		{
			model	data/models_strat/residences/roman_huge_city_wall_3.CAS
			base	settlement_roman_walled_level_6
		}
		large_stone_wall
		{
			model	data/models_strat/residences/roman_huge_city_wall_4.CAS
			base	settlement_roman_walled_level_6
		}
		epic_stone_wall
		{
			model	data/models_strat/residences/roman_huge_city_wall_5.CAS
			base	settlement_roman_walled_level_6
		}
	}

	;;models for ports (only relevant for settlements)
	ports
	{
		fishing_village
		{
			land_model	data/models_strat/residences/roman_fishing_village.CAS
			base	port_roman_level_1
		}
		sea_port
		{
			land_model	data/models_strat/residences/roman_port_01_land.CAS
			sea_model	data/models_strat/residences/roman_port_01_sea.CAS
			base	port_roman_level_2
		}
		shipwright
		{
			land_model	data/models_strat/residences/roman_port_02_land.CAS
			sea_model	data/models_strat/residences/roman_port_02_sea.CAS
			base	port_roman_level_3
		}
		dockyard
		{
			land_model	data/models_strat/residences/roman_port_03_land.CAS
			sea_model	data/models_strat/residences/roman_port_03_sea.CAS
			base	port_roman_level_4
		}
	}
}
}

```

#### Updated Ground & Street Plans

Minor updates to improve 3D battles

 * Updated Barbarian city ground type
 * Updated Barbarian town street plan
 * Added new Egyptian huge city plan

### sounds folder

 * Added new sub section for pre-battle speeches
 * 100s of small edits to improve audio levels and fading mostly in `descr_misc_sounds.txt`
 
 The files are all documented so you can read the headers in the folder to find out more about how pack/unpack and edit these files. 

### string_overrides

Reminder that only strings that you wish to change need to be added to the new files. Any strings not present in them will be taken from the original files.

### terrain folder

A bridge cas file was updated to fix minor issue

### text folder

There are a number of files here that have been modified with added or updated strings

#### event_titles.txt

`{script_prompt}	[PLACEHOLDER]` This isn't an issue as you can inject your own strings. 

You can look at the `script_prompt` example mod [here](/example_mods/ExampleMods.md) to see how you can add your own custom strings. The `Hot Seat` mod also uses this feature. 

#### expanded_bi.txt

Added in strings for the new senate roles now that they can be customised and added to.

```
{SMT_SENATE_OFFICE_QUAESTOR_TITLE}	Quaestor
{SMT_SENATE_OFFICE_QUAESTOR_DESCRIPTION}	The lowest rank of magistrate, usually charged with managing the treasury and the first meaningful appointment of all men looking for a political career in Rome.
{SMT_SENATE_OFFICE_AEDILE_TITLE}	Aedile
{SMT_SENATE_OFFICE_AEDILE_DESCRIPTION}	An administrative official in charge of supervising streets, temples and the quarters of a city and the distribution of the cura annonae, the all-important corn supply.
{SMT_SENATE_OFFICE_PRAETOR_TITLE}	Praetor
{SMT_SENATE_OFFICE_PRAETOR_DESCRIPTION}	A magistrate whose duties are mostly concerned with justice and law, particularly the ius civile (civil, not criminal, law) and ius gentium (laws dealing with foreigners). 
{SMT_SENATE_OFFICE_CONSUL_TITLE}	Consul
{SMT_SENATE_OFFICE_CONSUL_DESCRIPTION}	The supreme position of power and honour in the Republic, a consul has authority over magistrates, the army and law-making. He is, in many ways, a king in all but name during his time in office. 
{SMT_SENATE_OFFICE_CENSOR_TITLE}	Censor
{SMT_SENATE_OFFICE_CENSOR_DESCRIPTION}	An important office that conducts the census and keeps the lists of Roman citizens and Senators, meaning that it is the censors that decide who is Roman or not, and who is a Senator or not. 
{SMT_SENATE_OFFICE_PONTIFEX_MAXIMUS_TITLE}	Pontifex Maximus
{SMT_SENATE_OFFICE_PONTIFEX_MAXIMUS_DESCRIPTION}	The supreme head of the Roman state religion and controller of all religious colleges including the Vestal Virgins. He is in absolute control of doctrine and to a great extent above the jurisdiction of the Senate and People of Rome.
{SMT_TECH_TREE_THREAD_REQUIRES_TEMPLE_DESTRUCTION}	Building this item requires the destruction of an existing religious building
{roman_empire_stable_currency}	Currency Crisis Resolved
{Capability_TraitsAndRetinue}	Unlocks new traits and followers
```

#### quotes.txt

* Removed an errant full stop.

#### strat.txt

* Fixed a few descriptions so they work with negative values (due to negative bonus values now being possible)
* Added some missing colons on some bonus value strings

### toggles

Added toggles for a few improvements into the classic/remastered toggles for battle and campaign

#### battle.txt

 * improved blocked placement :: 1

#### campaign.txt

 * ai civil war :: 1

### ui_overrides folder

The following files have been updated to fix minor issues or linked to new features.

 * campaignuicentral.pos
 * campaignuileftagentinfo.pos 
 * campaignuileftbuildinginfo.pos 
 * campaignuireligiondetails.pos 
 * campaignuileftunitinfo.pos 
 * campaignuileftunitinfomergescreen.pos 
 * campaignuileftunitinfomergescreenmirrored.pos
 * campaignuileftsettlmentdialog.pos
 * campaignuifactiondialog.pos
 * factiondialog.pos
 * fullscreenfamilytree.pos
 * replayui.pos
 * saveloaddialog.pos
 * savereplaydialog.pos   

### world folder

There are a few edits in this folder for custom battles and the campaign.

#### custom battles

Updated gergovia battles so Gaius Julius is defined as a named_character not a general. This is part of the other fixes with names and expanding cultures etc

#### camapaign

Updated `descr_strat` with the following edits:

 * Gave `Vibius Julius` a `portrait_index` value so he has a fixed portait picture.
 * Added in brand new section to define a super faction as these are now moddable.

## Files Deleted

### loadingscreen/symbols

The symbols for loading screens have been moved to a new location. See faction_icons area in the new files area of this document for details.

### original_overrides

Merchants override file is no longer needed as merchants are now toggled in a different manner that doen't require an override file.


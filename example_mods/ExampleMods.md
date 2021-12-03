![Workshop_header_template](/Workshop_header_template.png)
# Example Mods

This page lists the various example mods that exist for Rome Remastered.

## Table Of Contents

   * [Table Of Contents](#table-of-contents)
      * [Adding Factions](#adding-factions)
      * [Adding Religions](#adding-religions)
      * [Unit Variation](#unit-variation)
      * [Display an interactable message via scripting](#display-an-interactable-message-via-scripting)
      * [Disable Region Names On Settlement Tags (Campaign Map)](#disable-region-names-on-settlement-tags-campaign-map)
      * [Med 2 Style Opaque FoW](#med-2-style-opaque-fow)
      * [Decorative Resources](#decorative-resources)
      * [Enhanced Tweaks](#enhanced-tweaks)
      * [Units With Multiple Requirements](#units-with-multiple-requirements)
      * [Super Factions with extra members and offices.](#super-factions-with-extra-members-and-offices)
      * [Unit Attributes - New RR Attributes](#unit-attributes---new-rr-attributes)
      * [New Limit of 9 Officers](#new-limit-of-9-officers)
      * [Night Torches Anytime](#night-torches-anytime)
      * [Factionwide Building Checks](#factionwide-building-checks)
      * [Use'building_factions' condition for recruitment lines](#usebuilding_factions-condition-for-recruitment-lines)
      * [UI Mod Example - Replacing Unit Info with large panel from Campaign](#ui-mod-example---replacing-unit-info-with-large-panel-from-campaign)
      * [Rome Hot-seat Example - Allows you to play hot-seat with in game UI for choosing factions.](#rome-hot-seat-example---allows-you-to-play-hot-seat-with-in-game-ui-for-choosing-factions)

### Adding Factions

Factions have been updated to support virtually unlimited numbers of factions. In doing so certain features linked to factions have been extended or improved.

We have made a sample mod that demonstrates how to add in additional factions beyond the original ones found in the game, it also demonstrates how to make a faction emergent.
	
This mod adds the unused White Huns and Moors factions to BI. The Moors start in Mauretania and the White Huns appear as an emergent faction. This mod is designed to work on BI only but the principle will work with all three games if you use the correct assets for that game.

You can see how to do this by referring to the```BI_extra_factions``` example mod in the example mod area of GitHub.

![BI_extra_factions](/example_mods/BI_extra_factions/BI_extra_factions.jpg)

### Adding Religions

Adds the Pagan, Daharmic, Zoroastrian and Hellenic religions to the Alexander campaign as an example. The key changes to religion compared to the original release are detailed below.

 * Reformated the religion file to make it easier to maintain with larger numbers of religions.
 * Change every instance of the religion pips from the sprite sheet to use external TGAs to allow mods to easily add in as many religions as they want. 
 * Add the ability to define the amount of unrest a religion will create relative to it's population. 
 * Allow religions with no influence to be hidden from the overview panel.
 * Add log_conversion_calc command line option to log end-of-turn settlement religious conversion to the command line.
 * Modify religion overview UI to allow scrolling when more than 3 religions are defined and leave empty spaces when less then 3 are present in a settlement.
 * Fix rebel settlements always being angry all the time because rebel settlements would always use the world dominant religion if no temple building was present so you'd get 90% christian settlements being officially pagan
 * Add three conditions to the building db: 
   * ```religion <religion> <comparison> <number>``` (i.e. "religion christian < 60") to test the influence of a religion
   * ```majority_religion <religion>``` to check if a given religion is the majority religion of this settlement
   * ```official_religion <religion>``` to check if a given religion is the official religion of this settlement
 * Allow religions to automatically create a trait for themselves if one doesn't exist.
 * Allow adding a ```religion``` section to settlement definitions in descr_strat.txt to override the religious profile defined in descr_regions.txt if needed.
 * Allow adding ```religious_order``` religious unrest suppression to buildings, which was previously limited to only character traits.
 * Allow traits and ancillaries to have more than one religious conversion and order effect and also fix the problem with some characters in BI getting stuck with zero commitment
  * We always show the _dominant_ commitment, not the official one in the settlement religion panel. Instead, official religion will be shown in a tooltip (assuming it's different from the dominant religion) with a reason for why it's like that (i.e. set by temple or by the governor).

![alex_extra_religions](/example_mods/alex_extra_religions/alex_extra_religions.jpg)

### Unit Variation

You can now specify multiple models that are then used at random by the game when rendering a unit on the battle field. You can also define the model grouping per upgrade level allowing for units to look different as they are upgraded as well. 

For more detail on the options review the files inside the```unit_variation``` example mod in the example mod area of GitHub. You can see the results by looking at the Hastati unit inside the game.

![unit_variation](/example_mods/unit_variation/unit_variation.jpg)

### Display an interactable message via scripting

You can now display an Alert message to the player which has a Yes/No decision attached to it. This message has to be responded to before the player ends their turn. This works in a similar manner to the adoption UX except the title, main content and image are all controlable by the modder.

The players responce is then passed back to the script where it can be used to trigger behaviour. In this example ticking yes will cause Alexander to die ending the Campaign.

This could be used to allow for the player to choose branching options or add more role playing based elements to the mod.

![script_message](/example_mods/script_message/script_message.jpg)

### Disable Region Names On Settlement Tags (Campaign Map)

As part of the 2.0.4 update the settlement tags now mention the settlement region below the settlement name. However this can be disabled using the data_controlled_features.json in the root of the game data folder.

You can see how to do this by referring to the```No_regions_on_tags``` example mod in the example mod area of GitHub.

![No_regions_on_tags](/example_mods/No_regions_on_tags/No_regions_on_tags.jpg)

### Med 2 Style Opaque FoW

Added an alternate campaign FOW mode. In the new mode, the FOW is opaque meaning that players cant see the terrain until they have explored it. This applies to the FOW over the actual terrain, the minimap and the map overlay.

This can be enabled using the data_controlled_features.json in the root of the game data folder. You can see how to do this by referring to the```opaque_fow_mode``` example mod in the example mod area of GitHub.

![opaque_fow_mode](/example_mods/opaque_fow_mode/opaque_fow_mode.jpg)


### Decorative Resources

These are a new type of resources that don't have any functionality and can be used purely to make the campaign map more detailed and interesting. 

For more detail on the options review the files inside the```decorative_resources``` example mod in the example mod area of GitHub. This mod demonstrates the feature by making all resources nonfunctional but still visible as decorative resources only.

![decorative_resources](/example_mods/decorative_resources/decorative_resources.jpg)

### Enhanced Tweaks

There is a mode inside the game that allows you full access to the settings inside the game engine which you can tune to make specific styles and visuals that you can then save inside your mod to share with others.

You can enabled the in game overlay adding ```enhanced_tweaks``` in the text box inside the Advanced tab of the pre game options window.

After that you can save and load settings files for the main menu, campaign map and 3d battles. The json files are saved in a folder called `EnhancedTweaks` in the root of the `Total War ROME REMASTERED` preferences folder. You can then copy them into the `enhanced_tweaks` folder inside your mod see this example mod for specifics.

Please note the 3 different modes have different options and they are not saved when you transition between the modes so please make sure you save your settings before you swap to a different area of the game else you will need to make them again.

In this example mod the trees on the campaign map have been made oversized and purple shaded!

![EnhancedTweaksExample](/example_mods/EnhancedTweaksExample/EnhancedTweaksExample.jpg)

### Units With Multiple Requirements

The UI in the building browser has been updated to support units having multiple requirements and having those requirements exposed to the user.

This mod adds the requirement of a Wooden Wall to recruit Town Watch. It also adds the limitation that you can no longer recuit Hastati once you have build a Stone Wall or above.

Both of these limitations when triggered will appear in the tooltip and the unit will become greyed out in the Building info panel.

![EDB_Units_Multiple_Requirements](/example_mods/EDB_Units_Multiple_Requirements/EDB_Units_Multiple_Requirements.jpg)

### Super Factions with extra members and offices.

You can now have (within reason) unlimited Superfactions, Super Faction Members and Offices per faction. See this example mod and the headers of the two files more more details.

Adds the following factions to make a new super faction:

 * Macedon
 * Egypt
 * Seleucid Empire
 * Parthia
 * Pontus
 
 The following Offices were extended:
 
 * 3x Consul
 * 2x Censors
 * 4x Pontifex Maximus


![super_faction](/example_mods/super_faction/super_faction.jpg)

### Unit Attributes - New RR Attributes

This is a very simple mod that shows how you can modify unit attributes using 3 newly added attributes unique to Rome Remastered.
	
This mod will add for following attributes to some of the base units for the Julii faction:

 * `extremely_hardy` - An additional level of stamina above hardy. (Town Watch)
 * `infinite_ammo` - Allows a unit to have infinite ammo. (Roman Archers)
 * `inexhaustible` - Disables stamina for this unit (No UI). (Roman peasant)

Load the mod using the Julii faction to see them in game.

![unit_features](/example_mods/unit_features/unit_features.jpg)

### New Limit of 9 Officers

Rome Remastered has increased the maximum number of officers from 3 to 9. This mod enables the Roman Peasants to have 9 officers in their unit as an example.

![extra_officers](/example_mods/extra_officers/extra_officers.jpg)


### Night Torches Anytime

This mod allows you to edit what angle of sun makes units start using torches. This allows more ability to allow units to use torches at sunrise and sunset depending on other lighting mods. In some mods you might want all sunrise and sunset battles to use torches.

You can refer to the files inside the mod.

 * set `night_control` to true to enable this feature (`data_controlled_features.json`)
	
 * `torches_min_sun_angle` - This defines what angle units start to use torches in the morning (`data_controlled_variables.json`)
 * `torches_max_sun_angle` - This defines what angle units start to use torches in the afternoon (`data_controlled_variables.json`)

In this example we have set the values to 0 and 360 meaning the units will use torches all day long.

![night_torches](/example_mods/night_torches/night_torches.png)

### Factionwide Building Checks

Example mod with a building that has a faction wide check. With this check you can restrict a building to one per faction instead of one per settlement.

Modifies EDB to prevent a faction building temples when one already exists in any settlment controlled by that faction. Allows for faction wide capabilities for buildings.

![FactionwideBuildingTest](/example_mods/FactionwideBuildingTest/FactionwideBuildingTest.jpg)

### Use'building_factions' condition for recruitment lines

This mod will restrict the "town watch" unit to only be recruitable in barracks created by the gauls. This means factions can gain access to specific factions only via conquest not via building.

Testing steps:

 * Play as the julii
 * Observe that Town Watch units cannot be created in any of your settlements
 * Capture the gaul settlement near Venice (Patavium)
 * Repair muster field if damaged
 * Observe that town watch units may be recruited there

![GaulTownWatch](/example_mods/GaulTownWatch/GaulTownWatch.jpg)

### UI Mod Example - Replacing Unit Info with large panel from Campaign

This mod demonstrates how UI panels in the Remaster can be rearranged and modified to look different. This is a very simple mod that takes the large unit panel from the Campaign mode and replaces the small battle optimised card with this bigger descriptive one.

This mod is also a good example of how UI mods are in most case completely compatible with other mods as long as those mods don't also modify the same UI files. This means if you enable this mod along with most other gameplay mods you can play most mods with a separate mod for the UI edits.

![UI_Battle_Large_Unit_Info](/example_mods/UI_Battle_Large_Unit_Info/UI_Battle_Large_Unit_Info.jpg)

### Rome Hot-seat Example - Allows you to play hot-seat with in game UI for choosing factions.

This mod allows you to play Total War: ROME REMASTERED in hot-seat mode. To use the mod just start a new campaign using the Julii faction. When the campaign loads you will get given alerts asking you if you'd like to play as each faction one by one.
	
Once you have gone through all of the factions, the game will save your choices and the hot-seat campaign will begin. Please note due the hot-seat being played on a single machine the following limitations apply.
	
Only the active player can fight battles in 3D so all battles should be auto resolved. Also on end turn the AI will fight players battles for them and make of tactical decisions so ensure any critical choices like completing unit movement is done during your turn.
	
This mod is also meant to be a simple demonstation of how you can use the new modding features provided inside Total War: ROME REMASTERED to allow for customised game experiences. This mod makes use of a number of new features including but not limited to, background script support, persistent counters, custom alerts with user responses, new camera positioning code and new script logging to help test functionality during debugging.
	
![HotseatFactionSelector](/example_mods/HotseatFactionSelector/HotseatFactionSelector.jpg)

### Localisation Example

This mod demonstrates how mods can be fully localised in the Remaster without needing to have sub mods or replacing the EN strings with localised ones.

In this mod we have renamed Segesta in all languages to Example_[Language Code]. This shows how you can localise your mod for all languages without needing to add sub mods, just add the extra files. If the localised language file is missing the game will default back to the EN version.

Although this example just edits a single strings file all strings files inside the game data have the same naming convention for other languages so the same provess can eb replicated.

![Localisastion_Test](/example_mods/Localisastion_Test/Localisastion_Test.jpg)

![Workshop_header_template](/Workshop_header_template.png)
# Rome Remastered 2.0.4 Update

This page focuses on the key updates and features added with the 2.0.4 patch.

## Table Of Contents

   * [New Game Features in 2.0.4](#new-game-features-in-204)
      * [New UX Features](#new-ux-features)
         * [New full size info panels for units and buildings.](#new-full-size-info-panels-for-units-and-buildings)
         * [Add region names underneath settlement names in the campaign tags](#add-region-names-underneath-settlement-names-in-the-campaign-tags)
         * [Add population and public order to settlement captured screen](#add-population-and-public-order-to-settlement-captured-screen)
         * [Add "Previously Seen" Fog Of War stage to the minimap.](#add-previously-seen-fog-of-war-stage-to-the-minimap)
         * [Show religion percentage on the settlement icon tooltip](#show-religion-percentage-on-the-settlement-icon-tooltip)
         * [Let players see religion in non-owned settlements if they can also see population loyalty](#let-players-see-religion-in-non-owned-settlements-if-they-can-also-see-population-loyalty)
         * [Add tooltips specifying the rebel sub-type for characters and settlements.](#add-tooltips-specifying-the-rebel-sub-type-for-characters-and-settlements)
         * [Improvements to card order when grouping/ungrouping units](#improvements-to-card-order-when-groupingungrouping-units)
         * [Minor fixes to avoid text clipping on some screens](#minor-fixes-to-avoid-text-clipping-on-some-screens)
         * [Building Browser, Info Panels &amp; Tooltips - Improved Requirements Information.](#building-browser-info-panels--tooltips---improved-requirements-information)
         * [Smaller Miscellaneous UX Improvements](#smaller-miscellaneous-ux-improvements)
      * [Factions](#factions)
         * [Line of sight correctly disables when the Roman Civil War starts](#line-of-sight-correctly-disables-when-the-roman-civil-war-starts)
      * [Religion](#religion)
         * [Fixed issue with rebel settlements always being angry due to religion](#fixed-issue-with-rebel-settlements-always-being-angry-due-to-religion)
      * [General Gameplay](#general-gameplay)
         * [Fix the trigger for Achievement 'My Trade Goods Bring all the Boys to the Yard'](#fix-the-trigger-for-achievement-my-trade-goods-bring-all-the-boys-to-the-yard)
         * [Fix rebel merchants generating income for the settlement they are sitting in](#fix-rebel-merchants-generating-income-for-the-settlement-they-are-sitting-in)
         * [Allow Assassins to queue up a move for next turn even if they have already conducted an action this turn.](#allow-assassins-to-queue-up-a-move-for-next-turn-even-if-they-have-already-conducted-an-action-this-turn)
         * [Armies can no longer construct sap points if they physically cannot use them with their current units](#armies-can-no-longer-construct-sap-points-if-they-physically-cannot-use-them-with-their-current-units)
         * [Improve and simplify ram &amp; chariot outlines and hitboxes](#improve-and-simplify-ram--chariot-outlines-and-hitboxes)
      * [Sound - Miscellaneous minor fixes and improvements](#sound---miscellaneous-minor-fixes-and-improvements)
         * [Duck audio if the battle is paused](#duck-audio-if-the-battle-is-paused)
         * [Fix units saying 'orders completed' when they were given invalid orders](#fix-units-saying-orders-completed-when-they-were-given-invalid-orders)
      * [New Campaign Features](#new-campaign-features)
         * [Support Multiple Family Trees &amp; Other Improvements](#support-multiple-family-trees--other-improvements)
         * [Prevent the AI from requesting a trade agreement with a faction they have an embargo with.](#prevent-the-ai-from-requesting-a-trade-agreement-with-a-faction-they-have-an-embargo-with)
         * [Prevent being able to simultaneously declare a trade embargo and offer trade rights in the same diplomatic proposition](#prevent-being-able-to-simultaneously-declare-a-trade-embargo-and-offer-trade-rights-in-the-same-diplomatic-proposition)
         * [Improve the chance of AI attacking forts especially when they are occupied in their own territory.](#improve-the-chance-of-ai-attacking-forts-especially-when-they-are-occupied-in-their-own-territory)
      * [New Battle Features](#new-battle-features)
         * [Battle AI Enhancements](#battle-ai-enhancements)
            * [Improve placement of units in enclosed areas](#improve-placement-of-units-in-enclosed-areas)
            * [Block invalid formations](#block-invalid-formations)
            * [Improve a number of aspects of wall pathing logic over original.](#improve-a-number-of-aspects-of-wall-pathing-logic-over-original)
            * [Pathing improvement when choosing first point on a path.](#pathing-improvement-when-choosing-first-point-on-a-path)
            * [Tighten conditions for stopping a charge so units can close gaps better.](#tighten-conditions-for-stopping-a-charge-so-units-can-close-gaps-better)
            * [Fix and optimise grouping algorithm for wall units.](#fix-and-optimise-grouping-algorithm-for-wall-units)
            * [Add implementation of "Hungarian Algorithm" that solves the assignment problem.](#add-implementation-of-hungarian-algorithm-that-solves-the-assignment-problem)
            * [Improve defensive AI for walls](#improve-defensive-ai-for-walls)
            * [Improve UI path logic for attacking siege towers.](#improve-ui-path-logic-for-attacking-siege-towers)
            * [Fix problems with climbing siege towers while being attacked.](#fix-problems-with-climbing-siege-towers-while-being-attacked)
            * [Make AI more consistently aggressive.](#make-ai-more-consistently-aggressive)
            * [Improve pathing for large units passing through gates.](#improve-pathing-for-large-units-passing-through-gates)
            * [Treat Cavalry that is getting further away as an invalid target for Infantry units.](#treat-cavalry-that-is-getting-further-away-as-an-invalid-target-for-infantry-units)
            * [Minor improvements to settlement layouts](#minor-improvements-to-settlement-layouts)
            * [Make defending AI artillery follow units.](#make-defending-ai-artillery-follow-units)
            * [Make AI more dynamic when defending the plaza.](#make-ai-more-dynamic-when-defending-the-plaza)
            * [For cities with no walls, consider the city and the outside as the same area (improves AI behaviour in these situations).](#for-cities-with-no-walls-consider-the-city-and-the-outside-as-the-same-area-improves-ai-behaviour-in-these-situations)
            * [Make units rotate to the correct direction when defending junctions.](#make-units-rotate-to-the-correct-direction-when-defending-junctions)
            * [Make soldiers move around rams when they run into them.](#make-soldiers-move-around-rams-when-they-run-into-them)
            * [Improve behaviour of AI reinforcements](#improve-behaviour-of-ai-reinforcements)
      * [Crash Fixes](#crash-fixes)
         * [Fixed a number of the most reported crashes from crash reporter](#fixed-a-number-of-the-most-reported-crashes-from-crash-reporter)
      * [Multiplayer Stability Improvements](#multiplayer-stability-improvements)
   * [New Modding Specific Features in 2.0.4](#new-modding-specific-features-in-204)
      * [New UX Features](#new-ux-features-1)
         * [Better support for displaying negative capabilities in the UI](#better-support-for-displaying-negative-capabilities-in-the-ui)
            * [Enable support for negative values on various bonuses](#enable-support-for-negative-values-on-various-bonuses)
         * [Allow mods to specify custom loading screens per map / location](#allow-mods-to-specify-custom-loading-screens-per-map--location)
         * [Allow hex values to be used in UX .pos files for font colours.](#allow-hex-values-to-be-used-in-ux-pos-files-for-font-colours)
         * [Building Browser, Info Panels &amp; Tooltips - Rework item requirements to display conditional strings.](#building-browser-info-panels--tooltips---rework-item-requirements-to-display-conditional-strings)
         * [Smaller Miscellaneous UX Improvements](#smaller-miscellaneous-ux-improvements-1)
      * [Factions](#factions-1)
         * [Factions have been updated to support virtually unlimited numbers of factions.](#factions-have-been-updated-to-support-virtually-unlimited-numbers-of-factions)
         * [Support for multiple Super Factions](#support-for-multiple-super-factions)
            * [All super factions have their own line of sight](#all-super-factions-have-their-own-line-of-sight)
            * [Senate AI now supports more than 3 child members](#senate-ai-now-supports-more-than-3-child-members)
            * [Allow options for super factions inside descr_strat data file.](#allow-options-for-super-factions-inside-descr_strat-data-file)
            * [Various minor improvements to super faction logic](#various-minor-improvements-to-super-faction-logic)
         * [Improvements to Shadow Factions &amp; Loyalty](#improvements-to-shadow-factions--loyalty)
            * [Shadowed factions won't automatically shadow back](#shadowed-factions-wont-automatically-shadow-back)
            * [Prevent shadow factions from stealing revolts while they're still alive](#prevent-shadow-factions-from-stealing-revolts-while-theyre-still-alive)
            * [Allow shadowed factions to have captain portraits](#allow-shadowed-factions-to-have-captain-portraits)
            * [Player factions can trigger shadow faction switchback](#player-factions-can-trigger-shadow-faction-switchback)
            * [Shadow faction resurrection has improved behaviour](#shadow-faction-resurrection-has-improved-behaviour)
            * [Shadow - Shadow Max Provinces Definition](#shadow---shadow-max-provinces-definition)
         * [Emergent Faction Improvements](#emergent-faction-improvements)
            * [All previously hard coded emergent factions are now moddable](#all-previously-hard-coded-emergent-factions-are-now-moddable)
            * [All factions can now be emergent or re_emergent](#all-factions-can-now-be-emergent-or-re_emergent)
            * [Detailed control of emergent factions via new sub-script](#detailed-control-of-emergent-factions-via-new-sub-script)
            * [Various minor improvements to Emergent Faction logic](#various-minor-improvements-to-emergent-faction-logic)
         * [Line of sight correctly disables when the Roman Civil War starts](#line-of-sight-correctly-disables-when-the-roman-civil-war-starts-1)
         * [Added Rebel portraits for roman rebels as mods might need it in certain circumstances.](#added-rebel-portraits-for-roman-rebels-as-mods-might-need-it-in-certain-circumstances)
         * [Allow ai_do_not_attack_faction to target multiple factions](#allow-ai_do_not_attack_faction-to-target-multiple-factions)
         * [Make pirate and brigand spawn rates at 0 disable spawns](#make-pirate-and-brigand-spawn-rates-at-0-disable-spawns)
         * [Allow rebel subfactions (as in, slave cosplay, not shadow factions) to have their own custom faction logos to match the banners.](#allow-rebel-subfactions-as-in-slave-cosplay-not-shadow-factions-to-have-their-own-custom-faction-logos-to-match-the-banners)
         * [Allow setting faction aggression levels in the descr_strat](#allow-setting-faction-aggression-levels-in-the-descr_strat)
         * [Allow Slave faction to have a functioning family in mods](#allow-slave-faction-to-have-a-functioning-family-in-mods)
         * [Various minor improvements to Faction behaviour](#various-minor-improvements-to-faction-behaviour)
      * [Culture](#culture)
         * [Culture has been updated to support virtually unlimited numbers of cultures.](#culture-has-been-updated-to-support-virtually-unlimited-numbers-of-cultures)
         * [Roman Faction AI Assists can now be controled via data files](#roman-faction-ai-assists-can-now-be-controled-via-data-files)
         * [A number of Settlement mechanics are now moddable](#a-number-of-settlement-mechanics-are-now-moddable)
         * [Enabled the ability specify which cultures are barbarian-like](#enabled-the-ability-specify-which-cultures-are-barbarian-like)
         * [Miscellaneous minor fixes and improvements](#miscellaneous-minor-fixes-and-improvements)
      * [Religion](#religion-1)
         * [Religion has been updated to support virtually unlimited numbers of religions.](#religion-has-been-updated-to-support-virtually-unlimited-numbers-of-religions)
         * [Religions can now specify a group](#religions-can-now-specify-a-group)
         * [Religions can have different unrest multipliers against other religions](#religions-can-have-different-unrest-multipliers-against-other-religions)
         * [Define the amount of unrest relative to the settlement population](#define-the-amount-of-unrest-relative-to-the-settlement-population)
         * [Changes to appropriate UX &amp; data files to allow for extra religions](#changes-to-appropriate-ux--data-files-to-allow-for-extra-religions)
         * [Support new religious conditions for buildings](#support-new-religious-conditions-for-buildings)
         * [Support new religious conversion logs for modders](#support-new-religious-conversion-logs-for-modders)
         * [Allow Traits &amp; Followers to have more than one religious effect](#allow-traits--followers-to-have-more-than-one-religious-effect)
         * [Smaller Miscellaneous improvements](#smaller-miscellaneous-improvements)
      * [Buildings](#buildings)
         * [Buildings have been updated to support virtually unlimited numbers of Buildings.](#buildings-have-been-updated-to-support-virtually-unlimited-numbers-of-buildings)
         * [Allow building_factions condition to be used for upgrade lines](#allow-building_factions-condition-to-be-used-for-upgrade-lines)
         * [Allow grouping buildings in multiple groups of mutual exclusivity](#allow-grouping-buildings-in-multiple-groups-of-mutual-exclusivity)
         * [The building_factions condition now works for recruitment lines](#the-building_factions-condition-now-works-for-recruitment-lines)
         * [Allow the building_factions condition to be used in the upgrades block](#allow-the-building_factions-condition-to-be-used-in-the-upgrades-block)
         * [Add factionwide keyword to building condition resource checks](#add-factionwide-keyword-to-building-condition-resource-checks)
         * [Support for new Religious based conditions](#support-for-new-religious-based-conditions)
         * [Add agent number limits for all agent types, modifiable through building effects](#add-agent-number-limits-for-all-agent-types-modifiable-through-building-effects)
         * [Added "ai_destruction_hint" option to building definitions](#added-ai_destruction_hint-option-to-building-definitions)
         * [Remove limit of 32 effects per building level](#remove-limit-of-32-effects-per-building-level)
         * [Added can_player_effect_this](#added-can_player_effect_this)
         * [Remove the implicitly decided "temple" type, which prevented building other temples while one existed, and replace it with a system of tags and the no_building_tagged condition](#remove-the-implicitly-decided-temple-type-which-prevented-building-other-temples-while-one-existed-and-replace-it-with-a-system-of-tags-and-the-no_building_tagged-condition)
         * [Allow specifying factionwide condition to check across the entire faction](#allow-specifying-factionwide-condition-to-check-across-the-entire-faction)
         * [Make unit availability restrictions in building definitions file implicit](#make-unit-availability-restrictions-in-building-definitions-file-implicit)
         * [Add scripting conditions for checking diplomacy status between two factions](#add-scripting-conditions-for-checking-diplomacy-status-between-two-factions)
         * [Make CAPABILITY_TRADE_FLEET moddable](#make-capability_trade_fleet-moddable)
         * [Allow using the "capability" settlement condition on capabilities and recruitment](#allow-using-the-capability-settlement-condition-on-capabilities-and-recruitment)
         * [Add the ability to specify custom strings in building capabilities](#add-the-ability-to-specify-custom-strings-in-building-capabilities)
         * [Allow specifying building slot guards using tags](#allow-specifying-building-slot-guards-using-tags)
         * [Support 'building_factions' condition for recruitment options](#support-building_factions-condition-for-recruitment-options)
         * [Miscellaneous minor fixes and improvements](#miscellaneous-minor-fixes-and-improvements-1)
      * [Combat_Vs effects are now fully moddable](#combat_vs-effects-are-now-fully-moddable)
      * [New Traits and Follower Features](#new-traits-and-follower-features)
         * [New Religious Abilities](#new-religious-abilities)
         * [Improved Culture support](#improved-culture-support)
         * [Add MaxAllowed variable to traits](#add-maxallowed-variable-to-traits)
         * [Add Inherit_chance to traits to allow them to be inherited by a character's children](#add-inherit_chance-to-traits-to-allow-them-to-be-inherited-by-a-characters-children)
      * [General Gameplay](#general-gameplay-1)
         * [Added mod accessible toggle for garrisons effecting revolt chance](#added-mod-accessible-toggle-for-garrisons-effecting-revolt-chance)
         * [Add scorch effects to campaign toggle](#add-scorch-effects-to-campaign-toggle)
         * [Add extremely_hardy attribute option to units](#add-extremely_hardy-attribute-option-to-units)
         * [Add unit specific move speeds](#add-unit-specific-move-speeds)
         * [LOD rendering distance of mounts respects DMB defaults](#lod-rendering-distance-of-mounts-respects-dmb-defaults)
      * [Sound - Miscellaneous minor fixes and improvements](#sound---miscellaneous-minor-fixes-and-improvements-1)
      * [New Campaign Features](#new-campaign-features-1)
         * [New Settlement Features](#new-settlement-features)
            * [Squalor &amp; Distance From Capital penalties are now moddable](#squalor--distance-from-capital-penalties-are-now-moddable)
            * [Minimum &amp; Upgrade Population levels are now moddable](#minimum--upgrade-population-levels-are-now-moddable)
            * [Make major events completely moddable (i.e. Marion Reforms)](#make-major-events-completely-moddable-ie-marion-reforms)
            * [Religious unrest penalties can now be modded (per religion)](#religious-unrest-penalties-can-now-be-modded-per-religion)
            * [Override the default religion of a settlement](#override-the-default-religion-of-a-settlement)
            * [Support for per settlement custom models on the Campaign Map](#support-for-per-settlement-custom-models-on-the-campaign-map)
            * [Allow settlement name to be used as a character surname](#allow-settlement-name-to-be-used-as-a-character-surname)
            * [Allow use of settlement loyalty/public order as a multiplier to region income](#allow-use-of-settlement-loyaltypublic-order-as-a-multiplier-to-region-income)
         * [Add Ambient Models on Campaign Map](#add-ambient-models-on-campaign-map)
         * [Allow defining of specific brigand and pirate factions per region](#allow-defining-of-specific-brigand-and-pirate-factions-per-region)
         * [Option to have Opaque Fog Of War in mods (hides undiscovered areas completely)](#option-to-have-opaque-fog-of-war-in-mods-hides-undiscovered-areas-completely)
         * [Allow overlapping mercenary pools](#allow-overlapping-mercenary-pools)
         * [Fort plans are now consistent](#fort-plans-are-now-consistent)
         * [Add support for unit-specific AI recruitment bias using recruit_priority_offset](#add-support-for-unit-specific-ai-recruitment-bias-using-recruit_priority_offset)
         * [Removed 32 variation cap on AI Personalities](#removed-32-variation-cap-on-ai-personalities)
         * [New Battle Features](#new-battle-features-1)
            * [Allow aspects of Battle AI to be moddable via data files](#allow-aspects-of-battle-ai-to-be-moddable-via-data-files)
            * [Increase maximum number of officers](#increase-maximum-number-of-officers)
            * [Add the ability to vary unit models including based on armour and weapon levels](#add-the-ability-to-vary-unit-models-including-based-on-armour-and-weapon-levels)
            * [Implement Field Of View slider for the Remastered and Classic camera modes](#implement-field-of-view-slider-for-the-remastered-and-classic-camera-modes)
            * [Allow setting tattoo_colour per faction](#allow-setting-tattoo_colour-per-faction)
            * [Additional Battle Map Sky modding options](#additional-battle-map-sky-modding-options)
            * [Allow Mods to control when torches and night lighting is triggered](#allow-mods-to-control-when-torches-and-night-lighting-is-triggered)
            * [Add a flag for globally disabling friendly fire](#add-a-flag-for-globally-disabling-friendly-fire)
      * [Enhanced Tweaks Mode - Expose Game Engine Settings For Mods](#enhanced-tweaks-mode---expose-game-engine-settings-for-mods)
      * [Save Games Record Enabled Mods](#save-games-record-enabled-mods)
      * [Refactored Name Lists for better modding control](#refactored-name-lists-for-better-modding-control)
      * [Logging Features](#logging-features)
         * [New logging mode launch options](#new-logging-mode-launch-options)
            * [Include per settlement religious conversion information](#include-per-settlement-religious-conversion-information)
            * [Include Model Mismatches](#include-model-mismatches)
            * [Include verbose skeleton &amp; animation pack logs](#include-verbose-skeleton--animation-pack-logs)
         * [Improved error logging for invalid names](#improved-error-logging-for-invalid-names)
         * [Increased information for descr_strat file loading](#increased-information-for-descr_strat-file-loading)
         * [Enable Campaign AI logging](#enable-campaign-ai-logging)
         * [Miscellaneous formating &amp; minor information improvements](#miscellaneous-formating--minor-information-improvements)
      * [Scripting Features](#scripting-features)
         * [Add go_to_char command for Campaign.](#add-go_to_char-command-for-campaign)
         * [Add ```go_to_capital`` command for Campaign.](#add-go_to_capital-command-for-campaign)
         * [Add scripting command to alter a region's religious profile](#add-scripting-command-to-alter-a-regions-religious-profile)
         * [Removed unit limits create_unit command (was 5 in original game)](#removed-unit-limits-create_unit-command-was-5-in-original-game)
         * [Added destroy_unit and swap_unit to scripting and romeshell.](#added-destroy_unit-and-swap_unit-to-scripting-and-romeshell)
         * [Added commands for setting the Faction Leader and Heir.](#added-commands-for-setting-the-faction-leader-and-heir)
         * [Allow a faction to be passed into capture_settlement](#allow-a-faction-to-be-passed-into-capture_settlement)
         * [Add HasOffice command](#add-hasoffice-command)
         * [Add MajorEventActive command](#add-majoreventactive-command)
         * [Add change_character_faction to move a name character to another faction.](#add-change_character_faction-to-move-a-name-character-to-another-faction)
         * [Add a new event start_turn trigger for the start of a round.](#add-a-new-event-start_turn-trigger-for-the-start-of-a-round)
         * [Add a new event FactionDestroyed trigger for when a faction is destroyed](#add-a-new-event-factiondestroyed-trigger-for-when-a-faction-is-destroyed)
         * [Enabled diplomatic_stance](#enabled-diplomatic_stance)
         * [Enabled faction command](#enabled-faction-command)
         * [Added give_everything Command](#added-give_everything-command)
         * [Support Local scope access for a number of script and console commands](#support-local-scope-access-for-a-number-of-script-and-console-commands)
            * [Console commands that support local scope:](#console-commands-that-support-local-scope)
            * [Script commands that support local scope:](#script-commands-that-support-local-scope)
         * [Add commands for adding and extracting counters from local scopes](#add-commands-for-adding-and-extracting-counters-from-local-scopes)
         * [Added support for mods adding their own income/expenditures](#added-support-for-mods-adding-their-own-incomeexpenditures)
         * [Allow setting senate standing directly from script](#allow-setting-senate-standing-directly-from-script)
         * [Allow set_counter to use another counter instead of a constant value and add counter_operation command](#allow-set_counter-to-use-another-counter-instead-of-a-constant-value-and-add-counter_operation-command)
         * [Add scripting conditions for checking diplomacy status between two factions](#add-scripting-conditions-for-checking-diplomacy-status-between-two-factions-1)
         * [Allow I_CompareCounter to compare two counters, instead of just one counter against one constant](#allow-i_comparecounter-to-compare-two-counters-instead-of-just-one-counter-against-one-constant)
         * [Add "break" command to exit scopes](#add-break-command-to-exit-scopes)
         * [Additional Miscellaneous Improvements](#additional-miscellaneous-improvements)
      * [RomeShell Features](#romeshell-features)
         * [Add support for pasting clipboard into RomeShell](#add-support-for-pasting-clipboard-into-romeshell)
         * [Display whether achievements are enabled or not in RomeShell (and if disabled, why)](#display-whether-achievements-are-enabled-or-not-in-romeshell-and-if-disabled-why)
         * [Add the ability to middle mouse scroll RomeShell while its in focus.](#add-the-ability-to-middle-mouse-scroll-romeshell-while-its-in-focus)
         * [Add verify_building_units to check for duplicate units in buildings](#add-verify_building_units-to-check-for-duplicate-units-in-buildings)
         * [Added a number of previous scripting only commands to RomeShell](#added-a-number-of-previous-scripting-only-commands-to-romeshell)
         * [Auto generate documentation for RomeShell commands in preferences folder](#auto-generate-documentation-for-romeshell-commands-in-preferences-folder)
         * [Fixed transitioning between previous commands](#fixed-transitioning-between-previous-commands)
         * [Can use this instead of using settlement or character names](#can-use-this-instead-of-using-settlement-or-character-names)
      * [Fixed issues loading specific assets from mod folders](#fixed-issues-loading-specific-assets-from-mod-folders)
      * [Crash Fixes](#crash-fixes-1)
         * [Cloned Characters CTD from original game is fixed](#cloned-characters-ctd-from-original-game-is-fixed)
      
## New Game Features in 2.0.4

### New UX Features

#### New full size info panels for units and buildings. 

These can be accessed by expanding the smaller info panel on the left side of the screen. When in campaign mode this will hide the smaller panel and instead expand a new larger middle panel. The panel settings will be saved so once a user selects the larger view all future info panels will be large until they toggle the setting back to the smaller mode. This larger panel doesn't exist in 3D battles.


#### Add region names underneath settlement names in the campaign tags

These can be disabled in mods if preferred by modding the  `data/data_controlled_features.json` file.

You can look at the example mod [here](/example_mods/ExampleMods.md) to see it in action.

![No_regions_on_tags](/example_mods/No_regions_on_tags/No_regions_on_tags.jpg)

#### Add population and public order to settlement captured screen 
 
 This addition gives players more useful information prior to making their decision on how to capture the settlement. This feature could be disabled by modding the .pos file for this screen.
 
![SettlementCaptured](/images/SettlementCaptured.jpg)
 
#### Add "Previously Seen" Fog Of War stage to the minimap. 

We were already doing this for the fullscreen version, but not for the minimap.

![FogOfWar](/images/FogOfWar.jpg)

#### Show religion percentage on the settlement icon tooltip

![ReligionInfo](/images/ReligionInfo.jpg)

#### Let players see religion in non-owned settlements if they can also see population loyalty

AN example of this in practise is if the player has a spy in the city

![ReligionInfoViaSpy](/images/ReligionInfoViaSpy.jpg)

#### Add tooltips specifying the rebel sub-type for characters and settlements.
 
 *Characters*
![RebelMerchants](/images/RebelMerchants.jpg)

*Settlements*
![RebelSettlements](/images/RebelSettlements.jpg)
 
#### Improvements to card order when grouping/ungrouping units
 
 * Maintain the card order when grouping/ungrouping. Previously we were adding all the cards to a set, so we lost the ordering. We would then sort them within the group so they somewhat made sense.
 
#### Minor fixes to avoid text clipping on some screens

 * Decrease the max width of the post-battle results screen title text to avoid spillage 
 * Increase the width of the merchant tooltip so we don't get text clipping in some languages.
  * Fix the positioning of the scroll bar in the building info panel.

#### Building Browser, Info Panels & Tooltips - Improved Requirements Information.

We now display all the requirements for buildings and units across the UI making it easier to see the status of buildings that have more complex requirements for example the Blacksmith building for the Julii.

![ImprovedBuildingRequirements](/images/ImprovedBuildingRequirements.jpg)

#### Smaller Miscellaneous UX Improvements
    
 * Add the ability to mouse wheel scroll the unit list menu
 * Remove income gained from a settlement's merchants from the "merchants" display in the settlement income panel.
 * Always display faction name regardless of if a faction is rebels to keep tooltips consistent.  
 * Remove the `Rebels (<rebel type>)` format from slaves, since in the base game slaves are named in the manner, "Galician rebels" so it is redundant to include that info. We also make sure we properly set surname based origin so we can detect when agents come from rebels 
 * Fix missing dividing line on agent tooltips under certain circumstances
 * Only display the "Move Followers" button when in the "Traits and Followers" tab
 * Update the left UI panel when characters gain/lose trait points
 * Fix gladiator revolts not using the trident banner

### Factions
 
#### Line of sight correctly disables when the Roman Civil War starts
 
 
### Religion 

#### Fixed issue with rebel settlements always being angry due to religion

 * Fix rebel settlements always being angry all the time because rebel settlements would always use the world dominant religion if no temple building was present so you'd get 90% christian settlements being officially pagan
 
### General Gameplay

#### Fix the trigger for Achievement 'My Trade Goods Bring all the Boys to the Yard'

This achievement can now be triggered.

![TradeGoodsToTheYard](/images/TradeGoodsToTheYard.jpg)

#### Fix rebel merchants generating income for the settlement they are sitting in

#### Allow Assassins to queue up a move for next turn even if they have already conducted an action this turn. 

The original game could already handle this if the action required multiple turns to reach the target, but couldn't if they could reach it on the same turn.

#### Armies can no longer construct sap points if they physically cannot use them with their current units

#### Improve and simplify ram & chariot outlines and hitboxes
 
### Sound - Miscellaneous minor fixes and improvements
 
#### Duck audio if the battle is paused

#### Fix units saying 'orders completed' when they were given invalid orders 
 
### New Campaign Features


#### Support Multiple Family Trees & Other Improvements

Add a way of cycling between the various family trees within a faction. Modders are able to add multiple families in descr_strat.txt, but previously the game would only display the family tree of the current faction leader. Now, if multiple families are present, buttons will be made visible in the full screen family tree window allowing the user to cycle between them.

![FamilyTree](/images/FamilyTree.jpg)

* When opening the large family tree, we will now centre the tree on the selected character.
* When exiting the large family tree, we will now scroll the family list so that the selected character is visible. 

This also exists for the Family tree lists in the same Factions Overview tabs.

#### Prevent the AI from requesting a trade agreement with a faction they have an embargo with.

#### Prevent being able to simultaneously declare a trade embargo and offer trade rights in the same diplomatic proposition

#### Improve the chance of AI attacking forts especially when they are occupied in their own territory.

Bump the priority of AI attacking forts so it's equal to the priority of engaging armies and as high as possible when the fort is in our own territory
 
 ### New Battle Features

#### Battle AI Enhancements

Improvements to the Battle AI.
 
##### Improve placement of units in enclosed areas
 
Allow both drawing and placement of units in enclosed areas (such as roads) even if the unit size is too large. The placement of individual soldier has also been changed. If a soldiers ideal formation position is blocked, they will now first attempt to stand next to another formation position. 

If all these alternate positions are either already in use or blocked, then we fall back to the original logic of just placing them as close to their ideal position as possible.
 
##### Block invalid formations
 
 * Dont allow users to input formations that are invalid. This still allows users to right-click units into somewhat-invalid positions, but no longer allows right-click drag formation positioning in such areas.
 
##### Improve a number of aspects of wall pathing logic over original.

 * Units will form up in the correct orientation when climbing off walls
 * Unit sub-groups will follow the main group when pathing off of walls whenever possible.
 * Unit sub-groups can now navigate wall->ground->wall correctly without getting stuck.
 * Fix issue where units would take weirdly long paths when climbing on to a wall.
 * Reduce colliders for some types of wall movement.
 * Add further improvements to pathing and make transition up walls smoother.
 * When placing units on walls, if we run out of space, attempt to traverse left to find more space.
 * Check both directions when looping through wall slots as formations can now go to the left.
 * Fix problem where the a certain action would make units march to the start of a line instead of to the nearest point.
 * Make units form up into a square before climbing towers.
 * Fix problem where units would only use 1 ladder when climbing down walls.
 * When a building changes damage level, run additional logic. This prevents paths from constantly being invalidated when buildings are being damaged.
 * Fix issue with entrance formations.
 * Fix issue where the unit had different actions assigned to different soldiers, which lead to the formation being split.
    
##### Pathing improvement when choosing first point on a path.

##### Tighten conditions for stopping a charge so units can close gaps better.
 
Old conditions for stopping a charge: 
 * 10% of soldiers have finished charging  

New conditions: 
 * 33% of soldiers have finished charging 
 * 33% of soldiers are within 25m of the enemy unit's centre.
 
##### Fix and optimise grouping algorithm for wall units.

   * Reformat ```AI_TACTIC_DEFEND_WALLS``` so that the threats are saved between updates.
   * Threats are saved between updates. This helps with making the AI more decisive, and also means that units that were assigned to deal with a threat will be kept on the same threat for the next update if it hasn't changed sufficiently.
   * Re-work wall deployment algorithm to order unit to more optimal places.
   
   
##### Add implementation of "Hungarian Algorithm" that solves the assignment problem.

The problem instance has a number of agents and a number of tasks. Any agent can be assigned to perform any task, incurring some cost that may vary depending on the agent-task assignment. It is required to perform as many tasks as possible by assigning at most one agent to each task and at most one task to each agent, in such a way that the total cost of the assignment is minimized.

##### Improve defensive AI for walls

   * AI is better at recognizing units that are climbing up the walls and docked siege engines as threats.
   * AI doesn't consider slows unavailable for placement if an enemy also wants to go there.
   * Improve logic surrounding merging new wall threats.
   * Reduce potential for units to get stuck on walls - Include units on walls as "inside the settlement" and order them directly to the plaza when retreating.
    
##### Improve UI path logic for attacking siege towers.

##### Fix problems with climbing siege towers while being attacked.

   * When reforming from wall->wall, go straight to the destination without waiting for all the other units within the reform group
   * Reduce colliders from units in the same alliance on walls to avoid units getting stuck.
   
##### Make AI more consistently aggressive.

   * Units assigned to the flank sub-objective will attempt to continue until the end whenever possible.
   * When they are finished they will be assigned the attack objective on the next update.
   * Units attacking will be more likely to keep the same target instead of switching.
   
##### Improve pathing for large units passing through gates.

##### Treat Cavalry that is getting further away as an invalid target for Infantry units. 

This should prevent infantry chasing cavalry for way too long when it has other options and doesn't have a chance to catch up.

##### Minor improvements to settlement layouts

* Create modified path finding cas for barbarian towns.
* Create modified street plan for huge egyptian cities.

##### Make defending AI artillery follow units.

##### Make AI more dynamic when defending the plaza.

##### For cities with no walls, consider the city and the outside as the same area (improves AI behaviour in these situations).

##### Make units rotate to the correct direction when defending junctions.

##### Make soldiers move around rams when they run into them.

##### Improve behaviour of AI reinforcements

AI reinforcements (human and AI sides) should now be more consistent. Previously in some cases the AI could enter with strange formations or be slow to enter the battlefield when playing in campaign.

### Crash Fixes

#### Fixed a number of the most reported crashes from crash reporter

 * Fix crash seen when the game tries to remove the last trait in a character's trait list.
* Crash fix - Make sure the contents of the active mods file is valid before continuing. If its not valid, we will just delete the file as it will be regenerated. 
* Fix Rare crash - Ensure there's a settlement before getting the number of visiting agents.
* Fixed Crash - Make sure the army pointer is valid before getting the general from it.
* Fix rare crash when loading settlement order pips while MAX_BELIEF_COUNT was 0

### Multiplayer Stability Improvements 

 * Force "base_map.rwm" to update when opening the multiplayer menu if its outdated
 * Display the compatibility status on the end of the incompatible multiplayer lobby report string.

## New Modding Specific Features in 2.0.4

### New UX Features

#### Better support for displaying negative capabilities in the UI 

The game now selects if + or - is needed using the value provided. This prevents us from displaying strings such as "...bonus: +-5" when we expected the bonus to be positive, but a mod has made it negative.  

The value itself is expected to always be positive, so for detrimental/reduction capabilities we were always adding "-" before them in the string, resulting in modded strings being displayed like "... reduction: --5%". 

To solve this, we now use the absolute value for the UI, and handle whether there should be a "+" or "-" before it ourselves.  Also, instead of always using the positive green arrow, we now decide whether that or the red arrow should be used based on the capabilities value.

![NegativeBonusValues](/images/NegativeBonusValues.jpg)

##### Enable support for negative values on various bonuses

 * Allow a unit's morale bonus to be negative
 * Display current unit morale (including morale bonuses) instead of the base unit morale.
 * Allow population growth bonus, population health bonus, law bonus and happiness bonus to support negative values
 * Allow building cost modifiers to be negative
 * Allow trade level bonus to have a negative value. It won't go any lower than 0 which will make the trade in the settlement drop to zero.
 * Display a different string when trade level bonus is negative and give a couple of other trade effects signs
 * Allow Tax Level bonus to be negative
   * Please note, the tax level multiplier for tax levels doesn't apply to buildings bonuses so if you have a huge negative tax income bonus it will still be overall negative value but increasing the taxation rate won't make it more negative.
 
 ![NegativeTaxBonus](/images/NegativeTaxBonus.jpg)

#### Allow mods to specify custom loading screens per map / location
 
We now optionally allow modders to specify the loading screen to be displayed for a given custom map. The loading screen is either defined in the battles "descr_battle.txt", or for maps that dont have that, its defined in "custom_locations.txt".  

e.g.  

```
battle Macedonian_Ruins 
playable 
end 
nonplayable 
end   
start_date 500 summer 
end_date 500 summer 
loading_screen data/loading_screen/MRuins_loading_screen.dds  

------------------------- OR -------------------------  

custom_location British Grassland 
{ 
location 123 96 
image data/menu/grass1.tga 
sett_locked no 
summer no 
sandstorm no 
loading_screen 
data/loading_screen/battle3_loading_screen.dds 
}
```
 
#### Allow hex values to be used in UX .pos files for font colours.  

We now allow hex values to be used in place of our pre-defined colours in .pos files for font colours. Should still be entered as a string, and start with a ```#```  

E.G. ```"font_colour": "#0a85ab",```

#### Building Browser, Info Panels & Tooltips - Rework item requirements to display conditional strings.

This feature allows you to display information about items that have multiple complex conditions surrounding them and have this information appear clearly in the UI.

 * Split the single "localised_string" method into several more granular methods to make the system a lot more clear
 * the existing "evaluate" method can be used to detect if a condition is currently true or not
 * the "get_requirements_string" method will get the localised requirement string for the condition
 * the "get_requirements_list" method will return a list of pairs of strings and the status of each condition the string corresponds to, so we can do nice text colouring to make it easier for the player to realise what they have to do
 * Add condition aliases, which are just sets of regular conditions which are defined as part of and can mask them
 
![EDB_Units_Multiple_Requirements](/example_mods/EDB_Units_Multiple_Requirements/EDB_Units_Multiple_Requirements.jpg)

You can look at the example mod [here](/example_mods/ExampleMods.md) to see it in action.

#### Smaller Miscellaneous UX Improvements
    
 * Added the ability to define the max line count for multiline strings in pos files
 * Added more areas of the game fonts (tooltips etc) to be modded with custom colours

--------------------------
### Factions

#### Factions have been updated to support virtually unlimited numbers of factions. 

In doing so certain features linked to factions have been extended or improved.

![BI_extra_factions](/example_mods/BI_extra_factions/BI_extra_factions.jpg)

#### Support for multiple Super Factions

##### All super factions have their own line of sight

* All line-of-sight updates to a super faction member are propagated via the superfaction leader. This means all super factions have their own shared line of sight.

##### Senate AI now supports more than 3 child members

 * Rewrite parts of the senate AI to make them be able to handle more than 3 children that are in places other than the first 3 faction slots
 
![super_faction](/example_mods/super_faction/super_faction.jpg)

##### Allow options for super factions inside ```descr_strat``` data file.

You can look at the example mod [here](/example_mods/ExampleMods.md) to see it in action.

##### Various minor improvements to super faction logic 

* When superfaction members get kicked out of the superfaction they get outlawed to avoid additional complexity.
* Make the entire system for checking against outlaws simpler by just kicking outlaws from the superfaction. 
* Remove all references to a single monolithic superfaction and instead use references to our local superfaction.

#### Improvements to Shadow Factions & Loyalty

##### Shadowed factions won't automatically shadow back
 * Make shadowing logistically simpler - shadowed factions won't automatically shadow their shadow back, that's explicit now
 
 		;;shadow faction (NOTE: shadow factions now have to be explicitly circular,
		;; if your shadow faction is not shadowing you the revolt order will be you->shadow->rebels instead of you->shadow->you)
		"shadow faction": "empire_east_rebels",
 
##### Prevent shadow factions from stealing revolts while they're still alive

 * Replace ```can_spawn_a_faction``` with a toggle which prevents shadow factions from stealing revolts while they're still alive

##### Allow shadowed factions to have captain portraits

 * Remove block preventing shadowed factions from having captain portraits, since they absolutely could need them under certain circumstances
 
##### Player factions can trigger shadow faction switchback

 * Improved shadow switchback so it can also effect players, this means if you're playing as western roman rebels, and then defeat the western empire, you then _become_ the western empire instead of remaining as rebels
 
##### Shadow faction resurrection has improved behaviour

 * When generating a faction leader, give them the religion of their current settlement
 * When taking a revolt, give them 1.5 turns worth of the settlement's income up front
 
This gives them a little bit of breathing room when they take a settlement, since they usually start with 0 denarii and more units than they can handle - so they immediately go into debt, and then every time they take a settlement they go even further into debt - this has the effect of essentially making them act like regular rebels, as they can't afford to build new units or fix their unrest problems - the above is even more devastating because their revolt garrisons are weaker than regular rebels would get - with this change they should hopefully be able to put up more of a fight and occasionally actually win

##### Shadow - Shadow Max Provinces Definition

You can now define the maximum number of provinces a shadow faction can have before it stops taking revolts.

		;;the maximum amount of provinces the shadow faction can have before it stops taking revolts
		"shadow max provinces": -1,

#### Emergent Faction Improvements

##### All previously hard coded emergent factions are now moddable

 * Allow spawning conditions for factions like the Romano British to be encoded into user-editable scripts rather than hardcoded
  * Change ostrogoths to work as an emergent faction that triggers on revolts instead of being a shadow faction
  * Allow users to define the unit lists used by emergent factions when they spawn - (`descr_sm_factions.txt`)

##### All factions can now be emergent or re_emergent

##### Detailed control of emergent factions via new sub-script

 * Implementation is very simple: at the end of the descr_strat (but before the main script), declare the name of the script like so:
   
   ```spawn_script romano_british, capture, romano_british_spawn_script_capture.txt```
   
   * ```spawn_script``` just indicates that we're declaring a new spawning condition
   * ```romano_british``` indicates the faction this applies to
   *  ```capture``` means that this script should only be checked when a settlement is captured
   * current possible triggers are ```end_of_turn```, ```capture```, and ```revolt```
   * ```romano_british_spawn_script_capture.txt``` is just the name of the script

 * The only return values are true/false, the faction either spawns or it doesn't
 * Spawning on a revolt will cause the faction to take over the revolting settlement, the other two will do a romano british horde thing
 * Also if you want a faction to have loyalty revolts even after they are defeated you can add ```re_emergent``` in the ```descr_strat``` before the ```superfaction``` and ```denarii``` but after the ```ai_do_not_attack``` or ```dead_until_resurrected```
 * We use a new ```return``` command to communicate with the script, if no return value is set, we assume the check failed
 
##### Various minor improvements to Emergent Faction logic

 * Spawned on event declaration in faction_db removed, we now display the emergent faction tooltip on the faction select if the faction is declared dead_until_resurrected in the descr_strat
 * Allow any faction to load in spawning scripts given the file has a correctly formatted name
 * Don't force all settlements to revolt if the player is playing an emergent faction that shadows the settlement owner


#### Line of sight correctly disables when the Roman Civil War starts

#### Added Rebel portraits for roman rebels as mods might need it in certain circumstances.

 * Add rebel portraits for the roman rebels because under certain circumstances mods may need to have a roman rebel rebel banner.
 
####  Allow ```ai_do_not_attack_faction``` to target multiple factions

 * Allow ```ai_do_not_attack_faction``` to target multiple factions, for example:
   * ```ai_do_not_attack romans_julii, romans_brutii, romans_senate, romans_scipii```

#### Make pirate and brigand spawn rates at 0 disable spawns

This allows mods to disable rebels spawning, the original game allowed you to lower this but you could never stop it completely. 

#### Allow rebel subfactions (as in, slave cosplay, not shadow factions) to have their own custom faction logos to match the banners.

#### Allow setting faction aggression levels in the `descr_strat`

 * Works exactly the same as `faction_relationships` and `core_attitudes`, and is defined after them
 * Ranges from 0 to 1000

#### Allow Slave faction to have a functioning family in mods

Allow Slave faction to have a functioning family tree, they can be assigned family members in the beginning, and they can produce offspring. This needs to be enabled in the mod specifically.

#### Various minor improvements to Faction behaviour 

 * Combine rebel and normal banner icons into the same array, as that makes attaching them to the faction definitions easier.
 * Add new ```descr_sm_faction_icons``` file to allow us to add faction icons into the sprite sheet after it's been initialised which makes dealing with the UI easier
 * Remove the greener gaul hardcode and just change the value in the descr_sm_factions.txt file
 * Add rebel type to admirals
 * Allow adding traits to character records in `descr_strat` - just add a line for traits after the record like you do for characters
 
### Culture

#### Culture has been updated to support virtually unlimited numbers of cultures. 

In doing so certain features linked to culture have been extended or improved.

#### Roman Faction AI Assists can now be controled via data files

 * Users can also control the special AI assist* which was given to the other roman factions in the base game to keep them competitive with the player

#### A number of Settlement mechanics are now moddable
 
 * Users can now control settlement population mechanics, including the amount of *squalor* generated and the *distance from capital unrest multiplier**
 * This also includes being able to *modify settlement upgrade levels and minimum population*

#### Enabled the ability specify which cultures are barbarian-like

 * Users can also specify which cultures are barbarian-like, without having to have a single culture named "barbarian"

#### Miscellaneous minor fixes and improvements

 * Rewrite culture descriptions to allow users better control over certain parts of the game
 * Multiple parts of the above were modified to make them not apply specifically between shadow factions and the faction they shadowed, as things like disabled aggression would cause issues.
 * Move strategy map model definitions into the settlement plan, which allows for per-settlement model definitions
 * Fix "faction" command line option not working to help with testing
 * Couple of UI/trait related fixes linked to culture triggers. 
 
------------- 
### Religion 

#### Religion has been updated to support virtually unlimited numbers of religions.

#### Religions can now specify a group
 
#### Religions can have different unrest multipliers against other religions

This depends on if they're heretics or heathens.

#### Define the amount of unrest relative to the settlement population

 * Add the ability to define the amount of unrest a religion will create relative to it's population. 

#### Changes to appropriate UX & data files to allow for extra religions

 * Reformated the religion file to make it easier to maintain with larger numbers of religions.
 * Change every instance of the religion pips from the sprite sheet to use external TGAs to allow mods to easily add in as many religions as they want. 
 * Allow religions with no influence to be hidden from the overview panel.
 * Modify religion overview UI to allow scrolling when more than 3 religions are defined and leave empty spaces when less then 3 are present in a settlement. 
 * Allow religions to automatically create a trait for themselves if one doesn't exist.
* We always show the _dominant_ commitment, not the official one in the settlement religion panel. Instead, official religion will be shown in a tooltip (assuming it's different from the dominant religion) with a reason for why it's like that (i.e. set by temple or by the governor).

#### Support new religious conditions for buildings

 * Add 4 conditions to the building db: 
   * ```religion <religion> <comparison> <number>``` (i.e. "religion christian < 60") to test the influence of a religion
   * ```majority_religion <religion>``` to check if a given religion is the majority religion of this settlement
   * ```official_religion <religion>``` to check if a given religion is the official religion of this settlement
   * Allow adding ```religious_order``` religious unrest suppression to buildings, which was previously limited to only character traits.
 
#### Support new religious conversion logs for modders
 
 * Add log_conversion_calc command line option to log end-of-turn settlement religious conversion to the command line.
 
#### Allow Traits & Followers to have more than one religious effect

 * Allow traits and ancillaries to have more than one religious conversion and order effect 
 
#### Smaller Miscellaneous improvements 

 * Fix the problem with some characters in BI getting stuck with zero commitment
 * Allow adding a ```religion``` section to settlement definitions in descr_strat.txt to override the religious profile defined in descr_regions.txt if needed.
 * If a faction has no default religion and the `descr_strat` fails to give them one, just give them the first defined religion and place a warning in the debug logs.

### Buildings

#### Buildings have been updated to support virtually unlimited numbers of Buildings.

Buildings have been updated to support virtually unlimited numbers of buildings and items.

#### Allow `building_factions` condition to be used for upgrade lines 

Read the [EDB](/documentation/data_file_guides/EDB.md) page for more information.

#### Allow grouping buildings in multiple groups of mutual exclusivity

Read the [EDB](/documentation/data_file_guides/EDB.md) page for more information.

#### The `building_factions` condition now works for recruitment lines

Read the [EDB](/documentation/data_file_guides/EDB.md) page for more information.

#### Allow the building_factions condition to be used in the upgrades block

Read the [EDB](/documentation/data_file_guides/EDB.md) page for more information.

#### Add factionwide keyword to building condition resource checks

* `building_present <building name> [queued] [factionwide]` - checks if a building exists at any level. **2.0.4 Feature**: The game now supports:
	 * `queued` - will also check the building queue not just constructed buildings
	 * `factionwide` - will check for the existence of a building across all settlments controlled by the faction allowing for buildings that can only be built once per faction.
* `building_present_min_level <building name> <level> [queued] [factionwide]` - checks if the building exists at at least the specified level.
	 * `factionwide` - will check for the existence of a building across all settlments controlled by the faction allowing for buildings that can only be built once per faction.
* `resource <resource name> [factionwide]` **2.0.4 Feature**: checks if the settlement has that resource can also use `factionwide` as a check to check if the resource is found withing the empire.
* `no_building_tagged <tag name> [queued] [factionwide]` **2.0.4 Feature**: As explained in more detail in the prior section (TODO link) this checks that no building with this tag exists (lower levels of this building within the same settlement are not counted). This is used in the base game to restrict temples to only one type. 
	 * `factionwide` - will check for the existence of a building across all settlments 

Read the [EDB](/documentation/data_file_guides/EDB.md) page for more information.

#### Support for new Religious based conditions

We have added 4 conditions to the building db: 
   * ```religion <religion> <comparison> <number>``` (i.e. "religion christian < 60") to test the influence of a religion
   * ```majority_religion <religion>``` to check if a given religion is the majority religion of this settlement
   * ```official_religion <religion>``` to check if a given religion is the official religion of this settlement
   * Allow adding ```religious_order``` religious unrest suppression to buildings, which was previously limited to only character traits.
 
#### Add agent number limits for all agent types, modifiable through building effects

This system piggybacks on the existing system put in place to limit merchant numbers. You just need to add:

```agent_limit_settlement <agent type> <additional units>``` to a buildings ```capability``` section.

If a building allows for the construction of a agent without having the above line, then it is assumed that an unlimited amount is allowed.

e.g.

```agent_limit_settlement diplomat 2```

Allows an additional two diplomats to be constructed.

Also changed the stringID used when the limit is reached from "ToolTips_MerchantLimit" to "ToolTips_AgentLimit" to be more accurate. (The string is the same as we only limit merchants, modders will have to alter the string to suit the needs of the mod and what types of units they are limiting). 

#### Added "ai_destruction_hint" option to building definitions

This will help to define logic for when the AI should destroy a building, like temples where it isn't exactly giving negative stats, but also they can't upgrade it so it's best to delete and start over. The original game the AI won't consider this as an option when in some cases it might be advantageous to do so.

#### Remove limit of 32 effects per building level

#### Added `can_player_effect_this` 

Use to check if the player can EVER make this condition true (means things like port buildings won't show in inland settlements since the player can't add an inland sea to the province)

#### Remove the implicitly decided "temple" type, which prevented building other temples while one existed, and replace it with a system of tags and the `no_building_tagged` condition

 * `no_building_tagged` condition by default will list the buildings that are blocking it, so if it's being "not"-ed, it needs to be aliased with a string to display properly
 * You can optionally specify `queued` after `no_building_tagged`, `building_present` and `building_present_min_level` conditions to include queued items in the check

#### Allow specifying `factionwide` condition to check across the entire faction

Allow specifying `factionwide` after the above conditions to check across the entire faction

Also made `factionwide` capabilities display properly in the UI - They should display as (faction) bonus - You add these by specifying "faction_capability" after the normal capability in a building.

Read the [EDB](/documentation/data_file_guides/EDB.md) page for more information.

#### Make unit availability restrictions in building definitions file implicit

To make the building description file a lot simpler we made unit availability restrictions implicit, if a unit is specified as recruitable it will automatically restrict itself to the factions it is available for.

#### Add scripting conditions for checking diplomacy status between two factions

Scripting has the following 4 commands 

 * `IsAlly`
 * `IsProtectorate`
 * `IsProtector`
 * `IsSameSuperfaction`
 * `at_war`
 
 And should be followed by a faction name which we need to test against.
 
Building conditions have a single check which should be laid out as:

`diplomacy <allied/protector/protectorate/same_superfaction> <faction_name> ` 

This does basically the same thing as the scripting commands, but in one condition

#### Make CAPABILITY_TRADE_FLEET moddable

Tie overseas income to CAPABILITY_TRADE_FLEET, instead of hardcoding to the port level - this is already set correctly on port buildings in HD, so this doesn't effect anything other than making it moddable

#### Allow using the "capability" settlement condition on capabilities and recruitment

This would allow you to use items like the level of law in a settlement as a condition of recruitment on a building. You could for example have a unit only recruitable if certain settlement conditions are met.

#### Add the ability to specify custom strings in building capabilities

* Add the ability to specify strings in building capabilities to display capabilities that are indirectly attached to the building (i.e. the education buildings giving extra traits)
* Make the extra trait effect on academy buildings use the new `dummy` string system as an example.

Read the [EDB](/documentation/data_file_guides/EDB.md) page for more information.

#### Allow specifying building slot guards using tags

* Allow specifying building slot guards using tags instead of (/alongside) buildings - also remove the cap on only allowing 6 buildings per plan slot variant


#### Support 'building_factions' condition for recruitment options

The `building_factions` condition condition can now be used on recruitment lines inside the EDB. This means you can make units recruitable based on the faction that built the building NOT the faction that controls it. This means you can make certain units only available to a faction via conquest not construction.

You can look at the GaulTownWatch example mod [here](/example_mods/ExampleMods.md) to see it in action.

#### Miscellaneous minor fixes and improvements

 * Make romano-british unit toggle restrictions explicit in data, so it's not hardcoded to specific units

-------------
### Combat_Vs effects are now fully moddable

Modified combat vs attributes to make them more flexible and remove certain limitations that would limit the potential of other additions like culture and factions. 

* Accommodate using dummy values after NUMBER_OF_ATTRIBUTE_TYPES to keep the UI trait colouring consistent with non-attribute attributes
* Use the above system to replace the old religious index system so you can have more than one religious conversion and religious order per trait
 * Remove old Combat_V attributes from the attribute list and make it it's own thing
 * Make ```Combat_V_``` attribute more generalised and allow 3 different types
   * Factions (i.e. ```Combat_V_Thrace```) which helps maintain the old ```Combat_V_Slaves```
   * Cultures (i.e. ```Combat_V_Roman```) which are internally remapped to faction types
   * Religions (i.e. ```Combat_V_Pagan```) 
   * Note: 
     * In the above the capitalisation after the V is optional, it's case-insensitive.
     * In the case of two things having the same name the list is ordered by the checking order.
 * Tweak how we calculate the Combat_V bonuses, so the effect is a sum of the total effects but bounded but the highest/lowest single effect
   * e.g. If you are terrified of Gauls and are going against 4 gaul armies and 1 German army, you don't have a +0 because you aren't afraid of germans)
 * Increment character record version to deal with the removal of the Combat_V_ attributes from the middle of the list 
 * `Combat_V_Culture` effect now supports negative points
 
-------------
### New Traits and Follower Features

#### New Religious Abilities

 * Allow traits and ancillaries to have more than one religious conversion and order effect 
 * Fix the problem with some characters in BI getting stuck with zero commitment

#### Improved Culture support
 
  * Couple of UI/trait related fixes linked to culture triggers.
  
#### Add `MaxAllowed` variable to traits

Specifies the amount of living characters that can have the trait at any one time - 

Added after `AntiTraits` as `MaxAllowed 6`

#### Add `Inherit_chance` to traits to allow them to be inherited by a character's children 

Has a range between 0-1

### General Gameplay

#### Added mod accessible toggle for garrisons effecting revolt chance

#### Add scorch effects to campaign toggle

#### Add `extremely_hardy` attribute option to units

#### Add unit specific move speeds

You can now specify move_speed_mod after attributes in the EDU

#### LOD rendering distance of mounts respects DMB defaults

### Sound - Miscellaneous minor fixes and improvements

 * Make looping sounds not effect the fading status of the sound, so fades will persist between loops
 * Make units try and pull a more specific generic selection line when they don't have one specific to them
 * Add new sound enums for more narrow generic voice barks for non specifically named units and fix a few issues with BI sound data
 * Add a bit more logging to custom music from scripts
 * Also allow disabling fades when changing state

### New Campaign Features

#### New Settlement Features

##### Squalor & Distance From Capital penalties are now moddable
  
 * Users can now control settlement population mechanics, including the amount of *squalor* generated and the *distance from capital unrest multiplier**  
 
##### Minimum & Upgrade Population levels are now moddable
 
 * You are now able to modify settlement upgrade levels and minimum population

##### Make major events completely moddable (i.e. Marion Reforms)

 * Major events are now defined in ```descr_sm_major_events```
 * Conditions for triggering/un-triggering events are now defined via scripts instead of being hardcoded.
 * Each event has a priority for new generals to use general units assigned to that event
   * If two events have the same priority, their generals will both be eligible for selection at the same time (providing both are active)
   * Also you can now have multiple general units for a faction, the game will just pick randomly between them
   * Replacement of in-game generals is now handled by explicit unit swaps, which can apply to any unit, not just generals
 * Senate offices are now completely user defined and not tied to any enums. If you want to make a superfaction with 500 different offices go ahead
 * Units used as rewards by the senate are no longer hardcoded, and are instead defined in descr_senate
 * Religions can now defined a specific image to be used in the dominant religion message if it triggers for them (BI religions were using generic messenger icon, they will now use their unique artworks)
 * Add ```HasOffice``` command which allows checking if a character holds a given senate office
 * Generalise all toggle-based building conditions into one (with aliases for the old system)
 * Add ```MajorEventActive``` script command to allow for checking if a given event is active

##### Religious unrest penalties can now be modded (per religion)

 * Add the ability to define the amount of unrest a religion will create relative to it's population
 
##### Override the default religion of a settlement
 
  * Allow adding a ```religion``` section to settlement definitions in descr_strat.txt to override the religious profile defined in descr_regions.txt if needed.
 
##### Support for per settlement custom models on the Campaign Map

* Moved strategy map model definitions into the settlement plan, which allows for per-settlement model definitions

##### Allow settlement name to be used as a character surname

  * Tie using the settlement name as surname to a bool so modders can use it for other character types if they want.
  
##### Allow use of settlement loyalty/public order as a multiplier to region income

Add a scaling multiplier to the majority of income sources depending on the settlements public order. The further above ```happy``` they are, the larger the multiplier.
Also, provide an additional construction/recruitment point if the public order meets a certain threshold (currently 180%).

These effects are disabled by default, and need to be enabled in ```data_controlled_features.json```.

#### Add Ambient Models on Campaign Map

Allow you to add single title 3D ambient models (similar to resources) that are used to beautify the map. They also support custom sounds.

* Add the ability to add ambient strat map models
* Add support for ambient objects in SMO soundbank
* Add resource types and ambient objects to SMO object bank description

#### Allow defining of specific brigand and pirate factions per region

 * After the normal rebel faction, you can include `brigands: <name>` and `pirates: <name>` to define the brigand and pirate factions
 * If no specific brigands or pirates were defined for the region we are spawning in, we will now select a random rebel faction with the appropriate rebel type
 * Also allow land based rebel factions to spawn handler units, which they couldn't before
 * Make pirate and brigand spawn rates at 0 disable spawns
 
#### Option to have Opaque Fog Of War in mods (hides undiscovered areas completely)

Added an alternate campaign FOW mode. In the new mode, the FOW is opaque meaning that players cant see the terrain until they have explored it. This applies to the FOW over the actual terrain, the minimap and the map overlay.

This has to be enabled via a modding file

You can look at the example mod [here](/example_mods/ExampleMods.md) to see it in action.

#### Allow overlapping mercenary pools

TODO: Example mod of how to do this is planned but you can refer to the game data for basic documentation.

#### Customise unit movement multipliers on the campaign map

You can now customise the movement multipliers for all unit and agent types on the campaign map. For more information refer to the following page.


Read the [feral_descr_movement_multipliers](/documentation/data_file_guides/feral_descr_movement_multipliers.md) page for more information.

#### Fort plans are now consistent

 * Keep fort plans consistent, previously they would be randomly generated every time a battle happened
 
#### Add support for unit-specific AI recruitment bias using `recruit_priority_offset`

In the EDU, you can now put `recruit_priority_offset` followed by a value on a new line after `stat_cost`. The value will be the % bias towards recruiting that unit. 

E.G. `recruit_priority_offset 100` means that unit is twice as likely to be recruited.

The calculation is effectively: 

`base_recruitment * ((100 + recruit_priority_offset) / 100)`

This feature accepts negative values so -100 would effectively prevent the unit from being recruited however blocking the AI from recruiting a unit could perhaps be better done using the `is_player` option.

#### Removed 32 variation cap on AI Personalities

Previous versions of the game made AI Personalities moddable with 2.0.4 the cap of 32 personalities has been lifted.

We also log the number of AI personalities in the database  
 
-------------

#### New Battle Features

##### Allow aspects of Battle AI to be moddable via data files

 * These values affect which orders the units are given, but not the pathfinding/way the orders are carried out.
 * These constants can be assigned on a *per-faction* basis in ```descr_sm_factions.txt```
 * You can view the default AI values in the ```descr_battle_ai_personalities.txt``` file

Read the [descr_battle_ai_personalities](/documentation/data_file_guides/descr_battle_ai_personalities.md) page for more information.

##### Increase maximum number of officers

* Allow a maximum of 9 officers instead of the original 3
* Allow optionally redefining officers and extra data in remastered stat block

##### Add the ability to vary unit models including based on armour and weapon levels

 * Each unit can now define multiple multiple soldier models in the EDU, and the soldiers will randomly choose between them
 * You can specify armour level and optionally weapon level, if weapon level isn't specified it'll just set it for all weapon levels
 * A total of 255 unique models can be assigned to a unit across all weapon and armour levels.
 * For formatting, see example mod (in mod area of GitHub)
 * Using models with skeletons with different speeds may have some awkward effects on the unit
 * Similarly there may be unexpected behaviour if ranged units have different animation times for firing weapons
 * Excessive use if this feature can have performance implications especially on lower end hardware. The use of sub-mods with this feature disabled for lower end machines might be appropriate in some circumstances.

You can look at the example mod [here](/example_mods/ExampleMods.md) to see it in action.
 
##### Implement Field Of View slider for the Remastered and Classic camera modes
 
 Also support different defaults for Classic vs Remastered
 
##### Allow setting tattoo_colour per faction  

So you can do:

```tattoo_colour blue ```
 
To set it for all factions (i.e. default) and then add:
 
```tattoo_colour gauls gold ```
 
To override for a specific faction

##### Additional Battle Map Sky modding options
 
The TrueSky sequences can be modified per climate-season-weather-time combination instead of just weather. Said combinations are loaded in from ```data/feral_descr_truesky.txt```.

##### Allow Mods to control when torches and night lighting is triggered

* Add variables to data controlled variables to control the sun angles at which units will use torches - variables are torches_min_sun_angle and torches_max_sun_angle - both are defined in degrees, where 0 is the sun being directly overhead (defined in data_controlled_variables.json)
* Add a flag to disable torch allocation to units via `data_controlled_features.json`

You can look at the example mod [here](/example_mods/ExampleMods.md) to see it in action.

##### Add a flag for globally disabling friendly fire

This feature will disable all friendly fire in battles. 

* Add a flag for globally disabling friendly fire this can be controlled using `data_controlled_features.json`

Read the [data_controlled_features](/documentation/data_file_guides/data_controlled_features.md) page for more information.

------------- 
### Enhanced Tweaks Mode - Expose Game Engine Settings For Mods
 
Add the ability to import/export game engine variables and load them in from mods. Modders can now export their settings (done at the bottom of the EnhancedTweaks ImGui panel) and then copy the exported file into their mod.  

Import/Export works from ```Total War ROME REMASTERED\EnhancedTweaks```. 

Enhanced Tweaks settings are auto-loaded from mods using the folder ```data/enhanced_tweaks```.  When exporting settings, only the settings currently listed in the EnhancedTweaks panel will be exported.

This means campaign setting will have to be exported separately from battle settings for example).

Mods can contain multiple json files to be loaded in. This allows mods to have different files for things such as Campaign, Main Menu, Battle etc. This also allows differing mods to provide settings for different elements of the game.

This can be enabled using the command ```enhanced_tweaks``` in the Advanced Options text box.

* Allow modders to alter imgui variables from RomeShell/scripts. Example call: `imgui_set "[CMT]Ally Colour" colour 255 0 255`

You can look at the example mod [here](/example_mods/ExampleMods.md) to see it in action.

------------- 
### Save Games Record Enabled Mods

We now store the active mods in the save header and compare them against the currently active mods when loading them. We also added some new UI and altered the logic so that we can display a confirm/cancel dialog when mods dont match. This allows users to choose whether they want to continue loading the save even with different mods. 

Opening the custom battle menu will no longer auto-load the previous custom battle if the units it used are no longer valid (such as being from a mod that is no longer active).

 When comparing mods:
  * Mods must be in the same order to be seen as compatible, as conflicting mods can cause differing game logic depending on load order.
  * If the mod is from the Steam Workshop, we compare the PublishID (WorkshopID) (This allows the name to change and still be seen as compatible)
  * If the mod is local, we just compare the names of the mods (Not all that much more we can do sadly)
   * When mods differ, we log the entire saved mod list to message.txt (debug log), as the UI can only display up to 8 mods and trims the end of any long mod names to fit the dialog box. This allows for a fallback for the very rare edge case if some people have a huge number of mods at once.


-------------
### Refactored Name Lists for better modding control

Name lists have been disconnected from factions. These can then be linked up to factions. This should allow more flexibility on name lists and also beter integrate with improvements to other areas of the game like cultures and faction increases.

 * Make namelists a separate thing from factions, but have them temporarily assigned per-faction
 * This is to future-proof against future character changes to give better modding control 
 * Add the ability to inherit one namelist into another to cut down on duplicates (saving ~2000 lines in the namelist file)
 * Improved logging for invalid names by virtue of the new and more logical/flexible layout. 
 * Tie using the settlement name as surname to a bool so modders can use it for other character types if they want.
 * Fix rebel merchants all being roman by correctly setting their original faction.
 * Use global indexes for names rather than namelist-dependent ones because that could cause issues when moving characters between factions.
 * Remove hardcode for women not to use surnames to open up future possibility of letting women have surnames

-------------
### Logging Features

#### New logging mode launch options

We have added some new pre game launch options to enable specific logging modes to aid debugging of mod issues. This allows you to enable specific features when needed but also keep the core logs to a reasonable size.

##### Include per settlement religious conversion information

  * Add `log_conversion_calc` command line option to log end-of-turn settlement religious conversion to the command line.
  
Read the [logging](/documentation/feature_guides/logging/logging.md) page for more information.  
  
##### Include Model Mismatches

 * Hide the entire model mismatch log messages behind the ```report_model_mismatches``` command line option. This avoids the main logs including 300+ lines of mismatches that in most cases aren't useful when modding.

##### Include verbose skeleton & animation pack logs

 * Move verbose skeleton & animation pack logs behind the new `verbose_skeletons` command line option.
  
#### Improved error logging for invalid names
  
  * Improved logging for invalid names by virtue of the new and more logical/flexible layout.
  
#### Increased information for descr_strat file loading 

 * Re-enable some previously developer only logging when loading ```descr_strat.txt``` to better inform modders whats going wrong.

#### Enable Campaign AI logging

* Re-enable Campaign AI logging. This will export the AI campaign processing to file to help with mod campaign balancing. Enabled using `enable_logging` - and the file can be found in `/VFS/Local/Rome/logs/campaign_ai_log.txt`

Example snippet from AI Logs:

```
AI: ltgd: Update enemies of gauls
AI: finance: est income 10600, est maintenance 6623, est outgoings 7489 -- spending max 5000, spending norm 3977; balance AFB_EARN_PLENTY, state AFS_ENOUGH
AI: ltgd: defend (frontline .00008, free 1.38049, product 2.492362) vs fac 'romans_julii': not at war, bad frontline, decent free strength >> ALD_DEFEND_DEEP.
AI: ltgd: defend (frontline .000255, free .877193, product 1.225303) vs fac 'carthage': not at war, bad frontline, bad free strength >> ALD_DEFEND_FORTIFIED.
AI: ltgd: defend (frontline 1.0, free 3.987589, product 1.668765) vs fac 'germans': not at war, neither at war elsewhere >> ALD_DEFEND_NORMAL.
AI: ltgd: defend (frontline .000212, free 1.072179, product 2.507092) vs fac 'britons': not at war, bad frontline, decent free strength >> ALD_DEFEND_DEEP.
AI: ltgd: defend (frontline .119502, free 1.341115, product 1.875332) vs fac 'spain': not at war, bad frontline, decent free strength >> ALD_DEFEND_DEEP.
AI: ltgd: 'gauls' against 'romans_julii', his frontline: 12568, our frontline: 1
AI: ltgd: 'gauls' against 'romans_julii', frontline balance: .00008, production balance: 2.492362
AI: ltgd: forbidden to attack 'carthage'.
AI: ltgd: forbidden to attack 'germans'.
AI: ltgd: forbidden to attack 'britons'.
AI: ltgd: forbidden to attack 'spain'.
AI: ltgd: 'gauls' invade 'slave', since they have a neighbouring region >> ALI_INVADE_OPPORTUNISTIC (850).
AI: ltgd: number of invasion targets: 2
AI: ltgd: army strength 26181, free army strength 17350, navy strength 171.
AI: ltgd: are at war with: Rebels, 
AI: region control: settlement 'Condate Redonum' has changed from 'AI_PROD_TROOP_MISSILE' to 'AI_PROD_TROOP_CAVALRY'.
AI: region control: settlement 'Lemonum' has changed from 'AI_PROD_TROOP_INFANTRY' to 'AI_PROD_TROOP_MISSILE'.
AI: region control: settlement 'Patavium' has changed from 'AI_PROD_TYPE_MILITARY' to 'AI_PROD_TYPE_BALANCED'.
AI: region control: settlement 'Patavium' has changed from 'AI_PROD_TROOP_MISSILE' to 'AI_PROD_TROOP_SIEGE'.
AI: region control: settlement 'Lemonum' has changed from 'AI_PROD_TROOP_MISSILE' to 'AI_PROD_TROOP_SIEGE'.
AI: region control: settlement 'Condate Redonum' has changed from 'AI_PROD_TROOP_CAVALRY' to 'AI_PROD_TROOP_SPEARMEN'.
AI: region control: settlement 'Alesia' has changed from 'AI_PROD_TYPE_MILITARY' to 'AI_PROD_TYPE_BALANCED'.
AI: region control: settlement 'Narbo Martius' has changed from 'AI_PROD_TROOP_CAVALRY' to 'AI_PROD_TROOP_INFANTRY'.
AI: region control: settlement 'Numantia' has changed from 'AI_PROD_TROOP_CAVALRY' to 'AI_PROD_TROOP_MISSILE'.
AI: region control: settlement 'Lemonum' has changed from 'AI_PROD_TROOP_SIEGE' to 'AI_PROD_TROOP_INFANTRY'.
AI: region control: settlement 'Lemonum' has changed from 'AI_PROD_TROOP_INFANTRY' to 'AI_PROD_TROOP_MISSILE'.
AI: Threat from gauls to romans_julii: they're not too much of a threat 1, war planned 0, they aren't too strong (free) 1, we are strong enough (frontline) 1   (Will only threaten if all are 1 and stance is neutral)
```

Read the [logging](/documentation/feature_guides/logging/logging.md) page for more information.  
 
#### Miscellaneous formating & minor information improvements

 * Expose some more debug functionality to modders in a few miscellaneous areas.
 * Increase the size of the exit error dialog buffer. Due to long path names, the previous size would often be too small, causing the logs to be trimmed.
 * Logging - Don't print the output of the various ```list_x``` commands as errors.
 * Make it possible to print text to console when a command succeeds. Previously this would only happened if a command failed.
 * Log number of units in the database
 * Make message builder error a script combo so it outputs where it failed
 * Use sprite sheet name instead of ID when logging sprite sheet loading to make logs a bit easier to read.
 * Make general-enemy relationship look a bit nicer in the logs
 * Log game creating default settlements to aid debugging
 * Fix complaint in log about checking the status of nonexistent toggle "rebel merchants"
 * Fix constant log of "could not find character trait(Immortal)" in non-alexander games
 * Add some extra logging about emergent faction messages
 * Add better logging for creating brigand/pirate armies
 * When failing to get a quote, include the quote we failed to get in the error message
 * Make the ```descr_strat``` verify the next section to catch errors caused by malformed ```descr_strat``` files.
 * Add a more explicit error message when the game fails to create a general unit
 * Use verbose scripting error for strat formatting errors
 * Log the number of AI personalities loaded in the database

-------------
### Scripting Features
   
   A list of scripting related features and improvements.
   
#### Add ```go_to_char``` command for Campaign.

Allows you to script the game to jump to a specific character on the campaign map

#### Add ```go_to_capital`` command for Campaign.

Allows you to script the game to jump to the active factions capital city on the campaign map. Useful for hot seat mods.

#### Add scripting command to alter a region's religious profile

Read the [Scripts](/documentation/feature_guides/scripts/Scripts.md) page for more information.

#### Removed unit limits ```create_unit``` command (was 5 in original game) 

We removed the create_unit limit so this can now be controlled by the script. This does mean you can create a lot of units at once so make sure you keep to sane numbers.

#### Added ```destroy_unit``` and ```swap_unit``` to scripting and romeshell.

```swap_unit``` is essentially the same as ```destroy_unit```, however it takes in a second unit ID when called. When destroying the units at the end, we first make a copy of the relevant unit data (soldiers remaining, experience, weapon/armour level) and then use those stats to create a new unit with the type of the second unit ID.  

Should be useful to modders as while the majority of the behaviour could be emulated with a combination of ```destroy_unit``` and ```create_unit```, this way the number of destroyed/created units is the same, as you are able to transfer the stats of the old units to the new ones.
 
#### Added commands for setting the Faction Leader and Heir. 

These can be use in scripts and in RomeShell

```set_leader <character>``` and ```set_heir <character>```

#### Allow a faction to be passed into `capture_settlement` 
   
   This means players can use it to give settlements to the AI. Previously, `capture_settlement` would just give the settlement to the player (which is still the default behaviour if no faction type is provided).

#### Add ```HasOffice``` command 

Allows scripts to check if a character holds a given senate office

#### Add ```MajorEventActive``` command 

Allows scripts to check if a given event is active. For example Marion Reforms.

#### Add ```change_character_faction``` to move a name character to another faction.

This essentially forces a bribe of a character, and has the same effects.  ```change_character_faction <character> <faction>```

#### Add a new event `start_turn` trigger for the start of a round.

Added a new event trigger so you can trigger events at the start of a round as well as at the end of a round.

#### Add a new event `FactionDestroyed` trigger for when a faction is destroyed

Allows you to trigger script events if a faction is destroyed.

```
Identifier:         FactionDestroyed
Event:              A script prompt has received player input
Exports:            faction
Class:              ET_FACTION_DESTROYED
```

#### Enabled `diplomatic_stance`

Enabled this feature for use in modding scripts.

Read the [Scripts](/documentation/feature_guides/scripts/Scripts.md) page for more information.
   
#### Enabled ```faction``` command

 * Fixed ```faction``` command line option, this command existed in the orignal game but didn't work. This feature should help with debugging faction related issues with mods.

#### Added give_everything Command

* Add `give_everything` command which should work as a more complete version of `surrender_regions`

#### Support Local scope access for a number of script and console commands

What this feature provides is the ability in scripts to sub some of the arguments with "local" and the game will pull the character/settlement/faction from the current script scope (assuming one exists).

Due to the nature of this feature it is possible for this to cause stability issues if used incorrectly so this feature should be used with care and as the modders own their own risk.

Unless specified the command will take "local" as an argument to get the settlement/charater from context. If a specific command needs a special variation(s) they are listed below.


##### Console commands that support local scope:
 * add_money
 * add_population
 * move_character
 * set_leader
 * set_heir
 * give_ancillary
 * give_trait
 * process_cq
 * process_rq
 * character_reset
 * give_trait_points
 * mp
 * set_building_health
 * invulnerable_general (local_character)
 * vulnerable_general (local_character)
 * victory (local_faction)
 * damage_wall
 * kill_faction
 * kill_character
 * kill_army
 * control
 * go_to_sett
 * go_to_capital
 * go_to_char
 * set_move_points
 * create_building
 * capture_settlement
 * halt_ai
 * surrender_regions
 * give_everything
 * toggle_automanage
 * create_merchant
 * create_assassin
 * create_spy
 * create_diplomat
 * add_expenditure (local_settlement/local_faction)
 * add_income (local_settlement/local_faction)
 * create_unit (local_character/local_settlement)
 * destroy_unit (local_character/local_settlement)
 * swap_unit (local_character/local_settlement)
 * add_soldiers (local_character/local_settlement)
 * change_character_faction (local_character + local_faction)

##### Script commands that support local scope:

 * IsAlly
 * IsProtectorate
 * IsProtector
 * IsSameSuperfaction
 * spawn_character_child
 * provoke_rebellion
 * move
 * reposition_character
 * replenish_action_points
 * replenish_units
 * add_religion
 * add_hidden_resource
 * remove_hidden_resource
 * destroy_building
 * I_SettlementOwner
 * I_SettlementOwnerCulture
 * I_SettlementLevel
 
 

#### Add commands for adding and extracting counters from local scopes
 
Commands are store_counter and retrieve_counter respectively.  Format for storing is:
 
```store_counter <counter name> <storage location> <storage label>```  

Acceptable locations are "settlement", "character", "faction" or "unit"  

For retrieving the format is reversed: 

```retrieve_counter <storage label> <storage location> <counter name>```

#### Added support for mods adding their own income/expenditures

We now allow mods to add custom income/expenditures via RomeShell/scripts and prpvide full support to be displayed on the UI. There are two types of custom income/expenditures. 

*Settlement Specific* - As the name suggests, this is income/expenditure that is specific to a given settlement. Could be useful for custom buildings that add gold, or cost gold to maintain. 

*Faction Wide* - This works similarly to the above, however is applied to the faction as a whole. The income/expenditures will be displayed in the factions capital (UI is updated if the capital changes).  

There is also an optional parameter which controls whether the income/expenditure is maintained if the settlement is captured (only applied to settlement specific, as faction wide income will move over to the new capital). If false, the income/expenditure is lost when the settlement is captured. If true, then it is kept by the new owner. False is default.  

Once added, income/expenditure will be present until lost due to a settlement being captured, or is removed via calling the same command again, but with a value of 0 If you call the command again with an existing ID, the previous income/expenditure will be overwritten (allowing you to update the value)  

The command will autogenerate the UI icon path and string from the provided ID.  

Example RomeShell calls:

 * `add_income romans_julii Loan 400` <- Adds a faction income of `400 gold` per turn to Julii using the string ID `Rome.InGame.Loan` and the UI path `data/ui/pips/Loan.tga`.
 * `add_expenditure Arretium BuildingMaintenance 600 true` <- Adds a settlement specific expenditure of `600 gold` to `Arretium` using the string ID `Rome.InGame.BuildingMaintenance` and the UI path `data/ui/pips/BuildingMaintenance.tga`. As `true` has been provided, this expenditure will be maintained even if the settlement is captured.
 * `add_expenditure Arretium BuildingMaintenance 300 true` <- Updated the previously added expenditure from `Arretium` to have a value of `300` instead of the previously set `600`.
 * `add_expenditure Arretium BuildingMaintenance 0` <- Removes the previously added expenditure from Arretium.
 
 #### Allow setting senate standing directly from script
 
IMPORTANT: Before setting the popularity `override_superfaction_popularity <faction name> true` needs to be done to prevent the normal processing from overriding script inputs on end of turn. 

* `set_faction_senate_standing` and `set_faction_people_standing` can then be used to control popularity
* Both take `<faction name> <value>` as arguments
* `Faction name` can be substituted for `local`
* `Value` can be substituted for a `counter name`

#### Allow `set_counter` to use another counter instead of a constant value and add `counter_operation` command  

`counter_operation` works like:

`counter_operation <counter name> = <counter name> + <counter name>`  

It can only use counters, not constants. It can also only do one operation at a time, so  `counter_a = counter_b + counter_c + counter_d` 

Needs to be written out as: 

`counter_a = counter_b + counter_c` 
`counter_a = counter_a + counter_d`

#### Add scripting conditions for checking diplomacy status between two factions

Scripting has the following 5 commands 

 * `IsAlly`
 * `IsProtectorate`
 * `IsProtector`
 * `IsSameSuperfaction` 
 * `at_war`
 
 And should be followed by a faction name which we need to test against.
 
#### Allow `I_CompareCounter` to compare two counters, instead of just one counter against one constant

#### Add "break" command to exit scopes

Allows you to use the break command in a script to exist a scope.

#### Additional Miscellaneous Improvements

   * Fix ```is_player``` settlement condition to check the current owning faction, rather than whatever ```settlement_faction_type``` is
   * Add new scripting conditions for checking if a settlement is revolting from a particular faction (only useful inside spawning scripts), if it is a capital, and if a faction is alive (i.e. not waiting to emerge)
   * Make scripted settlement rebellions ignore the usual restrictions for settlement revolts
   * Generalise all toggle-based building conditions into one (with aliases for the old system)
   * Fix `TestFaction` not accepting pre logic token
   * Add script output when failing to get aerial map base in settlement plan model database
   * Fix `for_each` script loops continuing to execute after the being told to kill the script
   * Change SettlementName condition so that it uses the internal, rather than the on-screen name of a settlement (the on-screen one may be changed or have special characters)
   * Implement religion- and historic event-conditioned recruitment and construction (details covered in relavent sections)
   * Make `EnslavePopulation` and `ExterminatePopulation` include the settlement in their scope
   * Fix units jittering after the `control` command is used
   * Allow modders to alter imgui variables from RomeShell/scripts. Example call: `imgui_set "[CMT]Ally Colour" colour 255 0 255`
   
   
-------------
### RomeShell Features

#### Add support for pasting clipboard into RomeShell

You can now paste a command into RomeShell inside the game. This should make things quicker and help avoid typos and other mistakes when using the shell.

#### Display whether achievements are enabled or not in RomeShell (and if disabled, why)

#### Add the ability to middle mouse scroll RomeShell while its in focus.

#### Add `verify_building_units` to check for duplicate units in buildings

#### Added a number of previous scripting only commands to RomeShell
 * Fix "faction" command line option not working to help with testing
 * DocuDaemon file in preferences folder now lists all accepted commands for easy reference.
 
#### Auto generate documentation for RomeShell commands in preferences folder

Not perfect as the formatting on the help strings isnt fully consistent, but it should help users compared to the previous lack of in game documentation. 

Outputs to user preferences folder in ```Total War ROME REMASTERED\VFS\Local\Rome\documentation\docudemon_romeshell.txt```

#### Fixed transitioning between previous commands

Transitioning between previous commands didn't reset the caret position, so if you were at pos 10, then transitioned to a command with length 6, weird behaviour occurred. Also fix the rendering of RomeShell so that the final line is fully visible when the slider is visible.

#### Can use this instead of using settlement or character names

Instead of needing to enter a settlement name or character name when using a command you can usually replace the name with `this` and just make sure the settlement or character has been selected in the campaign map before running the command.

For example you could select Segesta then run the command: 

`add_population 9000 this`

This will add 9000 population to Segesta, however if you then select Rome and run the command again it will instead add the population to Rome.

-------------
### Fixed issues loading specific assets from mod folders

 * Allow campaign trees to be loaded in from mods
 * Allow burn ground types to be loaded from mods
 * Allow Bridge models to be loaded from mods
 * Fix texture path exists logic for mods
 * Always try and get cas files from a mod, even if it already exists in the base game
 * Don't generate item files unnecessarily & generate them inside the mod folder
 * Save bpi files to the mod folder the cas was loaded from
 * Save vegetation sprites into mod folder - you need to have a `vegetation/sprites/` folder inside the mod for this to generate sprites
 * Fix crash when failing to loading a character model texture certain circumstances.
 * Allowing loading of custom Overview map images from inside custom campaign directories (previously only worked for mods using `imperial_campaign` folder)

### Crash Fixes

#### Cloned Characters CTD from original game is fixed

See http://www.twcenter.net/forums/showthread.php?418396-Myth-Buster-Cloned-Characters for an explanation of the original issue. 

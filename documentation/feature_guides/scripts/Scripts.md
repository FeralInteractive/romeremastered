![Workshop_header_template](/Workshop_header_template.png)
# scripts

# Table Of Contents

* [Introduction](#introduction)
* [Background Script Setup](#background-script-setup)
* [Enable Script Logging](#enable-script-logging)
* [Triggers, conditions, events &amp; commands](#triggers-conditions-events--commands)
   * [New events](#new-events)
   * [New conditions](#new-conditions)
   * [New commands](#new-commands)

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

### New events

The following new events have been added to the dictionary for the Remaster.

* AdvisorAudioStopped
* AdvisorOpened
* AgentHubOpened
* AgentListPopulated
* AgentSelected
* AmbushMode
* AssassinSelected
* BattleMapGesture
* BattleMinimapAction
* BattleNewsTabOpened
* BattlePlayerUnitSelected
* BattleReinforcementsHack
* BattleToggleMenu
* BattleUnitActionStatus
* CampaignDoingBadly
* CampaignHudShown
* CampaignMapGesture
* CharacterInfoScreen
* ConstructionItemClicked
* ConstructionPopulated
* ContextPopupInteraction
* DiplomacyConstructingCounterOffer
* DiplomacyConstructingOffer
* DiplomacyOpponentPresentsCounterOffer
* DiplomacyOpponentPresentsOffer
* DiplomacyScrollPopulated
* DiplomaticStandingShown
* DiplomatSelected
* ElectionResults
* EmbargoIsAvailable
* EnemyCharacterSelected
* EnemySettlementSelected
* EnemySettlementSelected
* EnteredBattle
* EnteredCityView
* EnterTacticalMode
* FactionDetails
* FactionFactions
* FactionFamilyTree
* FactionFinancesShown
* FactionLists
* FactionRankings
* FactionSenate
* FactionSenateFloor
* FactionSenateMissions
* FactionSenateOfficials
* FactionSenatePolicy
* FactionSummary
* FailedToEndTurn
* FamilyTreeShown
* FeralNewsVisible
* FirstStratUpdates
* FleetSelected
* FormationTypesShown
* FriendlyCharacterSelected
* FriendlySettlementSelected
* HideBattleUI
* HighTaxesCauseDisorder
* ItemDeselected
* MapOverlayOpened
* MerchantSelected
* MergeArmiesOpened
* MissionSelected
* MoveRetinueAncillaryDeselected
* MoveRetinueAncillarySelected
* MoveRetinueOpened
* MoveRetinuePopulated
* MoveRetinuePressed
* MovieStopped
* NavalCombatStarted
* NewsTabClosed
* NewsTabOpened
* OwnFactionDetailsOpened
* PostBattleScreen
* PreBattleScreen
* QuickListsOpened
* RebelCharacterSelected
* RecruitmentItemClicked
* RecruitmentPopulated
* RoutesBlockaded
* ScrollDidOpen
* SelectionAssistPossible
* SendAgentPanel
* SettlementButtonPressed
* SettlementCharacter
* SettlementDetailsShown
* SettlementOverview
* SettlementTrade
* SiegeDetailsShown
* SpySelected
* TacticalMapShown
* UnitHasRouted
* UnitInfoOpened
* UnitsGrouped
* WorldScriptTerminate


### New conditions

The following new conditions have been added to the dictionary for the Remaster.

* BattleSelectedPlayerUnitSpecialAbilitySupported
* BattleUnitActionStatus
* `CharacterName`
* ConstructionItemClicked
* DistanceCapital
* FeralSettlementAutoManaged
* FeralUIType
* `HasResource`
* HomeSettlementBuildingExists
* I_AdvisorSpeechPlaying
* I_AmountOfUnitInSettlement
* I_AnnotationDisplayed
* I_BattleEnd
* I_BattleEndPending
* I_BattleFinished
* I_CharacterNameNearTile
* I_CompareCounter
* I_IsPlayerTurn
* I_IsTutorialEnabled
* I_SoundPlaying
* I_TimerElapsed
* I_UnitCardSelected
* LangIs
* LocalPlayerBattlesFought
* LocalPlayerHasAIReinforcements
* LocalPlayerHasManualReinforcements
* LocalPlayerHasReinforcements
* MerchantIsAvailableToBuild
* NightBattlesEnabled
* RecruitmentItemClicked
* RemasteredEducation
* ScrollDidOpen
* SettlementCapabilityLevel
* SettlementOrderLevel
* SettlementHasDamagedBuilding
* TestFaction
* Toggled
* TradingExotic
* UnitHasRouted


### New commands

The following new conditions have been added to the dictionary for the Remaster.

* `add_hidden_resource`
* advance_completed_tasks
* allow_campaign_battles
* block_unit_selection
* box_drag_selection
* clear_restrict_battle_movement
* clear_restrict_strat_movement
* clear_strat_selection_unblocker
* click_drag_move
* close_news_panel
* control_feral_anim
* create_mercenary_pool
* `declare_persistent_counter`
* deselect_current_selection
* `destroy_building`
* disable_agent_hub
* disable_agent_hub_all
* disable_all_ui_cards
* disable_diplomacy_ui
* disable_move_retinue
* disable_move_retinue_all
* disable_pause_shortcut_in_campaign
* disable_popups
* disable_specific_shortcut
* disable_ui_card
* e_select_unit
* enable_agent_hub
* enable_agent_hub_all
* enable_all_ui_cards
* enable_diplomacy_voices
* enable_move_retinue
* enable_move_retinue_all
* enable_ui_card
* enable_unit_voices
* end_benchmark
* finish_battle
* `for_each`
* force_agent_succeed
* force_ai_control
* force_autoresolve_outcome
* force_deselect_trigger
* force_diplomacy
* force_settlement_tab
* forced_gate_success
* `goto`
* hide_ui_element
* `if_not`
* include_script
* move_to_settlement
* open_siege_scroll
* open_stop_tutorial_confirmation_dialog
* play_sound_flourish
* point_at_agent_hub
* point_at_diplomacy_offer
* point_at_move_retinue
* point_at_strat_position_alt
* release_music_control
* `remove_hidden_resource`
* `rename_settlement_in_region`
* restrict_battle_movement
* restrict_strat_movement
* script_log
* select_captial
* set_advice_page
* set_battle
* set_label
* set_marriage_allowed
* set_min_formation_width
* set_strat_camera_speed
* show_annotations
* show_building_info
* show_movie
* show_ui_element
* show_unit_info
* snap_to_settlement
* spawn_character_child
* start_benchmark
* stop_all_point_at_indicators
* stop_point_at_indicator
* strat_selection_unblocker
* toggle_minimap
* trigger_marriage_proposal
* ui_card_selection_lock
* unit_group_automate_attack
* unit_group_automate_defend_position
* unit_order_move_to_orientation
* `while_not`

The following commands have been updated or extended from the original game.

* hide_all_revealed_tiles
* play_sound_event
* reveal_tile
* select_ui_element
* set_music_state
* simulate_mouse_click

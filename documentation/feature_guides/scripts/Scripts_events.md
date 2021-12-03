![Workshop_header_template](/Workshop_header_template.png)
# Scripts - Events

# Table Of Contents

* [Table Of Contents](#table-of-contents)
   * [New 2.0.4 Events](#new-204-events)
   * [Modified 2.0.4 Events](#modified-204-events)
   * [New 2.0.0 -&gt; 2.0.3 Events](#new-200---203-events)
   * [Removed 2.0.4 Events](#removed-204-events)
   * [Full List of Events](#full-list-of-events)

## New 2.0.4 Events

The following are new commands added with the 2.0.4 patch


```
Identifier:    	TakeOffice
Event: 		The character has taken a senate office
Exports:	nc_character_record, character_record, faction, region_id, character_type
Class:          ET_TAKE_OFFICE
Note:		Replaces office specific commands above as office names and types are now modifiable.
```


```
Identifier:         LeaveOffice
Event:              The character has left a senate office
Exports:            nc_character_record, character_record, faction, region_id, character_type
Class:              ET_LEAVE_OFFICE
Note:				Replaces office specific commands above as office names and types are now modifiable.
```

```
Identifier:         NewTurnStart
Event:              A new turn has started (not triggered on game open)
Exports:            nothing
Class:              ET_NEW_TURN_START
```

```
Identifier:         ScriptPromptCallback
Event:              A script prompt has received player input
Exports:            nothing
Class:              ET_SCRIPT_MESSAGE_CALLBACK
```

```
Identifier:         FactionDestroyed
Event:              A script prompt has received player input
Exports:            faction
Class:              ET_FACTION_DESTROYED
```

## Modified 2.0.4 Events

The following events have been modified to accept additional export options.



```
Identifier:         ExterminatePopulation
Event:              A settlement has been captured and some of its population has been decimated
Exports:            nc_character_record, character_record, faction, region_id, character_type, settlement
Class:              ET_EXTERMINATE_POPULATION
Added:				Added settlement to the command
```

```
Identifier:         EnslavePopulation
Event:              A settlement has been captured and some of its population has been enslaved
Exports:            nc_character_record, character_record, faction, target_faction, region_id, character_type, settlement
Class:              ET_ENSLAVE_POPULATION
Added:				Added settlement to the command
```

## New 2.0.0 -> 2.0.3 Events



```
Identifier:         AdvisorAudioStopped
Event:              Called when the advisor audio gets stopped.
Exports:            
Class:              ET_ADVISOR_AUDIO_STOPPED
```

```
Identifier:         AdvisorOpened
Event:              Player has opened the advisor panel.
Exports:            
Class:              ET_FTH_ADVISOR_OPENED
```

```
Identifier:         AgentHubOpened
Event:              The Agent Hub tab in the faction overview is opened.
Exports:            
Class:              ET_FTH_AGENT_HUB_OPENED
```

```
Identifier:         AgentListPopulated
Event:              Called when agent list has been populated
Exports:            
Class:              ET_AGENT_LIST_POPULATED
```

```
Identifier:         AgentSelected
Event:              Called when a agent has been selected
Exports:            resource_description
Class:              ET_AGENT_SELECTED
```

```
Identifier:         AmbushMode
Event:              A unit has entered ambush mode
Exports:            character record, faction, region, character type
Class:              ET_FTH_AMBUSH_MODE
```

```
Identifier:         AssassinSelected
Event:              You have selected an assassin
Exports:            
Class:              ET_ASSASSIN_SELECTED
```

```
Identifier:         BattleMapGesture
Event:              You have performed gesture navigation on the battle map
Exports:            
Class:              ET_BATTLE_MAP_GESTURE
```

```
Identifier:         BattleMinimapAction
Event:              Clicked or hid/shown the battle minimap
Exports:            
Class:              ET_BATTLE_MINIMAP_ACTION
```

```
Identifier:         BattleNewsTabOpened
Event:              The News tab was opened.
Exports:            
Class:              ET_BATTLE_NEWS_TAB_OPENED
```

```
Identifier:         BattlePlayerUnitSelected
Event:              player selected a unit of their army
Exports:            
Class:              ET_BATTLE_PLAYER_UNIT_SELECTED
```

```
Identifier:         BattleReinforcementsHack
Event:              Early Update in battle menu to notify for possible reinforcements
Exports:            
Class:              ET_BATTLE_REINFORCEMENTS_HACK
```

```
Identifier:         BattleToggleMenu
Event:              The battle toggle menu was opened.
Exports:            
Class:              ET_FTH_BATTLE_TOGGLE_MENU
```

```
Identifier:         BattleUnitActionStatus
Event:              Called when a unit changes status
Exports:            resource_description, resource_status
Class:              ET_BATTLE_UNIT_ACTION_STATUS
```

```
Identifier:         CampaignDoingBadly
Event:              Campaign is not going well
Exports:            
Class:              ET_CAMPAIGN_DOING_BADLY
```

```
Identifier:         CampaignHudShown
Event:              We are at the campaign hud with no screens visible
Exports:            
Class:              ET_CAMPAIGN_HUD_SHOWN
```

```
Identifier:         CampaignMapGesture
Event:              You have performed gesture navigation on the campaign map
Exports:            
Class:              ET_CAMPAIGN_MAP_GESTURE
```

```
Identifier:         CharacterInfoScreen
Event:              A character's detailed info is displayed.
Exports:            
Class:              ET_FTH_CHARACTER_INFO_SCREEN
```

```
Identifier:         ConstructionItemClicked
Event:              Called when a construction item is clicked
Exports:            resource_description
Class:              ET_CONSTRUCTION_ITEM_CLICKED
```

```
Identifier:         ConstructionPopulated
Event:              Called when construction options are added
Exports:            
Class:              ET_CONSTRUCTION_POPULATED
```

```
Identifier:         ContextPopupInteraction
Event:              A context popup button has been tapped
Exports:            
Class:              ET_CONTEXT_POPUP_INTERACTION
```

```
Identifier:         DiplomacyConstructingCounterOffer
Event:              We are constructing a counter offer in the diplomacy scroll
Exports:            
Class:              ET_DIPLOMACY_CONSTRUCTING_COUNTER_OFFER
```

```
Identifier:         DiplomacyConstructingOffer
Event:              We are constructing an offer in the diplomacy scroll
Exports:            
Class:              ET_DIPLOMACY_CONSTRUCTING_OFFER
```

```
Identifier:         DiplomacyOpponentPresentsCounterOffer
Event:              We are presented a counter offer in the diplomacy 
Exports:            
Class:              ET_DIPLOMACY_OPPONENT_PRESENTS_COUNTER_OFFER
```

```
Identifier:         DiplomacyOpponentPresentsOffer
Event:              We are presented an offer in the diplomacy scroll
Exports:            
Class:              ET_DIPLOMACY_OPPONENT_PRESENTS_OFFER
```

```
Identifier:         DiplomacyScrollPopulated
Event:              Called when diplomacy offers are added
Exports:            
Class:              ET_DIPLOMACY_SCROLL_POPULATED
```

```
Identifier:         DiplomaticStandingShown
Event:              The Diplomatic Standings are shown in the faction overview.
Exports:            
Class:              ET_FTH_DIPLOMATIC_STANDING_SHOWN
```

```
Identifier:         DiplomatSelected
Event:              You have selected a diplomat
Exports:            
Class:              ET_DIPLOMAT_SELECTED
```

```
Identifier:         ElectionResults
Event:              The senate election results notification has appeared.
Exports:            
Class:              ET_FTH_ELECTION_RESULTS
```

```
Identifier:         EmbargoIsAvailable
Event:              EmbargoIsAvailable.
Exports:            
Class:              ET_EMBARGO_IS_AVAILABLE
```

```
Identifier:         EnemyCharacterSelected
Event:              An enemy character is selected on the Strat map.
Exports:            
Class:              ET_FTH_ENEMY_CHARACTER_SELECTED
```

```
Identifier:         EnemySettlementSelected
Event:              An enemy Settlement is selected on the Strat map.
Exports:            
Class:              ET_FTH_ENEMY_SETTLEMENT_SELECTED
```

```
Identifier:         EnteredBattle
Event:              Player has entered a battle.
Exports:            
Class:              ET_FTH_ENTERED_BATTLE
```

```
Identifier:         EnteredCityView
Event:              City View battle entered
Exports:            
Class:              ET_CITY_VIEW_ENTERED
```

```
Identifier:         EnterTacticalMode
Event:              Entering tactical mode
Exports:            
Class:              ET_ENTER_TACTICAL_MODE
```

```
Identifier:         FactionDetails
Event:              Faction Details Screen Open
Exports:            
Class:              ET_FACTION_DETAILS
```

```
Identifier:         FactionFactions
Event:              Faction Factions Screen Open - Overlaps with FactionSummaryPanelOpen
Exports:            
Class:              ET_FACTION_FACTIONS
```

```
Identifier:         FactionFamilyTree
Event:              Faction Family Tree Open
Exports:            
Class:              ET_FACTION_FAMILY_TREE
```

```
Identifier:         FactionFinancesShown
Event:              The player's finances are shown in the faction overview.
Exports:            
Class:              ET_FTH_FACTION_FINANCES_SHOWN
```

```
Identifier:         FactionLists
Event:              Faction Lists Screen Open
Exports:            
Class:              ET_FACTION_LISTS
```

```
Identifier:         FactionRankings
Event:              Faction Rankings Screen Open
Exports:            
Class:              ET_FACTION_RANKINGS
```

```
Identifier:         FactionSenate
Event:              Faction Senate Screen Open
Exports:            
Class:              ET_FACTION_SENATE
```

```
Identifier:         FactionSenateFloor
Event:              Faction Senate Officials Screen Open
Exports:            
Class:              ET_FACTION_SENATE_FLOOR
```

```
Identifier:         FactionSenateMissions
Event:              Faction Senate Missions Screen Open
Exports:            
Class:              ET_FACTION_SENATE_MISSIONS
```

```
Identifier:         FactionSenateOfficials
Event:              Faction Senate Officials Screen Open
Exports:            
Class:              ET_FACTION_SENATE_OFFICIALS
```

```
Identifier:         FactionSenatePolicy
Event:              Faction Senate Policy Screen Open
Exports:            
Class:              ET_FACTION_SENATE_POLICY
```

```
Identifier:         FactionFactions
Event:              Faction Factions Screen Open - Overlaps with FactionSummaryPanelOpen
Exports:            
Class:              ET_FACTION_FACTIONS
```

```
Identifier:         FailedToEndTurn
Event:              FailedToEndTurn.
Exports:            
Class:              ET_FAILED_TO_END_TURN_TRIGGER
```

```
Identifier:         FamilyTreeShown
Event:              The Faction family tree is shown in fullscreen
Exports:            
Class:              ET_FTH_FAMILY_TREE_SHOWN
```

```
Identifier:         FeralNewsVisible
Event:              The Feral News Dialog is visible to the user
Exports:            
Class:              ET_FERAL_NEWS_VISIBLE
```

```
Identifier:         FirstStratUpdates
Event:              First strategy map updates
Exports:            none
Class:              ET_FIRST_STRAT_UPDATES
```

```
Identifier:         FleetSelected
Event:              You have selected a fleet
Exports:            
Class:              ET_FLEET_SELECTED
```

```
Identifier:         FormationTypesShown
Event:              Player has opened the tab that shows formation types in a battle.
Exports:            
Class:              ET_FTH_FORMATION_TYPES_SHOWN
```

```
Identifier:         FriendlyCharacterSelected
Event:              A friendly character is selected on the Strat map.
Exports:            
Class:              ET_FTH_FRIENDLY_CHARACTER_SELECTED
```

```
Identifier:         FriendlySettlementSelected
Event:              A friendly Settlement is selected on the Strat map.
Exports:            
Class:              ET_FTH_FRIENDLY_SETTLEMENT_SELECTED
```

```
Identifier:         HideBattleUI
Event:              You have actively hidden the battle UI
Exports:            
Class:              ET_HIDE_BATTLE_UI
```

```
Identifier:         HighTaxesCauseDisorder
Event:              HighTaxesCauseDisorder.
Exports:            
Class:              ET_FTH_HIGH_TAXES_CAUSE_DISORDER
```

```
Identifier:         ItemDeselected
Event:              Called when an item on the campaign map is deselected
Exports:            
Class:              ET_ITEM_DESELECTED
```

```
Identifier:         MapOverlayOpened
Event:              The map overlay screen is opened.
Exports:            
Class:              ET_FTH_MAP_OVERLAY_OPENED
```

```
Identifier:         MerchantSelected
Event:              Player has selected a merchant on the campaign map.
Exports:            
Class:              ET_FTH_MERCHANT_SELECTED
```

```
Identifier:         MergeArmiesOpened
Event:              The Merge Army scroll has opened.
Exports:            
Class:              ET_FTH_MERGE_ARMIES_OPENED
```

```
Identifier:         MissionSelected
Event:              Called when a mission on the agent hub has been selected
Exports:            
Class:              ET_MISSION_SELECTED
```

```
Identifier:         MoveRetinueAncillaryDeselected
Event:              
Exports:            
Class:              ET_MOVE_RETINUE_ANCILLARY_DESELECTED
```

```
Identifier:         MoveRetinueAncillarySelected
Event:              
Exports:            
Class:              ET_MOVE_RETINUE_ANCILLARY_SELECTED
```

```
Identifier:         MoveRetinueOpened
Event:              The Move Retinue tab in the faction overview is opened.
Exports:            
Class:              ET_FTH_MOVE_RETINUE_OPENED
```

```
Identifier:         MoveRetinuePopulated
Event:              Called when move retinue window gets populated
Exports:            
Class:              ET_MOVE_RETINUE_POPULATED
```

```
Identifier:         MoveRetinuePressed
Event:              Called when move retinue character gets pressed
Exports:            
Class:              ET_MOVE_RETINUE_PRESSED
```

```
Identifier:         MovieStopped
Event:              The player stopped the movie
Exports:            
Class:              ET_MOVIE_STOPPED
```

```
Identifier:         NavalCombatStarted
Event:              Player has opened the tab that shows formation types in a battle.
Exports:            
Class:              ET_FTH_NAVAL_COMBAT_STARTED
```

```
Identifier:         NewsTabClosed
Event:              The News tab was closed using the Escape key.
Exports:            
Class:              ET_NEWS_TAB_CLOSED
```

```
Identifier:         NewsTabOpened
Event:              The News tab was opened.
Exports:            
Class:              ET_NEWS_TAB_OPENED
```

```
Identifier:         OwnFactionDetailsOpened
Event:              The Faction Details tab in the faction overview is opened.
Exports:            
Class:              ET_FTH_OWN_FACTION_DETAILS_OPENED
```

```
Identifier:         PostBattleScreen
Event:              A battle ends and the post battle stats screen opens.
Exports:            
Class:              ET_FTH_POST_BATTLE_SCREEN
```

```
Identifier:         PreBattleScreen
Event:              The pre-battle scroll is open.
Exports:            
Class:              ET_FTH_PRE_BATTLE_SCREEN
```

```
Identifier:         QuickListsOpened
Event:              Quick lists opened.
Exports:            
Class:              ET_QUICK_LISTS_OPENED
```

```
Identifier:         RebelCharacterSelected
Event:              RebelCharacterSelected.
Exports:            
Class:              ET_FTH_REBEL_CHARACTER_SELECTED
```

```
Identifier:         RecruitmentItemClicked
Event:              Called when a recruitment item is clicked
Exports:            resource_description
Class:              ET_RECRUITMENT_ITEM_CLICKED
```

```
Identifier:         RecruitmentPopulated
Event:              Called when recruitment options are added
Exports:            
Class:              ET_RECRUITMENT_POPULATED
```

```
Identifier:         RoutesBlockaded
Event:              The bloackaded routes or ports notification has appeared.
Exports:            
Class:              ET_FTH_ROUTES_BLOCKADED
```

```
Identifier:         ScrollDidOpen
Event:              Called when a scroll is opened
Exports:            resource_description
Class:              ET_SCROLL_DID_OPEN
```

```
Identifier:         SelectionAssistPossible
Event:              Selection assist could be useful
Exports:            
Class:              ET_SELECTION_ASSIST_COULD_FIRE
```

```
Identifier:         SendAgentPanel
Event:              The 'Send Agent' button is pressed
Exports:            
Class:              ET_FTH_SEND_AGENT_PANEL
```

```
Identifier:         SettlementButtonPressed
Event:              The player has clicked on a button associated with a settlement
Exports:            resource_description, faction, settlement, region_id
Class:              ET_SETTLEMENT_BUTTON_PRESSED
```

```
Identifier:         SettlementCharacter
Event:              Settlement Character Panel is Opened
Exports:            
Class:              ET_SETTLEMENT_CHARACTER
```

```
Identifier:         SettlementDetailsShown
Event:              A settlement's details are displayed.
Exports:            
Class:              ET_FTH_SETTLEMENT_DETAILS_SHOWN
```

```
Identifier:         SettlementOverview
Event:              Settlement Panel is opened to the main screen(Phone UI)
Exports:            
Class:              ET_SETTLEMENT_OVERVIEW
```

```
Identifier:         SettlementTrade
Event:              Settlement Trade Panel is Opened (Phone UI)
Exports:            
Class:              ET_SETTLEMENT_TRADE
```

```
Identifier:         SiegeDetailsShown
Event:              The siege overview scroll is open.
Exports:            
Class:              ET_FTH_SIEGE_DETAILS_SHOWN
```

```
Identifier:         SpySelected
Event:              You have selected a spy
Exports:            
Class:              ET_SPY_SELECTED
```

```
Identifier:         TacticalMapShown
Event:              The Tactical map is toggled on in a battle.
Exports:            
Class:              ET_FTH_TACTICAL_MAP_SHOWN
```

```
Identifier:         UnitHasRouted
Event:              Called when a unit starts routing
Exports:            resource_description
Class:              ET_UNIT_HAS_ROUTED
```

```
Identifier:         UnitInfoOpened
Event:              Called when a unit's info panel is opened in a battle.
Exports:            
Class:              ET_UNIT_INFO_OPENED
```

```
Identifier:         UnitsGrouped
Event:              Units have been grouped in a battle.
Exports:            
Class:              ET_FTH_UNITS_GROUPED
```

```
Identifier:         WorldScriptTerminate
Event:              A world script has finished
Exports:            resource_description
Class:              ET_WORLD_SCRIPT_TERMINATE
```

## Removed 2.0.4 Events

These features are no longer needed as they have been replaced with the single `TakeOffice` & `LeaveOffice` commands above.


```
Identifier:         BecomeQuaestor
Event:              The character has been made Quaestor
Exports:            nc_character_record, character_record, faction, region_id, character_type
Class:              ET_BECOME_QUAESTOR
```

```
Identifier:         BecomeAedile
Event:              The character has been made Aedile
Exports:            nc_character_record, character_record, faction, region_id, character_type
Class:              ET_BECOME_AEDILE
```

```
Identifier:         BecomePraetor
Event:              The character has been made Praetor
Exports:            nc_character_record, character_record, faction, region_id, character_type
Class:              ET_BECOME_PRAETOR
```

```
Identifier:         BecomeConsul
Event:              The character has been made Consul
Exports:            nc_character_record, character_record, faction, region_id, character_type
Class:              ET_BECOME_CONSUL
```

```
Identifier:         BecomeCensor
Event:              The character has been made Censor
Exports:            nc_character_record, character_record, faction, region_id, character_type
Class:              ET_BECOME_CENSOR
```

```
Identifier:         BecomePontifexMaximus
Event:              The character has been made Pontifex Maximus
Exports:            nc_character_record, character_record, faction, region_id, character_type
Class:              ET_BECOME_PONTIFEX_MAXIMUS
```

```
Identifier:         CeasedQuaestor
Event:              The character is no longer Quaestor
Exports:            nc_character_record, character_record, faction, region_id, character_type
Class:              ET_CEASED_QUAESTOR
```

```
Identifier:         CeasedAedile
Event:              The character is no longer Aedile
Exports:            nc_character_record, character_record, faction, region_id, character_type
Class:              ET_CEASED_AEDILE
```

```
Identifier:         CeasedPraetor
Event:              The character is no longer Praetor
Exports:            nc_character_record, character_record, faction, region_id, character_type
Class:              ET_CEASED_PRAETOR
```

```
Identifier:         CeasedConsul
Event:              The character is no longer Consul
Exports:            nc_character_record, character_record, faction, region_id, character_type
Class:              ET_CEASED_CONSUL
```

```
Identifier:         CeasedCensor
Event:              The character is no longer Censor
Exports:            nc_character_record, character_record, faction, region_id, character_type
Class:              ET_CEASED_CENSOR
```

```
Identifier:         CeasedPontifexMaximus
Event:              The character is no longer Pontifex Maximus
Exports:            nc_character_record, character_record, faction, region_id, character_type
Class:              ET_CEASED_PONTIFEX_MAXIMUS
```

## Full List of Events

* [docudemon_events.txt](/documentation/feature_guides/scripts/docudemon_events.txt)
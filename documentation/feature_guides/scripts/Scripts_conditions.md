![Workshop_header_template](/Workshop_header_template.png)
# Scripts - Conditions

# Table Of Contents

* [Table Of Contents](#table-of-contents)
   * [New 2.0.4 Events](#new-204-events)
   * [New 2.0.0 -&gt; 2.0.3 Events](#new-200---203-events)
   * [Full List of Conditions](#full-list-of-conditions)

## New 2.0.4 Events

The following are new commands added with the 2.0.4 patch:

```
Identifier:              HasOffice
Trigger requirements:    character
Parameters:              
Sample use:              HasOffice Aedile
Description:             Checks if a character holds a senate office (or is just about to leave one, in the case of LeaveOffice)
Battle or Strat:         Strat
Class:                   HAS_OFFICE
Implemented:             Yes
```

```
Identifier:              FactionIsAlive
Trigger requirements:    none
Parameters:              faction name
Sample use:              FactionIsAlive romans_julii
Description:             Checks if the given faction is alive (as opposed to waiting to emerge or defeated)
Battle or Strat:         Strat
Class:                   FACTION_IS_ALIVE
Implemented:             Yes
```

```
Identifier:              IsAlly
Trigger requirements:    faction
Parameters:              other faction type
Sample use:              IsAlly romans_julii
Description:             is this faction allied to the other
Battle or Strat:         Strat
Class:                   FACTION_IS_ALLY
Implemented:             Yes
```

```
Identifier:              IsProtectorate
Trigger requirements:    faction
Parameters:              other faction type
Sample use:              IsProtectorate romans_julii
Description:             is this faction a protectorate of ours?
Battle or Strat:         Strat
Class:                   FACTION_IS_PROTECTORATE
Implemented:             Yes
```

```
Identifier:              IsProtector
Trigger requirements:    faction
Parameters:              other faction type
Sample use:              IsProtector romans_julii
Description:             is this faction our protector?
Battle or Strat:         Strat
Class:                   FACTION_IS_PROTECTOR
Implemented:             Yes
```

```
Identifier:              IsSameSuperfaction
Trigger requirements:    faction
Parameters:              other faction type
Sample use:              IsSameSuperfaction romans_julii
Description:             is this faction in the same superfaction as us? Returns false against former members of our superfaction that were outlawed
Battle or Strat:         Strat
Class:                   FACTION_IS_SAME_SUPERFACTION
Implemented:             Yes
```

```
Identifier:              MajorEventActive
Trigger requirements:    
Parameters:              "major event name", faction type (optional, checks local/first faction by default)
Sample use:              MajorEventActive "currency_crisis", empire_west
Description:             Is this event active for the given faction
Battle or Strat:         Either
Class:                   MAJOR_EVENT_ACTIVE
Implemented:             Yes
```

```
Identifier:              SettlementRevoltingFrom
Trigger requirements:    settlement
Parameters:              faction name or tag
Sample use:              SettlementRevoltingFrom roman_empire
Description:             Only useful in revolt faction spawning scripts - says who the faction that we are in the process of revolting from is
Battle or Strat:         Either
Class:                   REVOLTING_FROM
Implemented:             Yes
```

```
Identifier:              IsCapital
Trigger requirements:    settlement
Parameters:              none
Sample use:              IsCapital
Description:             Checks if this settlement is a capital
Battle or Strat:         Either
Class:                   IS_CAPITAL
Implemented:             Yes
```

```
Identifier:              I_SettlementOwnerCulture
Trigger requirements:    settlement if name == local
Parameters:              settlement name, logic token, culture type
Sample use:              I_SettlementOwnerCulture local = eastern
Description:             Is this settlement owned by this faction with this culture?
Battle or Strat:         Strat
Class:                   SETTLEMENT_OWNER_CULTURE
Implemented:             Yes
```

```
Identifier:              I_SettlementLevel
Trigger requirements:    settlement if name == local
Parameters:              settlement name, logic token, settlement level
Sample use:              I_SettlementLevel local == huge_city
Description:             Is this settlement at this level?
Battle or Strat:         Strat
Class:                   SETTLEMENT_LEVEL_IS
Implemented:             Yes
```

## New 2.0.0 -> 2.0.3 Events

The following new conditions have been added to the dictionary for the Remaster:

```
Identifier:              BattleSelectedPlayerUnitSpecialAbilitySupported
Trigger requirements:    
Parameters:              special_ability ( testudo, phalanx, wedge, drop_engines, flaming_ammo, warcry, chant, curse, beserk, rally, kill_elephants, move_and_shoot, cantabrian_circle, shield_wall, stealth, feigned_rout, schiltrom )
Sample use:              BattleSelectedPlayerUnitSpecialAbilitySupported = flaming_ammo
Description:             What special ability can the selected units support?
Battle or Strat:         Battle
Class:                   BATTLE_SELECTED_PLAYER_UNIT_SPECIAL_ABILITY_SUPPORTED
Implemented:             Yes
```

```
Identifier:              BattleUnitActionStatus
Trigger requirements:    resource_description
Parameters:              Unit Name, Unit Status to detect
Sample use:              BattleUnitActionStatus player_general, routing
Description:             Checks when a unit changes status
Battle or Strat:         Battle
Class:                   BATTLE_UNIT_ACTION_STATUS
Implemented:             Yes
```

```
Identifier:              CharacterName
Trigger requirements:    character_record
Parameters:              Character Name
Sample use:              CharacterName Flavious Fella
Description:             Checks for a given characters name
Battle or Strat:         Strat
Class:                   CHARACTER_NAME
Implemented:             Yes
```

```
Identifier:              ConstructionItemClicked
Trigger requirements:    resource_description
Parameters:              id
Sample use:              ConstructionItemClicked stables
Description:             Check for a given construction item
Battle or Strat:         Strat
Class:                   CONSTRUCTION_ITEM_CLICKED
Implemented:             Yes
```

```
Identifier:              DistanceCapital
Trigger requirements:    character_record
Parameters:              logic token, level
Sample use:              DistanceCapital >= 40
Description:             Does the characters distance to the faction capital exceed the given threshold?
Battle or Strat:         Strat
Class:                   CHARACTER_DISTANCE_CAPITAL
Implemented:             Yes
```

```
Identifier:              FeralSettlementAutoManaged
Trigger requirements:    settlement
Parameters:              Automanagement type (Troops, Buildings, Mechanics)
Sample use:              not SettlementAutoManaged Troops
Description:             Is the settlement auto managed in a particular way?
Battle or Strat:         Strat
Class:                   FERAL_SETTLEMENT_AUTO_MANAGED
Implemented:             Yes
```

```
Identifier:              FeralUIType
Trigger requirements:    
Parameters:              UI Type
Sample use:              FeralUIType phone
Description:             Detect what UI we are using
Battle or Strat:         Yes
Class:                   FERAL_UI_TYPE
Implemented:             Yes
```

```
Identifier:              HasResource
Trigger requirements:    settlement
Parameters:              resource name (includes hidden resources)
Sample use:              HasResource sparta
Description:             For scripting - does the region have this resource
Battle or Strat:         Either
Class:                   HAS_RESOURCE
Implemented:             Yes
```

```
Identifier:              HomeSettlementBuildingExists
Trigger requirements:    character
Parameters:              building description, logic token, test level
Sample use:              HomeSettlementBuildingExists = governors_house
Description:             Test to see if the home settlement of the triggering character has a building at a particular level
Battle or Strat:         Strat
Class:                   HOME_SETTLEMENT_BUILDING_LEVEL_EXISTS_TEST
Implemented:             Yes
```

```
Identifier:              I_AdvisorSpeechPlaying
Trigger requirements:    
Parameters:              
Sample use:              I_AdvisorSpeechPlaying
Description:             Detect whether advisor speech is playing or not
Battle or Strat:         Both
Class:                   ADVISOR_SPEECH_PLAYING
Implemented:             Yes
```

```
Identifier:              I_AmountOfUnitInSettlement
Trigger requirements:    
Parameters:              Settlement_name, Amount_of_unit_wanted, Unit_name
Sample use:              I_AmountOfUnitInSettlement Arretium 2 roman triarii
Description:             Check how many of a unit is in a settlement.
Battle or Strat:         Strat
Class:                   AMOUNT_OF_UNIT_IN_SETTLEMENT
Implemented:             Yes
```

```
Identifier:              I_AnnotationDisplayed
Trigger requirements:    
Parameters:              Annotation image name
Sample use:              I_AnnotationDisplayed set_general
Description:             Detect what annotation scroll is showing
Battle or Strat:         Yes
Class:                   FERAL_ANNOTATION_DISPLAYED
Implemented:             Yes
```

```
Identifier:              I_BattleEnd
Trigger requirements:    
Parameters:              None
Sample use:              I_BattleEnd
Description:             Has the battle entered one of the end phases (ending or finish countdown, not end pending, see IBattleEndPending for that)
Battle or Strat:         Battle
Class:                   IS_BATTLE_END
Implemented:             Yes
```

```
Identifier:              I_BattleEndPending
Trigger requirements:    
Parameters:              None
Sample use:              I_BattleEndPending
Description:             Has the battle entered the end pending phase (ie dialog to the human player for whether they want to mop up the leftovers)
Battle or Strat:         Battle
Class:                   IS_BATTLE_END_PENDING
Implemented:             Yes
```

```
Identifier:              I_BattleFinished
Trigger requirements:    
Parameters:              None
Sample use:              I_BattleFinished
Description:             Has the battle 'finished' phase started
Battle or Strat:         Either
Class:                   IS_BATTLE_FINISHED
Implemented:             Yes
```

```
Identifier:              I_CharacterNameNearTile
Trigger requirements:    
Parameters:              faction, character name, distance in squares, x, z
Sample use:              I_CharacterNameNearTile Flavius Julius, named_character, 10 48,30
Description:             Is a particular character near a particular tile?
Battle or Strat:         Strat
Class:                   I_CHARACTER_NAME_NEAR_TILE
Implemented:             Yes
```

```
Identifier:              I_CompareCounter
Trigger requirements:    
Parameters:              script counter, value
Sample use:              I_CompareCounter blib < 17
Description:             Compare a script counter to a value
Battle or Strat:         Either
Class:                   COMPARE_COUNTER
Implemented:             Yes
```

```
Identifier:              I_IsPlayerTurn
Trigger requirements:    
Parameters:              
Sample use:              I_IsPlayerTurn
Description:             Check to see if the current turn is for player
Battle or Strat:         Both
Class:                   IS_PLAYER_TURN
Implemented:             Yes
```

```
Identifier:              I_IsTutorialEnabled
Trigger requirements:    
Parameters:              
Sample use:              I_IsTutorialEnabled
Description:             Check if a tutorial is enabled
Battle or Strat:         Both
Class:                   IS_TUTORIAL_ENABLED
Implemented:             Yes
```

```
Identifier:              I_SoundPlaying
Trigger requirements:    
Parameters:              <sound event tag>
Sample use:              I_SoundPlaying snd_IntroSpeech
Description:             Detect whether the tagged sound is playing or not
Battle or Strat:         Both
Class:                   SOUND_EVENT_PLAYING
Implemented:             Yes
```

```
Identifier:              I_TimerElapsed
Trigger requirements:    
Parameters:              logic token, timer_id, duration (milliseconds)
Sample use:              I_TimerElapsed rout_timer > 1000
Description:             How long has it been since the script timer restarted
Battle or Strat:         Either
Class:                   SCRIPT_TIMER_ELAPSED
Implemented:             Yes
```

```
Identifier:              I_UnitCardSelected
Trigger requirements:    
Parameters:              unit name, amount of unit to select
Sample use:              I_UnitCardSelected roman city militia, 1, roman hastati, 3
Description:             Detect whether the unit card is currently selected
Battle or Strat:         Strat
Class:                   UNIT_CARD_SELECTED
Implemented:             Yes
```

```
Identifier:              LangIs
Trigger requirements:    
Parameters:              language ID (EN, DE, FR, ES, IT, RU, zh_CN)
Sample use:              LangIs cn_cz
Description:             Test the language
Battle or Strat:         Either
Class:                   CHECK_LANG
Implemented:             Yes
```

```
Identifier:              LocalPlayerBattlesFought
Trigger requirements:    
Parameters:              logic token, quantity
Sample use:              LocalPlayerBattlesFought = 6
Description:             How many battles has the player fought so far during this campaign?
Battle or Strat:         Either
Class:                   LOCAL_PLAYER_BATTLES_FOUGHT
Implemented:             Yes
```

```
Identifier:              LocalPlayerHasAIReinforcements
Trigger requirements:    
Parameters:              
Sample use:              LocalPlayerHasAIReinforcements
Description:             Test to see if the player has AI reinforcements
Battle or Strat:         Battle
Class:                   BATTLE_PLAYER_WITH_AI_REINFORCEMENTS_TEST
Implemented:             Yes
```

```
Identifier:              LocalPlayerHasManualReinforcements
Trigger requirements:    
Parameters:              
Sample use:              LocalPlayerHasManualReinforcements
Description:             Test to see if the player has manual reinforcements
Battle or Strat:         Battle
Class:                   BATTLE_PLAYER_WITH_MANUAL_REINFORCEMENTS_TEST
Implemented:             Yes
```

```
Identifier:              LocalPlayerHasReinforcements
Trigger requirements:    ET_PRE_BATTLE_PANEL_OPEN
Parameters:              
Sample use:              LocalPlayerHasReinforcements
Description:             Player has at least one reinforcement army
Battle or Strat:         Strat
Class:                   LOCAL_PLAYER_HAS_REINFORCEMENTS
Implemented:             Yes
```

```
Identifier:              MerchantIsAvailableToBuild
Trigger requirements:    ET_BUILDING_COMPLETED
Parameters:              faction, building
Sample use:              MerchantIsAvailableToBuild
Description:             Building that was built, can recruit merchants
Battle or Strat:         Strat
Class:                   MERCHANT_IS_AVAILABLE_TO_BUILD
Implemented:             Yes
```

```
Identifier:              NightBattlesEnabled
Trigger requirements:    IS_TOGGLED("night battles")
Parameters:              
Sample use:              WorldwideAncillaryExists
Description:             Is night battles enabled
Battle or Strat:         Strat
Class:                   NIGHT_BATTLE_ENABLED
Implemented:             Yes
```

```
Identifier:              RecruitmentItemClicked
Trigger requirements:    resource_description
Parameters:              id
Sample use:              RecruitmentItemClicked roman peasant
Description:             Check for a given recruitment item
Battle or Strat:         Strat
Class:                   RECRUITMENT_ITEM_CLICKED
Implemented:             Yes
```

```
Identifier:              RemasteredEducation
Trigger requirements:    None
Parameters:              None
Sample use:              RemasteredEducation
Description:             Test to see if the remastered education triggers should be used
Battle or Strat:         Strat
Class:                   REMASTERED_EDUCATION
Implemented:             Yes
```

```
Identifier:              ScrollDidOpen
Trigger requirements:    resource_description
Parameters:              Scroll Name
Sample use:              
Description:             Checks when scroll is open
Battle or Strat:         Both
Class:                   SCROLL_DID_OPEN
Implemented:             Yes
```

```
Identifier:              SettlementCapabilityLevel
Trigger requirements:    settlement
Parameters:              capability_type_strings (population_growth_bonus, population_loyalty_bonus, population_health_bonus, trade_base_income_bonus, trade_level_bonus, trade_fleet, taxable_income_bonus, mine_resource, farming_level, road_level, gate_strength, gate_defences, wall_level, tower_level, armour, stage_games, stage_races, fire_risk, weapon_simple, weapon_missile, weapon_bladed, weapon_siege, weapon_other, upgrade_bodyguard, recruits_morale_bonus, recruits_exp_bonus, happiness_bonus, law_bonus, construction_cost_bonus_military, construction_cost_bonus_religious, construction_cost_bonus_defensive, construction_cost_bonus_other, construction_time_bonus_military, construction_time_bonus_religious, construction_time_bonus_defensive, construction_time_bonus_other), logic token, test level
Sample use:              SettlementCapabilityLevel law_bonus > 0
Description:             Test to see if the settlement has a capability at a particular level
Battle or Strat:         Strat
Class:                   SETTLEMENT_CAPABILITY_LEVEL
Implemented:             Yes
```

```
Identifier:              SettlementOrderLevel
Trigger requirements:    settlement
Parameters:              settlement_order_type_strings (garrison, law, fun, influence, tax_bonus, triumph, wonder, boom, squalour, distance_to_capital, culture_penalty, no_governance, tax_penalty, turmoil, underpopulation, besieged, blockaded, recession, entertained, health, governor_religion_unrest, leader_religion_unrest), logic token, test level
Sample use:              SettlementOrderLevel law > 0
Description:             Test to see if the settlements order factor is at a particular level
Battle or Strat:         Strat
Class:                   SETTLEMENT_ORDER_LEVEL
Implemented:             Yes
```

```
Identifier:              SettlementHasDamagedBuilding
Trigger requirements:    SETTLEMENT_EVENT_TRIGGER
Parameters:              settlement
Sample use:              SettlementHasDamagedBuilding
Description:             Settlement has at least one damaged building
Battle or Strat:         Strat
Class:                   SETTLEMENT_HAS_DAMAGED_BUILDING
Implemented:             Yes
```

```
Identifier:              TestFaction
Trigger requirements:    
Parameters:              faction name
Sample use:              TestFaction romans_julii
Description:             Test is a given faction is being used by the player
Battle or Strat:         Either
Class:                   COMPARE_FACTION
Implemented:             Yes
```

```
Identifier:              Toggled
Trigger requirements:    
Parameters:              toggle name
Sample use:              Toggled 'gradual trait loss'
Description:             Is the remaster toggle for this enabled?
Battle or Strat:         Either
Class:                   TOGGLE_ENABLED
Implemented:             Yes
```

```
Identifier:              TradingExotic
Trigger requirements:    character_record
Parameters:              None
Sample use:              TradingExotic
Description:             Is the character trading an exotic resource?
Battle or Strat:         Strat
Class:                   TRADING_EXOTIC
Implemented:             Yes
```

```
Identifier:              UnitHasRouted
Trigger requirements:    resource_description
Parameters:              Unit Name
Sample use:              
Description:             Checks when a unit has routed
Battle or Strat:         Battle
Class:                   UNIT_HAS_ROUTED
Implemented:             Yes
```

## Full List of Conditions

* [docudemon_conditions.txt](/documentation/feature_guides/scripts/docudemon_conditions.txt)
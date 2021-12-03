![Workshop_header_template](/Workshop_header_template.png)
# Scripts - Commands

# Table Of Contents

* [Table Of Contents](#table-of-contents)
   * [New 2.0.4 Commands](#new-204-commands)
   * [New 2.0.0 -&gt; 2.0.3 Commands](#new-200---203-commands)
   * [Modified Conditions](#modified-conditions)
   * [Full List of Conditions](#full-list-of-conditions)

## New 2.0.4 Commands

The following are new commands added with the 2.0.4 patch:

```
Identifier:         override_superfaction_popularity
Parameters:         faction type, true/false
Description:        Disable normal superfaction popularity processing so that it can be controlled by a script
Sample use:         override_superfaction_popularity romans_julii true
Class:              SENATE_OVERRIDE_POPULARITY
Implemented:        Yes
```

```
Identifier:         set_faction_senate_standing
Parameters:         faction type, value or counter
Description:        Set the senate standing of a given faction
Sample use:         set_faction_senate_standing romans_julii blib
Class:              SENATE_SET_SENATE_POPULARITY_SENATE
Implemented:        Yes
```

```
Identifier:         set_faction_people_standing
Parameters:         faction type, value or counter
Description:        Set the people standing of a given faction
Sample use:         set_faction_people_standing romans_julii 70
Class:              SENATE_SET_SENATE_POPULARITY_PEOPLE
Implemented:        Yes
```

```
Identifier:         message_prompt
Parameters:         (inside braces) flag_counter, result_counter, title, body and optional image
Description:        Creates a new news message with a simple yes/no prompt. Will set flag_counter to 1 and result_counter to 1 or 0 depending on player selection.
Using the same counter for both the flag and result will set it to the result only.
Use ScriptPromptCallback event to detect responses
Sample use:         message prompt
{
	flag_counter blib
	result_counter blob
	title string_from_expanded_bi
	body string_from_expanded_bi
	image event_image_name
Class:              SCRIPT_MESSAGE_PROMPT
Implemented:        Yes
```

```
Identifier:         break
Parameters:         
Description:        immediately exit the current scope
Sample use:         break
Class:              BREAK_SCOPE
Implemented:        Yes
```

```
Identifier:         set_ao_visible
Parameters:         object tag, show/hide and optional region name
Description:        set visibility of all ambient objects with the given tag in the specified region (if no region name specified, taken from context)
Sample use:         set_ao_visible "dockyard_ships" show ["Latium"]
Class:              SET_AO_VISIBLE
Implemented:        Yes
```

```
Identifier:         set_all_ao_visible
Parameters:         object tag and show/hide
Description:        set visibility of all ambient objects with the given tag throughout the entire map
Sample use:         set_ao_visible "shipwrecks" show
Class:              SET_ALL_AO_VISIBLE
Implemented:        Yes
```

```
Identifier:         return
Parameters:         true/false
Description:        return a value from the script and terminate, used for faction spawn scripts
Sample use:         return true
Class:              SCRIPT_RETURN
Implemented:        Yes
```

```
Identifier:         counter_operation
Parameters:         <result counter> = <counter> <operation> <counter>
Description:        Sets the result counter to the result of the expression. Valid operations are *, /, +, -
Sample use:         counter_operation blib = foo + bar
Class:              COUNTER_OPERATION
Implemented:        Yes
```

```
Identifier:         store_counter
Parameters:         store_counter <counter name> <storage location> <storage label>
Description:        Stores a counter in the given location type in scope, with the label specified
Sample use:         store_counter blib settlement blib_in_a_settlement
Class:              STORE_COUNTER
Implemented:        Yes
```

```
Identifier:         retrieve_counter
Parameters:         retrieve_counter <storage label> <storage location> <counter name>
Description:        Extacts a counter with the given label from the location type in scope, and loads it into the supplied counter
Sample use:         retrieve_counter blib_in_a_settlement settlement blib
Class:              RETREIVE_COUNTER
Implemented:        Yes
```

```
Identifier:         add_religion
Parameters:         religion name, region name, commitment to add
Description:        Add commitment to a given religion into a region
Sample use:         add_religion Christianity Latium -10
Class:              ADD_RELIGION
Implemented:        Yes
```

## New 2.0.0 -> 2.0.3 Commands

The following new commands have been added to the dictionary for the Remaster:


```
Identifier:         add_hidden_resource
Parameters:         region name and resource name
Description:        add a hidden resource to a given region
Sample use:         add_hidden_resource Latium sparta
Class:              ADD_HIDDEN_RESOURCE
Implemented:        Yes
```

```
Identifier:         advance_completed_tasks
Parameters:         <task number to set>
Description:        Advances the right tutorial panel list of completed tasks to the specified task.
Sample use:         advance_completed_tasks 2
Class:              ADVANCE_COMPLETED_TASKS
Implemented:        Yes
```

```
Identifier:         allow_campaign_battles
Parameters:         yes/no
Description:        Allows battles to be started/not started from campaign UI. This is a workaround for how we start the tutorial battles
Sample use:         allow_campaign_battles yes
Class:              ALLOW_CAMPAIGN_BATTLES
Implemented:        Yes
```

```
Identifier:         block_unit_selection
Parameters:         switch, unit
Description:        Enable/disable ability to select units.
Sample use:         block_unit_selection on player_archers
Class:              BLOCK_UNIT_SELECTION
Implemented:        Yes
```

```
Identifier:         box_drag_selection
Parameters:         on/off
Description:        Switches the ability to use the box drag selection on units in battles.
Sample use:         box_drag_selection on;
Class:              BOX_DRAG_SELECTION
Implemented:        Yes
```

```
Identifier:         clear_restrict_battle_movement
Parameters:         (circle, <x>, <y>)
Description:        
Sample use:         
Class:              CLEAR_RESTRICT_BATTLE_MOVEMENT
Implemented:        Yes
```

```
Identifier:         clear_restrict_strat_movement
Parameters:         
Description:        Clear the restricted movement
Sample use:         clear_restrict_strat_movement
Class:              CLEAR_RESTRICT_STRAT_MOVEMENT
Implemented:        Yes
```

```
Identifier:         clear_strat_selection_unblocker
Parameters:         
Description:        Clears the list of selectable items on the strat map, making everything selectable.
Sample use:         clear_strat_selection_unblocker
Class:              CLEAR_STRAT_SELECTION_UNBLOCKER
Implemented:        Yes
```

```
Identifier:         click_drag_move
Parameters:         on/off
Description:        Switches the ability to use the right-click and drag movement on units in battles.
Sample use:         click_drag_move on;
Class:              CLICK_DRAG_MOVE
Implemented:        Yes
```

```
Identifier:         close_news_panel
Parameters:         
Description:        instantly closes the news panel
Sample use:         close_news_panel;
Class:              CLOSE_NEWS_PANEL
Implemented:        Yes
```

```
Identifier:         control_feral_anim
Parameters:         string: animation key, string: element id, flag: 'reverse'
Description:        Triggers feral animations
Sample use:         control_feral_anim tightness order_tightness reverse
Class:              FERAL_CONTROL_ANIM
Implemented:        Yes
```

```
Identifier:         create_mercenary_pool
Parameters:         
Description:        
Sample use:         
Class:              CREATE_MERCENARY_POOL
Implemented:        Yes
```

```
Identifier:         declare_persistent_counter
Parameters:         name of the counter, a single word identifier.
Description:        declare a counter that will be persistent between saves and give it an initial value of zero, assuming it hasn't been defined in a previous save
Sample use:         declare_persistent_counter blib
Class:              DECLARE_PERSISTENT_COUNTER
Implemented:        Yes
```

```
Identifier:         deselect_current_selection
Parameters:         
Description:        Deselect the currently selected settlement, unit, etc.
Sample use:         deselect_current_selection
Class:              DESELECT_CURRENT_SELECTION
Implemented:        Yes
```

```
Identifier:         destroy_building
Parameters:         settlement name and the building ID
Description:        destroy a building in a settlement
Sample use:         destroy_building "Rome" market
Class:              DESTROY_BUILDING
Implemented:        Yes
```

```
Identifier:         disable_agent_hub_all
Parameters:         
Description:        Disables all of the given targets from being clickable
Sample use:         disable_agent_hub_all (agent | mission)
Class:              DISABLE_AGENT_HUB_ALL
Implemented:        Yes
```

```
Identifier:         disable_agent_hub
Parameters:         agent name
Description:        Disable an agent with a given name
Sample use:         disable_agent_hub_agent Decius Curtius
Class:              DISABLE_AGENT_HUB_AGENT
Implemented:        Yes
```

```
Identifier:         disable_all_ui_cards
Parameters:         card type (unit | character | building)
Description:        Disable all ui cards of the given type
Sample use:         disable_all_ui_cards building
Class:              DISABLE_ALL_UI_CARDS
Implemented:        Yes
```

```
Identifier:         disable_diplomacy_ui
Parameters:         
Description:        disable all diplomacy ui elements
Sample use:         disable_diplomacy_ui
Class:              DISABLE_DIPLOMACY_UI
Implemented:        Yes
```

```
Identifier:         disable_move_retinue_all
Parameters:         (Character | Ancillary)
Description:        Disables all of the given targets from being clickable
Sample use:         disable_move_retinue_all (Character | Ancillary)
Class:              DISABLE_MOVE_RETINUE_ALL
Implemented:        Yes
```

```
Identifier:         enable_move_retinue_all
Parameters:         (Character | Ancillary)
Description:        Enable all of the given targets from being clickable
Sample use:         disable_move_retinue_all (Character | Ancillary)
Class:              ENABLE_MOVE_RETINUE_ALL
Implemented:        Yes
```

```
Identifier:         disable_pause_shortcut_in_campaign
Parameters:         true/false
Description:        Stop esc from bringing up Pause menu while on campaign map
Sample use:         disable_pause_shortcut_in_campaign true;
Class:              DISABLE_PAUSE_SHORTCUT_IN_CAMPAIGN
Implemented:        Yes
```

```
Identifier:         disable_popups
Parameters:         none
Description:        Disable the popup style help in the prologue
Sample use:         disable_popups
Class:              FERAL_END_PROLOGUE_POPUPS
Implemented:        Yes
```

```
Identifier:         disable_specific_shortcut
Parameters:         {element_id}, {shortcut_id}, true/false
Description:        This will disable/enable a given keyboard shortcut for a given element (or all elements if element_id is omitted), except the key defined as being the 'quit' key (ESC by default).  See data/descr_shortcuts.txt for the element_ids that are useable
Sample use:         disable_specific_shortcut camera rot_l true - to disable, disable_specific_shortcut camera rot_l false - to enable it again
Class:              DISABLE_SPECIFIC_SHORTCUT
Implemented:        Yes
```

```
Identifier:         disable_ui_card
Parameters:         card type (unit | character | building), id, nth instance
Description:        Disables a given UI card
Sample use:         disable_ui_card building, militia_barracks, 0
Class:              DISABLE_UI_CARD
Implemented:        Yes
```

```
Identifier:         e_select_unit
Parameters:         N/A
Description:        Selects the trigger unit
Sample use:         e_select_unit
Class:              E_FERAL_SELECT_UNIT
Implemented:        Yes
```

```
Identifier:         enable_agent_hub
Parameters:         agent name
Description:        Enable an agent with a given name
Sample use:         enable_agent_hub_agent Decius Curtius
Class:              ENABLE_AGENT_HUB_AGENT
Implemented:        Yes
```

```
Identifier:         enable_agent_hub_all
Parameters:         
Description:        Enable all of the targets from being clickable
Sample use:         enable_agent_hub_all (agent | mission)
Class:              ENABLE_AGENT_HUB_ALL
Implemented:        Yes
```

```
Identifier:         enable_all_ui_cards
Parameters:         card type (unit | character | building)
Description:        Enables all ui cards of the given type
Sample use:         enable_all_ui_cards building
Class:              ENABLE_ALL_UI_CARDS
Implemented:        Yes
```

```
Identifier:         enable_diplomacy_voices
Parameters:         on/off
Description:        enable or disable all diplomacy barks
Sample use:         enable_diplomacy_voices on
Class:              ENABLE_DIPLOMACY_VOICES
Implemented:        Yes
```

```
Identifier:         enable_move_retinue_all
Parameters:         (Character | Ancillary)
Description:        Enable all of the given targets from being clickable
Sample use:         disable_move_retinue_all (Character | Ancillary)
Class:              ENABLE_MOVE_RETINUE_ALL
Implemented:        Yes
```

```
Identifier:         enable_move_retinue_all
Parameters:         (Character | Ancillary)
Description:        Enable all of the given targets from being clickable
Sample use:         disable_move_retinue_all (Character | Ancillary)
Class:              ENABLE_MOVE_RETINUE_ALL
Implemented:        Yes
```

```
Identifier:         enable_ui_card
Parameters:         card type (unit | character | building), id, nth instance
Description:        Enables a given UI card
Sample use:         enable_ui_card building, militia_barracks, 0
Class:              ENABLE_UI_CARD
Implemented:        Yes
```

```
Identifier:         enable_unit_voices
Parameters:         on/off
Description:        enable or disable all unit command lines
Sample use:         enable_unit_voices on
Class:              ENABLE_UNIT_VOICES
Implemented:        Yes
```

```
Identifier:         end_benchmark
Parameters:         none
Description:        Ends a benchmark run
Sample use:         end_benchmark
Class:              FERAL_END_BENCHMARK
Implemented:        Yes
```

```
Identifier:         finish_battle
Parameters:         n/a
Description:        Completes the 'Finished' battle phase
Sample use:         finish_battle
Class:              FINISH_BATTLE
Implemented:        Yes
```

```
Identifier:         for_each
Parameters:         [iterator type] in [scope type] <scope identifier (assumed local if not supplied or scope is not faction, character or settlement)>. Scope types are faction, settlement, fort, character, army and unit.
Description:        iterate through all instances of a certain type within a given scope (note that unit iterator will always be fed through as player unit)
Sample use:         for_each settlement in faction "romans_brutii"
Class:              FOR_EACH
Implemented:        Yes
```

```
Identifier:         force_agent_succeed
Parameters:         yes/no
Description:        Ensures that the chances of agent actions are as normal or 100%
Sample use:         force_agent_succeed yes
Class:              FORCE_AGENT_SUCCEED
Implemented:        Yes
```

```
Identifier:         force_ai_control
Parameters:         n/a
Description:        Gives all armies to the AI
Sample use:         force_ai_control
Class:              FORCE_AI_CONTROL
Implemented:        Yes
```

```
Identifier:         force_autoresolve_outcome
Parameters:         target faction
Description:        Forces the outcome for the given faction
Sample use:         force_autoresolve_outcome roman_julii
Class:              FORCE_AUTORESOLVE_OUTCOME
Implemented:        Yes
```

```
Identifier:         force_deselect_trigger
Parameters:         
Description:        Triggers the Item Deselected event trigger.
Sample use:         force_deselect_trigger
Class:              FORCE_DESELECT_TRIGGER
Implemented:        Yes
```

```
Identifier:         force_diplomacy
Parameters:         (accept | reject), (yes | no)
Description:        Forces the ai to either accept or reject diplomacy requests
Sample use:         force_diplomacy accept, yes
Class:              FORCE_DIPLOMACY
Implemented:        Yes
```

```
Identifier:         force_settlement_tab
Parameters:         <tab name> - This can be 'units', 'buildings', 'characters' or 'passengers' 
Description:        Forces the tab of the settlement ui to change to the specified one.
Sample use:         force_settlement_tab units
Class:              FORCE_SETTLEMENT_TAB
Implemented:        Yes
```

```
Identifier:         forced_gate_success
Parameters:         boolean, chance(optional)
Description:        Sets the gate opening chance by a spy to a certain value
Sample use:         forced_gate_success on, 100
Class:              FORCED_GATE_SUCCESS
Implemented:        Yes
```

```
Identifier:         set_label
Parameters:         
Description:        Set a label that can be jumped to with a Goto statement
Sample use:         set_label location
Class:              SET_LABEL
Implemented:        Yes
```

```
Identifier:         hide_ui_element
Parameters:         ui ID
Description:        Hides a given UI element
Sample use:         hide_ui_element faction_button
Class:              HIDE_UI_ELEMENT
Implemented:        Yes
```

```
Identifier:         if_not
Parameters:         conditions to satisfy to execute the scope
Description:        conditional execution
Sample use:         if_not TimerElapsed < 1000
Class:              IF_NOT
Implemented:        Yes
```

```
Identifier:         goto
Parameters:         
Description:        jump to a place in the script marked by a label
Sample use:         goto location
Class:              GOTO
Implemented:        Yes
```

```
Identifier:         include_script
Parameters:         
Description:        terminate a script
Sample use:         include_script
Class:              INCLUDE_SCRIPT
Implemented:        Yes
```

```
Identifier:         move_to_settlement
Parameters:         settlement name
Description:        Moves the camera position to a settlement
Sample use:         move_to_settlement Rome
Class:              MOVE_TO_SETTLEMENT
Implemented:        Yes
```

```
Identifier:         open_siege_scroll
Parameters:         N/A
Description:        Opens the siege scroll
Sample use:         open_siege_scroll
Class:              FERAL_OPEN_SIEGE_SCROLL
Implemented:        Yes
```

```
Identifier:         open_stop_tutorial_confirmation_dialog
Parameters:         
Description:        Open a confirmation dialog that allows the user to stop the tutorial.
Sample use:         open_stop_tutorial_confirmation_dialog
Class:              OPEN_STOP_TUTORIAL_CONFIRMATION_DIALOG
Implemented:        Yes
```

```
Identifier:         play_sound_flourish
Parameters:         sound_name [force_no_fade]
Description:        Plays a sound over the top of any music, with or without a fade
Sample use:         play_sound_flourish ANIM_ARCHER_FIRE
Class:              PLAY_SOUND_FLOURISH
Implemented:        Yes
```

```
Identifier:         point_at_agent_hub
Parameters:         (Agent | Mission), (character name | nth), [circle|square|arrow], [direction]
Description:        Points at the agent hub element
Sample use:         point_at_agent_hub Mission, 2
Class:              POINT_AT_AGENT_HUB
Implemented:        Yes
```

```
Identifier:         point_at_agent_hub
Parameters:         (Agent | Mission), (character name | nth), [circle|square|arrow], [direction]
Description:        Points at the agent hub element
Sample use:         point_at_agent_hub Mission, 2
Class:              POINT_AT_AGENT_HUB
Implemented:        Yes
```

```
Identifier:         point_at_diplomacy_offer
Parameters:         offer id, [circle|square|arrow], scale X,Y
Description:        Points at the offer in the diplomacy panel
Sample use:         point_at_diplomacy_offer, diplomacy_item_map_information
Class:              POINT_AT_DIPLOMACY_OFFER
Implemented:        Yes
```

```
Identifier:         point_at_move_retinue
Parameters:         (Character | Ancillary), character name, [circle|square|arrow]
Description:        Points at the target in move retinue
Sample use:         point_at_move_retinue Character, 2
Class:              POINT_AT_MOVE_RETINUE
Implemented:        Yes
```

```
Identifier:         point_at_strat_position_alt
Parameters:         strategy map position
Description:        separate point_at_strat with different properties
Sample use:         point_at_strat_position_alt, slot 1, 83, 84, y_offset -70
Class:              POINT_AT_STRAT_POSITION_ALT
Implemented:        Yes
```

```
Identifier:         release_music_control
Parameters:         none
Description:        Releases script control over the music, letting it play and transition normally
Sample use:         release_music_control
Class:              RELEASE_MUSIC_CONTROL
Implemented:        Yes
```

```
Identifier:         remove_hidden_resource
Parameters:         region name and resource name
Description:        remove a hidden resource to a given region
Sample use:         remove_hidden_resource Latium sparta
Class:              REMOVE_HIDDEN_RESOURCE
Implemented:        Yes
```

```
Identifier:         rename_settlement_in_region
Parameters:         region name and new settlement name
Description:        rename a settlement to a given name
Sample use:         rename_settlement_in_region Latium "Reme"
Class:              RENAME_SETTLEMENT
Implemented:        Yes
```

```
Identifier:         restrict_battle_movement
Parameters:         (circle, (location <x>, <y>) | (label <label>)
Description:        
Sample use:         
Class:              RESTRICT_BATTLE_MOVEMENT
Implemented:        Yes
```

```
Identifier:         clear_restrict_strat_movement
Parameters:         
Description:        Clear the restricted movement
Sample use:         clear_restrict_strat_movement
Class:              CLEAR_RESTRICT_STRAT_MOVEMENT
Implemented:        Yes
```

```
Identifier:         script_log
Parameters:         the message to be logged
Description:        logs a message to the console/stdout (not the in-game romeshell)
Sample use:         script_log This is a message, use it for logging in scripts.
Class:              FERAL_LOG
Implemented:        Yes
```

```
Identifier:         select_captial
Parameters:         N/A
Description:        selects the player's capital
Sample use:         select_captial
Class:              SELECT_PLAYER_CAPTIAL
Implemented:        Yes
```

```
Identifier:         set_advice_page
Parameters:         <page number>
Description:        Sets the page number of a type D advice panel. Page numbers start at 1.
Sample use:         set_advice_page 2;
Class:              SET_ADVICE_PAGE
Implemented:        Yes
```

```
Identifier:         set_battle
Parameters:         file name
Description:        
Sample use:         
Class:              SET_BATTLE
Implemented:        Yes
```

```
Identifier:         set_label
Parameters:         
Description:        Set a label that can be jumped to with a Goto statement
Sample use:         set_label location
Class:              SET_LABEL
Implemented:        Yes
```

```
Identifier:         set_marriage_allowed
Parameters:         on/off
Description:        Controls if the automatic marriage proposals are triggered at the start of the round
Sample use:         set_marriage_allowed on
Class:              SET_MARRIAGES_ALLOWED
Implemented:        Yes
```

```
Identifier:         set_min_formation_width
Parameters:         <min formation width>
Description:        Sets the minimum width that the player can have their units at.
Sample use:         set_min_formation_width 10;
Class:              SET_MINIMUM_UNIT_WIDTH
Implemented:        Yes
```

```
Identifier:         set_strat_camera_speed
Parameters:         strategy camera speed
Description:        Sets the movement speed of the camera
Sample use:         set_strat_camera_speed 15
Class:              SET_STRAT_CAMERA_SPEED
Implemented:        Yes
```

```
Identifier:         show_annotations
Parameters:         <annotations file>
Description:        Display the annotations file
Sample use:         show_annotations doop
Class:              FERAL_SHOW_ANNOTATIONS
Implemented:        Yes
```

```
Identifier:         show_building_info
Parameters:         N/A
Description:        Trys to show a building info for the currently selected settlement
Sample use:         show_building_info
Class:              SHOW_BUILDING_INFO
Implemented:        Yes
```

```
Identifier:         show_movie
Parameters:         file [file/path], width [uint], height [uint], x [int], y [int]
Description:        Displays a movie
Sample use:         show_movie data/path/to/moviefile path/to/moviewidth 640height 360x 200y 150end_show_movie
Class:              SHOW_MOVIE
Implemented:        Yes
```

```
Identifier:         show_ui_element
Parameters:         ui ID
Description:        Shows a given UI element
Sample use:         show_ui_element faction_button
Class:              SHOW_UI_ELEMENT
Implemented:        Yes
```

```
Identifier:         show_unit_info
Parameters:         N/A
Description:        Trys to show a unit's info for the currently selected settlement
Sample use:         show_unit_info
Class:              SHOW_UNIT_INFO
Implemented:        Yes
```

```
Identifier:         snap_to_settlement
Parameters:         settlement name
Description:        Snaps camera position to a settlement
Sample use:         snap_to_settlement Rome
Class:              SNAP_TO_SETTLEMENT
Implemented:        Yes
```

```
Identifier:         spawn_character_child
Parameters:         faction, age, birth_season, father, name, surname
Description:        Spawns a new character with given parameters and a given father
Sample use:         spawn_character_child romans_julii, age 15, birth_season spring, father Flavius Julius, name Gnaeus, surname Julius
Class:              SPAWN_CHARACTER_CHILD
Implemented:        Yes
```

```
Identifier:         start_benchmark
Parameters:         name
Description:        Starts logging frametime benchmark data
Sample use:         start_benchmark campaign
Class:              FERAL_START_BENCHMARK
Implemented:        Yes
```

```
Identifier:         stop_all_point_at_indicators
Parameters:         
Description:        
Sample use:         
Class:              STOP_ALL_POINT_INDICATORS
Implemented:        Yes
```

```
Identifier:         stop_point_at_indicator
Parameters:         
Description:        
Sample use:         
Class:              STOP_POINT_AT_INDICATOR
Implemented:        Yes
```

```
Identifier:         strat_selection_unblocker
Parameters:         Settlement|Character, On|Off, Settlement/Character name
Description:        Adds the given character/settlement to a list of selectable items on the strat map. All units are unblocked by default until the first is added with this command - then they're all blocked.
Sample use:         strat_selection_unblocker settlement on Ariminum
Class:              STRAT_SELECTION_UNBLOCKER
Implemented:        Yes
```

```
Identifier:         toggle_minimap
Parameters:         
Description:        Toggles the top-right map in the strat view.
Sample use:         toggle_minimap;
Class:              TOGGLE_MAP
Implemented:        Yes
```

```
Identifier:         trigger_marriage_proposal
Parameters:         
Description:        Triggers a marriage proposal for a player.
Sample use:         trigger_marriage_proposal
Class:              TRIGGER_MARRIAGE_PROPOSAL
Implemented:        Yes
```

```
Identifier:         ui_card_selection_lock
Parameters:         on/off
Description:        Switches the ability to select/deselect unit cards.
Sample use:         ui_card_selection_lock on;
Class:              UI_CARD_SELECTION_LOCK
Implemented:        Yes
```

```
Identifier:         unit_group_automate_attack
Parameters:         group_label enemy_unit_label
Description:        Instructs an automated unit group to attack a specified enemy unit
Sample use:         unit_group_automate_attack enemy_unit
Class:              UNIT_GROUP_AUTOMATE_ATTACK
Implemented:        Yes
```

```
Identifier:         unit_group_automate_defend_position
Parameters:         group_label location radius
Description:        Instructs an automated unit group to defend position
Sample use:         unit_group_automate_defend_position 106 -56 75
Class:              UNIT_GROUP_AUTOMATE_DEFEND_POSITION
Implemented:        Yes
```

```
Identifier:         unit_order_move_to_orientation
Parameters:         unit_label x y width_in_men rotation_in_degrees run (optional)
Description:        orders the specified unit to move to the specified position with a specified rotation and orientation
Sample use:         unit_order_move_to_orientation cohort1 100 60 20 45 run
Class:              UNIT_ORDER_MOVE_TO_ORIENTATION
Implemented:        Yes
```

```
Identifier:         while_not
Parameters:         conditions to satisfy to execute this while
Description:        start a while loop
Sample use:         while_not TimerElapsed < 1000
Class:              WHILE_NOT
Implemented:        Yes
```

## Modified Conditions

The following commands have been added updated or extended for the Remaster:

```
Identifier:         hide_all_revealed_tiles
Parameters:         
Description:        restore all tile shrouds
Sample use:         hide_all_revealed_tiles
Class:              HIDE_ALL_REVEALED_TILES
Implemented:        Yes
```

```
Identifier:         play_sound_event
Parameters:         <event id> [<index>] [tag = <something>] [ignore_volume_prefs]
Description:        Plays sound event
Sample use:         play_sound_event PREBATTLE_TEST
Class:              PLAY_SOUND_EVENT
Implemented:        Yes
```

```
Identifier:         reveal_tile
Parameters:         strategy map position
Description:        remove the shroud from the tile
Sample use:         reveal_tile 25, 43
Class:              REVEAL_TILE
Implemented:        Yes
```

```
Identifier:         select_ui_element
Parameters:         element id (see available_ui_element_ids.txt for appropriate identifiers)
Description:        Use in conjunction with simulate mouse click to store the element that will next recieve the simulated mouse click
Sample use:         select_ui_element hud_show_buildings_tab
			  simulate_mouse_click lclick_down
Class:              SELECT_ELEMENT
Implemented:        Yes
```

```
Identifier:         set_music_state
Parameters:         tension, mobilize, battle or custom
Description:        Sets the music state in the battle
Sample use:         set_music_state mobilize
Class:              SET_MUSIC_STATE
Implemented:        Yes
```

```
Identifier:         simulate_mouse_click
Parameters:         [lclick_down|lclick_up|rclick_down|rclick_up|ldbl_click]
Description:        Acts as if the given mouse event had happened on the currently 'selected' ui_element (see 'select_ui_element' command)
Sample use:         select_ui_element hud_show_buildings_tab
			  simulate_mouse_click lclick_down
Class:              SIMULATE_MOUSE_CLICK
Implemented:        Yes
```

## Full List of Conditions

* [docudemon_commands.txt](/documentation/feature_guides/scripts/docudemon_commands.txt)

![Workshop_header_template](/Workshop_header_template.png)
# feral_descr_ai_personality.txt

## Table Of Contents

* [Introduction](#introduction)
   * [Overall Personality Definition Format](#overall-personality-definition-format)
   * [Example of feral_descr_ai_personality.txt](#example-of-feral_descr_ai_personalitytxt)
   * [Building Priorities](#building-priorities)
      * [building_priority](#building_priority)
      * [population_growth_bonus](#population_growth_bonus)
      * [population_loyalty_bonus](#population_loyalty_bonus)
      * [population_health_bonus](#population_health_bonus)
      * [trade_base_income_bonus](#trade_base_income_bonus)
      * [trade_level_bonus](#trade_level_bonus)
      * [trade_fleet](#trade_fleet)
      * [taxable_income_bonus](#taxable_income_bonus)
      * [mine_resource_level](#mine_resource_level)
      * [farming_level](#farming_level)
      * [road_level](#road_level)
      * [gate_strength](#gate_strength)
      * [gate_defenses](#gate_defenses)
      * [wall_level](#wall_level)
      * [tower_level](#tower_level)
      * [stage_games](#stage_games)
      * [stage_races](#stage_races)
      * [weapon_bladed](#weapon_bladed)
      * [weapon_missile](#weapon_missile)
      * [armour](#armour)
      * [population_fire_risk_bonus](#population_fire_risk_bonus)
      * [bodyguard](#bodyguard)
      * [recruits_morale_bonus](#recruits_morale_bonus)
      * [recruits_experience_bonus](#recruits_experience_bonus)
      * [happiness_bonus](#happiness_bonus)
      * [law_bonus](#law_bonus)
   * [Military Priorities](#military-priorities)
      * [military_priority](#military_priority)
      * [mass](#mass)
      * [infantry_light](#infantry_light)
      * [infantry_heavy](#infantry_heavy)
      * [infantry_missile](#infantry_missile)
      * [infantry_spearmen](#infantry_spearmen)
      * [cavalry_light](#cavalry_light)
      * [cavalry_heavy](#cavalry_heavy)
      * [cavalry_missile](#cavalry_missile)
      * [siege_artillery](#siege_artillery)
      * [special](#special)
      * [sally_agression](#sally_agression)
      * [sally_desperate](#sally_desperate)
      * [attack_risk_taker](#attack_risk_taker)
      * [subterfuge_risk_taker](#subterfuge_risk_taker)
   * [Diplomatic Priorities](#diplomatic-priorities)
      * [diplomatic_priority](#diplomatic_priority)
      * [aggresiveness](#aggresiveness)

## Introduction

This is a new addition for Rome Remastered. This file allows you to modify the different in-game personalities for building, military and diplomatic aspects and create overall personalities that can be mapped onto factions.


### Overall Personality Definition Format

The personalities you assign the factions are made up of three parts:

* Building Priorities - Impact the choices made inside settlements.
* Miltary Priorities - Impact recuitment & military decisions.
* Diplomatic Priorities - Impacts the AI's aggresiveness.

These three options are then combined into an overall personality that you can then assign to a faction. This is formatted in the following manner.

```
personality balanced_smith
building_priority Balanced
military_priority smith
diplomatic_priority default
```

* personality - Give this personality combination a unique name
* building_priority - Select a personality from the existing building_priority options.
* military_priority - Select a personality from the existing military_priority options.
* diplomatic_priority - Select a personality from the existing diplomatic_priority options.

The existing personalties can be found at the bottom of the file.

There are currently 27 different personalities and the number of personalities is no longer limited as of the 2.0.4 update.

### Example of feral_descr_ai_personality.txt
Below contains a single example of all 4 parts of the personality system.

```
;;; Building Priorities

building_priority Balanced
population_growth_bonus 80
population_loyalty_bonus 64
population_health_bonus 32
trade_base_income_bonus 32
trade_level_bonus 64
trade_fleet 48
taxable_income_bonus 80
mine_resource_level 16
farming_level 48
road_level 48
gate_strength 16
gate_defenses 16
wall_level 64
tower_level 16
stage_games 48
stage_races 48
weapon_bladed 32
weapon_missile 32
armour 32
population_fire_risk_bonus 16
bodyguard 48
recruits_morale_bonus 32
recruits_experience_bonus 64
happiness_bonus 48
law_bonus 48

;;; Military Priorities

military_priority smith
mass 64
infantry_light 64
infantry_heavy 64
infantry_missile 64
infantry_spearmen 64
cavalry_light 64
cavalry_heavy 64
cavalry_missile 64
siege_artillery 64
special 64
sally_agression 15
sally_desperate 80
attack_risk_taker 2
subterfuge_risk_taker 1

;;; Diplomatic Priorities

diplomatic_priority default
aggresiveness 100

;;; Personalities

personality balanced_smith
building_priority Balanced
military_priority smith
diplomatic_priority default

```

### Building Priorities
Below you can find an explaination of what all the different variables do inside the building priorties personality.

#### building_priority
Overall personalities are the things connected to factions and building priorities aren't used alone but as part of an overall personality.

Inside the default file you'll find the following personalities. There are 8 different default personalities.

* Balanced
* Trader
* Religious
* Comfortable
* Bureaucrat
* Craftsman
* Sailor
* Fortified

**NOTE** The buildings linked to each priority can be found in the export_descr_buildings.txt file.

#### population_growth_bonus
How much importance the AI puts on constructing buildings with a population growth bonus. The higher the value the more likely they are to priortise a building with this bonus.

Stored as an int32 value so you can set this value at high levels. However the values are all compared against each other so the key is to balance the ratio between all the various options to match the AI recruitment style you'd like to see.

#### population_loyalty_bonus
How much importance the AI puts on constructing buildings with a population loyalty bonus. The higher the value the more likely they are to priortise a building with this bonus.

Stored as an int32 value so you can set this value at high levels. However the values are all compared against each other so the key is to balance the ratio between all the various options to match the AI recruitment style you'd like to see.

#### population_health_bonus
How much importance the AI puts on constructing buildings with a health bonus. The higher the value the more likely they are to priortise a building with this bonus.  

Stored as an int32 value so you can set this value at high levels. However the values are all compared against each other so the key is to balance the ratio between all the various options to match the AI recruitment style you'd like to see.

#### trade_base_income_bonus
How much importance the AI puts on constructing buildings which provide a base trade income bonus. The higher the value the more likely they are to priortise a building with this bonus.

Stored as an int32 value so you can set this value at high levels. However the values are all compared against each other so the key is to balance the ratio between all the various options to match the AI recruitment style you'd like to see.  

#### trade_level_bonus
How much importance the AI puts on constructing buildings which provide a percentage bonus to the trade income. The higher the value the more likely they are to priortise a building with this bonus.  

Stored as an int32 value so you can set this value at high levels. However the values are all compared against each other so the key is to balance the ratio between all the various options to match the AI recruitment style you'd like to see.

#### trade_fleet
How much importance the AI puts on constructing and upgrading ports. The higher the value the more likely they are to priortise building ports.

Stored as an int32 value so you can set this value at high levels. However the values are all compared against each other so the key is to balance the ratio between all the various options to match the AI recruitment style you'd like to see.

#### taxable_income_bonus
How much importance the AI puts on constructing buildings which provide a bonus to the taxable income. The higher the value the more likely they are to priortise a building with this bonus.

Stored as an int32 value so you can set this value at high levels. However the values are all compared against each other so the key is to balance the ratio between all the various options to match the AI recruitment style you'd like to see.  

#### mine_resource_level
How much importance the AI puts on constructing and upgrading mines. The higher the value the more likely they are to priortise building mines.

Stored as an int32 value so you can set this value at high levels. However the values are all compared against each other so the key is to balance the ratio between all the various options to match the AI recruitment style you'd like to see.

#### farming_level
How much importance the AI puts on constructing and upgrading farms. The higher the value the more likely they are to priortise building farms.

Stored as an int32 value so you can set this value at high levels. However the values are all compared against each other so the key is to balance the ratio between all the various options to match the AI recruitment style you'd like to see.

#### road_level
How much importance the AI puts on constructing and upgrading roads. The higher the value the more likely they are to priortise building roads.

Stored as an int32 value so you can set this value at high levels. However the values are all compared against each other so the key is to balance the ratio between all the various options to match the AI recruitment style you'd like to see.

#### gate_strength
How much importance the AI puts on improving a settlments gate strength. The higher the value the more likely they are to priortise building or upgrading walls if they will also upgrade the gates strength value.

Stored as an int32 value so you can set this value at high levels. However the values are all compared against each other so the key is to balance the ratio between all the various options to match the AI recruitment style you'd like to see.
#### gate_defenses
How much importance the AI puts on improving a settlments gate defences. The higher the value the more likely they are to priortise building or upgrading walls if they will also upgrade the gates defence stats.

Stored as an int32 value so you can set this value at high levels. However the values are all compared against each other so the key is to balance the ratio between all the various options to match the AI recruitment style you'd like to see.
#### wall_level
How much importance the AI puts on improving a settlments wall level. The higher the value the more likely they are to priortise building or upgrading walls.

Stored as an int32 value so you can set this value at high levels. However the values are all compared against each other so the key is to balance the ratio between all the various options to match the AI recruitment style you'd like to see.
#### tower_level
How much importance the AI puts on creating or improving a settlments tower defences. The higher the value the more likely they are to priortise building or upgrading walls if they will also upgrade or create towers.

Stored as an int32 value so you can set this value at high levels. However the values are all compared against each other so the key is to balance the ratio between all the various options to match the AI recruitment style you'd like to see.
#### stage_games
How much importance the AI puts on constructing buildings that allow for games. The higher the value the more likely they are to priortise them.

Stored as an int32 value so you can set this value at high levels. However the values are all compared against each other so the key is to balance the ratio between all the various options to match the AI recruitment style you'd like to see.
#### stage_races
How much importance the AI puts on constructing buildings that allow for races. The higher the value the more likely they are to priortise them.

Stored as an int32 value so you can set this value at high levels. However the values are all compared against each other so the key is to balance the ratio between all the various options to match the AI recruitment style you'd like to see.
#### weapon_bladed
How much importance the AI puts on constructing or upgrading buildings that allow for recuitment of infantry units. The higher the value the more likely they are to priortise these buildings.

Stored as an int32 value so you can set this value at high levels. However the values are all compared against each other so the key is to balance the ratio between all the various options to match the AI recruitment style you'd like to see.
#### weapon_missile
How much importance the AI puts on constructing or upgrading buildings that allow for recuitment of missle units. The higher the value the more likely they are to priortise these buildings.

Stored as an int32 value so you can set this value at high levels. However the values are all compared against each other so the key is to balance the ratio between all the various options to match the AI recruitment style you'd like to see.
#### armour
How much importance the AI puts on constructing or upgrading buildings that will upgrade units armour. The higher the value the more likely they are to priortise these buildings.

Stored as an int32 value so you can set this value at high levels. However the values are all compared against each other so the key is to balance the ratio between all the various options to match the AI recruitment style you'd like to see.
#### population_fire_risk_bonus
Not currently used in rtw
#### bodyguard
How much importance the AI puts on constructing or upgrading buildings that will allow you to recuit a generals bodyguard. The higher the value the more likely they are to priortise these buildings.

Stored as an int32 value so you can set this value at high levels. However the values are all compared against each other so the key is to balance the ratio between all the various options to match the AI recruitment style you'd like to see.
#### recruits_morale_bonus
How much importance the AI puts on constructing or upgrading buildings that will give new recruits a morale bonus. The higher the value the more likely they are to priortise these buildings. For example the Temple of Battle

Stored as an int32 value so you can set this value at high levels. However the values are all compared against each other so the key is to balance the ratio between all the various options to match the AI recruitment style you'd like to see.

#### recruits_experience_bonus
Not in use in base game but would increase the importance of constructing or upgrading buildings that add an experience bonus to new recruits

Use can be modded in as the code is in place for it to work

Stored as an int32 value so you can set this value at high levels. However the values are all compared against each other so the key is to balance the ratio between all the various options to match the AI recruitment style you'd like to see.

#### happiness_bonus
How much importance the AI puts on constructing or upgrading buildings that increase happiness. The higher the value the more likely they are to priortise these buildings.

Stored as an int32 value so you can set this value at high levels. However the values are all compared against each other so the key is to balance the ratio between all the various options to match the AI recruitment style you'd like to see.
#### law_bonus
How much importance the AI puts on constructing or upgrading buildings that increase law. The higher the value the more likely they are to priortise these buildings.

Stored as an int32 value so you can set this value at high levels. However the values are all compared against each other so the key is to balance the ratio between all the various options to match the AI recruitment style you'd like to see.

### Military Priorities
Below you can find an explaination of what all the different variables do inside the building priorties personality.

#### military_priority
Overall personalities are the things connected to factions and building priorities aren't used alone but as part of an overall personality.

Inside the default file you'll find the following personalities. There are 7 different default personalities.

* smith
* mao
* genghis
* stalin
* napoleon
* henry
* caesar


#### mass
How much importance the AI puts on recuiting units with more soliders. This can be useful if you want the AI to recuit large sized units to keep the population down.

Stored as an int32 value so you can set this value at high levels. However the values are all compared against each other so the key is to balance the ratio between all the various options to match the AI recruitment style you'd like to see.
#### infantry_light
How much importance the AI puts on recuiting light infantry units.

Stored as an int32 value so you can set this value at high levels. However the values are all compared against each other so the key is to balance the ratio between all the various options to match the AI recruitment style you'd like to see.
#### infantry_heavy
How much importance the AI puts on recuiting heavy infantry units.

Stored as an int32 value so you can set this value at high levels. However the values are all compared against each other so the key is to balance the ratio between all the various options to match the AI recruitment style you'd like to see.
#### infantry_missile
How much importance the AI puts on recuiting missile units.

Stored as an int32 value so you can set this value at high levels. However the values are all compared against each other so the key is to balance the ratio between all the various options to match the AI recruitment style you'd like to see.
#### infantry_spearmen
How much importance the AI puts on recuiting spearmen units.

Stored as an int32 value so you can set this value at high levels. However the values are all compared against each other so the key is to balance the ratio between all the various options to match the AI recruitment style you'd like to see.
#### cavalry_light
How much importance the AI puts on recuiting light cavalry units.

Stored as an int32 value so you can set this value at high levels. However the values are all compared against each other so the key is to balance the ratio between all the various options to match the AI recruitment style you'd like to see.
#### cavalry_heavy
How much importance the AI puts on recuiting heavy cavalry units.

Stored as an int32 value so you can set this value at high levels. However the values are all compared against each other so the key is to balance the ratio between all the various options to match the AI recruitment style you'd like to see.
#### cavalry_missile
How much importance the AI puts on recuiting missile cavalry units.

Stored as an int32 value so you can set this value at high levels. However the values are all compared against each other so the key is to balance the ratio between all the various options to match the AI recruitment style you'd like to see.
#### siege_artillery
How much importance the AI puts on recuiting siege artillery.

Stored as an int32 value so you can set this value at high levels. However the values are all compared against each other so the key is to balance the ratio between all the various options to match the AI recruitment style you'd like to see.
#### special
How much importance the AI puts on recuiting faction special units.

Stored as an int32 value so you can set this value at high levels. However the values are all compared against each other so the key is to balance the ratio between all the various options to match the AI recruitment style you'd like to see.
#### sally_agression
How likely is a besieged garrison to sally when understrength. (0-100)
#### sally_desperate
How likely is a besieged garrison to sally in desperation when the settlement is about to surrender. (0-100)
#### attack_risk_taker
How likely it is for this faction to invade regions. (0-4)

* 0 = STAY_AT_HOME Never invades regions (eg. the senate)
* 1 = MINIMAL AI will attempt to allocate army with x0.5 of enemy region strength
* 2 = SOLID will attempt to allocate army with x1 of enemy region strength
* 3 = STRONG will attempt to allocate army with 2 of enemy region strength
* 4 = OVERWHELM  will attempt to allocate army with 4 of enemy region strength

Allocating a larger army to attack will mean leaving your own settlments less defended. It also means the AI will go for sudden overwhelming attacks instead of wearing down enemies with multiple smaller attacks.

#### subterfuge_risk_taker
How likely the AI will be to take risks when assigning subterfuge missions. (0-7)

### Diplomatic Priorities
Below you can find an explaination of what all the different variables do inside the building priorties personality.

#### diplomatic_priority
default

#### aggresiveness
How likely the AI will be to want war. This has a small effect and is mostly driven by all the other factors in the AI chain. There are 4 possible levels of modifier, these are triggered at 25, 50 & 75. By default all the factions have a value of 100 (maximum aggresiveness)

**NOTE** The `aggresiveness` variable has a typo that you should keep when modding!

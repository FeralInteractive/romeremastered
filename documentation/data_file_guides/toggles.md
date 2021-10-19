![Workshop_header_template](/Workshop_header_template.png)
# toggles - Classic vs Remastered

## Table Of Contents

* [Introduction](#introduction)
   * [toggle button states.txt](#toggle-button-statestxt)
   * [Individual Toggle Files](#individual-toggle-files)
      * [ai improvements.txt](#ai-improvementstxt)
      * [battle.txt](#battletxt)
      * [camera.txt](#cameratxt)
      * [campaign.txt](#campaigntxt)
      * [diplomacy.txt](#diplomacytxt)
      * [end turn.text](#end-turntext)
      * [population balancing.txt](#population-balancingtxt)
      * [trade.txt](#tradetxt)
      * [unit balancing.txt](#unit-balancingtxt)

## Introduction

This is a new addition for Rome Remastered. These files allows you to:

* Control if players can chnage between Classic and Remastered toggles.
* Set the default settings for each of the in game toggles.
* Provide finer grained control of individual features linked to the toggles.

All of the toggle features are controlled using files found in the 'toggles' folder. Replicating the folder structure in a mod allows you to restrict players options for your mod. For example if your mod is designed to use specific features you can enable these and disable the players ability to change the settings inside the game UI.

See below for further details on the individual files.

### toggle button states.txt

This is the master file that sets what toggles a user can alter in game and what each toggle will default to. It uses the following format:

```
// This file controls the overall toggles (the ones you can control through the UI)
// "Enabled" controls whether the user is able to change between Classic and Remastered
// "Default" controls which state the toggle will be set to by default (Classic = 0, Remastered = 1)

unit balancing
enabled :: 1
default :: 1
```

### Individual Toggle Files

For each toggle there are two identically named files. One will be in the classic folder the other in the remastered folder. These files determine what individual features are enabled or disabled when the toggle in is Classic and Remastered modes.

For the base game classic has all the individual features disabled and remastered has them all enabled however you can manipulate these how you like below.

* 0 = Feature Disabled
* 1 = Feature Enabled

#### ai improvements.txt
* **improved ai** - Use Rome Remastered campaign AI.
* **improved battle ai** - Use Rome Remastered campaign AI.

#### battle.txt
* **autoresolve improvements** - Use Rome Remastered Auto-resolve logic improvements
* **romano-british units** -
* **night battles** - Allow night battles in Rome
* **unlimited men** -
* **rain affects flames** - Rain effects flaming arrows effectiveness
* **improved routing** -
* **misc battle improvements** -
* **friendly spear passthrough** - Allow friendly units pass through spears
* **reduce collider climbing walls** -
* **elephant collision** -
* **reorder unit group** -
* **enhanced locked group attack** -

#### camera.txt
* **modern camera** - Use the modern camera controls. (Users can chnage this)

#### campaign.txt
* **squalor effects** - Limit maximum squalor impact
* **barb bonuses** -
* **upkeep costs** - Charge units to the global treasury instead of indivudal settlments for easier ability to view settlments finances.  
* **construction costs** -
* **slave distribution** - Distribute slaves evenly over the entire empire not just the ones with governers.
* **ambushes** - Increase ambush area of effect from a single tile to a 3x3 grid surrounding the unit.
* **tavern changes** - Add bonus to taverns to help barbarian factions with settlement stability.
* **improved historical disasters** -
* **normalised disaster radius** - Damage casued by natural disasters have a normalised radius of effect.
* **base or bi storms** - Use updated storms from BI with lightning etc
* **disaster tail off** -
* **mercenary retraining** - Allow Mercs to be retrained.
* **edit automanaged settlement** -
* **blockaded navy** -
* **settlement condition** -
* **remastered education** - Use improved balancing of edutcation bonuses to make academies more worthwhile.
* **gradual trait loss** - Traits will gradually improve/worsen instead of flip flopping. With this enabled failing a negotation will no longer cause a diplomat to have a trait go from +3 to -1 instead it will change gradually by a single stage per trigger.
* **dismissable agents** - Allow agents to be dismissed.

#### diplomacy.txt
* **protectorate** - Use imprpved protectorate logic
* **improved diplomacy** - Use improved diplomacy logic

#### end turn.text
* **end_turn** -

#### population balancing.txt
* **normalised pop reduction** - The number of people needed when recruiting units from a settlement is normalised so the number taken from the population uses the number linked to the "medium" aka Normal unit size. This prevents issues when playing on larger unit sizes where the popuation would be too low due to extra amount needed to recuit units. This has a knock on effect that means AI controlled factions on larger unit sizes tend to not develop their settlements have have low tier units even into the end game.

#### trade.txt
* **merchants** - Enable Merchants
* **embargo** - Enable Trade Embargos
* **resource_quantity** - Combine duplicate resources in the same region into a single resource with combined value. This is useful for merchants.
* **trade_anywhere** - Allow merchants to earn money when they are in a region. They only need to trade in Settlements or Resources to gain the addional bonuses those behaviours bring.

#### unit balancing.txt
* **unit_balancing** -
* **hiding general** -

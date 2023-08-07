![Workshop_header_template](/Workshop_header_template.png)
# Battle and Campaign Formulae

## Table Of Contents

   * [Introduction](#introduction)
   * [Battle Calculations and Bonuses](#battle-calculations-and-bonuses)
		* [Generals Bodyguard Size](#generals-bodyguard-size)
		* [Generals Battle Bonuses](#generals-battle-bonuses)
		* [Chanting and Screeching Bonuses](#chanting-and-screeching-bonuses)
		* [Warcry and Berserk Bonuses](#warcry-and-berserk-bonuses)
  		* [Hiding Bonuses](#hiding-bonuses)	
		* [Battle Difficulty Bonuses](#battle-difficulty-bonuses)
		* [Experience Chevrons](#experience-chevrons)
		* [Eagle Units](#eagle-units)
		* [Fear Effects](#fear-effects)
		* [Hiding Bonuses](#hiding_bonuses)
   * [Campaign Calculations and Bonuses](#campaign-calculations-and-bonuses)
		* [Campaign Difficulty bonuses](#campaign-difficulty-bonuses)
		* [Distance To Capital Penalty](#distance_to_capital_penalty)


This page is a collection of information about battle and campaign formulae used inside the battle and campaign engine. 

## Battle Calculations and Bonuses

In this subsection we have a number of bits of information on how the game logic calculates bonuses and unit sizes. These cannot be modded but can be useful when modding units to ensure good overall balance.

### Generals Bodyguard Size

The bodyguard calculation gives the size of the unit before the unit scale modifier is applied.

 1. Start with the default bodyguard unit size. This is defined in the EDU, in the example below the starting value will be `12`.
 
```
type             roman generals guard cavalry early
dictionary       roman_generals_guard_cavalry_early      ; Roman General
category         cavalry
class            heavy
voice_type       Heavy_1
voice_indexes    0 1 2
soldier          roman_medium_cavalry, 12, 0, 1
mount            generals horse
```

 2. Add `+6` if it's the faction leader
 3. Add `+4` if it's the faction heir
 4. Add half of the character's influence start, rounded down
 5. Add the character's `PersonalSecurity` stat
 7. Clamp resulting number between `4` and `31`
 8. Multiply the resulting value by the unit scale factor to get the final unit size

NOTE: The General and other officers (i.e. centurions and standard bearers in legionary cohorts) aren't counted towards this number.

### Generals Battle Bonuses

Your General will give all your units some bonuses to their morale, they don't impact any of the other stats. These bonuses are as follows:

 * The general gives `+12` morale to their bodyguard unit while they're rallying, and `+8` at all other times. This is on top of the base value below.
 * The general gives nearby units `+10` morale when they are rallying and `+4` at all other times. This is on top of the base value below.
 * As long as the general is alive, all units on the field no matter how far from the general get a base morale bonus of `2 + command points + half influence + TroopMorale stat`.
 * The range of influence of a General is calculated using the following formula `6 + (7 * command) + (4 * influence)`. The number is using the internal engine distance this should be assumed to be similar to meters inside the game world.
 * Units can only be influenced by the general that is in command of their army. Killing any secondary generals or generals in reinforcing armies will have no effect on the main army beyond removing the +8 morale bonus given to bodyguard units at all time listed above
 
Extra information about General's influence range: 
 
 * Being near a general makes a broken unit rally sooner than they would otherwise
(assuming it's possible for them to rally).
 * Units that can charge without orders won't do so if they're near the general.
 * A General's rallying buff will be combined with any separate chanting and screeching bonuses that are within the same range.
 
### Chanting and Screeching Bonuses


 * Being in range of friendly chanting grants `+6` morale, being in range of enemy chanting gives `-5`.
 * Being in range of friendly  screeching will grant `+3`  morale, being in range of enemy screeching gives `-5`.
 * Chanting takes priority over screeching if both are active by the same side.
 * You cannot stack multiple bonuses at once, only a single one will count for any specific unit. For example if you trigger 2x Chanting and 1x Screeching units within the range of a 4th unit that unit will only ever get a single buff at once.
 * If both factions have buff's running at once both the positive and negative values are calculated for units in the area of influence.
 * The units doing the chanting/screeching **do not get the bonus from the action*** only units around them.
 * Units with chanting or screeching abilities **can still get the bonus from other units*** if they are within range they just cannot buff themselves.
 * If multiple buffs are within range and one of them runs out the game will switch to the next best buff to apply automatically. 
 * Neither of these bonuses effect anything other than morale.
 * Both effects have a range of 75 using the internal engine distance this should be assumed to be similar to meters inside the game world.
 
 * If a unit has more friendly chanting units influencing it than enemy chanting units, it gains a +2 to hit
 * If a unit has more enemy screeching units influencing it than friendly screeching units, it gains a -2 to hit
 
 For example:
 
 * If your unit is chanting and they are within range of an enemy unit screeching your units overall buff is +1 (+6-5) and theirs will be -2 (+3-5).
 * Having two monk units on the same side chanting next to each other will give surrounding units a single buff from chanting but they will also additionally buff each others stats. This means although the bonus doesn't stack you can use multiple units to ensure even the unit chanting has an active buff to morale.
 * If a unit is within range of 3 friendly screeching units, and 2 enemy screeching units, it's chance to hit will not suffer the -2 debuff due to having more friendly screeching units than enemies
 
 ### Warcry and Berserk Bonuses
 
 Warcry and Berserk bonuses don't have any bonuses to nearby units and only impact their own stats. Both of these features impact the default recovery time for a unit. 
 
  * The recovery time is stored in the EDU in the `stat_pri` and `stat_sec` values. They are the second to last numbers on those lines.
  * This represents the number of deciseconds (10ths of a second) that units will take, on average, between attacks.
  * When a soldier makes an attack, they will add a random number between -5 to +5 to the base stat and wait that long before making another attack
  
  * If a unit is berserk, the stat is reduced to 25% of it's original value
  
  * Warcry can reduce the stat by between 40% to 100% depending on how long the warcry is allowed to charge up
  * After starting a unit's warcry ability, they will begin to taunt and a counter will begin to increment in the background
  * If a unit is attacked, ordered to move, or otherwise have their taunting interrupted, the counter will remain frozen at wherever it was
  * After 2.8 seconds of charging the attack rate bonus will become active at a 40% reduction in the base stat
  * Between 2.8 seconds and 7 seconds the bonus will ramp up to 100%, and will remained capped there. Any additional charge time will have no effect
  * After 40 seconds the effects of warcry will end immediately

### Hiding Bonuses

Some units have the ability to hide in woods or long grass. Those units (beyond not being visible to enemy units until they get close) have the following modifers on morale.

  * +4 morale when hiding
  * -7 morale for enemy units for 60 seconds, this is triggered when the unit comes out of hiding near an enemy. However the following requirements need to be true:
    * Enemy unit needs to be within 80 in game meters of your unit when you come out of hiding.
    * Enemy unit needs to be facing away from the unit when they come out of hiding.

### Battle Difficulty Bonuses

When playing on different difficulty settings for battles **enemy** units get the following additional chance to hit when attacking another unit

```
Easy:    -6
Normal:  +0
Hard:    +4
Extreme: +7
```

This means on higher difficulties enemy units will have an easier time hitting and dealing damage to enemies

### Experience Chevrons

Experience effects both the attack strength and the accuracy of the attacks. 

#### Chance to hit bonus

When a unit receives an attack, the change of the attack to hit and deal damage is calculated based on the difference in experience between the two units

The modifier is calculated by using the following formula and looking up the result in the table below

Formula: `9 + (attacker's experience - defender's experience)`

| -9 | -8 | -7 | -6 | -5 | -4 | -3 | -2 | -1 | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|----|----|----|----|----|----|----|----|----|---|---|---|---|---|---|---|---|---|---|
| -6 | -5 | -4 | -4 | -3 | -3 | -2 | -2 | -1 | 0 | 1 | 2 | 2 | 3 | 3 | 4 | 4 | 5 | 6 |

Having more experience will therefore not only increase the chance to hit of a unit, but also lessen the bonus that more experienced units get against that unit

Note that if the attack is made by a non-unit entity (i.e. a gatehouse pouring boiling oil or a tower shooting an arrow) the experience of the attacker is assumed to be 0

#### Missile Accuracy

 * When calculating the angle to fire at for ranged units, the game applies an offset of up to 0.45 to the desired angle
 * For every bar of experience, this offset is reduced by 0.05
 * This means that units with 9 chevrons of experience will be able to perfectly hit what they're aiming at
 * Note that the above chance to hit table still applies when a missile hits something (except in the case of seige engine projectiles i.e. onagers), so ranged units with more experience are not only more likely to hit what they're aiming at, but also more likely to actually deal damage to whatever they hit

### Eagle Units

 * Eagle units have a `+4` morale boost to the all friendly units within the area of influence.
 * Similar to monks the morale boost is only effective on other units not themselves.
 * You cannot stack multiple Eagle bonuses at once, only a single one will count for any specific unit. You can however have a unit gain a bonus from an Eagle and Chanting or Screeching at the same time.
 * The effect has a range of 75 using the internal engine distance this should be assumed to be similar to meters inside the game world.
 
### Fear Effects

When a unit has a modifier that means they are afraid of a certain type of unit this is calculated in the following manner.

 * The fear will impact the units morale value.
 * The modifier increases depending on the number of units nearby.
   * 1 unit:          -4 morale
   * 2 units:         -6 morale
   * 3 or more units: -8 morale
 * Multiple units of the same type can be stacked, you don't need to use separate types of unit to increase the bonus.
 * The effect has a range of 100 using the internal engine distance this should be assumed to be similar to meters inside the game world.

### Formation Bonuses

Some formations have some bonuses, these are:

Wedge: +10 Attack & -5 Defence
Testudo: -10 Attack & +5 Defence
Shield Wall: -10 Defence
Cantabrian Circle: +3 to missile attacks

Horde, Column, Square, Phalanx, Wall and Schiltrom have no Attack or Defence bonuses.
 
## Campaign Calculations and Bonuses

### Campaign Difficulty bonuses

When playing on different difficulty settings for campaign your units get the following morale modifiers.

**Easy:**
  *  -1 population growth
  *  -2 order
  *  no bonus denarii
  * AI soldiers gain experience at the normal rate
  * AI does not hire mercs
  * AI gets brigands at the normal rate
  * human gets brigands at the normal rate
  * human gets 120% tax income
  * human gets 120% farm income
  * human can get up to 20 turns of peace
  * AI gets no bonus to income
  * AI values human regions 0% more
  * brigands are not allowed to attack human settlements

**Normal:**
  *  +0 population growth
  *  +0 order
  *  +200 bonus denarii per round
  * AI soldiers gain experience at the normal rate
  * AI does not hire mercs
  * AI gets brigands at the normal rate
  * human gets brigands at the normal rate
  * human gets 100% tax income
  * human gets 100% farm income
  * human can get up to 10 turns of peace
  * AI gets a bonus to income up to 120% based on number of regions
  * AI values human regions 80% more
  * brigands are not allowed to attack human settlements

**Hard:**
  *  +2 population growth
  *  +2 order
  *  AI soldiers gain experience 2 times faster
  *  +400 bonus denarii per round
  * AI can hire mercs
  * AI gets brigands at the 88% of the normal rate
  * human gets brigands at 112% of the normal rate
  * human gets 92% tax income
  * human gets 92% farm income
  * human can get up to 4 turns of peace
  * AI gets a bonus to income up to 120% based on number of regions
  * AI values human regions 120% more
  * brigands can attack human settlements
 
**Extreme:**
  *  +4 population growth
  *  +6 order
  *  AI soldiers gain experience 3 times faster
  *  +700 bonus denarii per round
  * AI can hire mercs
  * AI gets brigands at the 80% of the normal rate
  * human gets brigands at 120% of the normal rate
  * human gets 85% tax income
  * human gets 85% farm income
  * human can get up to 2 turns of peace
  * AI gets a bonus to income of 120%
  * AI values human regions 300% more
  * brigands can attack human settlements
  
NOTE: `human can get up to [X] turns of peace` means after the human has been at peace for [X] turns the AI will force someone to attack you. This will appear in the Campaign AI log file as `ltgd: invade '%s' set for forced attack on human`

### Distance To Capital Penalty

This explains how the distance to capital penalty is calculated.

First we need to calculate the direct distance between the capital and the settlement we'll call this: `Distance_To_Capital`.

Second we have the `capital distance multiplier` values inside the `descr_cultures.txt` file. This file allows you to define a different modifier per culture. This is a new feature in Rome Remastered. By default this value is set to `1`.

Using these values the penalty is calculated using the following formula:

`(Distance_To_Capital - 10) * capital distance multiplier`

This value is then rounded down to the nearest 5. For example if the formula results in a value of 54 the game would round this down to 50.

This value is then used as the unrest value in the game. In the above example you'd have +50% unrest for this settlement.

**[NOTE]** If you are making a map that is twice as big as the retail map the distances between settlements will also get bigger so it is recommend you look at balancing your modifier so the penalty doesn't get too large on bigger maps. 

You can also make penalties greater for different cultures. For example if you want a greater penalty for barbarian cultures or a lesser one for the roman culture that's now all possible using the `descr_cultures.txt` file.

### Siege Turn Calculations

Below is the calculation to work how how long a settlement can hold out. 

First, take the settlement type to get the base number of turns:

  * Village - 2 Turns
  * Town - 3 Turns
  * Large town - 4 Turns
  * Minor city - 4 Turns
  * Large city - 5 Turns
  * Huge city - 5 Turns

Now take the `wall_level` value then add `+1` then add the result to the value above. 

Finally add governor's management level divided by 3 (rounded down to nearest number)


**NOTE:**

  * If you have no wall the wall_level value is technically  `-1` so the calculation will be `-1 + 1 = 0` so you add nothing to the value.
  * Add -4 if the settlement has plague
  * Forts are hardcoded to have 3 turns when an army is in them


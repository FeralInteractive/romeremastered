![Workshop_header_template](/Workshop_header_template.png)
# descr_mount

### Author: Dagovax

## Table Of Contents

* [Introduction](#introduction)
* [Mount breakdown](#mount-breakdown)
* [Generic](#generic)
   * [Example of a complete mount definition](#example-of-a-complete-mount-definition)
   * [type](#type)
   * [class](#class)   
   * [model](#model)
   * [radius (and x_radius)](#radius-and-x_radius)
   * [height](#height)
   * [mass](#mass)
   * [banner_height](#banner_height)
   * [bouyancy_offset](#bouyancy_offset)
   * [water_trail_effect & water_trail_effect_running](#water-trail-effect-water-trail-effect-running)
* [Horse, camel or elephant specific](#horse-camel-or-elephant-specific)
   * [root_node_height](#root_node_height)
* [Horse and camel specific](#horse-and-camel-specific)
   * [rider_offset](#rider_offset)
* [Elephant, chariot and scorpion cart specific](#elephant-chariot-and-scorpion-cart-specific)
   * [attack_delay](#attack_delay)
* [Elephant specific](#elephant-specific)
   * [dead_radius](#dead_radius)
   * [tusk_z](#tusk_z)
   * [tusk_radius](#tusk_radius)
   * [riders](#riders)
   * [rider_offset](#rider_offset)
* [Chariot and scorpion cart specific](#chariot-and-scorpion-cart-specific)
   * [axle_width](#axle_width)
   * [wheel_radius](#wheel_radius)
   * [pivot_offset](#pivot_offset)
   * [pole_length](#pole_length)
   * [pole_pivot](#pole_pivot)
   * [pole_connect](#pole_connect)
   * [harness_connect](#harness_connect)
   * [attack_delay, scythe_radius & revs_per_attack](#attack_delay-scythe_radius-revs_per_attack)
   * [horse_type](#horse_type)
   * [horses](#horses)
   * [horse_offset](#horse_offset)
   * [riders](#riders)
   * [rider_offset](#rider_offset)
   * [lods](#lods)
   * [lod](#lod)
   * [trail_effect](#trail_effect)
* [Scorpion cart specific](#scorpion-cart-specific)
	* [scorpion_offset](#scorpion_offset)
	* [scorpion_height](#scorpion_height)
	* [scorpion_forward_length](#scorpion_forward_length)
	* [scorpion_reload_ticks](#scorpion_reload_ticks)

## Introduction

The **descr_mount.txt** file defines the mounts that can be used for units, such as elephants, camels, horses and chariots.
For RR, the amount of mounts in this file is practically unlimited. 

## Mount breakdown
To give a better understanding of what all of these lines mean, we are breaking this down per line.

### Example of a complete mount definition

```
type				elephant african
class				elephant
model				elephant_african
radius				5.5
x_radius			1.3
height				3
mass				15
banner_height		1
bouyancy_offset		3
water_trail_effect	elephant_water_trail
water_trail_effect_running  elephant_water_trail
root_node_height	2.52
attack_delay		1
dead_radius			2.5
tusk_z				3.0
tusk_radius			2.0
riders				3
rider_offset		0.0, 1.225, 1.306
rider_offset		0.0, 1.1, 0.5
rider_offset		0, 1.1, -.25
```

## Generic
The following breakdown lines are generic for every mount

### type

*Indicates a new mount type, must be followed by id name string.*

The name of your new mount. This is the reference to this specific mount. This is the name that will be used in EDU and in for example sound files. This must be an unique name.

### class

This is the class of the mount. These classes are hardcoded so you have to choose one from this list:
* **horse**
* **camel**
* **elephant**
* **chariot**
* **scorpion_cart**

Each class has its own unique properties. For example, if you choose the elephant class you can have multiple *riders*. Elephants can also attack gate and walls, while other classes are not able to do that.
A *scorpion_cart* is a chariot with an artillery piece. This is only used in barbarian invasion afaik.

### model

This is a reference to the model id defined in DMB (descr_model_battle).
This applies to all classes but *chariot* and *scorpion_cart*; they have their LODS defined in this file.

### radius (and x_radius)

The collision box of the mount is in the form of an ***Ellipse***. The **radius** property is the *length* (y_radius), and the **x_radius** is the *width*.
You can calculate the perfect collision of the mount by dragging an ellipse arround your mount inside your graphical editor, and setting the ellipse coordinates to 0,0,0 (x,y,z).

You then have the *length* and the *width* of the Ellipse. You can then calculate the **radius** and **x_radius** using the following formula:

* **radius = ellipse length / 2**
* **x_radius = ellipse width / 2**

**Note that the x_radius should always be smaller than the radius. Not having this will result in the mount not having a collision at all.**

### height

The height of the mount in meters. This is used for collision. You can draw a plane in your graphical editor to view the height of your mount.

### mass

Mount mass. If you have a high value here, units being trampled by this mount will fly far away.

### banner_height

This is the height in meters of the banner above your mount.

### bouyancy_offset

This is used to determine how high the water must be above the mount's root node for it to start swimming.

### water_trail_effect & water_trail_effect_running

Display effect for moving through water. Note that the *water_trail_effect_running* was added in RR, and is required for swimming mounts. If you forget this line, the game will crash as soon the mount starts swimming!

## Horse, camel or elephant specific
The following breakdown lines are specifically for horses, camels and elephants.

### root_node_height

Height of the horse, camel or elephants root node above the ground. Tt just adds itself to the y component of the rider offset
before it gets rotated, so it's probably to allow for X/Z rotation without it looking weird.

## Horse and camel specific
The following breakdown lines are specifically for horses and camels.

### rider_offset
(x, y, z) for the rider relative to horse or camel root node

## Elephant, chariot and scorpion cart specific
The following breakdown lines are specifically for elephants, chariots and scorpion carts.

### attack_delay
Delay between mount attacks (tusks and scythes) in seconds

## Elephant specific
The following breakdown lines are for elephants only.

### dead_radius
Radius of dead obstacle (so when this mount is dead)

### tusk_z
Distance along the z axis of tusks from centre

### tusk_radius
Radius of tusk attack

### riders
Number of riders

### rider_offset
(x, y, z) for each rider relative to elephant root node (bone_E_platform). You need this line for every single rider. So if you defined 4 riders, you need this line 4 times.
* **The first *rider_offset* line is for the mount driver.** 
* **The second *rider_offset* line is for the general (if present), or a regular unit.** 
* **The third and above *rider_offset* line is for any oter unit (these are archers in base game).** 

## Chariot and scorpion cart specific
The following breakdown lines are for chariots and scorpion carts only.

### axle_width
Width of the chariot/scorpion cart axle

### wheel_radius
Radius of the chariots/scorpion cart wheels

### pivot_offset
(x, y, z) position of the tow-pole pivot point releative to the axle centre

### pole_length
Length of the tow pole

### pole_pivot
Offset from pole origin to pivot point

### pole_connect
Height at which pole connects to harness above ground

### harness_connect
height at which harness connects to horse above ground

### attack_delay, scythe_radius & revs_per_attack

#### [
	attack_delay			delay between scythe attacks in seconds
	scythe_radius 		radius of scythe from end of axle
	revs_per_attack		revolutions per second per scythe attack on an individual (rounded down)
#### ]
Ommitting above section will mean no scythes are displayed and no scythe attacks will be used.  

### horse_type
Type of horse to tow chariot/scorpion cart. Note that is a reference to another defined mount. So be sure that this horse is defined before this entry, or the game will fail.

### horses
Amount of horses

### horse_offset
(x, z) for each horse relative to pivot point

### riders
Amount of riders 

### rider_offset
(x, y, z) for each rider releative to axle centre

### lods
Amount of lods - min 1, max 5

### lod
(model_filename, range) for each lod in ascending order of distance (use range = max for furthest lod)

### trail_effect
Effect definition for water trails

## Scorpion cart specific
The following breakdown lines are for scorpion carts only.

### scorpion_offset
(x, y, z) offset of the 'scorpion' releative to axle centre

### scorpion_height
Height of the scorpion's hitbox

### scorpion_forward_length
Defines how far forward the projectile appears from the scorpion when it's fired

### scorpion_reload_ticks
This is self explanatory, it's the time between attacks


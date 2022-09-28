![Workshop_header_template](/Workshop_header_template.png)
# data_controlled_features

## Table Of Contents

   * [Introduction](#introduction)
   * [opaque_black_fow](#opaque_black_fow)
   * [region_name_in_tags](#region_name_in_tags)
   * [public_order_bonuses](#public_order_bonuses)
      * [order_income_bonus_start](#order_income_bonus_start)
      * [order_income_bonus_multiplier](#order_income_bonus_multiplier)
      * [order_construction_bonus_threshold](#order_construction_bonus_threshold)
      * [order_recruitment_bonus_threshold](#order_recruitment_bonus_threshold)
   * [type_specific_movement_point_modifiers](#type_specific_movement_point_modifiers)
   * [night_control](#night_control)
   * [disable_friendly_fire](#disable_friendly_fire)
   * [disable_torch_allocation](#disable_torch_allocation)

## Introduction

This file allows modders to enable specific features that certain mods might want to use to change the behaviour away from the default. See below for info on the various items.

Some of these features can be further customised using the accompanying `data_controlled_variables.json` file.

All of these features are new to Rome Remastered as of 2.0.4.

## opaque_black_fow

Makes the in game fog of war completely opaque hiding any undiscovered areas from the player.

`default: false`

You can look at the example mod [here](/example_mods/ExampleMods.md) to see it in action.

## region_name_in_tags

Allows you to disable the region names from the settlement tags. This is useful if the mod uses variables as region names instead of human readable names.

You can look at the example mod [here](/example_mods/ExampleMods.md) to see it in action.

## public_order_bonuses

This feature allows a scaling multiplier to the majority of income sources depending on the settlements public order. The further above "happy" they are, the larger the multiplier.

Also, provide an additional construction/recruitment point if the public order meets a certain threshold (currently 180%). These can be set inside the accompanying `data_controlled_variables.json` file.

### order_income_bonus_start

What percentage of happiness is required to enable the bonus income, in this case 120%. This gets capped at 180%.

Example:  `"order_income_bonus_start": 120,`
  
### order_income_bonus_multiplier  

What multiplier to use for bonus income, in this case 0.25%.

Example:  `"order_income_bonus_multiplier": 0.0025,`
  
### order_construction_bonus_threshold 

What percentage of happiness is required to enable the extra construction build point, in this case 180%.

Example:  `"order_construction_bonus_threshold": 180,`
  
### order_recruitment_bonus_threshold

What percentage of happiness is required to enable the extra recruitment build point, in this case 180%.

Example:  `"order_recruitment_bonus_threshold": 180,`

## type_specific_movement_point_modifiers

Allow different movement ranges for different unit classes on the campaign map (so that light infantry moves faster than heavy infantry) and make those modifiers moddable. This only occurs when "type_specific_movement_point_modifiers" is set to true in `data_controlled_features.json`

The values are controlled in `feral_descr_movement_multipliers.txt`

```
; feral_descr_movement_multipliers - all the pertutations of unit category and unit class to a movement points multiplier
;
; Units
; Syntax: multiplier	<value>
;		  category		<category_type>, 	[optional]<category_type>...
;		  class			<class_type>,  		[optional]<class_type>...

; Characters
; Syntax: multiplier	<value>
;		  type			<character_type>, 	[optional]<character_type>...
```

For more details on the syntax please refer to the `feral_descr_movement_multipliers.txt` file.

## night_control

This feature allows modders to define when torches are used in 3D battles based on the angle of the sun.

You can look at the example mod [here](/example_mods/ExampleMods.md) to see it in action.

`default: false`

When enabled you need to set the minimum and maximum angles for torches to trigger. These can be set inside the accompanying `data_controlled_variables.json` file.

  `"torches_min_sun_angle": 90.0,`
  `"torches_max_sun_angle": 265.95`

## disable_friendly_fire

Will disable friendly fire in 3D battles. Useful in some mods and could also be used to make battles easier for some players.

`default: false`

## disable_torch_allocation

Completely disables allocating a torch to units during a night battle. This can be used if you have units where torches don't make sense but you still want to have building windows light up as if it's night.

`default: false`

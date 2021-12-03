![Workshop_header_template](/Workshop_header_template.png)
# descr_campaigns.txt

## Table Of Contents

* [Introduction](#introduction)
      * [Example of default feral_descr_movement_multipliers.txt](#example-of-default-feral_descr_movement_multiplierstxt)

## Introduction

This is a new addition for Rome Remastered. This file allows you to:

* Assign different unit categories & classes custom movement multipliers
* Requires ```type_specific_movement_point_modifiers``` set to true in ```data/data_controlled_features.json```

See comments in the file for further details.

### Example of default feral_descr_movement_multipliers.txt

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

;
; Notes: - This file only comes into effect when "type_specific_movement_point_modifiers" is set to true in "data/data_controlled_features.json"
;
;		 - The modifier assignment is done in the order they are described here, so a lower modifier assignment will overwrite previous ones
;
;		 - Assinging multiple categories/classes to a speed will make it so that speed is used for all combinations of categories/classes
;
;		 - category_types, class_types and character_types can be defines as shorthand for any set of categories/classes/characters
;
;		 - Category types that can be used: infantry, cavalry, siege, ship, handler
;
;		 - Class types that can be used: heavy, light, skirmish, spearmen, missile
;
;		 - Characters types that can be used: spy, assassin, diplomat, merchant, admiral, army_captain/general, named_character
;
;		 - Character multipliers MUST come after unit multipliers
;
;		 - If you DON'T mention one of the parameters for a speed then ALL the posibilities are being assigned
;
;		 - Make sure to use Windows line endings, it massively messes up stuff if you don't
```

These are used in the base game to make siege weapons have reduced movement and agents have increased movement. See below for two examples.

Siege Weapons have 75% of standard movement range:
```multiplier	0.75
category	siege
```

Agents have 140% of standard movement range:

```multiplier	1.4
type		agents```
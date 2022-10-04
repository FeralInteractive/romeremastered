![Workshop_header_template](/Workshop_header_template.png)
# descr_model_battle

## Table Of Contents

* [Introduction](#introduction)
* [DMB Breakdown](#dmb-breakdown)
   * [Example of a complete unit definition](#example-of-a-complete-unit-definition)
   * [type](#type)
   * [skeleton](#skeleton)
      * [skeleton (always required)](#skeleton-always-required)
      * [skeleton_horse (optional)](#skeleton_horse-optional)
      * [skeleton_elephant (optional)](#skeleton_elephant-optional)
      * [skeleton_chariot (optional)](#skeleton_chariot-optional)
      * [skeleton_camel (optional)](#skeleton_camel-optional)
      * [Original Game Skeletons](#original-game-skeletons)
      * [Remastered Game Skeletons](#remastered-game-skeletons)
   * [male/female](#malefemale)
   * [body](#body)
   * [angry_face](#angry_face)
   * [medieval_features](#medieval_features)
   * [tired](#tired)
   * [aged](#aged)
   * [pbr_texture](#pbr_texture)
   * [texture](#texture)
   * [model](#model)
   * [no_variation](#no_variation)
   * [model_flexi](#model_flexi)

## Introduction

The Descr_Model_Battle.txt (DMB) file defines the visual attributes for units, in combination with the Export_Descr_Unit (EDU) it completely defines how units look and act in the game.

We actively encourage modders to update this document with useful information and we can merge in any changes so this document can be the main resource for editing the EDU in Rome Remastered.

## DMB Breakdown

The file contains the entries for all the units in the game; the limit has been raised from the original games 500 unit maximum to practically unlimited. The order the units are arranged in is not specified, but the format each entry is coded in, is of course strictly specified. Here we will use a single, generic entry as an example, break it to its separate lines and then analyse each line individually, and then break it down to its entries when needed.
Note that certain lines may be missing depending on the type of the unit.

### Example of a complete unit definition

```
type carthaginian_general
skeleton			fs_dagger
skeleton_horse		fs_hc_swordsman
skeleton_elephant	fs_forest_elephant_rider
skeleton_chariot	fs_chariot_sword
skeleton_camel		fs_hc_swordsman
male
body Default
angry_face no
medieval_features no
tired VeryTired
aged 0.00
pbr_texture data/characters/textures/carthaginian_general_pbr.tga
pbr_texture numidia, data/characters/textures/carthaginian_general_numidia_pbr.tga
pbr_texture spain, data/characters/textures/carthaginian_general_spain_pbr.tga
texture data/characters/textures/carthaginian_general.tga
texture numidia, data/characters/textures/carthaginian_general_numidia.tga
texture slave, data/characters/textures/carthaginian_general_slave.tga
texture spain, data/characters/textures/carthaginian_general_spain.tga
model African data/characters/carthaginian_general_African
model carthage, African data/characters/carthaginian_general_carthage_African
model numidia, African data/characters/carthaginian_general_numidia_African
model slave, African data/characters/carthaginian_general_slave_African
model spain, African data/characters/carthaginian_general_spain_African
no_variation model African data/characters/carthaginian_general_African_no_variation
no_variation model carthage, African data/characters/carthaginian_general_carthage_African_no_variation
no_variation model numidia, African data/characters/carthaginian_general_numidia_African_no_variation
no_variation model spain, African data/characters/carthaginian_general_spain_African_no_variation
model Arabic data/characters/carthaginian_general_Arabic
model spain, Arabic data/characters/carthaginian_general_spain_Arabic
no_variation model Arabic data/characters/carthaginian_general_Arabic_no_variation
no_variation model spain, Arabic data/characters/carthaginian_general_spain_Arabic_no_variation
model Caucasian data/characters/carthaginian_general_Caucasian
model carthage, Caucasian data/characters/carthaginian_general_carthage_Caucasian
model numidia, Caucasian data/characters/carthaginian_general_numidia_Caucasian
model spain, Caucasian data/characters/carthaginian_general_spain_Caucasian
no_variation model Caucasian data/characters/carthaginian_general_Caucasian_no_variation
no_variation model carthage, Caucasian data/characters/carthaginian_general_carthage_Caucasian_no_variation
no_variation model numidia, Caucasian data/characters/carthaginian_general_numidia_Caucasian_no_variation
no_variation model spain, Caucasian data/characters/carthaginian_general_spain_Caucasian_no_variation
model EastAsian data/characters/carthaginian_general_EastAsian
model carthage, EastAsian data/characters/carthaginian_general_carthage_EastAsian
model numidia, EastAsian data/characters/carthaginian_general_carthage_EastAsian
model slave, EastAsian data/characters/carthaginian_general_carthage_EastAsian
model spain, EastAsian data/characters/carthaginian_general_spain_EastAsian
no_variation model EastAsian data/characters/carthaginian_general_EastAsian_no_variation
no_variation model carthage, EastAsian data/characters/carthaginian_general_carthage_EastAsian_no_variation
no_variation model numidia, EastAsian data/characters/carthaginian_general_carthage_EastAsian_no_variation
no_variation model slave, EastAsian data/characters/carthaginian_general_carthage_EastAsian_no_variation
no_variation model spain, EastAsian data/characters/carthaginian_general_spain_EastAsian_no_variation
model Egyptian data/characters/carthaginian_general_Egyptian
model slave, Egyptian data/characters/carthaginian_general_slave_Egyptian
model spain, Egyptian data/characters/carthaginian_general_spain_Egyptian
no_variation model Egyptian data/characters/carthaginian_general_Egyptian_no_variation
no_variation model slave, Egyptian data/characters/carthaginian_general_slave_Egyptian_no_variation
no_variation model spain, Egyptian data/characters/carthaginian_general_spain_Egyptian_no_variation
model Indian data/characters/carthaginian_general_Indian
model carthage, Indian data/characters/carthaginian_general_carthage_Indian
model numidia, Indian data/characters/carthaginian_general_numidia_Indian
model slave, Indian data/characters/carthaginian_general_slave_Indian
model spain, Indian data/characters/carthaginian_general_spain_Indian
no_variation model Indian data/characters/carthaginian_general_Indian_no_variation
no_variation model carthage, Indian data/characters/carthaginian_general_carthage_Indian_no_variation
no_variation model numidia, Indian data/characters/carthaginian_general_numidia_Indian_no_variation
no_variation model slave, Indian data/characters/carthaginian_general_slave_Indian_no_variation
no_variation model spain, Indian data/characters/carthaginian_general_spain_Indian_no_variation
model Mediterranean data/characters/carthaginian_general_Mediterranean
model spain, Mediterranean data/characters/carthaginian_general_spain_Mediterranean
no_variation model Mediterranean data/characters/carthaginian_general_Mediterranean_no_variation
no_variation model spain, Mediterranean data/characters/carthaginian_general_spain_Mediterranean_no_variation
```

### type

```Code: type             unit_type```

The type name which is referenced in the recruitment lines of *export_descr_buildings.txt*, the starting armies of *descr_strat.txt*, the unit description stats in *export_descr_unit.txt* and the armies of *descr_battle.txt* for historical battles.

### skeleton

```
Code:
skeleton          primary_weapon secondary_weapon
skeleton_horse    horse_skeleton
skeleton_elephant elephant_skeleton
skeleton_chariot  chariot_skeleton
skeleton_camel    camel_skeleton
```

All models have skeleton(s) associated with them. For reference all valid skeletons are listed in two files, the original game skeletons can be found in descr_skeleton.txt, new and updated skeletons created for Rome Remastered can be found in the descr_skeleton_feral_overrides.txt file. Depending on the unit there are number of possible skeletons. Models that are used in multiple units will have alternative skeletons for the various in battle situations.

General units are a most complex example of this as they can be linked with infantry or various mounted units and need to have the correct skeleton for all types of units. Below is a quick guide to the various types of skeleton code and how they are associated.

#### skeleton (always required)

* **primary_weapon** - the skeleton used when the unit is wielding their primary weapon.
* **secondary_weapon** (optional) - the skeleton used when the unit is wielding their secondary weapon.

#### skeleton_horse (optional)

* **horse_skeleton** -  - the skeleton used when the unit is sat on a horse.

#### skeleton_elephant (optional)

* **elephant_skeleton** -  - the skeleton used when the unit is sat on an elephant.

#### skeleton_chariot (optional)

* **chariot_skeleton** -  - the skeleton used when the unit is sat on a chariot.

#### skeleton_camel (optional)

* **camel_skeleton** -  - the skeleton used when the unit is sat on a camel.

#### Original Game Skeletons

Below is a list of all the skeletons from the original game that are also used in the remaster. When picking a skeleton for a new unit check the DMB for a similar unit to get an idea of the best option for your new unit.

* fs_swordsman
* fs_slow_swordsman
* fs_fast_swordsman
* fs_semi_fast_swordsman
* fs_standard_bearer
* fs_dagger
* fs_fast_dagger
* fs_semi_fast_dagger
* fs_javelinman
* fs_fast_javelinman
* fs_semi_fast_javelinman
* fs_spearman
* fs_slow_spearman
* fs_semi_fast_spearman
* fs_fast_spearman
* fs_2handed
* fs_slow_2handed
* fs_2handed_berserker
* fs_crossbow
* fs_archer
* fs_semi_fast_archer
* fs_fast_archer
* fs_slinger_new
* fs_hc_swordsman
* fs_hc_archer
* fs_hc_javelinman
* fs_hc_spearman
* fs_forest_elephant_rider
* fs_big_elephant_rider
* fs_chariot_sword
* fs_chariot_archer
* fs_chariot_javelinman
* fs_carriage_ballistae_crew
* fs_horse
* fs_medium_horse
* fs_fast_horse
* fs_cataphract_horse
* fs_forest_elephant			;small-ish elephant, currently 2.35m
* fs_indian_elephant			;medium-large elephant, currently 3.25m. Good for Indian or average African
* fs_african_elephant		;extra large elephant, size of largest Syrian or African bull elephants
* fs_indian_giant_elephant			;cheat oliphaunt skeleton
* fs_camel
* fs_dog
* fs_pig

#### Remastered Game Skeletons

Below is a list of all the skeletons created for the Remaster. When picking a skeleton for a new unit check the DMB for a similar unit to get an idea of the best option for your new unit.

* fs_hc_swordsman
* fs_hc_archer
* fs_hc_javelinman
* fs_hc_spearman
* fs_forest_elephant_rider
* fs_big_elephant_rider
* fs_camel
* fs_2handed
* fs_slow_2handed
* fs_2handed_berserker
* strat_spy
* fs_dagger
* fs_fast_dagger
* fs_semi_fast_dagger
* fs_crossbow
* fs_archer
* fs_fast_archer
* fs_semi_fast_archer
* fs_swordsman
* fs_slow_swordsman
* fs_fast_swordsman
* fs_semi_fast_swordsman
* fs_javelinman
* fs_fast_javelinman
* fs_semi_fast_javelinman
* fs_spearman
* fs_slow_spearman
* fs_semi_fast_spearman
* fs_fast_spearman
* strat_named_with_army
* fs_standard_bearer
* fs_slinger_new

### male/female

```Code: male/female```

The game allows you to define the gender of the unit. This means the game will select from female textures and voices when the unit is rendered in a battle.

You just need to have the string `male` or `female`.

### body

```
    example:
        [argument] [value]
        body Default
    options:
        Default - References Default skin body texture
        Athletic - References Athletic skin body texture
        Bulky - References Bulky skin body texture
        Skinny - References Skinny skin body texture
        SkinnyAthletic - References SkinnyAthletic skin body texture
        Overweight - References Overweight skin body texture
    details:
        This is limiting the body texture slots used in atlas accordingly. See image below for potential variants.
  ```
  ![Workshop_header_template](/documentation/techart_guides/images/Unit_UV_skin_texture_atlas.jpg)

**TIP:** These settings require that the cas model and textures have the correct assets. It is reccomended you open up some of the existing models and textures from Remastered to get a better idea of how they are contructed and relate to the `EDU`.


### angry_face

```
    example:
        [argument] [value]
        angry_faces no
    options:
        no - Uses head texture ([race]_[gender]_faces_serious/ example: mediterranean_m_faces_serious)
        yes - Uses head texture ([race]_[gender]_faces_angry/ example: mediterranean_m_faces_angry)
    details:
        This setting which head texture file to reference.
```

### medieval_features
```
    example:
        [argument] [value]
        medieval_features no
    options:
        no - Does NOT use head texture slots in texture atlas
        yes - Does use head texture slots in texture atlas
    details:
        This is limiting the head texture slots used in atlas
```

* **NOTE 1:**  (slots 12-15 / see [skin_texture_atlas.jpg](/documentation/techart_guides/images/skin_texture_atlas.jpg) )
* **NOTE 2:** Also can be set differently per faction like so: `medieval_features dacia, 0.00`


### tired
```
    example:
        [argument] [value]
        tired Tired
    options:
        No
        Tired
        VeryTired
    details:
            Not required **TODO**
```

### aged
```
    example:
        [argument] [value]
        aged 0.00
    options:
        0.00 - 0% min / Does NOT use head texture slots in texture atlas
        1.00 - 100% max / Does use head texture slots in texture atlas
    details:
        This is the percentage of aged faces which are distributed across a set of units.
```
* **NOTE 1:**  (slots 0-4 / see [skin_texture_atlas.jpg](/documentation/techart_guides/images/skin_texture_atlas.jpg) )
* **NOTE 2:** Also can be set differently per faction like so: `aged dacia, 0.00`


### pbr_texture
```
    example:
        [argument] [faction /optional], [value]
        pbr_texture spain, data/characters/textures/carthaginian_general_spain_pbr.tga
    options:
        faction (optional) - Can set texture reference specific to a faction
        value - File path to texture (note: tga is not the format it is part of the name)
    details:
        This is simply referring to a file and path.
        File contains the Normal, Roughness and Metallic into the channels accordingly.
        File should be constructed using the "RomeTextureCompress" tool.
```

### texture
```
    example:
        [argument] [faction /optional], [value]
        texture data/characters/textures/carthaginian_general.tga
        texture spain, data/characters/textures/carthaginian_general_spain.tga
    options:
        faction (optional) - Can set texture reference specific to a faction
        value - File path to texture (note: tga is not the format it is part of the name)
    details:
        This is simply referring to a file and path.
        File format should be dds.
        File contains the Albedo and Alpha.
        File should be constructed using the "RomeTextureCompress" tool.
```

### model
```
    example:
        [argument] [faction /optional], [ethnicity] [value]
        model African data/characters/carthaginian_general_African
        model spain, African data/characters/carthaginian_general_spain_African
    options:
        faction (optional) - Sets faction
        ethnicity - Sets ethnicity
        value - File path to texture (note: tga is not the format it is part of the name)
    details:
        This is simply referring to a file and path.
        File format should be cas.
        File should be constructed using the "Cas exporter" tool.
```


### no_variation
```
    example:
        [argument] [faction /optional], [value (file path)]
        no_variation model spain, African data/characters/carthaginian_general_spain_African_no_variation
    options:
        faction (optional) - Sets faction
        ethnicity - Sets ethnicity
        value - File path to texture (note: tga is not the format it is part of the name)
    details:
        Same setup as "model", however these models will be used instead when the graphics setting "Unit Variation" is false
```

### model_flexi


```
type							camel
skeleton						fs_camel
male
pbr_texture						data/animals/textures/mount_camel_pbr.tga
texture	Default, 				data/animals/textures/mount_camel_base_default.tga	; Used for Mercs
texture	numidia, 				data/animals/textures/mount_camel_base_numidia.tga
texture	egypt, 					data/animals/textures/mount_camel_base_egypt.tga
model_flexi_m 					data/animals/mount_camel_lod0.cas, 15
model_flexi 					data/animals/mount_camel_lod1.cas, 30
model_flexi 					data/animals/mount_camel_lod2.cas, 60
model_flexi	 					data/animals/mount_camel_lod3.cas, max
no_variation model_flexi_m 		data/animals/mount_camel_lod0.cas, 15
no_variation model_flexi 		data/animals/mount_camel_lod1.cas, 30
no_variation model_flexi 		data/animals/mount_camel_lod2.cas, 60
no_variation model_flexi	 	data/animals/mount_camel_lod3.cas, max
```

`Model_flexi_m` - This is only used for models with a small number of weighted vertices. You will rarely see this.

`Model_flexi_c` - This is only used for a flexi model which contains per-vertex colors. Again, it is very rarely used.

`Model_flexi` - This is by far the most commonly used type of model. What this (and the other model_flexi_x lines) do is specify what model to use with the unit. Each unit will typically have up to four models, and the game swaps from one to the other depending on the level of distance (lod), using lower resolution models when further away to reduce the load on the processor. They are listed from nearest (top) to the farthest (bottom).

As with the texture, the path of the model file must be provided. It is followed by a comma and then a number. The number tells the game the maximum distance to use the model from. Max means the maximum distance.

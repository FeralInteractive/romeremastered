![Workshop_header_template](/Workshop_header_template.png)
# feral_descr_grass_usage

## Table Of Contents

* [Introduction](#introduction)
	 * [Example of feral_descr_grass_usage.txt](#example-of-feral_descr_grass_usagetxt)

## Introduction

grass variations for the different climates, seasons, and ground types see [feral_descr_grass_textures.txt](/documentation/data_file_guides/feral_descr_grass_textures.md) for how sprites are mapped to textures.

valid climates types are:
* `test_climate`
* `sandy_desert`
* `rocky_desert`
* `temperate_grassland_fertile`
* `temperate_grassland_infertile`
* `temperate_forest_open`
* `temperate_forest_deep`
* `swamp`
* `highland`
* `alpine`
* `sub_arctic`
* `semi_arid`

valid seasons are:
* `summer`
* `winter`

valid ground types are:

* `grass_short`
* `grass_long`
* `sand`
* `rock`
* `forest_dense`
* `scrub_dense`
* `swamp`
* `mud`
* `mud_road`
* `stone_road`
* `water`
* `ice`
* `snow`
* `wood`
* `dirt`

Every ground_type has a scale, to indicate how big the grass should be. Use this to make "long grass" bigger without having to define a seperate sprite

`sprite <name of sprite from feral_descr_grass_textures.txt> <relative weighting>`

`Weighting` is the relative probability of this sprite being used instead of others for the same season, ground type, and climate.

**NOTES:**
* We have limited randomness to pick grass, so there's a limit to how different the weightings can be, on the order of ~1000->10000. There's currently ~1000 pieces of grass per 8x8m patch of grassy ground. So you can't have grass that's more rare than once every patch or 2. Also, patches are reused to reduce creation time and storage used, so lower probability grass wouldn't work anyway.

### Example of feral_descr_grass_usage.txt

```
climate test_climate
{
	summer
	{
		texture data/feral_textures/temperate_grassland_infertile_sprites
		ground_type grass_short
		{
			scale	1.125
			sprite	grass1de_c_basecolor	250
			sprite	grass1de_b_basecolor	250
			sprite	grass2de_b_basecolor	250
			sprite	shoots					50
		}
		ground_type grass_long
		{
			scale	1.5
			sprite	grass1de_a_basecolor	300
			sprite	grass2de_a_basecolor	250
			sprite	grass2de_c_basecolor	200
			sprite	grass2de_d_basecolor	150
			sprite	plant1_a_basecolor		50
			sprite	plant3_basecolor		50
		}
		ground_type scrub_dense
		{
			scale	2.25
			sprite	grass1de_a_basecolor	100
			sprite	grass2de_a_basecolor	100
			sprite	grass2de_c_basecolor	100
			sprite	grass2de_d_basecolor	100
			sprite	plant1_a_basecolor		50
			sprite	plant3de_basecolor		50
			sprite	grass1de_c_basecolor	100
			sprite	grass1de_b_basecolor	100
			sprite	grass2de_b_basecolor	100
		}
	}
```

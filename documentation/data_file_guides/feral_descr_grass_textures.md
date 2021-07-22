![Workshop_header_template](/Workshop_header_template.png)
# feral_descr_grass_textures

## Table Of Contents

* [Introduction](#introduction)
	 * [Example of feral_descr_grass_textures.txt](#example-of-feral_descr_grass_texturestxt)

## Introduction

grass sprite texture lookups. Max 32 sprites per texture. Only 1 texture per map (climate/season combonation).

See [feral_descr_grass_usage.txt](/documentation/data_file_guides/feral_descr_grass_usage.md) for mapping to climate/season/groundtype.

Each grass sprite is a triangle described by the values below:

* `height`: Height in meters (adjusted by the scale in feral_descr_grass_usage) of the grass sprite
* `width`:  Width in meters (adjusted by the scale in feral_descr_grass_usage) of the grass sprite. The ratio of this to height should match the uv coords to avoid distorted textures.
* `top_position`: The proportion of the space between vertex 0 and vertex 1 where the top vertex should be placed. 0 is above vertex 0, 1 is above vertex 1, and 0.5 is right in the middle. This could be ouside the range 0 to 1 if desired. This should match the uv coords to avoid distorted textures.
* `u0`,`v0`->`u2`,`v2`: Texture coordinates for the grass clump verticies, with the top vertex last. These will be squished into two 16 bit unsigned integers each which will be separated in Grass.hlsl and scaled to the range -0.5 to 1.5.
* `colour_*`:
  * The grass colour will be shifted to match the terrain colour instead of the raw colours from texture *unless* the assigned colour is 0,0,0(black), in which case we can't mix even if we wanted to (there's no room to shift the colours), so we use it as a magic value to indicate no mixing should be done. This allows for eg red flowers in an otherwise green landscape.
  * A representative colour of the grass. Used when recolouring to match the terrain. This can be intentionally inaccurate to shift the colours used (but probably shouldn't be!).
  * The colour is in HSV aka hue/saturation/value(brightness) space, all with values between `0` and `1`, and with `hue`: `0` and `1`==`pure red`, `0.333`==`pure green`, `0.667`==`pure blue`.

When generating a sprite atlas texture, keep in mind it will be alpha keyed, and the mipmaps must be generated based on that (if you have an option to lock the alpha-coverage ratio, set that to 0.5). Also, make sure the transparent areas aren't bleeding black/garbage colour data into the higher mip levels. Try making transparent pixels be a blurred version of the image.

### Example of feral_descr_grass_textures.txt

```
texture data/feral_textures/temperate_grassland_infertile_sprites
{
	sprite grass1de_a_basecolor
	{
		height			0.7369685098528862
		width			0.7377926558256140
		top_position	0.5666789268883952
		u0				0.001250130357220769
		v0				0.3815930485725403
		u1				0.3715040683746338
		v1				0.3814723491668701
		u2				0.18046700954437256
		v2				0.7326439619064331
		colour_hue		0.12057324244254812
		colour_sat		0.8131648064869749
		colour_val		0.5467327943678653
	}
```

![Workshop_header_template](/Workshop_header_template.png)
# feral_descr_tonemap_lut

## Table Of Contents

* [Introduction](#introduction)
	 * [Example of feral_descr_tonemap_lut.txt](#example-of-feral_descr_tonemap_luttxt)

## Introduction

This is a new file for Rome Remastered. This file maps all the pertutations of weather and climate to a texture name that contains the hue shift that should be done in mentioned conditions.
```
name			<texture_name>
map				<map_name>
climate		<climate_type>, [optional]<climate_type>...
season		<season_type>,  [optional]<season_type>...
weather		<weather_type>, [optional]<weather_type>...
daytime		<daytime>,			[optional]<daytime>...
```
**Notes:**

* The LUT assignment is done in the order they are described here, so a lower LUT assignment will overwrite previous ones
* The LUT map determines if the LUT is used for the campaign or 3d battles / settlement view
* In the campaign we only use season and daytime to pick the LUT
* Assinging multiple climates/weathers to a LUT will make it so that LUT is used for all combinations of climates/weathers
* `climate_types`, `weather_types`, `daytime_types` can be defines as shorthand for any set of climates/weather/daytimes
* Weather types that can be used: `calm`, `hazy`, `dense_fog`, `light_fog`, `rain_drizzle`, `rain_storm`, `sand_storm`, `snow_falling`, `blizzard`
* Daytimes that can be used: `midnight`, `sunrise`, `mid_morning`, `morning`, `midday`, `sunset`, `mid_evening`, `night`
* If you DON'T mention one of the parameters for a texture then ALL the posibilities are being assigned
* Make sure to use Windows line endings

### Example of feral_descr_tonemap_lut.txt

```
;;; Climate/Weather/Daytime groups

climate_types

vibrant	default, semi_arid, temperate_grassland_fertile

blue	temperate_grassland_infertile, temperate_forest_open, temperate_forest_deep, swamp, highland, alpine, sub_arctic

red 	sandy_desert, rocky_desert

weather_types

clear	calm, hazy, sand_storm

cloudy	light_fog, dense_fog

rainy	rain_drizzle, rain_storm

snow 	snow_falling, blizzard

daytime_types

day_summer 		sunrise, mid_morning, morning, midday, sunset

day_winter 		sunrise, mid_morning, morning, midday, sunset, mid_evening

night_summer 	midnight, night, mid_evening

night_winter 	midnight, night

;;; LUTs

; Summer

; Campaign map

name      campaign_summer.tga
map       campaign
season    summer
daytime   day_summer

name      campaign_summer_night.tga
map       campaign
season    summer
daytime   night_summer
```

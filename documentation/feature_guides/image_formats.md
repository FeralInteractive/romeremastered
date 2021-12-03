![Workshop_header_template](/Workshop_header_template.png)
# Image Formats - A quick guide to the image formats used throughout the game.

## Table Of Contents

   * [Introduction](#introduction)
   * [Faction Icons](#faction-icons)
   * [Unit Cards](#unit-cards)
   * [Large Unit Images](#large-unit-images)
   * [Building Cards](#building-cards)
   * [News Banners](#news-banners)
   * [3D Unit Textures](#3d-unit-textures)
   * [Hair Textures](#hair-textures)
   * [3D Building Textures](#3d-building-textures)
   * [3D Specialist textures (trees, shrubs etc if applicable)](#3d-specialist-textures-trees-shrubs-etc-if-applicable)
   * [UI Textures](#ui-textures)
   * [Loading Screens](#loading-screens)
   
## Introduction

Below you'll find a list of all the major images used throughout the game from in game textures to loading screens. These can be used as a reference when modding different areas of the game to ensure you are saving textures in the correct format.


## Faction Icons

 * Format: .TGA 32 bits
 * Aspect Ratio: 1:1
 * Resolution: 512x512
 * Tested the following ratios and resolutions with no major issues visible:
   * 1920x1080 16:9
   * 960x640 3:2
   * 1024x768 4:3
   * 3840x2160 16:9

## Unit Cards

 * Format: .TGA 32 bits w/ Alpha channel
 * Aspect Ratio: 4:3
 * Resolution: 164x224
 * Tested the following ratios and resolutions with no major issues visible:
   * 1920x1080 16:9
   * 960x640 3:2
   * 1024x768 4:3
   * 3840x2160 16:9

## Large Unit Images

 * Format: .TGA 32 bits w/ Alpha Channel
 * Aspect Ratio: 4:3
 * Resolution: 328x448
 * Tested the following ratios and resolutions with no major issues visible:
   * 1920x1080 16:9
   * 960x640 3:2
   * 1024x768 4:3
   * 3840x2160 16:9 - caused graphical corruption on main menu

## Building Cards 

 * Format: .TGA 32 bits w/ Alpha Channel
 * Resolution: 128x102 
 * Tested the following ratios and resolutions with no major issues visible:
   * 1920x1080 16:9
   * 960x640 3:2
   * 1024x768 4:3
   * 3840x2160 16:9

## News Banners
 * Format: .TGA 24 bits
 * Various resolutions and ratios present

## 3D Unit Textures

 * Format: .DDS 
 * Resolution: 2048x2048
 * Aspect Ratio: 1:1
 * Compression:
   * Diffuse - BC1 4bpp
   * Diffuse + Alpha - BC3 8bpp
   * Normal - BC5 8bpp
   * Greyscale maps - BC4 4bpp
 * Compression completed with Intel Texture Works v1.0.4 plugin for Photoshop CC
 * Compressed further in LZ4
 * **Supports MIPS**
 * Using a different Image Resolution and ratio did not cause any errors, however UV layout should be taken into account if this is altered. Textures split into a diffuse and normal maps (_pbr at end of normal map file name).
 * Tested the following ratios and resolutions with no major issues visible:
   * 960x640 3:2
   * 3840x2160 16:9
   * 1024x768 4:3
   * 1920x1080 16:9

## Hair Textures

 * Format: DDS DXT5
   * Red Channel = X Normals
   * Green Channel = Y Normals
   * Blue Channel = Diffuse Brightness
   * Alpha Channel = Alpha 
 * Resolution: 9216 x 1024
 * LZ4 Compression
 * **Supports MIPS**
 * All hairstyles exist in a single texture map.

## 3D Building Textures

 * Format: .DDS w/ Alpha Channel (Alpha Channel present for texture maps with transparency)
 * Various resolutions and aspect ratios present
 * **Notes:** Textures with an alpha channel typically saved with a ‘##’ or ‘#&’ at the start of the name. Each texture has a Diffuse Map, Normal map (file name contains ‘_n’) and a Roughness map (file name contains _s). Some files also contain a Metallic map (file name contains ‘_m)
 * Compression:
   * Diffuse - BC1 4bpp
   * Diffuse + Alpha - BC3 8bpp
   * Normal - BC5 8bpp
   * Greyscale maps - BC4 4bpp
 * Compression completed with Intel Texture Works v1.0.4 plugin for Photoshop CC
 * **Supports MIPS**


## 3D Specialist textures (trees, shrubs etc if applicable)

 * **Supports MIPS**Format: .DDS
 * **Supports MIPS**Resolution: 2048x1024
 * **Supports MIPS**Aspect Ratio: 2:1
 * **Supports MIPS**Compression:
   * Diffuse + Alpha - BC3 8bpp
   * Normal - BC5 8bpp
   * Roughness - BC4 4bpp
 * **Supports MIPS**
 * Compression completed with Intel Texture Works v1.0.4 plugin for Photoshop CC
 * Notes: Any resolution and ratio supported (as long as rule of 2n is abided by either height or width)

## UI Textures

 * Format: .TGA 32 bits
 * Various aspect ratios and resolutions present

## Loading Screens

 * Format: .DDS DXT1
 * Aspect Ratio: 64:27
 * 5120 x 2160
 * Notes: Application will **crash** if aspect ratio/resolution is changed. 

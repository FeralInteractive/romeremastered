![Workshop_header_template](/Workshop_header_template.png)
# casconv.exe - Tool for packing cas files

## Table Of Contents

* [Introduction](#introduction)
* [Casconv help](#casconv-help)
* [Example Models](#example-models)
* [01 Campaign terrain pieces](#01-campaign-terrain-pieces)
* [02 Crop field model](#02-crop-field-model)
* [03 Wall destruction model with animation](#03-wall-destruction-model-with-animation)
* [04 Character units](#04-character-units)
* [05 Building models](#05-building-models)
* [06 Unit animation](#06-unit-animation)
* [07 Campaign models](#07-campaign-models)
* [Resources](#resources)

## Introduction

This is the casconv tool. This tool will convert fbx files into cas files. The tool is a commandline tool that allows you to take an fbx file and export it into a cas file that can be loaded by the game.

It has an interactive help that provides more details on the format of the different commands.   

## Casconv help

Command: `casconv.exe -h`

Passing "-i ."" as input will convert every fbx in the folder to cas file.
Without "-o dirctory" the output directory is going to be the same as the input files.

## Example Models

Included below are 7 different examples that the cas converter can convert into game assets. These should be used as examples when making your own models.

## 01 Campaign terrain pieces

Command: `casconv.exe -i . asset_location = "data\terrain\campaign\pieces"`

* This piece is placed in "data\terrain\campaign\pieces"


## 02 Crop field model

Command: `casconv.exe -i . --no-backfacecull asset_location = "data\terrain\campaign\models_building"`

* This piece is placed in "data\models_building".
* Then delete "data/descr_item.db" and run the game.


## 03 Wall destruction model with animation

Command: `casconv.exe" -i . --calculate-missing-bones asset_location = "data\models_building\models_walls" / "data\items"`

* `--calculate-missing-bones` is needed when there are no bones in the animation, but the mesh is animated itself.
* This piece is placed in "data\models_building\models_walls".
* Delete the item file version of the cas.
* Then delete "data/descr_item.db" and run the game (game will take a little longer to load due to generating the deleted files).


## 04 Character units

Command: `casconv.exe -f cas --input-directory <path to input fbx files> --output-directory <path to output cas files> --ignore-textures
	asset_location = "data\characters"`

* Only only the highest lod can have 2 bone skinning weight influences(lod0)
* All other lods only support 1 in the game engine.


## 05 Building models

Command: `casconv.exe -f cas --input-directory <path to input fbx files> --output-directory <path to output cas files> (--no-backfacecull)`

* Meshes can only have 1 material assigned, if you cas file will have more make sure they are seperate meshes
* Asset must be parented under a node named "Scene_Root", this can be a Location (Maya) or an Empty (Blender)
* Once your cas file is create and named accordingly, replace the file you want to update in the game data


## 06 Unit animation

**TODO**


## 07 Campaign models

* 3D models / assets found within data\models_strat are simple to edit and replace, relative to all other in-game assets.
* The models seen within this folder make up the majority of the 3D objects seen on the campaign map, including towns, walls, resources, wonders, ect.  
* Essentially, they are .fbx files, created in your 3D software of choice, converted to .cas (using the .exe converter provided).
* After conversion to the .cas format, they can then be dropped directly into game data, with no .item file regeneration necessary, as is required with some other assets within game data.
* Textures for these assets are found (and should be saved) within 2 folders found in data/models_strat;
	* data\models_strat\textures
	* data\models_strat\residences\textures

You'll find an in-game model provided, in.fbx format, trade_boat.fbx.

Refer to this as a working example of a campaign map model. Note the use of an empty or a locator (name differs dependant on 3D software), titled Scene_Root, this is a requirement.

## Resources

Resources seen on the campaign map have been changed in Total War: Rome Remastered compared to the original title.

In an effort to reduce the number of 3D models on the map, resources within close proximity on the map are grouped and replaced with a different model to signify a larger quanitity.

These entreies can be seen and edited within descr_sm_resources.txt

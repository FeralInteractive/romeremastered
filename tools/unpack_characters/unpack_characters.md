![Workshop_header_template](/Workshop_header_template.png)
# unpack_characters - Extract .cas files from packed game data

## Table Of Contents

* [Introduction](#introduction)
* [Instructions](#instructions)
   * [Generate CharacterExportFile](#generate-characterexportfile)
   * [Setup Feral Pre Game Options Window](#setup-feral-pre-game-options-window)
   * [View extracted cas files](#view-extracted-cas-files)
   * [View extraction log](#view-extraction-log)
      * [Example of Extraction starting](#example-of-extraction-starting)

## Introduction

Rome Remastered has the ability to export cas models from the packed data files using launch options accessed via the Pre Game Options Window.

## Instructions

Below are the steps you need to follow to get the game to export the cas files you want.

### Generate CharacterExportFile

You can find all of the different cas files in the game by referencing the *descr_model_battle.txt* for units. Please note that in Rome Remastered units have multiple LOD versions of the models so you might want to extract all LOD levels so your updated unit can be modelled at all quality levels.

Below is an example of the file path you'd add if you wanted to extract the following models from the character model pak files.

```
data/characters/barb_archer_dacia_Arabic_lod0.cas
data/characters/roman_peasant_romans_brutii_Caucasian_lod0.cas
data/characters/roman_velite_Arabic_no_variation_lod3.cas
```

[Example Character Export File](/tools/unpack_characters/filelist.txt)

### Setup Feral Pre Game Options Window

To make the game run in extraction mode you need to place the text file in a location the game can access and then run the game with special launch options.

usage:
```
unpack_characters:dir="path/to/extraction/folder":filelist="path/to/characterexportfile.txt"
```

In this example we'll be assuming that:
* The user is using Microsoft Windows
* The users account is found on the C drive
* The users account name is swill
* The CharacterExportFile is called filelist.txt and is in the Downloads folder
* We want to export the resulting cas files into the Downloads folder.


Add the following command into the advanced launch commands:

```
unpack_characters:dir="C:\Users\swill\Downloads\ModelExport\":filelist="C:\Users\swill\Downloads\filelist.txt"
```

Your Pre Game Options Window should look a little like this:

![FileManager](/tools/unpack_characters/images/PGOW.png)

Once done press play, the game should stay open for a few seconds then close.

### View extracted cas files

Inside the folder structure you should see all of the cas files you listed to be extracted.

![FileManager](/tools/unpack_characters/images/Desktop.png)

Once extracted you might want to convert them into FBX format so you can edit them in Blender or another 3D tool. You can find out how to use the [CAS Exporter Tool](tools/CasPacker/casconv.md) here.

### View extraction log

Whenever you run this command the game will save out a log file (message_log.txt) containing all extract attempts and if they are successful or not.

You can find more info on the location of log files on the [logging feature page](documentation/features/logging.md).

#### Example of Extraction starting


```
==== message log start, build date: Jul  7 2021 ===
Unpack characters: Extracting `data/characters/barb_archer_dacia_Arabic_lod0.cas` to `C:\Program Files (x86)\Steam\steamapps\common\Total War ROME REMASTERED\Contents\Resources\Data\data\unpacked character testdata\characters\barb_archer_dacia_Arabic_lod0.cas` of size `293314`
```

```
Unpack characters: Done `data/characters/barb_archer_dacia_Arabic_lod0.cas` to `C:\Program Files (x86)\Steam\steamapps\common\Total War ROME REMASTERED\Contents\Resources\Data\data\unpacked character testdata\characters\barb_archer_dacia_Arabic_lod0.cas`
```


Unpack characters: Extracting `data/characters/roman_peasant_romans_brutii_Caucasian_lod0.cas` to `C:\Program Files (x86)\Steam\steamapps\common\Total War ROME REMASTERED\Contents\Resources\Data\data\unpacked character testdata\characters\roman_peasant_romans_brutii_Caucasian_lod0.cas` of size `236099`

Unpack characters: Done `data/characters/roman_peasant_romans_brutii_Caucasian_lod0.cas` to `C:\Program Files (x86)\Steam\steamapps\common\Total War ROME REMASTERED\Contents\Resources\Data\data\unpacked character testdata\characters\roman_peasant_romans_brutii_Caucasian_lod0.cas`

Unpack characters: No such file `data/characters/this_should_trigger_an_error.cas` in pack
```

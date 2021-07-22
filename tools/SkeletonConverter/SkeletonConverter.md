![Workshop_header_template](/Workshop_header_template.png)
# skelconverter.py - Convert from original to remastered format

## Table Of Contents

* [WARNING](#warning)
* [How it works](#how-it-works)
* [How to use](#how-to-use)

## WARNING

This script is intended to convert **original-style packs ONLY**, attempting to convert a pack which contains skeletons decompiled from the pack included with RR will cause this to **CRASH**

## How it works

Skeletons from the original game DO NOT need to be included in new mod packs, the skeletons from the base game (and also expansions, if your mod runs on one of them) will automatically be included. Including a skeleton with the same name as one in the base game will **OVERRIDE** the one from the base game with the version included in your mod.

## How to use

The original skeleton modding tools from Rome Total War are required to modify skeletons and create a new **skeleton.idx** and **.dat**, however these will be in the old format *(which can be confirmed by checking the 4 bytes at offset 12, they form a version number which will be 3 for old packs, and 4 for new ones.)* This script will convert the old version into the new one.

To use, first you need to create your new skeleton.idx and .dat files using the tools and methods created for the original release. Then simply place the script in the same directory as the skeleton packs and run. The script should auto-detect the files and create two new files: **skeleton_new.idx** and **skeleton_new.dat**, these can be renamed and added to the animations folder of a mod and should function as expected.

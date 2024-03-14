![Workshop_header_template](/Workshop_header_template.png)
# RSD (Un)Packer - Tool for packing/unpacking UI textures to and from raw files

## Table Of Contents

* [Introduction](#introduction)
* [Setup](#setup)
* [Unpacking](#unpacking)
* [Repacking](#repacking)

## Introduction

This is the RSD packer/unpacker python script. This script will read `.rsd` files and extract UI textures located in `data/ui/roman/interface` into seperate `.tga` files based on `collision` data. You can then modify seperate UI textures, and then pack them together in a single interface texture page. 

## Setup

First of all, I recommend to **not** modify the textures in your mod/base game folder directly!! This way you prevent messing things up.<br><br>
So, create a folder somewhere in your documents folder, and place the 2 `.bat` files, as well as the `python` files inside it.<br>
Then, copy paste the `data/ui/interface` folder (keep that order!) to the same directory.<br><br>
It will look like this:

![rsd_folder_structure](/tools/RSDPacker/rsd_folder_structure.jpg) 

The `data/ui/` directory should contain the `.rsd` files, and the `data/ui/roman/interface/` directory should contain the `.tga` textures.<br><br>

Next up, be sure to have python installed. Then, run the following command:

`python -m pip install --upgrade Pillow`

This will install the required image package for the python script to run without error.

## Unpacking

If you completed the setup correctly, you can now run `unpack.bat`. It will run the unpack python script. You should see a lot of debug information on the console window.<br><br>
Also, when things went correctly, you should see a new directory named `spritesheet_unpack`. If you open it, you will see a bunch of new `.tga` collision files which you currently do not need to do anything with.<br><br>
The other sub-directories contain all the seperated textures. You can modify them as you like. For example, you can edit `spritesheet_unpack/UI_STRAT_V2_SPRITE_PAGE/0437building_navy.tga` to edit the icon of port buildings.

## Repacking

After you have made changes to any UI icon, you can run `repack.bat`, which will then combine the `.tga` images back together in the shared UI pages they came from. Note that if you run this bat (and thus `rsdpacker.py`), the script will automatically unpack all the textures again after completion.
To prevent overriding the original files, I modified the script so that the updated combined textures will now be placed in a new directory, `spritesheet_repack`.<br><br>The script will search for this folder when unpacking/repacking, and use those `.tga` images if the folder is present. If not, it will use the default ones in `data/ui/roman/interface`. So keep that in mind...<br><br>
Now check the created textures in `spritesheet_repack` and see if it actually put your modified texture in it correctly. You can then place these `.tga` in your mod folder interface directory and check them in game!
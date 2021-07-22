![Workshop_header_template](/Workshop_header_template.png)
# Characters

## Table Of Contents

* [Provided files](#provided-files)
* [Models](#models)

## Provided files

| Assets                                           |
|--------------------------------------------------|
| **[Unpack_characters](/tools/unpack_characters/unpack_characters.md)** <br/> All character files can be extracted from the game using the unpack_characters feature built into the game (see above link). |
| **All character textures (TGA.DDS format)** <br/> <br/> The character textures used in the game are compressed using BC7 compression. You can use this [Intel plugin](https://software.intel.com/content/www/us/en/develop/articles/intel-texture-works-plugin.html) to decompress them. <br/> There is also a bulk decompression tool inside the free community [IWTE Tool](https://wiki.twcenter.net/index.php?title=IWTE) created by Wilddog. |


| Tools                                            |
|--------------------------------------------------|
| **[Cas converter](/tools/CasPacker/casconv.md)** <br/> Allows access to convert and edit models.|
| **[Rome texture compression](/documentation/techart_guides/Importing_RTW_units_to_Remastered.md#dds-textures)** <br /> Format  texture (dds-lz4). You can do this using the free open source tool [GNU Image Manipulation Program](https://www.gimp.org/downloads/).|


## Models


| Concept | Details |
|-|-|
| **LODs**| There are 4 lods setup for units starting from **`lod0`**(highest) to **`lod3`**(lowest) |
| **Unit UV Layout**| Overall layout of a character UV. Plain example and an actual unit. <br/> ![Bone Hierarchy Image](/documentation/techart_guides/images/Unit_UV_Layout.jpg) <br/><br/> ![Bone Hierarchy Image](/documentation/techart_guides/images/Unit_UV_Layout_Texture.jpg)|
| **UV Hair & Facial Hair**| UV layout information for hair and facial hair.  <br/> ![Bone Hierarchy Image](/documentation/techart_guides/images/Unit_UV_Hair_Mapping.jpg) |
| **UV Arms, Legs, Torso and Pelvis**| UV layout information for Arms, Legs, Torso and Pelvis.  <br/> ![Bone Hierarchy Image](/documentation/techart_guides/images/Unit_UV_Body_Texture_Example.jpg) |
| **UV Faces**| UV layout information for faces.  <br/> ![Bone Hierarchy Image](/documentation/techart_guides/images/Unit_UV_Face_Texture_Example.jpg)|
| **UV Clothing & Props**| UV layout information for Clothing & Props.  <br/> ![Bone Hierarchy Image](/documentation/techart_guides/images/Unit_UV_screenshot.jpg)|
| **Skeletons**| For units there are 2 different types of skeleton structures. <br/> <br/> <ul> <li> **Normal skeleton** </li> <li> **Slinger skeleton** *(in `descr.txt` files this is reference to as **“`fs_slinger_new`”**)* </li></ul> Both skeletons are pretty much the same, however the slinger has an extra bone parented under the **“rbone_hand”**. </br></br> The bone hierarchy __must not change!__  The game expects the bones to be listed in a specific order. <span style="color:red"> ***Slinger ONLY*!** </span> <br/> ______________________________________________________________ <br/>  **Bone Hierarchy** </br></br> ![Bone Hierarchy Image](/documentation/techart_guides/images/Bone_Hierarchy.png) <br/> ______________________________________________________________ <br/></br> ![Blender Bone Hierarchy Image](/documentation/techart_guides/images/Blender_Bone_Hierarchy.png) |
|**Props** </br> *(Non-skinned)* | Props which are not skinned to the skeleton should be **parented under the bone accordingly.** </br> </br> The pivot should match the bone position and its transformations reset. </br></br> **Naming:** </br> For primary & secondary weapons they must be named like so: <ul><li>**Primary_weapon**</li><li>**Secondary_weapon**</li></ul>If the naming is not the following they will always be visible on the model.  For cases such as shields you can call them whatever you wish. </br></br>The primary weapon animations are linked in the **“`descr_model_battle.txt`”** files, with the order of skeletons listed

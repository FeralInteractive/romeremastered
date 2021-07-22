![Workshop_header_template](/Workshop_header_template.png)
# Campaign Map Tool - Mesh Generation

## Table Of Contents

* [Introduction](#Introduction)
* [Making a new Campaign map geometry](#making-a-new-campaign-map-geometry)
    * [Generating a new campaign mesh in Blender with Displacement Modifier](#generating-a-new-campaign-mesh-in-blender-with-displacement-modifier)
    * [Alternative methods to create a campaign map](#alternative-methods-to-create-a-campaign-map)
 * [River and Coastline meshes](#river-and-coastline-meshes)
 * [Blender Tool to generate map chunks](#blender-tool-to-generate-map-chunks)
    * [Slice Tool](#slice-tool)
    * [Scene Root Tool](#scene-root-tool)
    * [Export Tool](#export-tool)
 * [Substance Tool](#substance-tool)


## Introduction

On this page you will find details of how you can create a fully custom map for Rome Remastered using Blender. This will allow for a very customised and detailed map but will also require more time than an automatically generated map.

The [IWTE](https://wiki.twcenter.net/index.php?title=IWTE) tool by WildDog has a beta feature that will generate a mesh map that might be an quicker option if you don't require the level of customisation a manual process provides.

## Making a new Campaign map geometry
To make a new campaign in Rome Remastered you will need all files you used with the original game (refer to existing guide for them) plus a campaign map geometry, textures, a river mesh, and a coastline waves mesh. You can generate all the components however you like. Next there will be some examples.
</br>

### Generating a new campaign mesh in Blender with Displacement Modifier
One pixel in `map_regions.tga` is going to be 1 meter inside Blender. Make sure Blender is set up to use **metric units**. First of all we will need a height map. We can create this however we want (with photoshop for example). Then we will create a map with the Array and the Displacement modifiers. In the end we will modify the height map we used to how the game expects it. We will create a **150x100** meter map.

![Plane - Campaign Map Tool Image](/tools/CampaignMapTool/images/CampaignMapTool_Plane.png)

Start creating a 1 meter plane. Offset it in edit mode by 0.5m in both x and y direction so the origin will sit on the bottom left corner in `(0,0,0)`.

![Properties Pane - Campaign Map Tool Image](/tools/CampaignMapTool/images/CampaignMapTool_PropertiesPane.png)

Add 2 Arrays modifiers: the first one for the **`x`** size and the second one for the **`y`** size. Make sure to check the Merge checkbox to generate the map as a single continuous mesh piece. Apply both of them.

![UV Unwrap - Campaign Map Tool Image](/tools/CampaignMapTool/images/CampaignMapTool_UVUnwrap.png)

And UV unwrap the mesh from orthographic top view using `Project from View (Bounds)`.

![Displacement Modifier - Campaign Map Tool Image](/tools/CampaignMapTool/images/CampaignMapTool_DisplacementModifier.png)

Use a Displacement modifier with your height map to generate the whole campaign map. Modify the Strength parameter as you like.

![Texture Image - Campaign Map Tool Image](/tools/CampaignMapTool/images/CampaignMapTool_TextureImage.png)

In the Texture image setting set the Color Space to `Linear` and the Mapping Extension to `Extend`.

![Height Map Example - Campaign Map Tool Image](/tools/CampaignMapTool/images/CampaignMapTool_HeightMapExample.png)

As an example this is the result using the heightmap shown in the above picture.

In this example for a map of 150x100 meters, you can use a height map of any dimension as long as the ratio is the same as the map size. In the end you will scale `map_heights.tga` twice the size of `map_regions.tga` **+1** as you would for Rome classic. You can also put in this height map your river shapes if you want. We will now convert this map into what the game expects. First thing, convert the map to a 150x100 size (for your example). Then use a level tool to make the ocean completely black.

![Colour Levels - Campaign Map Tool Image](/tools/CampaignMapTool/images/CampaignMapTool_ColourLevels.png)

Now paint the ocean blue `(0,0,253)`.

![Blue Ocean Heightmap - Campaign Map Tool Image](/tools/CampaignMapTool/images/CampaignMapTool_OceanBlueHeightmap.png)

</br>

### Alternative methods to create a campaign map
Other methods to generate the campaign map are possible. </br>
You can first generate the mesh however you like to the dimensions you like. You can sculpt it, model it, or use a specific tool to generate terrain like Houdini, Terragen or Instant Terra. After you have your terrain geometry you can bake the height map and convert it to the game format.

## River and Coastline meshes
Currently Rivers and Coastlines will have to be made manually.

![Rivers and Coastline meshes - Campaign Map Tool Image](/tools/CampaignMapTool/images/CampaignMapTool_RiverCoastlineMeshes.png)

Both meshes are polygon strips unwrapped so they use the all UV space vertically and extend as much as needed in the horizontal direction. The base of the texture points to the land for coastlines (otherwise waves will go backwards). In the case of rivers the direction does not matter. I suggest using the spline tool and converting the strips to geometry. Coastlines meshes can all stay flat at sea levels. Rivers will have to follow the geometry elevation.

## Blender Tool to generate map chunks
*This Blender tool is being maintained for Blender version 2.92.*

| | |
| -| - |
| Feral Blender Add-on to process and export a campaign map geometry. Both export functions will align the pieces to the Rome world space, export an fbx and re-align the piece to the Blender space. If you export a piece manually make sure to: rotate the piece by 180 degree around the origin and apply the rotation before exporting. Use the [Casconv tool](../CasPacker/casconv.exe) to convert to a cas file.| <img src="https://github.com/FeralInteractive/romeremastered/blob/e555b8b1917ca4f21eabc6974c19c88a42fd0260/documentation/Images/CampaignMapTool_FeralCampaignTools.png" width="1000">|

### Slice Tool
Save your file. Select your campaign mesh and set how many pieces you want to slice it. Try to get the pieces as square as possible. The slicing process will also UV unwrap each piece to use the full 0-1 UV space. If the slice tool is taking a lot of time you may have forgotten to check the Merge function in the Arrays modifiers (and Blender will likely crash). To fix this enter `Edit Mode` and merge all vertices by distance (default settings should be fine).

### Scene Root Tool
Select all your campaign pieces and add a scene root for each piece, or group all your pieces under a single scene root. It’s up to you what you prefer.

### Export Tool
If you grouped all the pieces under a single root you can use the `Export from Single Root` function. This will export all the visible pieces under that scene root. The exported fbxs will be named as the piece name. If you have a scene root per campaign piece you can use the `Export Selected` function. Select all the scene roots you want to export and then press the button.

## Substance Tool
This is a Substance tool you can use in [Substance Player](https://www.substance3d.com/substance-player/) (free from the substance website) to help generate base textures for all your pieces. These textures are not meant as finals and will likely suffer some alignment issues, but should be a good place to start testing.

![Substance Tool - Campaign Map Tool Image](/tools/CampaignMapTool/images/CampaignMapTool_SubstanceTool.png)

The reference texture is a color texture similar to the `map_ground_types.tga` used by the game, but used only as reference to generate new textures for the campaign. You will have to insert how many tiles there are in your campaign map and how many biomes. Currently **20** is the maximum. You can use the slider Biomes Blend Amount (not shown in the picture) to control how much biomes blend into each other. If some of your biomes occupy a small section of the map try putting them first in the list. The `Generate All` function is off by default. You can scroll through the tiles with the slider, see the result in the viewport and export a single tile.

To avoid having to export all tiles manually you can enable `Generate All`. This will use the animation feature of Substance Player to generate and export all your tiles. You will have to set a time (in seconds) to regenerate each tile. A value of 0.5 seconds is set by default, but this will depend on how many biomes you have and your hardware. Set the fps (bottom right corner) to 1/time. So in the case of 0.5 second to regenerate set fps to 2. You can play the animation to check you see all your tiles.

![Biome Texture Fill - Campaign Map Tool Image](/tools/CampaignMapTool/images/CampaignMapTool_BiomeTexture.png)

For each biome you will have a texture section to fill. I suggest having your reference texture open by your side (using [pureRef](https://www.pureref.com/) would be the easiest way) and color pick the color of your biomes. Then add an Albedo texture and a Material texture for it. A material texture is the texture used for pbr rendering of the campaign. It packs `Normal`, `Roughness` and `AO` all in one texture. Start from a normal map. Replace the Blue channel with your Roughness textures. Add an alpha channel and place an inverted Ambient Occlusion texture. If you don’t have these textures you can use RGBA `(128,128,255,0)`. These values are a flat normal, full roughness and no AO.

![Export - Campaign Map Tool Image](/tools/CampaignMapTool/images/CampaignMapTool_Export.png)

When you hit export you will have to set the Fps of your animation and the Count. The count is going to be the number of tiles you have. In the base name pattern make sure to include `####` so that each texture will have the frame number in the name. The pattern dropdown list includes all possible patterns you can use in the name. You are not forced to use them if you don’t want to with the exception of `####`.

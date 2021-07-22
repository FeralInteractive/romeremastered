![Workshop_header_template](/Workshop_header_template.png)
# Buildings

## Table of Contents

* [Battle Map](#battle-map)
* [Campaign Map](#campaign-map)
   * [Settlements/Wonders](#settlementswonders)
   * [Walls](#walls)
   * [Resources](#resources)
   * [Trees/Vegitation](#treesvegitation)

## Battle Map


| Concept | Details |
|-|-|
| **Tenements**| Tenements work the same way as they did in OG. We increased the number of variations (e.g. `roman_tenamentA` in OG has been replaced by `roman_tenamentA1` to `A5`). Note: we kept the spelling mistake in those models.|
|**Props**| Props are placed within tenements. Are defined the same way as any other buildings model (item file). To spawn in the correct tenement thay are simply added to the item list in the appropriate dbb text file. </br></br> ![Props Image](/documentation/techart_guides/Images/Props_Image.png) </br></br> We also separated props in category by dimensions and can end in `_big`, `_medium`, `_small`. Based on the building graphic setting the game will spawn some, or all of them. </br></br> **Ultra:** all visible </br> **High:** small not visible </br> **Medium:** small and medium not visible </br> **Low:** none visible |
|**Buildings**| Buildings work the same way as OG.|
|**Textures**| Textures for buildings are **albedo**, **normal**, **metallic**, **roughness** and **displacement**. Naming convention follows the on from OG.</br></br> **Albedo:** `texture_name.tga` </br> <li>Missing albedo will result in pink color. </br> ______________________________________________________________ <br/> **Normal:** `texture_name_n.tga` </br> <li>This can be a 3 channel tga, or 2 channel dds. Missing normal will result in shiny surfaces. </br> ______________________________________________________________ <br/> **Metalness:**  `texture_name_m.tga` </br> <li>Missing metalness will result in using a default black texture </br> ______________________________________________________________ <br/> **Roughness:** `texture_name_s.tga` </br> <li>Missing roughness will result in using a default gray texture </br> ______________________________________________________________ <br/> **Displacement:** `texture_name_d.tga` </br> <li> Grayscale textures used for parallax occlusion. Think of it as an inverted height map. White values are the base and black values are the one “extruded”. In the game this feature is not used, but is fully implemented in code and working. A missing displacement texture will result in the feature not being used.


## Campaign Map
### Settlements/Wonders

The logic behind Settlement and Wonder models seen in-game have been unchanged from OG Rome, the models and textures used have simply been updated.

The method of updating/altering these models remains the same as it was previously, with scenes within your 3D modelling software of choice requiring a locator / point object /empty named ***`Scene_Root`***, containing your 3D model.

![Settlement/Wonder Image](/documentation/techart_guides/Images/Blender_SettlementWonders.jpg)

The Settlement models are split between 3 cultures, Roman, Eastern, and Barbarian (shortened to Barb in data), with Greek and Roman making use of the same Settlement models, as in the original release, this differs when compared to walls, in that there are Greek varieties of walls.

### Walls

Similar to settlements, walls on the campaign map are currently split between 4 cultures, `Roman`, `Greek`, `Eastern`, and `Barb`. They are currently configured so that certain wall types are shared between cultures (keep this in mind when adjusting settlement layouts, as to avoid geometry clipping between the two models, keep both model types handy for size reference!).

Wall models in-game follow the same rules as Settlements and Wonders, in regards to scene layout and export from `.fbx` to `.cas`

### Resources

Resources within the game are interesting, as we’ve made a slight change to how they appear in-game when compared to OG Rome: Total War.

In Total War: Rome Remastered, a number of the most commonly occurring resources now have **3** model types, as opposed to **1** as seen in the original game. This was introduced with the intention of reducing ‘clutter’ on the campaign map, improving readability. For example, there now exists 3 models for `resource_wine`, each one signifying a different quantity of a resource in-game (pictured below).

![Resources Image](/documentation/techart_guides/Images/Blender_Resources.jpg)

The idea is that where you would before find 2 or 3 `resource_wine` models within a close proximity on the campaign map, you will now see 1 model in its place which will signify a greater quantity of wine, such are `resource_wine_02` or `resource_wine_03`.

Alongside updating the 3D models, you now need to update **`descr_sm_resources.txt`** to ensure the changes take effect (only applies if the names of resources are altered).

### Trees/Vegitation

| Concept | Details |
|-|-|
| **Models** | Models are located in `terrain/aerial_map/tree_models`. There are no lods and backface culling is disabled. |
| **Textures** | Textures are located in `terrain/aerial_map/tree_models/textures`. Only the albedo with alpha is required. When converting textures for trees on the campaign map some trial and error are needed to find a good value for the alpha coverage used when creating mips (dds). </br></br>Use the option `-keepcoverage <number>` with number between `0` and `1`. It’s possible that different textures will need different values. In the current game good values have been between `0.85` and `0.95`. This is needed so alpha section of trees won’t disappear or look too thick when zooming out resulting in using a lower texture mip. |
| **Canopy** | For some trees there are canopy and normal trees. Canopy trees don’t have a trunk in the model to save on vertices since that won’t be seen anyway. Normal trees with trunk are placed automatically by the game at the edge forests. |

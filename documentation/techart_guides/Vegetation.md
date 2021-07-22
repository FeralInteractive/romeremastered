![Workshop_header_template](/Workshop_header_template.png)
# Vegetation

| Concept | Details |
|-|-|
| **Lods**| There are 3 LODs setup for trees starting from **`lod0`** (highest) to **`lod2`** (lowest)|
| **UVs**| To remove foliage from trees during a game, tree foliage needs to be offset in the **U** direction in UV space by 1. UVs can extend out of the 0-1 space as much as they want in the **V** direction. </br></br> ![Vegetation UV Image](/documentation/techart_guides/Images/Vegitation_UV_image.png)|
| **Models folder**| Models folder is “`models_vegetation`”. </br> There is also a texture subfolder, but this is not used to my knowledge. |
| **Textures folder**| Textures used by the game are located in “`vegetation/textures`”. |
| **Regeneration of files**| Vegetation works the same way as the OG. After adding/modifying trees to the appropriate text files and update the cas file in the model folder, delete all `.vege` files in “vegetation” along with all the sprites in “vegetation/sprites”. Delete the file “`descr_vegetation.db`” and run the game. The game will regenerate all `.vege` files and sprites (in tga format). If you want to have mips you can use `rome_texture_convert` to convert all these files to dds. |
| **Sprites to DDS**| Both albedo and normal need to be converted as if they were albedo textures. These can be converted to dds, or dds-lz4. They need to end with `.tga.dds` if converted to dds. </br></br> `textureCompress.exe -in-albedo /path/to/tgas -out /path/to/output -ft dds -sx .tga` |

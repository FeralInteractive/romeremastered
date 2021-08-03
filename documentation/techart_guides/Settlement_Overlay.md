![Workshop_header_template](/Workshop_header_template.png)
# Settlement Overlay

## Keywords and Usage
Meshes inside a settlement overlay can use different keywords that affects their behaviour from a rendering point of view.

### Ordered
The word ordered followed by a 2 digit number (e.g. ordered01) is used to specify the render order of different meshes. Bigger numbers are rendered last. This is a way to fix z-fighting between overlapping meshes.
For example if the are 3 mesehs in an underlay called *ordered01 - mesh\_a*, *ordered02 - mesh\_b*, *ordered03 - mesh\_c* the game will render them in order starting from *mesh\_a*, then *mesh\_b* and last *mesh\_c*.

### Grid
The word grid followed by a 2 digit number (e.g. grid01) is used to tile a specific amount of time the texture assigned to the mesh. The only possible numbers are the one defined in *descr\_landscape\_global\_uv\_grids.txt*. Fro each grid defined in this file a tile value, an offset value and a rotation value can be set. The most common use case is stone streets that don't ahve any alpha blend with the terrain.

### Detail
The word detail followed by a 2 digit number, an underscore and another 2 digit number (e.g. detail02\_03) is used to combine the alpha of the texture assigned to the mesh with a tiling texture. The first number acts the same way as the number for the grid keyword. The second number is used to reference a texture in *descr\_landscape\_multi\_textures.txt*. The game will tile the texture defined in the file as many time as defined by the grid value, but it will use the alpha of the texture assigned to the mesh without any tiling. The most common use case is muddy roads in settlements that use alpha blends with the terrain underneath.
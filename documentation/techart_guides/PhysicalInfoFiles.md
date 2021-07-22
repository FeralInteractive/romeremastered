![Workshop_header_template](/Workshop_header_template.png)
# Physical Info Files

## Table Of Contents

* [Table Of Contents](#table-of-contents)
* [DATA ENCODED INTO PHYSICAL INFO FILES](#data-encoded-into-physical-info-files)
   * [General warnings:](#general-warnings)
* [PERMITTED GEOMETRIES](#permitted-geometries)
   * [Collision outlines and volumes:](#collision-outlines-and-volumes)
   * [Tunnels](#tunnels)
   * [Platforms](#platforms)
   * [Spawn positions:](#spawn-positions)
   * [Entry ways:](#entry-ways)
   * [Banner positions:](#banner-positions)
   * [Arrow slots:](#arrow-slots)

## DATA ENCODED INTO PHYSICAL INFO FILES

### General warnings:
Export options can be tricky.  Some items require vertex colour data, so export that. Once exported, the geometries should remain separate and not have several merged into one.  

For collision outlines and tunnels, make sure there are no duplicated verts.  For
multi-level outline geoms (e.g. three-way tunnels), smoothing may have to be enabled to prevent multiple verts being generated for different planes.

## PERMITTED GEOMETRIES
### Collision outlines and volumes:
Geometry names starting with '`collision`'.  2D and 3D collision data.  3D collision data starts
'`collision_3d`'.
3D data is converted into a collision representation for projectiles and mouse interaction.  All 3D collision geometries in an info file are merged into one representation.  There is a mechanism to provide a default 3D collision volume, i.e. if no collision 3D geometries are found, it uses all the geoms in the supplied default model.  This is currently used in buildings so that the lowest lod models are always used.
Listing the info file in its `descr_building_battle` entry with an extra `no_3d_default parameter`
prevents the use of the default, eg: `physical_info no_3d_default <filename> `


2D collision geometries are projected to 2D, then have their outline traced to yield a clockwise connected loop.
Note that each geometry results in exactly one outline - disconnected outlines must be provided in separate geometries.  Vertices must be exact, and the vertex list for the geom should contain no duplicates.  The outline can be created in 3D, i.e. it need not all be in the same plane - however, when exported extra vertices will be added if the normals are not smoothed, causing the tracing code to fail, so **count your verts!**

### Tunnels
Geometry names starting with '`tunnel`'.

These are defined for either two-door or three-door tunnels currently.  The geometry should
project to a 2D outline of four sides or six sides for two-door and three-door tunnels respectively.
The shortest edge in the geometry is used to flag a door position, with alternate edges then
also being considered to be doors.  The sizes of the door edges dictate the sizes of the tunnel entry and exit areas, while the middles of the door edges are entry and exit positions.

Note the outlines should have four or six verts, and so the geoms should also only have four or six verts.

The entry direction for the door defaults to inward, i.e. from outside the outline to inside.
If the doorway is coloured with black verts, this flips the direction - used in siege towers.
Entry vector is 2D.

At this level, the tunnels are any-to-any tunnels.  In `battle_map`, they get added as multiple
single-direction tunnels.

### Platforms
Geometry names '`platform_N_<edges>`' for `N` 0-9.  The names must have an edge-specifier part at the end, which labels platform edges as hard (obstructed), soft (can fall off), and clear (allowed to pass over).

The geometry has its outline traced, and one edge must have verts that are black at both ends, flagging it as the front edge for the platform (required for soldier positioning and other reasons).  The edge specifier consists of **`H`**, **`S`** or **`C`** for **h**ard, **s**oft and **c**lear, and dictates the edge status in a clockwise order starting with the front edge.
E.g. a straight wall segment may have a hard front, soft back, and clear elsewhere.  So, the platform would be called `platform_0_HCSC`

Soldier positions on platforms are also specified in geometries.  The positions are given as slot rows, one for each rank.  Each rank is defined using a line and number of men along that line, which we encode as a single-triangle geometry using an isosceles triangle.  The first soldier position is the middle of the shortest edge, and the last is the opposite tip.  By default, the spacing is roughly one metre, but the total number of men for that slot can be specified in the geometry name, as can details of the nature of each slot position - each position can be given info as to whether its covered, half-covered, or open, defaulting to open.

Geometries for slot rows are named '`slot_platform_N_M<_options>`'. The **`N`** refers to the platform it is for, e.g. `platform_0` has slot rows called `slot_platform_0...`  The **`M`** refers to the rank of the slot row, with **`0`** being the front rank.  Direction of the triangle doesn't matter.  The row number **`M`** **CAN** be multiple digits.

The optional part can contain a number of men, and/or an open/covered specifier.  The number of men can be any number of digits, but the value must be at least **2**.  The open/covered specifier consists of **`H`**, **`C`**, and **`O`** for **h**alf-covered, **c**overed and **o**pen.  These values are repeated, so **`HO`** will flag alternate slots positions as half-covered and open.

Eg, `platform_0` could have `slot_platform_0_0_10_HHO` as its front rank of 10 soldiers, flagged as `HHOHHOHHOH`.

Tests for validity include rank order - bigger rank should mean farther from the front edge.

### Spawn positions:
For ambient spawning.  These are named '**spawn**' or '**respawn**'.  '**spawn**' positions are battle-start only.
</br> '**respawn**' can be used throughout the battle.  They are encoded as isosceles triangles, with the base centre being the creation position and the tip being the target after creation.

### Entry ways:
An entry consists of a muster position and a set of entryways.  Each entryway consists of start and end and a number of waypoints (possibly zero).  Start is outside the building, the end is inside.

These are encoded as follows.  The muster position is a simple geometry starting ‘`muster_`’.  It should be followed by a one-digit number so that entryways can be associated with it.  The centre of the geometry is used as the muster position.  

For a given muster point e.g. '`muster_0`’, entryways are defined as '`entry_0`'.  Multiple entryways for the same muster point should be called '`entry_0_0`', '`entry_0_1`' etc.  Entry geoms must consist of a simple outline defining a directed line.  Required features:  
* odd number of faces and verts;
* number of verts = number of faces + 2;
* all verts must appear in the traced outline (note same conditions for outlines as for collision outline - no duplicated verts).  

The line is defined by a single triangle at one end of a list of quads, like a pointy-headed worm. If there's only the triangle, it has to be isosceles to flag which way it's pointing.  The tip of the head, then each edge centre of the linked quad sides, are used to define the line.  See an example to clarify this.

A building can have multiple entryways.

### Banner positions:
When a unit hides in a building then it's banner is displayed on top of the building.  The 'banner' geometry specifies at what point on the building to show the banner

### Arrow slots:
Arrow slots are defined for towers. Each arrow slot should have an '`arrow_horizontal_x`' and '`arrow_vertical_x`' geometry. </br>
Where the **x** is a single digit to specify which slot number.  The two geometries should be simple isosceles triangles with a shared point to specify the weapons position (just inside the slot), and the angle of both geometries at that point describing a field of view for the weapon.

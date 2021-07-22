![Workshop_header_template](/Workshop_header_template.png)
# Destruction

## Table Of Contents

* [Table Of Contents](#table-of-contents)
* [Warmachine Destruction](#warmachine-destruction)
   * [Warmachine - 01 CREATING YOUR DESTRUCTION FILE](#warmachine---01-creating-your-destruction-file)
   * [Warmachine - 02 CONVERTING YOUR DESTRUCTION FILE TO CAS](#warmachine---02-converting-your-destruction-file-to-cas)
   * [Warmachine - 03 UPDATING THE GAME FILES](#warmachine---03-updating-the-game-files)
* [Wall](#wall)

## Warmachine Destruction

### Warmachine - 01 CREATING YOUR DESTRUCTION FILE
Create your destruction animation by simply keyframing geometry nodes whist keeping the hierarchy structure.
We have provided a example blender scene with destruction test asset, you can download that here: [warmachine_destruction_example.blend](/documentation/techart_guides/Images/warmachine_destruction.zip).

![Destruction Test](/documentation/techart_guides/Images/destruction_test.png)

* `warmachine_destruction_example.blend` was created using blender version 2.93.0
* The node hierarchy should be as follows:
        'Scene_Root' ('Empty' node)
        >    'pack' ('Empty' node)
            >    *destruction_pieces ('Geometry' nodes - can be named as you wish)

![Destruction Test](/documentation/techart_guides/Images/blender_scene__warmachine_destruction_example.png)

* There can only be a total of 64 nodes in the file (including the "Scene_Root" and "pack" nodes).
* Translate and Rotate keys are supported.
* Make sure your apply the Rotation & Scale transforms (rotation should  0 at the start of the animation and scale should be 1)
* Geometry with different materials should be split into different meshes.

![Destruction Test](/documentation/techart_guides/Images/dead_model.png)

* In game animations are 20fps (keep this in mind while animating)
* You do not need an armature for the destruction as the 'casconverter' can calculate missing bones
* You should take the last frame of your animation and export that as a static mesh with no animation keys.
 * This for the dead version of your model (which gets swapped out after the animation has finished).
 * You may want to delete geometry pieces which will be under the floor to optimize the file.
* Animations in game must end on a odd number
 * The 'casconverter' will simply remove the last keyframe if an even number

![Destruction Test](/documentation/techart_guides/Images/destruction_in_blender.png)

### Warmachine - 02 CONVERTING YOUR DESTRUCTION FILE TO CAS
Once you have exported out your destruction animation as a fbx you will need to cas convert it.
This should work fine:

    `casconv.exe -i ./file.fbx -o ./file.cas --calculate-missing-bones`

**NOTE** `--calculate-missing-bones` is not needed for the dead version (as there is no animation)

### Warmachine - 03 UPDATING THE GAME FILES
There are a few files which will need updating:

* Reference hierarchy model (`\data\models_engine\`) - You can just copy your destruction animation file for this
* Destruction animation (`\data\animations\engine\tower\`) - This is your destruction animation file
* Dead model (`\data\models_engine\`) - A static mesh of the dead model, this will be swapped after the animation has finished (remember to make sure meshes are broken up by material assignment)

The siege tower files are as follows:

**heliopolis**:
* Reference hierarchy model (helio'_dying_model.cas)
* Destruction animation (helio'_dying_anim.cas)
* Dead model (helio'_dying_dead.cas)
**small tower**:
* Reference hierarchy model (small_tower_dying_model.cas)
* Destruction animation (small_tower_dying_anim.cas)
* Dead model (small_tower_dying_dead.cas)
**small tower**:
 * Reference hierarchy model (mid_tow_dying_model.cas)
 * Destruction animation (mid_tow_dying_anim.cas)
 * Dead model (mid_tow_dying_dead.cas)

**Notes:**
* Updating the normal animations are very similar to this.  Just make sure you update the normal model and use their skeleton.
* Rigged warmachine usually are not skin bound, each piece is parented under the relivate bone.
* While testing the animation, we suggest simply update the normal model and idle animation.  This will save you having to destroy the tower and the animation will loop.
* The game must be relaunched when updating animation files.


## Wall
Walls work in the same way as they did in OG.

| Concept | Details |
|-|-|
| **Models** | Models are located in “`models_buildings/models_walls`”. There are 2 LODs: **high** and **low** for static models. Animated models and destroyed models have only 1 LOD. The geometry for a piece needs to be parented to an empty/locator called *`Scene_Root`*. |
| **Textures** | Textures follows the same rules as buildings. |
| **Animated models** | Animated models refers to the destroyed bits of wall that animates. </br></br> Differently from OG we can convert an animated fbx to an animated cas file without the need of a skeleton. If the animation is saved in the mesh piece we can use a special flag on the casconv. Animated pieces still need to be parented to an empty/locator called *`Scene_Root`*. </br></br> *`casconv.exe --calculate-missing-bones -i input_file`* |
| **Info file** | Each wall section has its own physical info file. </br> On walls they are used to define collision for pathfinding, collisions for camera and projectiles, define areas where units can stand on and traverse, and sap point attachment. On gateways they also define where arrows spawn and ram attachment. </br></br> Refer to the [Physical Info Files](PhysicalInfoFiles.md) section for more detail. |
| **Spot_fx** | Spot_fx on gateways are used to place flags and oil jets. For them to work the origin of the mesh is what counts for the placement. Geometry pieces need to be parented to an empty/locator called *`Scene_Root`*. When converting them to a cas file use the flag *`--calculate-missing-bones`* so the game will place them in the correct place. |

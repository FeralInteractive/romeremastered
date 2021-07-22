![Workshop_header_template](/Workshop_header_template.png)
# movie_cam - Replay battles with custom camera movement

## Table Of Contents

* [How to Use the Battle Replay “Movie-Cam” Feature](#how-to-use-the-battle-replay-movie-cam-feature)
* [How to enable](#how-to-enable)
* [Using Movie-Cam](#using-movie-cam)
   * [Normal Controls](#normal-controls)
   * [Replay Controls](#replay-controls)
* [Quick Controls Guide](#quick-controls-guide)
   * [Most Useful Controls](#most-useful-controls)
   * [Other Controls](#other-controls)
* [Working examples](#working-examples)
   * [Set up a camera shot using two keyframes:](#set-up-a-camera-shot-using-two-keyframes)
   * [Create a “hard-cut”:](#create-a-hard-cut)
   * [Change the speed of the camera between two keyframes:](#change-the-speed-of-the-camera-between-two-keyframes)
* [Important notes:](#important-notes)

## How to Use the Battle Replay “Movie-Cam” Feature

The Movie-Cam feature allows you to manipulate and pre-program the camera movement during a Battle Replay to essentially let you setup and then replay keyframed camera shots to create visuals that can be used in custom intro videos or for YouTube etc.

Camera movements are recorded as “keyframes” and are able to be saved to a replay file which can then be recalled later on. After keyframes have been set, pressing “preview” will cause the camera to move from one keyframe to the next in chronological order. Camera movements can either be smooth transitions (e.g.: 1>2>3>4) or hard cuts (e.g.: 1>2, 3>4).

The controls are largely unchanged from the original Rome:Total War so any online guides or experience with the original game will also be useful for Rome Remastered. We also highly recommend spending some time getting used to the system making practice shots/footage before jumping into trying to create final footage.

## How to enable

 * Launch Rome to the PGOW
 * Select the Advanced Tab and enter ```-movie_cam```
 * Load desired battle replay
  * If none available, create a battle replay first

![PGOW](/documentation/feature_guides/images/PGOW.jpg)  

## Using Movie-Cam
Once loaded into the replay, you will notice a timeline along the bottom, and control prompts listed on-screen.

### Normal Controls

![NormalControls](/documentation/feature_guides/images/NormalControls.jpg)  

### Replay Controls

![ReplayControls](/documentation/feature_guides/images/ReplayControls.jpg)


## Quick Controls Guide

### Most Useful Controls

|Key|Action|Explanation|
|---|------|-----------|
|`N`|Toggle movie-cam/camera controls|Due to overlapping WASD key usage, the camera cannot be controlled simultaneously with the movie-cam controls. This control swaps between the two modes.|
|`BACKSPACE`|camera.preview|Previews all keyframes from the beginning (without resuming battle playback).|
|`ENTER`|camera.toggle_playback|This key will begin real-time playback of the replay and keyframes. Use this to start playback of the replay, and after setting all keyframes to view your finalised sequence when recording. Pressing this with no keyframes added OR when at the current timeline position, this will resume the playback. Pressing this at the beginning of the timeline after loading [L] your camera  file will start playback of all keyframes with battle playback.|
|`Y/INS`|camera.add_key(false) (key frame as a smooth transition)|Adds a keyframe. A keyframe records the information for the current placement and orientation of the camera at the current timeline position. Can only be placed while battle playback is running (i.e.: cannot be placed whilst replay is paused). Upon previewing saved keyframes the camera will smoothly transition between them in sequence.|
|`END`|camera.add_key(true) (key frame as a cut)|If you do not wish to have a smooth transition between two keyframes (i.e.: a hard cut), use this key when highlighting your desired keyframe to place the cut to remove the smooth transition effect.|
|`DEL`|camera.delete_current_key|Deletes highlighted keyframe|
|`SPACE`|camera.toggle_free_cam|Pause replay playback and show the movie-cam UI again **or** if already paused, will preview all keyframes from the current timeline position (without resuming battle playback)|
|`[`|camera.prev_key|Skips to the previous keyframe on the timeline.|
|`]`|camera.next_key|Skip to the next keyframe on the timeline.|
|`,`|camera.advance_key_time(-0.1f) (move the time position of the current key)|Nudge keyframe backward on timeline. This can be used to edit the time between two keyframes (i.e.: speed of a shot).|
|`.`|camera.advance_key_time(+0.1f) (move the time position of the current key)|Nudge keyframe forward on timeline. This can be used to edit the time between two keyframes (i.e.: speed of a shot).|
|`L`|camera.import_cam|Load movie-cam file data|
|`S`|camera.export_cam|Save current keyframes to movie-cam file|
|`R`|handler_replay_reset (reload/restart)|Restart battle (ensure to save [`S`] keyframes before doing this)|


### Other Controls

List of other actions that are possible, but have less utility or are less frequently used for most video creation.

|Key|Action|Explanation|
|---|------|-----------|
|`T`|camera.toggle_target_cam|Alters camera rotation behaviour from default to “orbit” the cursor instead.|
|`Q`|camera.select_final_keyframe|Jumps to last keyframe in the timeline|
|`E`|camera.toggle_ease_current_key|This sets the current keyframe to “ease. This seems to help in smoothing out transitions between keyframes even further, and can also help in preventing the camera from clipping through geometry.|
|`HOME`|camera.advance_to_game_time|Fast forwards the battle replay to the current keyframe (cannot be used to rewind).|
|`U`|camera.update_key (update current key with free cam data)|Can be used to update the highlighted keyframe with new camera data.|
|`W`|camera.toggle_widescreen|Bit of a legacy feature given the Remaster supports wide and uktrawide natively, will affect the width of the skybox if used.|
|`I`|camera.cycle_replay_timeline_mode (none/full/zoom)|Toggles 3 zoom levels for the timeline.|

## Working examples

### Set up a camera shot using two keyframes:

1. Use camera controls to set camera to desired starting location/orientation
2. Toggle to movie-cam controls [`N`]
3. Resume battle playback [`ENTER`}
4. Insert keyframe [`Y`]/[`INS`]
5. Pause replay playback [`SPACE`} - not required but helpful to give you time to think/set up the next camera shot
6. Toggle to camera controls [`N`]
7. Position camera to desired end location/orientation
8. Toggle to movie-cam controls [`N`]
9. Resume battle playback [`ENTER`]
10. Once battle reaches desired position in playback (i.e.: whatever you’re looking to record has happened), insert second keyframe [`Y`]/[`INS`]

### Create a “hard-cut”:

Since by default all keyframes will smoothly transition from one to the next, it can be very useful to have a hard-cut between two shots (particularly if there is a large amount of time between one shot and the next).
For this example, let’s say you have two shots “Shot A” and “Shot B”. You wish to have a hard cut from Shot A into Shot B

1. Set up Shot A and Shot B using keyframes
2. Use `[` to skip through the timeline to the keyframe you wish to hard cut from
3. When desired keyframe is highlighted (appears yellow on the timeline) press [`END`]
4. You will see the red line connecting the two keyframes on the timeline disappear, a hard cut has now been created.

**Note**: It is not possible to undo this action, so just be sure you have highlighted the correct keyframe or you may need to delete the shot and start afresh.

### Change the speed of the camera between two keyframes:

If after setting up a shot between two keyframes you find the camera moves too slowly/fast between them, you can adjust the speed on the timeline without needing to retake the shot. This is done by moving the keyframes themselves either closer together (to speed up) or further apart (to slow down).

For this example, we will move the end-point of a shot to increase the speed of the camera, however this can work with the start-point as well. Just be aware that this will obviously affect where the shot starts/ends.

1. Using `[` or `]` navigate the timeline to highlight the end-point keyframe of the shot you wish to adjust
2. Hold `,` to move the keyframe on the timeline closer to the start point
3. This will increase how fast the camera moves from start-to-end. Note however this will mean the shot ends sooner than first established.
 1. Alternatively, use `.` to slow down the camera

**Note**: After adjusting a keyframe, previewing it immediately with [`BACKSPACE`] or [`SPACE`] will not correctly display the new camera speed (it will show as the same speed at first, then speed up/slow down right at the end until the battle replay has been reloaded [`R`]. Be sure to save [`S`] your adjustments before reloading!

## Important notes:

Since battle playback cannot be rewound, you will need to restart the battle [`R`] if you wish to preview any additional shots made with the correct battle timeline. You can preview the camera movement alone (i.e.: independent of the actual battle replay) using [`BACKSPACE`] to preview the entire sequence from the beginning, or [`SPACE`] to preview from the current playback point in the timeline.

Rome only ever stores **one** camera file at a time, which is overwritten with every press of save [S]. **Once happy with your camera placements, ensure to backup and name your replay file!**

The camera file is found within the Replays folder within the game’s preferences. These can be found at the following path:
```C:\Users\[USER]\AppData\Local\Feral Interactive\Kraken\VFS\Local\VFS\Rome\replays```

The file itself is called `replay.cam` by default. Copy and backup this file to a separate folder and name it something you’ll recognise.
If wishing to swap back to an older cam file, simply paste your backed up file back to the original folder, rename back to `replay.cam`  and load the corresponding replay in-game and use load [`L`] to load your cam file.

Mouse camera controls cannot unfortunately be used in movie-cam mode.

**Be patient!** There are times where the game can appear to pause for a while when loading previews, skipping through the timeline (e.g.: hard-cuts or using [`HOME`] key to fast-forward) and other areas;  but it should recover in short order.

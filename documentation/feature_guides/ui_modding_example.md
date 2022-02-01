![Workshop_header_template](/Workshop_header_template.png)
# Modding Total War Rome REMASTERED UI

## Table Of Contents
   
   * [Introduction](#introduction)
      * [Step One - Resize and reposition the background frame.](#step-one---resize-and-reposition-the-background-frame)
      * [Step Two - Altering the animation](#step-two---altering-the-animation)
      * [Step Three - Positioning the child elements](#step-three---positioning-the-child-elements)
      * [Step Four - You're Done](#step-four---youre-done)
   
## Introduction

An example mod has been created that displays what can be done by modding the UI.

The example mod can be found here: https://github.com/FeralInteractive/romeremastered/blob/main/example_mods/UI_Battle_Large_Unit_Info.zip

Before: ![ui_mod_before](/documentation/feature_guides/images/ui_mod_before.png)

After: ![ui_mod_after](/documentation/feature_guides/images/ui_mod_after.png)

Steps to (re)create this mod:

### Step One - Resize and reposition the background frame.

In this case the frame and its child elements are modified in different files.
The background frame can be found in `data/ui_overrides/battleui.pos` and is called `"animated_frame"`

Our first change should be resetting the frames position `("x": 0, "y": 0)`, this makes it much clearer as to what our following changes actually affect.

Closed: ![ui_mod_before](/documentation/feature_guides/images/ui_mod_closed.png)

Open: ![ui_mod_after](/documentation/feature_guides/images/ui_mod_open.png)


(All images will be shown in the “closed” state from now on unless stated otherwise)

Next, as we want the background to appear from the bottom center of the window, we first change the anchor point to the bottom center of the screen (`"anchor": "BC"`)
Also, as we want the background to be central on the screen, we set the align point to be bottom center (`"align": "BC"`). This means that whatever position we specify for the frame, that point will be the top centre of the frame. We will change this again later, but having it set to this is useful while developing.

![ui_mod_after](/documentation/feature_guides/images/ui_mod_center.png)


We can now resize the frame to our liking. (The example mod has a width of 1140 and a height of 1020).

**TIP:** I recommend being set to 120% UI scaling while altering UI. This way you dont resize elements in 100%, only to later find that they go off the screen on 120%!
If all has gone well, your UI should now look something like this:

![ui_mod_after](/documentation/feature_guides/images/ui_mod_center_large.png)

If you are happy with how the frame looks (ignore the child element for now), then change the alignment to "TC" from "BC" so that the frame is hidden by default.

Original:
```
        {
            "comment": "Unit_Info Frame",
            "name": "animated_frame",
            "x": -395,
            "y": -163,
            "size" : {
                "width": 385 ,
                "height" : 455
            },
            "anchor": "CL",
            "align": "TL",
            "priority": -1
        },
```
Modified:
```
        {
            "comment": "Unit_Info Frame",
            "name": "animated_frame",
            "x": 0,
            "y": 0,
            "size" : {
                "width": 1140 ,
                "height" : 1020
            },
            "anchor": "BC",
            "align": "TC",
            "priority": 1
        },
```


### Step Two - Altering the animation

We have have a bigger and central frame now, but it still slides to the right and we cant see it! Lets fix that.
For this, we need to alter `feralui.anims`

Our changes to this file are simple, we want to change the direction of the animation and how much it moves. The animation we want to change is `battle_ui_unit_info_frame_show`.
The default animation causes the frame to slide 372 units in the x axis and none in the 0, resulting in it sliding to the right.
As we only want the frame to slide upwards (y axis) so that we can see it, lets reset the `x` value to 0, and test some `y` values until we are happy with how far the panel slides up.
NOTE: The coordinate system uses the top left as `(0, 0)`, so to move upwards, the `y` value must be negative
(As the intention is for the panel to appear "attached" to the bottom of the screen, I would recommend you make the frames height slightly longer than what will appear on screen)

If all has gone well, your UI should now look something like this:

Closed: ![ui_mod_before](/documentation/feature_guides/images/ui_mod_closedv2.png)

Open: ![ui_mod_after](/documentation/feature_guides/images/ui_mod_openv2.png)





Original:
```
    {
        "name":"battle_ui_unit_info_frame_show",
        "end_pos": {
            "x": 372,
            "y": 0
        },
        "duration": 450,
        "timeout": -1,
        "relative":true,
    },
```

Modified:
```
    {
        "name":"battle_ui_unit_info_frame_show",
        "end_pos": {
            "x": 0,
            "y": -920
        },
        "duration": 450,
        "timeout": -1,
        "relative":true,
    },
```

### Step Three - Positioning the child elements

Now that we have our frame correctly sized, positioned and animated, its time to reposition and resize the child elements.

The child elements can be found at ```data/ui_overrides/battleuiunitinfo.pos```.

Our first port of call should be to get all of the elements visible on the panel at once. To do this is easy, simply remove all the `"tags": [...]` lines from the elements. Tags tell the code which elements should be visible/hidden when an action occurs. An element with no tags is visible by default.



Now that everything is visible, we can start resizing and repositioning the various elements. This can be done in the same way as we handled the frame, by altering the `x`, `y`, `width` and `height` parameters.

(I have also hidden the description toggle button as its no longer needed. There are multiple ways of doing this, you can use the "hidden" tag, or simply move it far off screen (e.g. `"x": -100000)`.)

We should now have something looking like this:

![ui_mod_openv3_messy](/documentation/feature_guides/images/ui_mod_openv3_basic.png)

While this looks pretty decent, there are still improvements we can make.

For starters, we can scale up the text elements to make better use of the increased space and make them easier to read. This can be done by altering the font the various elements use (see **Fonts** for the available fonts)

![ui_mod_openv3_messy](/documentation/feature_guides/images/ui_mod_openv3_fonts.png)

Increasing the font size of the title seems to have broken it though. Next we will fix that and properly centralise it.

To fix the title being offset, we simply have to grant it more space. To do this we can add a “size” tag and assign a width.
```
	"size": {
		"width" : 640,
	},
```

Next, we can use the "text_justification" tag. This lets us inform the game how we want the text to be justified. As we want it central, we will set it to "C". (You may need to reposition the title now that its being auto-centered)

![ui_mod_openv3_messy](/documentation/feature_guides/images/ui_mod_openv3_fonts.png)

Our next change is to fix the abilities list. While we have increased its width, the text isn’t making use of the new space. To fix that, we can use the "max_text_width" tag and set it just shy of the lists width (to prevent clipping).

![ui_mod_openv3_messy](/documentation/feature_guides/images/ui_mod_openv3_almost.png)


And with those additional changes we are done! 

### Step Four - You're Done

Your UI should now resemble something like this:

**120% UI Scale**

![ui_mod_after_120](/documentation/feature_guides/images/ui_mod_after_120.png)

**100% UI Scale**

![ui_mod_after](/documentation/feature_guides/images/ui_mod_after.png)

See the example mod for the full changes to this file, as there are too many to show here!

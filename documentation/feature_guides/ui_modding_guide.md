![Workshop_header_template](/Workshop_header_template.png)
# Modding Total War Rome REMASTERED UI

## Table Of Contents
   
   * [Introduction](#introduction)
   * [POS Files](#pos-files)
      * [Frames](#frames)
         * [Frame Tags](#frame-tags)
      * [List](#list)
         * [List Tags](#list-tags)
      * [Fonts](#fonts)
         * [Font Colours](#font-colours)
      * [Tags System](#tags-system)
      * [FeralUI.Anims](#feraluianims)
         * [FeralUI.Anims Tags](#feraluianims-tags)
      * [Possible Actions](#possible-actions)   
   
## Introduction

Rome REMASTERED UI falls under two main categories, the Main Menu UI, and the Campaign/Battle UI. This documentation will cover the Campaign/Battle UI.

## POS Files
The Campaign and Battle UI make use of the .pos file system.
The .pos files allow for many of the UI elements to be controlled via data files. This allows mods to alter how the majority of the various UI elements are presented to the player.
The .pos files can be found at "data/ui_overrides"

Pos files consist of two main sections, "frames" and "list".

### Frames
Frames as the name suggests allows the .pos file to create additional background frames.
An example frames element is:

```
{
    "position": {
        "x": -2 ,
        "y": -40
    },
    "size": {
        "width": 320 ,
        "height": 72
    },
    "priority": 2,
    "anchor":"TC",
    "align":"TC",
    "fill": "black_curved"
}
```

#### Frame Tags

You can have the following Frame Tags

* `name` // Name of the frame so it can be linked with code
* `notch%` // Should this element account for a possible notched screen? (i.e. webcam notch)
* `corner_avoid%` // Should this element account for a possible curved corner screen?
* `base_override` // Is this a UI override for base Rome?
* `bi_override` // Is this a UI override for BI?
* `alex_override` // Is this a UI override for Alexander?
* `ignore_scale` (true, false) // Should this element ignore the UI scaling?
* `ignore_aspect_ratio` (true, false) // Should this element ignore the windows aspect ratio
* `position` (x, y, x%, y%) // Where should this frames align point be positioned
* `lock_left` // Should this frame be locked to the left of the screen?
* `lock_right` // Should this frame be locked to the right of the screen?
* `anchor` (`TC`, `TR`, `CL`, `C`, `CR`, `BL`, `BC`, `BR`, `RIGHT_PNL`, `LEFT_PNL`) // Where on the screen is this element anchored? AKA where are the positional offsets calculated from? If this element is a child of another element, the parent element is used instead of the screen (i.e. TL would be the top left of the parent element, not the top left of the screen)
* `scale_width` // The element will scale it's width (good combined with scale_x_pos)
* `align` (TC, TR, CL, C, CR, BL, BC, BR) // Which point on this element should we use as its "position"?

These next 4 tags define the element's scaling behaviour when the aspect ratio is not 4:3                

* `fill_left` // The element will push it's left side to the left side of the screen, maintaining it's spacing from the ed
* `fill_right` // The element will push it's right side to the right side of the screen, maintaining it's spacing from the edge.
* `offset_right` // The element will move to the right depending on the screen aspect ratio
* `offset_left` // The element will move to the left depending on the screen aspect ratio
* `scale_x_pos` // The element will scale it's x coord (good for maintaining element spacing)
* `priority` // Where in the draw priority is this element? Elements with a higher draw priority will draw on top of elements with a lower priority. Also effect the priority given to elements when handling inputs
* `fill` (`clear`, `black`, `black_curved`, `invisible`, `clear_thick`, `gold_border`, `decorated`, `black_curved_close_embedded`, `decorated_close_embedded`, `interlocking`) (Some frame types have other effects than just visuals)
* `anim_id` // The animation ID linked with this element (if one exists)
* `ignore_mouse` // Should this element ignore all mouse input?
* `steal_input` // Should this element steal input from other elements?
* `collapsed_size` (width%, height%) // How large should the frame be in its collapsed state?
* `anim_children` // Adds children to be affected by our animations?
* `annotation_id` // The annotation string ID associated with this element
* `tags` // See “Tag System”
* `additional_clipping` (x, y, width, height, x%, y%, width%, height%, anchor, align)

### List

The “list” section contains each of the individual elements found within that section of the UI.
An example of an element found in the “list” section is below.

```
	{
		"name": "abilities_list",
		"x": 470 ,
		"y": 155,
		"size": {
			"width": 605 ,
			"height": 170
		},
		"anchor": "TL",
		"align": "TL",
		"font_colour":"dark_brown",
		"font":"verdana_med",
		"max_text_width": 600,
		"outside_slider": true,
		"slider_gap": 5
	},
```


#### List Tags

* `name` // Name of the element so it can be linked to the element in code
* `ignore_scale` (true, false)// Should this element ignore the UI scaling?
* `ignore_aspect_ratio` (true, false)// Should this element ignore the windows aspect ratio
* `reference` (true, false)// References don't apply any transformations, only some properties
* `notch%` (true, false) // Should this element account for a possible notched screen? (i.e. webcam notch)
* `corner_avoid%` (true, false) // Should this element account for a possible curved corner screen?
* `ar_correct_height%` (true, false)
* `base_override` // Is this a UI override for base Rome?
* `bi_override` // Is this a UI override for BI?
* `alex_override` // Is this a UI override for Alexander?
* `x` // The x position of the element in pixels
* `y` // The y position of the element in pixels
* `x`% // The x position of the element calculated from a % of the window width
* `y`% // The y position of the element calculated from a % of the window height
* `size` (width, height, max_height, width%, height%, max_height%)
* `hidden`
* `priority` // Where in the draw priority is this element? Elements with a higher draw priority will draw on top of elements with a lower priority. Also effect the priority given to elements when handling inputs
* `align` // Which point on this element should we use as its "position"?
* `fill_left` // The element will push it's left side to the left side of the screen, maintaining it's spacing from the edge.
* `fill_right` // The element will push it's right side to the right side of the screen, maintaining it's spacing from the edge.
* `offset_left` // The element will move to the left depending on the screen aspect ratio
* `offset_right` // The element will move to the right depending on the screen aspect ratio
* `scale_x_pos` // The element will scale it's x coord (good for maintaining element spacing)
* `scale_width` // The element will scale it's width (good combined with scale_x_pos)
* `scale_width_ar_correct` // The element will scale it's width (good combined with scale_x_pos) while changing height to maintain aspect ratio
* `fill_left_ar_correct` // The element will push it's left side to the left side of the screen, maintaining it's spacing from the edge.while changing height to maintain aspect ratio (good combined with scale_x_pos)
* `fill_right_ar_correct` // The element will push it's right side to the right side of the screen, maintaining it's spacing from the edge. while changing height to maintain aspect ratio (good combined with scale_x_pos)
* `hitbox` (left, top, right, bot)
* `anchor` (TL, TC, TR, CL, C, CR, BL, BC, BR, RIGHT_PNL, LEFT_PNL) // Where on the screen is this element anchored? AKA where are the positional offsets calculated from? If this element is a child of another element, the parent element is used instead of the screen (i.e. TL would be the top left of the parent element, not the top left of the screen)
* `font` // What font should the text elements use?
* `font_colour` // What colour should the text elements be?
* `max_lines` // What is the maximum amount of lines this element can use? (ONLY APPLIES TO MULTILINE STRINGS)
* `max_resizes` // What is the maximum amount of resizes this element can perform? (ONLY APPLIES TO MULTILINE STRINGS)
* `max_text_width` // What is the maximum width this element can use for text? (ONLY APPLIES TO MULTILINE STRINGS)
* `text_justification` (L, R, T, B, C, TL, TC, TR, CL, CC, CR, BL, BC, BR)
* `tags` // "See tags system"
* `triggers` // What other elements should be triggered by this element?
* `triggers_show` // What elements should be shown when this element is selected?
* `triggers_hide` // What elements should be hidden when this element is selected?
* `triggers_toggle` // What elements should be toggled when this element is selected?
* `annotation_id` // The annotation string ID associated with this element
* `anim_id` // The animation ID linked with this element (if one exists)
* `anim_children` // What elements should be affected by this elements animation?
* `ignore_mouse` // Should this element ignore all mouse input?
* `additional_clipping` (x, y, width, height, x%, y%, width%, height%, anchor, align)
* `outside_slider` // Should the slider be rendered outside the list element?
* `slider_gap` // How large should the gap be between the list and its slider?
* `use_label_width` // Alternative transformations for labelled elements


### Fonts

* `tnr`
* `tnr_lrg`
* `tnr_med`
* `tnr_sml`
* `verdana`
* `verdana_lrg`
* `verdana_med`
* `verdana_sml`
* `feral_sml_med`
* `feral_lrg_sml`
* `verdana_sml_med`
* `verdana_bold`
* `verdana_med_bold`
* `verdana_SML_med_bold`
* `verdana_sml_bold`
* `cinzel_huge`
* `cinzel_lrg`
* `cinzel_huge_bold`
* `cinzel_lrg_bold`
* `cinzel`
* `cinzel_bold`
* `cinzel_med`
* `cinzel_med_bold`
* `cinzel_sml_med`
* `cinzel_sml_med_bold`
* `cinzel_sml`
* `cinzel_sml_bold`
* `verdana_med_bold_italic`


#### Font Colours

* `white`
* `black`
* `gold`
* `khaki`
* `enemy_red`
* `ally_yellow`
* `dark_brown`
* `own_faction_blue`
* `grey`
* Also accepts hex colour values in the format: `“font_colour”: “#FFFFFF”`,


### Tags System

The tag system allows us to easily keep UI elements hidden until needed.

This system can be seen in use on the small unit description panels. All the elements are defined in the .pos file however they are only displayed when the code flags their tag as currently active.

This is how the small left unit descriptions can switch between showing the units stats and their description.

It is not possible for mods to add additional tags as they are activated from code, but its possible to alter what is shown when the existing tags are (de)activated. An element without tags is always active.

### FeralUI.Anims

This file works in collaboration with the .pos files and controls the animation of many of the UI elements in the game.



#### FeralUI.Anims Tags

* `end_pos` (x, y, x%, y%)// Where should this element be at the end of the animation
* `ignore_scale` // Should this animation ignore the games UI scaling?
* `scale_x_pos` // Should this element scale its x position based on aspect ratio
* `relative` // Should the end position be relative to its current position? (False would be relative to the screen instead)
* `anchor` // Used if relative is set to false. See: .pos anchor
* `duration` // How long should this animation take to complete?
* `timeout` // How long until this animation times out? (-1 to disable timeout)
* `start_actions` // Actions that should happen at the start of the animation
* `end_actions` // Actions that should happen at the end of the animation

### Possible Actions

* `show` // Makes the element visible
* `hide` // Hides the element
* `resize` (duration, width, width%, height) // Resizes the element over the given duration
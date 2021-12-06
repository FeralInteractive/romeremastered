![Workshop_header_template](/Workshop_header_template.png)
# Miscellaneous Hints and Tips

## Table Of Contents

   * [Introduction](#introduction)
   * [Faction Icons](#faction-icons)
   
## Introduction

This page is a collection of hints and tips that don't otherwise fit into their own page but could be useful to players and modders alike.


## Swap Merge & Sort Behaviour

In Rome Remastered you can sort your units on the campaign map into the orders you like, this is then remembered when you enter and leave battles meaning you can organise your armies as you recuit them on the map.

There are buttons in the UI to auto sort and auto merge units in your armies on the bottom of the screen.

![AutoMerge_Autosort](/documentation/feature_guides/images/AutoMerge_Autosort.jpg)

By default dragging will reorder units and you can use ctrl and drag to manually merge units. You can however swap this behaviour around inside the preferences folder if you prefer.

 1. Open the Pre-Game Options Panel and go to the Support tab
 2. Click on the `Open Preferences Folder` button.
![SupportOpenPreferences](/documentation/feature_guides/images/SupportOpenPreferences.jpg)
 3. Quick the launcher using the `Quit` button
 4. Now open the `Preferences Data` file from the `Total War ROME REMASTERED` in a text editor.
 5. Search for the line with `CtrlToMerge`. Edit the line so the value is `0` instead of `1`. Afterwards it should look like the line in point 6 below. 
 6. `<value name="CtrlToMerge" type="integer">0</value>`
 7. Save the file and restart the game. You can now merge by default and hold down ctrl if you want to reorder.


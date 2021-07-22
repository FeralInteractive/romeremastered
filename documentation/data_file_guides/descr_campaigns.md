![Workshop_header_template](/Workshop_header_template.png)
# descr_campaigns.txt

## Table Of Contents

* [Introduction](#introduction)
    * [Example of default descr_campaigns.txt](#example-of-default-descr_campaignstxt)

## Introduction

This is a new addition for Rome Remastered. This file allows you to:

* Add in custom campaigns to the main menu
* Enable Loyalty and/or Religion from BI / Alex into your mods
* Enable or disable Rebel merchants

See comments in the file for further details.

### Example of default descr_campaigns.txt

```
;; JNF 2021-06-10 - define a new campaign list so people can define new campaigns and enable/disable important features for them individually
"campaign list":
[
	{
		;;title is the panel header, menu is the menu button test, folder is the folder with data/world/maps/campaign to use
		"menu": "UI_FERAL_LP_CAMPAIGN",
		"title": "UI_FERAL_CAMPAIGN",
		"folder": "imperial_campaign",

		"features":
		{
			;; JNF 2021-06-14 - Loyalty should work, religion is as limited as the original release pending refactor but it should enable/disable the UI perfectly fine
			"loyalty":  false,
			"religion": false,

			"rebel merchants": true,
		},
	},
],
```

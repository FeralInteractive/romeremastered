![Workshop_header_template](/Workshop_header_template.png)
# descr_sm_resources

## Table Of Contents

* [Introduction](#introduction)
	 * [Example of default descr_sm_resources.txt](#example-of-default-descr_sm_resourcestxt)
	 * [Scripting (New Feature)](#scripting-new-feature)

## Introduction

This is a an updated file for Rome Remastered. This file now allows you to:

* Add in new resources (virtually unlimited)
* Fully define the type of resource based on the different types the original contained.
* Allow for full customisation of the strings, icons and 3d campaign models for each resource.
* Allow you to add a resource into groups for scripting triggers.

**NOTE** It is reported that the rome hidden resource must be kept as the game uses it when checking victory conditions. These are at the bottom of the descr_sm_resources.txt file. These hidden resources can be assigned to regions in the descr_regions.txt file or via scripting (see below).

### Example of default descr_sm_resources.txt

```
"gold":
{
	;; subtype of resource this is:

	;; hidden is not displayed to the user
	;; slaves are created when enslaving a settlement
	;; mineable can have a mine constructed on them
	;; none is just a normal resource
	"subtype": "mineable",

	;; the localised name and tooltip for this resource
	"name": "SMT_RESOURCE_GOLD",
	"tooltip": "TMT_GOLD_TOOLTIP",

	;; the UI icon to use
	"icon": "data/ui/resources/resource_gold.tga",

	;; mineable resources need a seperate tooltip for when they're being mined
	"mining tooltip": "TMT_GOLD_MINE_TOOLTIP",

	;; the tier and trade value
	"tier": 5,
	"trade value": 15,

	;; tags (groups) that this resource belongs to
	"tags":
		[ "precious_minerals", "all_minerals", ],

	;;the model to use for this resource's mine
	"mine model": "data/models_strat/resource_mine.CAS",

	;; models to use for specific quantities
	"quantity models":
	{
		"data/models_strat/resource_gold.CAS": 1,
		"data/models_strat/resource_gold_02.CAS": 2,
	},

	;; default model to use when the quantity is not one of the ones specified above
	"default model": "data/models_strat/resource_gold_03.CAS",
},
```

### Optional attributes

Some resources may have additional attributes set to give them additional properties beyond trade value

| Attribute name  | Explanation                                                                                                                                                                                                                                                                           | Example usage                                  |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------|
| growth modifier | Gives a growth boost to regions with this resource, equivalent to having a governor with an equivalent bonus to the "Health" attribute                                                                                                                                                | "growth modifier": 1,                          |
| base turns      | [Only applies to slave resources] After enslaving a settlement, this determines the minimum number of turns that the resource will become active for                                                                                                                                  | "base turns": 20,                              |
| pop impact      | [Only applies to slave resources] After enslaving a settlement, the resource will remain active for an additional number of turns equivalent to (population / pop impact) (i.e. if pop impact is 1000, a settlement of 3100 will keep this resource active for an additional 3 turns) | "pop impact": 1000,                            |
| single tooltip  | If a resource only has 1 turn left before it becomes inactive, it will use this tooltip instead of the normal one                                                                                                                                                                     | "single tooltip": "TMT_SLAVES_TOOLTIP_SINGLE", |
| mining tooltip  | [Only applies to mineable resources] If the settlement for the region has a "mine_resource" stat greater than 1 the resource will use this tooltip instead of the normal one  (the single tooltip will take priority over this if applicable)                                         | "mining tooltip": "TMT_SILVER_MINE_TOOLTIP",   |
| mine model      | [Only applies to mineable resources] If the settlement for the region has a "mine_resource" stat greater than 1 the resource will have this model applied over the top of the base model                                                                                              | "mine model": "data/path/to/model.cas",        |

### Scripting (New Feature)

You can now use hidden resources in scripting, you can add & remove hidden resources and then check for the existence of them in a specific region. These are exposed in the [scripting commands](/documentation/feature_guides/scripts/Scripts.md) but repeated here for clarity.


```
Identifier:              HasResource
Trigger requirements:    settlement
Parameters:              resource name (includes hidden resources)
Sample use:              HasResource sparta
Description:             For scripting - does the region have this resource
Battle or Strat:         Either
Class:                   HAS_RESOURCE
Implemented:             Yes
---------------------------------------------------
Identifier:              add_hidden_resource
Parameters:              region name and resource name
Description:             add a hidden resource to a given region
Sample use:              add_hidden_resource Latium sparta
Class:                   ADD_HIDDEN_RESOURCE
Implemented:             Yes
---------------------------------------------------
Identifier:              remove_hidden_resource
Parameters:              region name and resource name
Description:             remove a hidden resource to a given region
Sample use:              remove_hidden_resource Latium sparta
Class:                   REMOVE_HIDDEN_RESOURCE
Implemented:             Yes
```

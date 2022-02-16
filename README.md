![Workshop_header_template](/Workshop_header_template.png)
# Welcome to the Total War: ROME REMASTERED Modding Tools GitHub
Welcome! This is the home of the Total War: ROME REMASTERED modding tools and documentation. This is the main place to access the official tools required to get you started.

# Table Of Contents

* [List of acronyms](#list-of-acronyms)
* [Documentation](#documentation)
   * [Game Data File Guides](#game-data-file-guides)
   * [Feature Guides](#feature-guides)
   * [Asset Creation Guides](#asset-creation-guides)
* [Tool Guides](#tool-guides)
* [Example Mod](#example-mod)
* [Third Party Resources](#third-party-resources)
* [Rules](#rules)

# List of acronyms

* RR = **R**ome **R**emastered
* OG = **O**riginal **G**ame (Rome Classic)
* PGOW = Feral's **P**re **G**ame **O**ption **P**anel

# Documentation
* [2.0.0 -> 2.0.3 Differences & New Features](/RomeRemasteredDifferences.md)
* [2.0.3 -> 2.0.4 Differences & New Features](/RomeRemastered204.md)
* [2.0.3 -> 2.0.4 File Changes](/RomeRemastered204FileChanges.md)

## Game Data File Guides


* [data_controlled_features](/documentation/data_file_guides/data_controlled_features.md)
* [descr_battle_ai_personalities](/documentation/data_file_guides/descr_battle_ai_personalities.md)
* [descr_campaigns](/documentation/data_file_guides/descr_campaigns.md)
* [descr_sm_resources.txt](/documentation/data_file_guides/descr_sm_resources.md)
* [DMB - descr_model_battle](/documentation/data_file_guides/DMB.md)
* [EDB - export_descr_buildings](/documentation/data_file_guides/EDB.md)
	* [EDB - List of valid building capabilities](/documentation/data_file_guides/building_capabilties.md)
* [List of valid trait and ancillary effects](/documentation/data_file_guides/traits_and_ancillaries.md)
* [EDU - export_descr_unit](/documentation/data_file_guides/EDU.md)
	* [EDU - Unit Attributes](/documentation/data_file_guides/unit_capabilties.md)
* [feral_descr_ai_personality.txt](/documentation/data_file_guides/feral_descr_ai_personality.md)
* [feral_descr_movement_multipliers.txt](/documentation/data_file_guides/feral_descr_movement_multipliers.md)
* [feral_descr_reputations_and_relations](/documentation/data_file_guides/feral_descr_reputations_and_relations.md)
* [string_overrides](/documentation/data_file_guides/string_overrides.md)
* [toggles](/documentation/data_file_guides/toggles.md)
* [feral_descr_tonemap_lut.txt](/documentation/data_file_guides/feral_descr_tonemap_lut.md)
* [feral_descr_grass_textures.txt](/documentation/data_file_guides/feral_descr_grass_textures.md)
* [feral_descr_grass_usage.txt](/documentation/data_file_guides/feral_descr_grass_usage.md)

## Feature Guides
* [Hording](/documentation/feature_guides/hording.md)
* [Scripting](/documentation/feature_guides/scripts/Scripts.md)
* [Movie_Cam](/documentation/feature_guides/movie_cam.md)
* [Logging](/documentation/feature_guides/logging/logging.md)
* [Image Formats](/documentation/feature_guides/image_formats.md)
* [UI Modding Format Guide](/documentation/feature_guides/ui_modding_guide.md)
* [UI Modding Example](/documentation/feature_guides/ui_modding_example.md)
* [Miscellaneous Tips](/documentation/feature_guides/MiscellaneousTips.md)

## Asset Creation Guides
* [Animations](/documentation/techart_guides/Animations.md)
* [Buildings](documentation/techart_guides/Buildings.md)
* [Characters](documentation/techart_guides/Characters.md)
* [Destruction](documentation/techart_guides/Destruction.md)
* [Miscellaneous Tips](documentation/techart_guides/MiscellaneousTips.md)
* [Physical Info Files](documentation/techart_guides/PhysicalInfoFiles.md)
* [Vegetation](documentation/Vegetation.md)
* [Importing Rome Total War units to Total War: ROME REMASTERED](documentation/techart_guides/Importing_RTW_units_to_Remastered.md)
* [Upscaling Rome Total War textures to Total War: ROME REMASTERED](documentation/techart_guides/Upscaling_RTW_Textures_to_Remastered.md)
* [Settlement Overlay](documentation/techart_guides/Settlement_Overlay.md)

# Tool Guides

The tools folder is full of scripts and tools that can assist modders in creating assets for the game. Below is a list of the current tools. All tools will be in a separate folder with the tool and a brief documentation file.

* [Skeleton Converter (Update Skeleton version to Remastered format)](tools/SkeletonConverter/SkeletonConverter.md)
* [Audio Packer (Used to unpack/pack `.feral.dat` files to and from raw files)](tools/AudioPacker/AudioPacker.md)
* [CAS Exporter (This tool will convert fbx files into cas files.)](tools/CasPacker/casconv.md)
* [Campaign Map Tool (Mesh Generation using Blender)](tools/CampaignMapTool/CampaignMapTool.md)
* [Unpack Characters (.cas files from .pak files)](tools/unpack_characters/unpack_characters.md)

# Example Mod

We have created a number of example mods, these are designed to demonstate as many of the newer modding features as possible so people can use it as a reference when making their own mods or reading the documentation found elsewhere in this GitHub repository.

You can find the mods on the next page, just download the specific folder you want and place it inside the "My mods" folder on your installation to experience the mod.

* [Example Mod Documentation](/example_mods/ExampleMods.md)

# Third Party Resources

Below you will find links to third party resources that can help with modding Rome Remastered.

* [IWTE](https://wiki.twcenter.net/index.php?title=IWTE) - Extremely useful tool for any modder.
  * Create RR Map Mesh & Textures (Beta Feature)
  * Covert from .dae to .cas
  * Bulk decompress Rome Remastered texture directory
* [Dagovax's Rome Modding Tools & Features](https://github.com/Dagovax/Rome-Total-War-Tools-and-Features) - 3DS-Max scripts & more  
* [Settlement & Region Name Extractor](https://github.com/zkajo/RTW-Region-Extractor)
* [TWC Wiki - Rome:Total War & Remastered - Modding Index](https://wiki.twcenter.net/index.php?title=Rome:Total_War_%26_Remastered_-_Modding_Index)
* [Vercingetorix's xidx packer](https://github.com/AKAfreaky/XIDX) - Useful Packing Tool
  * Packs and Repacks various idx files used by Rome Total War & ROME REMASTERED

# Rules

* We welcome pull requests with improvements to the tools or documentation
* Bugs logged here should **ONLY** relate to modding questions.

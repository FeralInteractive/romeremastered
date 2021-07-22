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
* [Third Party Resources](#third-party-resources)
* [Rules](#rules)

# List of acronyms

* RR = **R**ome **R**emastered
* OG = **O**riginal **G**ame (Rome Classic)
* PGOW = Feral's **P**re **G**ame **O**ption **P**anel

# Documentation
* [Differences & New Features](/RomeRemasteredDifferences.md)

## Game Data File Guides


* [descr_campaigns](/documentation/data_file_guides/descr_campaigns.md)
* [descr_sm_resources.txt](/documentation/data_file_guides/descr_sm_resources.md)
* [DMB - descr_model_battle](/documentation/data_file_guides/DMB.md)
* [EDB - export_descr_buildings](/documentation/data_file_guides/EDB.md)
* [EDU - export_descr_unit](/documentation/data_file_guides/EDU.md)
* [feral_descr_ai_personality.txt](/documentation/data_file_guides/feral_descr_ai_personality.md)
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

## Asset Creation Guides
* [Animations](/documentation/techart_guides/Animations.md)
* [Buildings](documentation/techart_guides/Buildings.md)
* [Characters](documentation/techart_guides/Characters.md)
* [Destruction](documentation/techart_guides/Destruction.md)
* [Physical Info Files](documentation/techart_guides/PhysicalInfoFiles.md)
* [Vegetation](documentation/Vegetation.md)
* [Importing Rome Total War units to Total War: ROME REMASTERED](documentation/techart_guides/Importing_RTW_units_to_Remastered.md)

# Tool Guides

The tools folder is full of scripts and tools that can assist modders in creating assets for the game. Below is a list of the current tools. All tools will be in a separate folder with the tool and a brief documentation file.

* [Skeleton Converter (Update Skeleton version to Remastered format)](tools/SkeletonConverter/SkeletonConverter.md)
* [Audio Packer (Used to unpack/pack `.feral.dat` files to and from raw files)](tools/AudioPacker/AudioPacker.md)
* [CAS Exporter (This tool will convert fbx files into cas files.)](tools/CasPacker/casconv.md)
* [Campaign Map Tool (Mesh Generation using Blender)](tools/CampaignMapTool/CampaignMapTool.md)
* [Unpack Characters (.cas files from .pak files)](tools/unpack_characters/unpack_characters.md)


# Third Party Resources

Below you will find links to third party resources that can help with modding Rome Remastered.

* [IWTE](https://wiki.twcenter.net/index.php?title=IWTE) - Extremely useful tool for any modder.
  * Create RR Map Mesh & Textures (Beta Feature)
  * Covert from .dae to .cas
  * Bulk decompress Rome Remastered texture directory
* [Settlement & Region Name Extractor](https://github.com/zkajo/RTW-Region-Extractor)
* [TWC Wiki - Rome:Total War & Remastered - Modding Index](https://wiki.twcenter.net/index.php?title=Rome:Total_War_%26_Remastered_-_Modding_Index)
* [Vercingetorix's xidx packer](https://github.com/AKAfreaky/XIDX) - Useful Packing Tool
  * Packs and Repacks various idx files used by Rome Total War & ROME REMASTERED

# Rules

* We welcome pull requests with improvements to the tools or documentation
* Bugs logged here should **ONLY** relate to modding questions.

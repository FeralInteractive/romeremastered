![Workshop_header_template](/Workshop_header_template.png)
# AudioPacker - Commandline options to unpack & pack audio data

## Table Of Contents

* [Introduction](#introduction)
* [Unpacking audio data](#unpacking-audio-data)
* [Packing audio data](#packing-audio-data)
* [Modifying parameters](#modifying-parameters)
* [Additional Commands](#additional-commands)

## Introduction

The audio tools are built into the Rome Remastered game and are accessed by using commandline options.

Used to unpack `.feral.dat` files into raw files, to use place the script into the same folder as the pack file you want to extract and run.

The script will prompt you for a name, and will then unpack the files from that pack into the current folder

## Unpacking audio data (snd_decompile_sounds)

Rome’s audio files are stored in packs consisting of .dat and .idx files.

To extract these, run Rome with the following command line: `snd_decompile_sounds`.
The best way to do this is from the `PGOW>Advanced>Advanced` options.

![snd_decompile_sounds](/tools/AudioPacker/snd_decompile_sounds.jpg)

The files will be extracted to `...\Steam\steamapps\common\Total War ROME REMASTERED\Contents\Resources\Data\data\sounds\` and will maintain the folder structure they were packed in.

Note if you want to extract the files from the expansions or localised dialogue, simply run the command in the expansion and language you wish to extract.
* Barbarian Invasion data is here: `...\Resources\Data\bi\data\sounds\`
* Alexander data is here: `...\Resources\Data\alexander\data\sounds\`

This command will also unpack `manifest.txt` files, which contain lists of all of the files within each pack.


## Packing audio data (snd_compile_sounds)

To pack audio data back up, run Rome as before with: `snd_compile_sounds`

![snd_compile_sounds](/tools/AudioPacker/snd_compile_sounds.jpg)

This will read the manifest files and create the appropriate packs. If you’ve added new files or changed the names of existing files, this will need to be reflected in the manifest before packing.

Note that you should unpack all the game’s original audio files before repacking them with your new/modified ones.

Once packed, you can delete the loose audio files from your data folder.


## Modifying parameters

The parameter settings  (volume, probability, rolloff distance, etc.) can be found in the various descr files found in the game’s data. These are read sequentially when compiling, so if you want to create a mod that changes any of these, be sure to include the following files, even if you haven’t changed them:
* `...\data\descr_sounds.txt`
* `...\data\sounds\descrs\descr_bank_sounds.txt`


`Events.dat` is a pack containing the compiled parameter settings for all of the audio events in the game. To compile it from the existing descr files, run Rome with the command `snd_save_events`.
Please note that doing this will read the `descr_sounds.txt` and other descr files referenced therein from the first loaded audio mod, and save the compiled events to that mod.

The events packs will then be prioritised on launch starting with the first loaded mod, and ending with the game’s data.

If you want to have the game read the sound descr files directly without needing to compile (eg. when testing parameter changes), you can create a new blank .txt file and rename it to `events.dat` in your mod folder. Note that this will not update parameters in real time as it is still only read on initialisation.

The descr files themselves have been refactored for Rome Remastered to somewhat resemble json, and include plenty of comments and a standardised layout for usability. All available parameters and their current values for each event are now listed with the event.

It is possible to add new events to the game following the guidelines in `descr_sounds.txt`.

## Additional Commands

* `snd_check` - This will allow you to debug sound banks and get addional information in the log files.
* `snd_save_events` - create the events pack this will generate a new 'events.dat' file for your mod.
* `snd_ignore_packs` - Disable loading event packs, useful when debugging issues, you can use this to confirm if your issues are linked to these packs.


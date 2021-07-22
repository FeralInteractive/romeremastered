![Workshop_header_template](/Workshop_header_template.png)
# string_overrides

## Table Of Contents

   * [Introduction](#introduction)

## Introduction

Some of the text displayed in game isn't read from data/text folders, it's from:

`DRIVE:\Steam\steamapps\common\Total War ROME REMASTERED\Contents\Resources\en.lproj\Localizable_Game.strings`

these strings can be changed and included in modfolder just duplicate the file and place it in the following location:

`mod-folder\data\string_overrides\en.strings`

This example is for english same principle applies on other languages. Instructions are contained in the readme.txt inside data/string_overrides: This folder is used to override strings added to the game by Feral Interactive.

**NOTE**: The original override files can be found at "<languageCode>.lproj/Localizable_Game.strings" Override files should be named the language code they correspond with and have the file extension, ".strings" E.G. English Override: "en.strings"

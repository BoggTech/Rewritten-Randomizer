# Rewritten-Randomizer

A simple program for randomizing the contents of Toontown Rewritten's phase files.

## Usage
### Prerequisites
Using this script assumes that you are aware of how to extract game assets from phase files and that you already have them ready before starting. If you're unfamiliar with this process, there is a [beginner's tutorial on the Toontown Rewritten wiki](https://toontownrewritten.wiki/Phase_files).

Please ensure you have [Python 3](https://www.python.org/downloads/) installed before continuing.

### Step-by-step guide
- Run the script once to generate the `resources` directory, or create it yourself.
- Move your extracted phase files here, such that `resources` is the parent directory of the individual phase_*x* directories (e.g. `resources/phase_6`).
- Run the script again with `python3 main.py`. A copy of `resources` will be created in the `output` directory, containing the randomized assets.

### Compiling to a content pack
In order to make the final product usable, you must repack the phase files into a multifile. Assuming you have already installed Panda3D, the instructions are as follows:

- Create an **info.ini** file in the root folder of your new phase files (by default, this should be `output\resources\info.ini`) and edit it to include this text:
```
[PackInfo]
name=**Your Name Here**
description=**Your Description Here**

[FeatureFlags]
want-new-chaser=yes
```
- You are free to change anything wrapped in double astericks (**).
- **OPTIONAL:** Create a **pack.png** file and include it alongside info.ini. This will give your content pack an icon in-game, however, it is not required.
- Use the multify command, packaged with Panda3D, to repach your content pack into a usable `.mf` file. For example:
```
multify -c -f PackName.mf phase_3 phase_3.5 phase_4 phase_5 phase_5.5 phase_6 phase_7 phase_8 phase_9 phase_10 phase_11 phase_12 phase_13 phase_14 info.ini
```
- Make sure every folder within `output/resources` is included in this command. If you chose to include a pack icon, add `pack.png` to it. Feel free to edit PackName to whatever you want.

After doing all of this, assuming there was no errors, you should be left with a file named `PackName.mf`, or something else if you decided to change `PackName` in the previous command. Drag this into Toontown Rewritten's content packs folder and refresh the list if you are in-game. Your randomized content pack is **ready to use!**

If you want more information on content packs, check out the [Toontown Rewritten FAQ](https://www.toontownrewritten.com/help/faq/content-packs) or [contentpacks.net](https://contentpacks.net/contact.html) and their affiliated discord server.

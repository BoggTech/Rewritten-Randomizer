import os
import glob
from pathlib import Path
import random
import shutil

# valid extension names for randomization, i.e. anything we can change in a resource pack. 
validExtensions = (
    'ogg',
    'jpg',
    'ttf',
    'rgb'
)

# ensure no mixing between folder types - this mostly exists to prevent mixing bgm and sfx
folderMatch = True

# valid folders that will stay matched to eachother (i.e. phase_4/audio/sfx and phase_5/audio/sfx mix but not phase_4/audio/sfx and phase_5/audio/bgm)
validFolders = (
    'maps',
    'bgm',
    'sfx',
    'dial',
    'fonts'
)

# name of our input/output folders
inputFolder = 'resources'
outputFolder = 'output'

def randomizePathListToOutput(inputPaths):
    randomized = inputPaths.copy()
    random.shuffle(randomized)

    for i in range(0,len(inputPaths)):
        new_path = outputFolder / Path(randomized[i])
        folder_path = str(new_path.parent)                  # we need to get parent folder, otherwise makerdirs will treat the file as a directory.
        os.makedirs(folder_path, exist_ok=True)             # ensure dir exists before we move the file into it to prevent errors
        shutil.copy(inputPaths[i], str(new_path))
    
def main():
    if ( not os.path.exists(inputFolder) ):
        os.mkdir(inputFolder)
        print("Generated input folder ({}) - please add extracted phase files!".format(inputFolder))
        return

    if ( folderMatch ):
        for subfolder in validFolders:
            for ext in validExtensions:
                toRandomize = glob.glob(str(Path(inputFolder) / '**' / subfolder / ('*.'+ext)), recursive=True)
                randomizePathListToOutput(toRandomize)
    else:
        for ext in validExtensions:
            toRandomize = glob.glob(str(Path(inputFolder) / '**' / ('*.'+ext)), recursive=True)
            randomizePathListToOutput(toRandomize)

if __name__ == '__main__':
    main()


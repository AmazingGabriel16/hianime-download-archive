# To be used for episode downlods from Hi Anime
# Format (Name of episode) Ep - (Automatic number change)

# Based off the format given by Video Download Helper
# https://github.com/aclap-dev/video-downloadhelper

''' Instructions

1) Put this Python file into the download folder of where all of the downloaded files are.
2) Run file

'''

import os
import pathlib
import sys

''' Test
anime_name = 'AHO-GIRL'
anime_season = '1'
file_type = 'mp4'
'''
print('Anime episode renamer')
print('To be used with hianime.to and video download helper add-on')
print('Made with love for easy archiving on Archive.org')
anime_name = input('Anime name: ')
anime_season = input('Anime season: ')
print('Make sure that the file type for all files are the same!')
file_type = input('File type: ')

# Finds all file names in the current folder path
dir = os.listdir(pathlib.Path(__file__).parent.resolve())

# Remove script file name from list
dir.remove(os.path.basename(__file__))

# Finds the number of episodes in the season
num_of_episodes = len(dir)

# Sorting
dir.sort()
first_episode = dir[-1]
# Insert the first episode at the 0th index
dir.insert(0, first_episode)
# Remove to prevent duplicate
dir.pop()

# Subsequent episodes
episode_count = 1

# Folder path
folder_path = os.path.dirname(os.path.abspath(sys.argv[0]))
print(folder_path)

for n in dir:
    # Makes it "01" not "1" for Internet Archive purposes
    if episode_count < 10:
        os.rename(f'{folder_path}\{n}', f'{folder_path}\{anime_name} S{anime_season} Ep - 0{episode_count}.{file_type}')
    else:
        os.rename(f'{folder_path}\{n}', f'{folder_path}\{anime_name} S{anime_season} Ep - {episode_count}.{file_type}')
    episode_count+=1

print(f'Successfully renamed {num_of_episodes} episodes of {anime_name}!')
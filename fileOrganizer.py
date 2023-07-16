"""
Organizes files from a given directory into folders separated by file type.
"""

import os
import shutil

path = input('Enter path: ')
files = os.listdir(path)

for file in files:
    # splits files into name and extension
    filename, extension = os.path.splitext(file)
    extension = extension[1:]

    if os.path.exists(path + '/' + extension):  # if a folder with this filename exists, add it there
        shutil.move(path + '/' + file, path + '/' + extension + '/' + file)
    else:
        os.makedirs(path + '/' + extension)  # create a new folder if it doesn't exist
        shutil.move(path + '/' + file, path + '/' + extension + '/' + file)

print('Done organizing!')

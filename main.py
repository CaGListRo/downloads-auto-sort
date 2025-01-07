import os, shutil
from typing import Final

DOWNLOADS_DIRECTORY: Final[str] = 'C:/Users/admin/Downloads/'
FOLDER_NAMES: Final[list[str]] = ['PDFs', 'Programme', 'Bilder', 'Videos', 'Zips', 'blender', 'Audio', 'eBooks']

# check if all folders of the FOLDER_NAMES exist, and creates them if not
for idx, folder in enumerate(FOLDER_NAMES):
    if not os.path.exists(DOWNLOADS_DIRECTORY + FOLDER_NAMES[idx]):
        os.mkdir(DOWNLOADS_DIRECTORY + folder)

# sort the files in the downloadfolder according to ending of the file
with os.scandir(DOWNLOADS_DIRECTORY) as entries:
    for entry in entries:
        if entry.name.lower().endswith('.pdf') and not os.path.exists(DOWNLOADS_DIRECTORY + 'PDFs/' + entry.name):
            shutil.move(DOWNLOADS_DIRECTORY + entry.name, DOWNLOADS_DIRECTORY + 'PDFs/' + entry.name)
        if entry.name.lower().endswith('.exe') and not os.path.exists(DOWNLOADS_DIRECTORY + 'Programme/' + entry.name):
            shutil.move(DOWNLOADS_DIRECTORY + entry.name, DOWNLOADS_DIRECTORY + 'Programme/' + entry.name)
        if entry.name.lower().endswith('.jpg') or entry.name.lower().endswith('.png') and not os.path.exists(DOWNLOADS_DIRECTORY + 'Bilder/' + entry.name):
            shutil.move(DOWNLOADS_DIRECTORY + entry.name, DOWNLOADS_DIRECTORY + 'Bilder/' + entry.name)
        if entry.name.lower().endswith('.mp4') or entry.name.lower().endswith('.avi') and not os.path.exists(DOWNLOADS_DIRECTORY + 'Videos/' + entry.name):
            shutil.move(DOWNLOADS_DIRECTORY + entry.name, DOWNLOADS_DIRECTORY + 'Videos/' + entry.name)
        if entry.name.lower().endswith('.7s') or entry.name.lower().endswith('.zip') or entry.name.lower().endswith('.rar') and not os.path.exists(DOWNLOADS_DIRECTORY + 'Zips/' + entry.name):
            shutil.move(DOWNLOADS_DIRECTORY + entry.name, DOWNLOADS_DIRECTORY + 'Zips/' + entry.name)
        if entry.name.lower().endswith('.blend') and not os.path.exists(DOWNLOADS_DIRECTORY + 'blender/' + entry.name):
            shutil.move(DOWNLOADS_DIRECTORY + entry.name, DOWNLOADS_DIRECTORY + 'blender/' + entry.name)
        if entry.name.lower().endswith('.mp3') or entry.name.lower().endswith('.wav') or entry.name.lower().endswith('.aac') and not os.path.exists(DOWNLOADS_DIRECTORY + 'Audio/' + entry.name):
            shutil.move(DOWNLOADS_DIRECTORY + entry.name, DOWNLOADS_DIRECTORY + 'Audio/' + entry.name)
        if entry.name.lower().endswith('.epub') and not os.path.exists(DOWNLOADS_DIRECTORY + 'eBooks/' + entry.name):
            shutil.move(DOWNLOADS_DIRECTORY + entry.name, DOWNLOADS_DIRECTORY + 'eBooks/' + entry.name)
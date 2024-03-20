import os, shutil

download_dir = 'C:/Users/admin/Downloads/'
folder_names = ['PDFs', 'Programme', 'Bilder', 'Videos', 'Zips', 'blender', 'Audio', 'eBooks']

for idx, folder in enumerate(folder_names):
    if not os.path.exists(download_dir + folder_names[idx]):
        os.mkdir(download_dir + folder)

with os.scandir(download_dir) as entries:
    for entry in entries:
        if entry.name.lower().endswith('.pdf') and not os.path.exists(download_dir + 'PDFs/' + entry.name):
            shutil.move(download_dir + entry.name, download_dir + 'PDFs/' + entry.name)
        if entry.name.lower().endswith('.exe') and not os.path.exists(download_dir + 'Programme/' + entry.name):
            shutil.move(download_dir + entry.name, download_dir + 'Programme/' + entry.name)
        if entry.name.lower().endswith('.jpg') or entry.name.lower().endswith('.png') and not os.path.exists(download_dir + 'Bilder/' + entry.name):
            shutil.move(download_dir + entry.name, download_dir + 'Bilder/' + entry.name)
        if entry.name.lower().endswith('.mp4') or entry.name.lower().endswith('.avi') and not os.path.exists(download_dir + 'Videos/' + entry.name):
            shutil.move(download_dir + entry.name, download_dir + 'Videos/' + entry.name)
        if entry.name.lower().endswith('.7s') or entry.name.lower().endswith('.zip')or entry.name.lower().endswith('.rar') and not os.path.exists(download_dir + 'Zips/' + entry.name):
            shutil.move(download_dir + entry.name, download_dir + 'Zips/' + entry.name)
        if entry.name.lower().endswith('.blend') and not os.path.exists(download_dir + 'blender/' + entry.name):
            shutil.move(download_dir + entry.name, download_dir + 'blender/' + entry.name)
        if entry.name.lower().endswith('.mp3') or entry.name.lower().endswith('.wav') or entry.name.lower().endswith('.aac') and not os.path.exists(download_dir + 'Audio/' + entry.name):
            shutil.move(download_dir + entry.name, download_dir + 'Audio/' + entry.name)
        if entry.name.lower().endswith('.epub') and not os.path.exists(download_dir + 'eBooks/' + entry.name):
            shutil.move(download_dir + entry.name, download_dir + 'eBooks/' + entry.name)
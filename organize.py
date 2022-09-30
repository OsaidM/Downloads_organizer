'''Downloads Organizer
this script searches your downloads folder
and then organises your files into categorised subfolders
'''
import os
from pathlib import Path
import shutil
os.chdir('C:\\Users\\'+os.getlogin()+'\\Downloads')

def init_category_folders():
    # if these folders not there then create them otherwise ignore
    Path('Compressed').mkdir(exist_ok=True)
    Path('Documents').mkdir(exist_ok=True)
    Path('Music').mkdir(exist_ok=True)
    Path('Pictures').mkdir(exist_ok=True)
    Path('Programs').mkdir(exist_ok=True)
    Path('Video').mkdir(exist_ok=True)

def pick_a_category(ext):
    # different types of extensions for each category, might update them in future
    doc_ext = {'.pptx', '.doc', '.docx', '.pdf', '.xlsx', '.xls', '.ppt'}
    prog_ext = {'.exe', '.msi'}
    arch_ext = {'.zip', '.rar', '.7z', '.tar'}
    pics_ext = {'.gif', '.png', '.jpg', '.jpeg'}
    mov_ext = {'.mp4', '.mkv', '.mov', '.avi', '.flv', '.webm', '.f4v', '.avchd', '.mpeg-2'}
    music_ext = {'.mp3', '.aac', '.ogg', '.flac', '.alac', '.wav', '.m4a', '.wma'}
    return 'Documents' if ext in doc_ext \
    else 'Programs' if ext in prog_ext \
    else 'Compressed' if ext in arch_ext \
    else 'Pictures' if ext in pics_ext \
    else 'Music' if ext in music_ext \
    else 'Video' if ext in mov_ext else None

if __name__ == '__main__':
    init_category_folders()
    for file in os.listdir():
        # for each file in the downloads folder split extension and decide where to put
        name, ext = os.path.splitext(file)
        category = pick_a_category(ext)
        if category != None:
            print(file, category)
            shutil.move(file, category)

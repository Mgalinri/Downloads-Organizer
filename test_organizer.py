# Standard Library imports
import random
import string
from pathlib import Path

import os
from file_organizer_class import File_Organizer
from pyfakefs.fake_filesystem_unittest import TestCase


# This file was created to generate tests but these tests
# were later done with pyfakefs
image = [
    '.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp', '.tiff', '.tif',
    '.heic', '.heif', '.avif', '.svg', '.eps', '.ai', '.cr2',
    '.nef', '.arw', '.orf', '.dng', '.ico', '.cur', '.dds', '.jxr',
    '.hdp', '.exr', '.icns'
]
docs = ['.doc', '.docx', '.odt', '.rtf', '.txt', '.tex', '.wps', '.md']
executables = [
    '.exe', '.bat', '.cmd', '.sh', '.bin', '.msi', '.apk', '.app', '.com'
]
presentations = [
    '.ppt', '.pptx', '.odp', '.key'
]
videos = [
    '.mp4', '.avi', '.mov', '.wmv', '.flv', '.mkv', '.webm', '.mpeg',
    '.mpg', '.3gp', '.vob', '.ogv', '.m4v'
]
audio = [
    '.mp3', '.wav', '.aac', '.flac', '.ogg', '.wma', '.m4a', '.alac',
    '.aiff', '.opus'
]
spreadsheets = [
    '.xls', '.xlsx', '.ods', '.csv', '.tsv'
]

all_extensions = [*image,*docs,*executables,*presentations,*videos,*audio,*spreadsheets]


# To-Do: Understand POSIX

src_test = "C:/Users/mgali/Downloads/test"

def create_random_filename(file_length=100, extension = None ):
    """
     This function generates a random filename
    :param file_length: int, def:100
    :param extension: str, def:None
    :return: file_name: str
    """
    characters = (string.ascii_letters+string.digits)
    special_characters = "_ -"

    length = random.randint(1,file_length-2)

    file_name = [random.choice(characters)]
    file_name += random.choices(characters+special_characters,k=length)+[random.choice(characters)]
    file_name = "".join(file_name)

    if extension is None:
        file_name+= random.choice(all_extensions)
    else:
        file_name+=extension
    return file_name


def create_text_docs(test_path):
    """
    :param: test_path: str
    :return: file_name: str
    """
    characters = (string.ascii_letters + string.digits)
    length = random.randint(1, 1000000)
    file_name = create_random_filename(extension=random.choice(docs))
    new_file = Path(test_path)/file_name
    with open(new_file,'w') as f:
        f.write("".join(random.choices(characters,k=length)))

    return file_name




def test_directory_creation(fs):
        fs.create_dir("/test/")
        file = File_Organizer("/test/")
        file.create_organizational_folders()
        new_folders = ['Images', 'Videos', 'Audio', 'Spreadsheets', 'Docs', 'PDF', 'Executables', 'Presentations']
        for i in new_folders:
            path = os.path.join("/test/",i)
            assert(os.path.exists(path))

def test_files(fs):
    fs.create_dir("/test/")
    new_folders = ['Images', 'Videos', 'Audio', 'Spreadsheets', 'Docs', 'PDF', 'Executables', 'Presentations']
    for i in new_folders:
        Path(os.path.join("/test/", i)).mkdir(exist_ok=True)

    for i in range(0,1000):
        create_text_docs("/test/")
    open ("/test/file_py.csv",'w')
    open("/test/file.png", 'w')
    file = File_Organizer("/test/")
    doc_ = []
    files_left =  file.organize_files()
    for f in file.basePath.iterdir():
        if Path(f).is_file():
            doc_.append(f.name)
    assert(files_left==doc_)











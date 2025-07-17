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
    :return: word: str
    """
    characters = (string.ascii_letters+string.digits)
    special_characters = "_ -"

    length = random.randint(1,file_length-2)

    word = [random.choice(characters)]
    word += random.choices(characters+special_characters,k=length)+[random.choice(characters)]
    word = "".join(word)

    if extension is None:
        word+= random.choice(all_extensions)
    else:
        word+=extension
    return word


def create_text_docs():
    """
        
    :return: file_name: str
    """
    characters = (string.ascii_letters + string.digits)
    length = random.randint(1, 1000000)
    file_name = create_random_filename(extension=random.choice(docs))
    new_file = Path(src_test)/file_name
    with open(new_file,'w') as f:
        f.write("".join(random.choices(characters,k=length)))

    return file_name


#Create csv functions





# To-Do: Set Up the fake file system

def test_checkPath(fs):
        fs.create_dir("/test/")
        file = File_Organizer("/test/")
        file.create_organizational_folders()
        new_folders = ['Images', 'Videos', 'Audio', 'Spreadsheets', 'Docs', 'PDF', 'Executables', 'Presentations']
        for i in new_folders:
            path = os.path.join("/test/",i)
            assert(os.path.exists(path))











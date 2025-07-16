# Standard Library imports
import random
import string
from string import ascii_letters

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


def create_random_filename(file_length=100, extension = None ):
    """
     This function generates a random filename
    :param file_length: int, def:100
    :param extension: str, def:None
    :return: str
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


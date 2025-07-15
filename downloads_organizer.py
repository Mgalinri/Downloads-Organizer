from pathlib import Path
import shutil

class File:
    def __init__(self, path):
        self.basePath= Path(path)

    def create_organizational_folders(self):
        new_folders = ['Images','Videos','Audio','Spreadsheets','Docs','PDF','Executables', 'Presentations']


        for name in new_folders:
            path  = self.basePath/name
            path.mkdir(exist_ok=True)

    def organize_files(self):
       image_suffixes = [
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
           '.mpg', '.3gp', '.vob', '.ogv', '.m4v', '.wav'
       ]
       audio= [
           '.mp3', '.wav', '.aac', '.flac', '.ogg', '.wma', '.m4a', '.alac',
           '.aiff', '.opus'
       ]
       spreadsheets= [
           '.xls', '.xlsx', '.ods', '.csv', '.tsv'
       ]
       for f in self.basePath.iterdir():
           suffix = f.suffix.lower()
           if suffix in image_suffixes:
               f.rename(self.basePath/'Images'/f.name)
           elif suffix == '.pdf':
               f.rename(self.basePath / 'PDF' / f.name)
           elif suffix in presentations:
               f.rename(self.basePath / 'Presentations' / f.name)
           elif suffix in executables:
               f.rename(self.basePath / 'Executables' / f.name)
           elif suffix in docs:
               f.rename(self.basePath/'Docs'/f.name)
           elif suffix in videos:
               f.rename(self.basePath/'Videos'/f.name)
           elif suffix in audio:
               f.rename(self.basePath/'Audio'/f.name)
           elif suffix in spreadsheets:
               f.rename(self.basePath/'Spreadsheets'/f.name)
           else:
               print(f.name)

file = File("C:/Users/mgali/Downloads")
file.create_organizational_folders()

file.organize_files()


"""for f in d.iterdir():
       if f.is_file() :
         print(f)"""

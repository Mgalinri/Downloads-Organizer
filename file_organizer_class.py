from pathlib import  Path

class File_Organizer:
    def __init__(self, path):
        self.basePath= Path(path)

    def create_organizational_folders(self,*args):
        new_folders = []
        if not args:
            new_folders = ['Images', 'Videos', 'Audio', 'Spreadsheets', 'Docs', 'PDF', 'Executables', 'Presentations']
        else:
           for i in args:
            new_folders.append(i)

        for name in new_folders:
            path  = self.basePath/name
            path.mkdir(exist_ok=True)


    #To do: Design this one to take other extensions besides the existing one
    # Return a list with the files left that are not organize
    def organize_files(self):
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
       audio= [
           '.mp3', '.wav', '.aac', '.flac', '.ogg', '.wma', '.m4a', '.alac',
           '.aiff', '.opus'
       ]
       spreadsheets= [
           '.xls', '.xlsx', '.ods', '.csv', '.tsv'
       ]

       # Create a dictionary
       file_extensions = {**{x: 'Images' for x in image},
                          **{x: 'Docs' for x in docs},
                          **{'.pdf': 'PDF'},
                          **{x: 'Presentations' for x in presentations},
                          **{x: 'Audio' for x in audio},
                          **{x: 'Videos' for x in videos},
                          **{x: 'Spreadsheets' for x in spreadsheets},
                          **{x: 'Executables' for x in executables},
                          }

       excluded_files = []

       for f in self.basePath.iterdir():
           suffix = f.suffix.lower()
           dict_element = file_extensions.get(suffix)
           if dict_element  :
               new_path = self.basePath / dict_element / f.name
               number = 0
               while new_path.exists():
                  number+=1
                  new_name = f"{f.stem}({number}){f.suffix}"
                  new_path = self.basePath / dict_element / new_name
               try:
                f.rename(new_path)
               except Exception as e:
                   excluded_files.append(f.name)
                   print(f"{f.name} and {e}")
                   continue
       return excluded_files



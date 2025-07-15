from pathlib import Path

class File:
    def __init__(self, path):
        self.basePath= Path(path)

    def create_organizational_folders(self):
        new_folders = ['Images','Videos','Docs','PDF','Executables']

        for name in new_folders:
            path  = self.basePath/name
            path.mkdir(exist_ok=True)



file = File("C:/Users/mgali/Downloads")
file.create_organizational_folders()
# This gives me every file in the directory

#Check if there is a folder for word docs


"""for f in d.iterdir():
       if f.is_file() :
         print(f)"""

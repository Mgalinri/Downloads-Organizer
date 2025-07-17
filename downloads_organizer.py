# Standard Library
import time
from pathlib import Path

# External libraries imports
from watchdog.events import FileSystemEventHandler,  FileModifiedEvent
from watchdog.observers import Observer
from file_organizer_class import File_Organizer




class EventHandling (FileSystemEventHandler, File_Organizer):

    def on_modified(self,event):
        if isinstance(event, FileModifiedEvent):
            self.create_organizational_folders()
            self.organize_files()


# src = "C:/Users/mgali/Downloads"

src_test = "C:/Users/mgali/Downloads/test"

event_handler = EventHandling(src_test)

observer = Observer()

observer.schedule(event_handler,src_test)

observer.start()
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()

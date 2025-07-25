import tkinter.font
from tkinter import *
import  tkinter as tk
from tkinter import ttk


from downloads_organizer.file_organizer_class import File_Organizer
from pathlib import Path

root = Tk()
elements = Tk()
file = File_Organizer()

warning_label = tk.Label(root,text="This is not a valid path", fg="red",bg="#0E1070")

def handle_organization(path,pb):

    if Path(path).exists():
        warning_label.pack_forget()
        file.basePath = path
        file.create_organizational_folders()
        file.organize_files(pb)
    else:
        warning_label.pack()





root.configure(background="#0E1070")
root.title("File Organizer")
root.geometry("400x300")
mainFont = tkinter.font.Font(family="Verdana",size=15, weight='bold')
formLabelFont = tkinter.font.Font(family="Verdana",size=10, weight='bold')

tk.Label(root,
         padx=40,
         pady=40,
         text = "File Organizer",
         font=mainFont,
         foreground="white",
         background="#0E1070").pack()

tk.Label(root,text = "Directory",
              font=formLabelFont,
              foreground="white",
              background="#0E1070",
              padx=40).pack(anchor="w")

pathEntry = tk.Entry(root)
pathEntry.pack(anchor="w",
               fill="x",
               padx=40,
               pady=20)

progress = ttk.Progressbar(root,
                           maximum = 100)
progress.step(file.stepPointer)
progress.pack()


tk.Button(root ,
          text = "organize",
          bg ="#E8A30E",
          fg="white",
          font=formLabelFont,
          command=lambda :handle_organization(pathEntry.get(),progress)).pack()

root.mainloop()



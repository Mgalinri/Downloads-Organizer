# Downloads Organizer

This project is designed to 
allow the user to organize 
the files in a directory.

## Features
- **Feature 1** - The file organizes files by well-known extensions
- **Feature 2** - The app has a GUI to make it easier to use the automation

## Tech Stack
 **Language**: Python
 **Libraries**: Watchdog,tkinter

## Run Locally
```
git clone https://github.com/Mgalinri/Downloads-Organizer.git
```
```
pip install -r requirements.txt
```
Then just run  the downloads_organizer.ui.py file

## Deployment
```
pip install -U pyinstaller
```
```
pyinstaller downloads_organizer.ui.py

```

## Future Work
- Make the progressbar pop-up in a separate window
- Allow the user to choose the name of the new directories, 
and the extension that will belong in it 

## Tests
 To run tests install pytest
 ```
 pip install pytest
 ```
 Then 
 ```
 pytest test_organizer.py
 ```
 
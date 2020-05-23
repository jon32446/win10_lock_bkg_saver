# Windows 10 Lock Screen Background Saver
*Utility to save the Windows 10 lock screen images to a configurable folder.*

## Usage
The first time the utility runs it will create a config.ini file if it doesn't already exist.

By default, the utility will copy landscape images that it finds in the lock screen folder to 
"C:\Temp". The source and destination folders can be controlled by editing the config.ini. If you
want the destination folder to be something other than "C:\Temp" then create a config.ini and set
the desired destination folder.

Sample config.ini:

    [PATHS]
    destination = C:\some\path\to\a\folder

You can also use environment variables when specifying the destination, e.g.
`%USERPROFILE%\lock-screen-backgrounds`

If the utility encounters errors while processing files in the source folder, it will save the
filename to the config.ini file in an *ignored files* list, so that it won't be processed again the
next time the utility runs.

**NOTE:** The utility will overwrite files in the destination folder with ones from the source
folder every time it runs.

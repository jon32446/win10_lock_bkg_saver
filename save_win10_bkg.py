import configparser
import os
from shutil import copy2
from PIL import Image

# Read in the configuration file
config = configparser.ConfigParser(allow_no_value=True, interpolation=None)
config.read("config.ini")
# Init the basic config sections if they don't exist
if "IGNORED_FILES" not in config:
    config["IGNORED_FILES"] = {}
if "PATHS" not in config:
    config["PATHS"] = {}
# Read config values
ignored_files = config["IGNORED_FILES"]  # ignored files will be skipped
paths = config["PATHS"]  # the source and destination paths

# Cached images are always stored here, incl. lock screen backgrounds
default_source = r"%LOCALAPPDATA%\Packages\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\LocalState\Assets"
paths["source"] = source = paths.get("source", default_source)
source = os.path.expandvars(source)

paths["destination"] = dest = paths.get("destination", r"C:\Temp")
dest = os.path.expandvars(dest)

# Loop through the files in source
for file in os.listdir(source):
    # If the file is in the ignored list, then skip processing
    if file in ignored_files:
        continue

    src = os.path.join(source, file)
    dst = os.path.join(dest, file + ".jpg")

    # Try to process file as an image, if it fails then ignore the file in future
    try:
        with Image.open(src) as im:
            if im.size[0] > im.size[1]:
                # Copy any images that are in landscape orientation
                print(file, "{}x{}".format(*im.size), "copied")
                copy2(src, dest)
    except Exception as e:
        # Print error, and ignore file for the future
        print("ERROR: can't process {}. Exception: {}:".format(file, e))
        ignored_files[file] = None

# Save out the config again
with open("config.ini", "w") as configfile:
    config.write(configfile)

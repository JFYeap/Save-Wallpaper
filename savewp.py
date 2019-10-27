# savewp.py - Saves new Windows screen saver wallpapers.

import os, shutil, sys, image_parser, time

# The intermediate directory for images.
RAWS_DIR = 'D:\\Wallpapers\\Raws'

# Copies files to RAWS_DIR by overwriting it.
try:
    if os.path.exists(RAWS_DIR):
        shutil.rmtree(RAWS_DIR)
        print 'Raws removed.'

    default_dir = os.path.join(
        os.environ['UserProfile'],
        ('AppData\\Local\\Packages\\Microsoft.Windows.'
         'ContentDeliveryManager_cw5n1h2txyewy\\LocalState\\Assets')
    )
    shutil.copytree(default_dir, RAWS_DIR)
    print 'Successfully renewed Raws.'
except:
    print 'Raws renewal unsuccessful.'

files = os.listdir(RAWS_DIR)

# Converts files in RAWS_DIR into .jpg extensions.
for file in files:
    file = os.path.join(RAWS_DIR, file)
    try:
        os.rename(file, file + '.jpg')
    except Exception as e:
        print 'Error: %s. Renaming unsuccessful on file %s.' % (str(e), file)
        sys.exit()

images = os.listdir(RAWS_DIR)

# Iterates through all pictures in RAWS_DIR and move new pictures to library.
for image in images:
    image_name = os.path.join(RAWS_DIR, image)
    w, h = image_parser.get_image_size(image_name)

    # Moves landscape pictures to LANDSCAPE_DIR.
    if (w, h) == (1920, 1080):
        LANDSCAPE_DIR = 'D:\\Wallpapers\\Landscape'
        try:
            shutil.move(image_name, LANDSCAPE_DIR)
            print 'Move successful (Landscape).'
        except:
            print 'File exists, move unsuccessful (Landscape).'

    # Moves portrait pictures to PORTRAIT_DIR.
    elif (w, h) == (1080, 1920):
        PORTRAIT_DIR = 'D:\\Wallpapers\\Portrait'
        try:
            shutil.move(image_name, PORTRAIT_DIR)
            print 'Move successful (Portrait).'
        except:
            print 'File exists, move unsuccessful (Portrait).'

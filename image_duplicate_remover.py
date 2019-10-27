# image_duplicate_remover.py - Removes duplicate .jpg and .png in a directory.
# Run script using "python remove_dupes.py <PATH_TO_DIRECTORY>".

import sys, os, re, send2trash

IMAGE_REGEX = re.compile(r'(\w*\.jpg|\w*.png)', re.I)


def remove_duplicates(path):
    """Removes all duplicate .jpg and .png files in a directory.

    Keyword arguments:
    path -- Path to the directory.
    """

    os.chdir(path)
    all_files = os.listdir('.')
    all_images = filter(lambda f: IMAGE_REGEX.search(f), all_files)
    unique_images = []

    for image in all_images:
        with open(image, 'rb') as image_file:
            to_delete = False
            image_data = image_file.read()

            if image_data not in unique_images:
                unique_images.append(image_data)
            else:
                to_delete = True
                print 'Removed duplicate: %s' % image

        if to_delete:
            send2trash.send2trash(image)

    num_unique = len(unique_images)
    num_images = len(filter(lambda f: IMAGE_REGEX.search(f), os.listdir('.')))

    if num_unique == num_images:
        print 'Success! Number of images left in directory: %d.' % num_images
    else:
        print 'Descrepancies found when removing duplicates.'


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print 'Run script using "python remove_dupes.py <PATH_TO_DIRECTORY>".'
        sys.exit()
    else:
        path = sys.argv[1]
        remove_duplicates(path)

    sys.exit()

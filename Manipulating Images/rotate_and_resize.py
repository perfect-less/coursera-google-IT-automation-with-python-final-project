#!/usr/bin/env python3
import sys
import os

from PIL import Image

original_file_dir  = 'originalFiles/'
processed_file_dir = 'processedFiles/'

image_rotation = -90
new_width  = 600
new_height = 600


def rotate_and_resize_image(filepath, newpath):
    """Open image file at [filepath], rotate and resize it 
    and then save it as new file to [newpath] """
    image = Image.open(filepath)

    # return rotated and resized image
    try:
        image.rotate (image_rotation).resize(
                (
                    new_width,
                    new_height
                )
            ).save (
                newpath
            )
        print ('  {} resized to {}'.format (filepath, newpath))
    except:
        print ('FAILED to resize {}'.format (filepath))


def process_images(ori_dir , new_dir):
    """List all image files on the ori_dir and then save
    a new rotated and resized version of it to new_dir"""
    images = os.listdir(ori_dir)

    for image_name in images:

        if not os.path.isfile (os.path.join(ori_dir, image_name)):
            continue
        
        rotate_and_resize_image (
                os.path.join(ori_dir, image_name),
                os.path.join(new_dir, image_name) 
            )


def main ():
    ori_dir = os.path.join(os.getcwd(), original_file_dir)
    new_dir = os.path.join(os.getcwd(), processed_file_dir)
    
    process_images (ori_dir, new_dir)


if __name__ == "__main__":
    sys.exit (main())

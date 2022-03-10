#!/usr/bin/env python3
"""In this case, the image files did not have any extensions. It originally in tiff format
and need to be converte to RGB first before saved into JPEG format"""

import sys
import os

from PIL import Image

# Convertion Settings
original_file_dir  = os.path.join(os.getcwd(), 'images/')
processed_file_dir = "/opt/icons/"

image_rotation = -90 # 90 degree clockwise
new_width  = 128
new_height = 128


def rotate_and_resize_image(filepath, newpath, new_format='jpeg'):
    """Open image file at [filepath], rotate and resize it 
    and then save it as new file to [newpath] """
    # return rotated and resized image
    try:
        image = Image.open(filepath)
        image = image.rotate (image_rotation).resize(
                    (
                        new_width,
                        new_height
                    )
                ).convert(
                        'RGB'
                ).save(
                        newpath, 
                        new_format
                )
        print ('  SUCCESFULLY rotated and resized{}'.format (os.path.split(filepath)[-1]))
        
    except Exception as e:
        print ('FAILED to resize {}'.format (os.path.split(filepath)[-1]))
        print (e)


def process_images(ori_dir, new_dir):
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
    ori_dir = original_file_dir
    new_dir = processed_file_dir
    
    process_images (ori_dir, new_dir)


if __name__ == "__main__":
    sys.exit (main())

#!/usr/bin/env python3

import sys
import os

from PIL import Image

# Convertion Settings
original_file_dir  = os.path.join(os.getcwd(), 'supplier-data/images')
processed_file_dir = os.path.join(os.getcwd(), 'supplier-data/images')

new_width  = 600
new_height = 400


def rotate_and_resize_image(filepath, newpath, new_format='jpeg', new_mode='RGB'):
    """Open image file at [filepath], and resize it 
    and then save it as new file to [newpath] """
    # return rotated and resized image
    try:
        image = Image.open(filepath)

        if image.mode != new_mode:
            image = image.convert(new_mode)

        image = image.resize(
                    (
                        new_width,
                        new_height
                    )
                )

        image.save(newpath, new_format)
        
        print ('  SUCCESFULLY resized: {}'.format (os.path.split(filepath)[-1]))
        
    except Exception as e:
        print ('FAILED to resize {}'.format (os.path.split(filepath)[-1]))
        print (e)


def process_images(ori_dir: str, new_dir: str, old_extension='.tiff', new_extension='.jpeg'):
    """List all image files on the ori_dir and then save
    a new resized version of it to new_dir"""
    images = os.listdir(ori_dir)

    for image_name in images:

        if not os.path.isfile (os.path.join(ori_dir, image_name)):
            continue

        if not ori_dir.endswith(old_extension):
            continue
        
        rotate_and_resize_image (
                os.path.join(ori_dir, image_name),
                os.path.join(new_dir, image_name.removesuffix(old_extension)+new_extension) 
            )


def main ():
    ori_dir = original_file_dir
    new_dir = processed_file_dir
    
    process_images (ori_dir, new_dir)


if __name__ == "__main__":
    sys.exit (main())

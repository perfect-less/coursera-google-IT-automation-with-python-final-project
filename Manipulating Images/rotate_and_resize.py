#!/usr/bin/env python3
import sys
import os

from PIL import Image

original_file_dir  = os.path.join(os.getcwd(), 'images/')
processed_file_dir = "/opt/icons/"

image_rotation = -90 # 90 degree clockwise
new_width  = 128
new_height = 128


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
        print ('  SUCCESFULLY rotated and resized{}'.format (os.path.split(filepath)[-1]))
    except:
        print ('FAILED to resize {}'.format (os.path.split(filepath)[-1]))


def process_images(ori_dir, new_dir, old_format="tiff", new_format="jpeg"):
    """List all image files on the ori_dir and then save
    a new rotated and resized version of it to new_dir"""
    images = os.listdir(ori_dir)

    for image_name in images:

        if not os.path.isfile (os.path.join(ori_dir, image_name)):
            continue
        
        rotate_and_resize_image (
                os.path.join(ori_dir, image_name),
                os.path.join(new_dir, image_name[:-len(old_format)]+new_format) 
            )


def main ():
    ori_dir = original_file_dir
    new_dir = processed_file_dir
    
    process_images (ori_dir, new_dir)


if __name__ == "__main__":
    sys.exit (main())

#!/usr/bin/env python

import os
from gimpfu import *

def ResizeSquare(image, drawable):
    length = 128
    screen_resolution = 72
    unsharp_radius = 0.32
    unsharp_amount = 0.32
    unsharp_threshold = 32

    # Scale image to desired dimensions
    pdb.gimp_image_scale(image, length, length)

    # Scale image to desired resolution
    pdb.gimp_image_set_resolution(image, screen_resolution, screen_resolution)

    # Appy Unsharp Mask to account for lost detail in ResizeSquare
    pdb.plug_in_unsharp_mask(image, drawable, unsharp_radius, unsharp_amount, unsharp_threshold)

    # Export to PNG
    # file_path = pdb.gimp_image_get_filename(image)
    # pdb.gimp_message("file_path saved")

    # resized_path = "C:/Users/George/OneDrive/Workspace/doombuilder/00assets/1 TexturescomSource/Brick/Cinder Block/Clean/resized"
    # pdb.gimp_message("resized_path saved")

    # initial_path = os.path.commonprefix([file_path,resized_path])
    # pdb.gimp_message("initial_path saved")

    # filename = file_path[initial_path[-1],file_path[-1]]
    # pdb.gimp_message("filename saved")

    # pdb.gimp_message("Export PNG")
    # pdb.file_png_save_defaults(image, drawable, resized_path + filename, resized_path + filename)
    # pdb.gimp_message("PNG Exported")




    

register(
    "python-fu-ResizeSquare",
    "Adjusting large images to look pixelated for GZDoom",
    "Adjust edges to 128px, resolution to 72x72 dpi, Apply Unsharp Mask(.32, .32, 32)",
    "George Schafer", "George 'Jadedrakerider' Schafer", "2023",
    "ResizeSquare",
    "",
    [
        (PF_IMAGE, "image", "takes current image", None),
        (PF_DRAWABLE, "drawable", "Input layer", None)
    ],
    [],
    ResizeSquare, menu="<Image>/DOOMify")  # end Register

main()
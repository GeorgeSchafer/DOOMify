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
    source_path = "C:/Users/George/OneDrive/Workspace/doombuilder/00assets/1 TexturescomSource"
    export_path = "C:/Users/George/OneDrive/Workspace/doombuilder/00assets/assets/textures/texturescom"
    file_path = pdb.gimp_image_get_filename(image)
    file_path = file_path[len(source_path):]
    export_path += file_path
    # export_path defined
    
    png_path = export_path[0:-3]
    png_path += "png"
    # png_path defined

    pdb.file_png_save_defaults(image, drawable, png_path, png_path)
    # png exported




    

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
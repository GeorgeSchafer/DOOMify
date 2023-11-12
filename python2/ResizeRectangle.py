#!/usr/bin/env python

import os
from gimpfu import *

def ResizeRectangle(image, drawable):
    width = 256
    length = 128
    screen_resolution = 72
    unsharp_radius = 0.32
    unsharp_amount = 0.32
    unsharp_threshold = 32

    # Scale image to desired dimensions
    pdb.gimp_image_scale(image, width, length)

    # Scale image to desired resolution
    pdb.gimp_image_set_resolution(image, screen_resolution, screen_resolution)

    # Appy Unsharp Mask to account for lost detail in Resize-Square
    pdb.plug_in_unsharp_mask(image, drawable, unsharp_radius, unsharp_amount, unsharp_threshold)

    toResized(image, drawable)

def toResized(image, drawable):
    # Export to PNG
    # Setup export
    export_folder = "resized"
    export_path = ""
    file_path = pdb.gimp_image_get_filename(image)
    file_path_list = file_path.split(os.path.sep)
    if os.name == "nt":
        file_path_list[0] += "\\\\"

    # Isolate and relabel desired filename
    png = file_path_list.pop(len(file_path_list) - 1)
    png = png[0:-3] + "png"

    # build export_path
    for x in file_path_list:
        export_path = os.path.join(export_path, x)
    export_path = os.path.join(export_path, export_folder, png)

    # png export to resized folder
    pdb.file_png_save_defaults(image, drawable, export_path, export_path)


    

register(
    "python-fu-ResizeRectangle",
    "Adjusting large images to look pixelated for GZDoom",
    "Adjust edges to 128px, resolution to 72x72 dpi, Apply Unsharp Mask(.32, .32, 32)",
    "George Schafer", "George 'Jadedrakerider' Schafer", "2023",
    "ResizeRectangle",
    "",
    [
        (PF_IMAGE, "image", "takes current image", None),
        (PF_DRAWABLE, "drawable", "Input layer", None)
    ],
    [],
    ResizeRectangle, menu="<Image>/DOOMify")  # end Register

main()
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
    # Setup export
    export_folder = "resized/"
    export_path = ""
    file_path = pdb.gimp_image_get_filename(image)
    file_path_list = file_path.split("\\")
    pdb.gimp_message("setup complete")
    pdb.gimp_message("file_path_list: " + file_path_list)


    # Isolate and relabel desired filename
    
    png = file_path_list.pop(file_path_list.count() - 1)
    pdb.gimp_message("pop finished")
    png = png[0:-3] + "png"
    pdb.gimp_message("png concatenated")
    pdb.gimp_message("png named: "+ png)

    # build export_path
    for x in file_path_list:
        export_path += x + "/"
    pdb.gimp_message("export_path started")
    
    # export_path defined
    export_path += export_folder + png
    pdb.gimp_message("export_path finished")
     
    pdb.file_png_save_defaults(image, drawable, export_path, export_path)
    pdb.gimp_message("export finished")
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
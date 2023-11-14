#!/usr/bin/env python

import os
from gimpfu import *

def ResizeSquare(image, drawable):
    # Scale image to desired dimensions
    length = width = 128
    setDimensions(image, length, width)

    # Scale image to desired resolution
    screen_resolution = 72
    setResolutions(image, screen_resolution)

    # Apply Brightness-Contrast
    brightness = -0.039
    contrast = 0.01
    applyContrast(drawable, brightness, contrast)

    # Apply Unsharp Mask to account for lost detail in ResizeSquare
    unsharp_radius = 3.0
    unsharp_amount = 0.5
    unsharp_threshold = 0.2
    applyUnsharpMask(image, drawable, unsharp_radius, unsharp_amount, unsharp_threshold)

    # Apply Index Color Profile
    dither_type = 0
    palette_type = 4
    num_cols = 256 # the number of colors to quantize to, ignored unless (palette_type == GIMP_CONVERT_PALETTE_GENERATE)
    alpha_dither = False
    remove_unused = False
    palette = "Doom"
    applyColorIndex(image, dither_type, palette_type, num_cols, alpha_dither, remove_unused, palette)

    # Export to PNG
    toResized(image, drawable)

def setDimensions(image, length, width):
    pdb.gimp_image_scale(image, length, width)

def setResolutions(image, screen_resolution):
    pdb.gimp_image_set_resolution(image, screen_resolution, screen_resolution)

def applyContrast(drawable, brightness, contrast):
    pdb.gimp_drawable_brightness_contrast(drawable, brightness, contrast)

def applyUnsharpMask(image, drawable, unsharp_radius, unsharp_amount, unsharp_threshold):
    pdb.plug_in_unsharp_mask(image, drawable, unsharp_radius, unsharp_amount, unsharp_threshold)

def applyColorIndex(image, dither_type, palette_type, num_cols, alpha_dither, remove_unused, palette):
    pdb.gimp_image_convert_indexed(image, dither_type, palette_type, num_cols, alpha_dither, remove_unused, palette)

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
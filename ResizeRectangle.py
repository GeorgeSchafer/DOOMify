#!/usr/bin/env python

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
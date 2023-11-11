#!/usr/bin/env python

from gimpfu import *

def exportPNG(image, drawable):
    file_path = pdb.gimp_image_get_filename(image)
    # file_path defined
    
    png_path = file_path[0:-3]
    png_path += "png"
    # png_path defined

    pdb.file_png_save_defaults(image, drawable, png_path, png_path)
    # png exported

register(
        "python_fu_export_png",
        "Save As PNG",
        "Exports the current image to a PNG in the current folder.",
        "George Schafer", "George 'Jadedrakerider' Schafer", "2023",
        "Save As PNG",
        "",
        [
            (PF_IMAGE, "image", "takes current image", None),
            (PF_DRAWABLE, "drawable", "Input layer", None)
        ],
        [],
        exportPNG, menu="<Image>/DOOMify")

main()
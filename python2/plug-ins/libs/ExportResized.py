#!/usr/bin/env python

import os
from gimpfu import *

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
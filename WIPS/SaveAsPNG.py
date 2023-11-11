#!/usr/bin/env python

from gimpfu import *

def exportPNG():


register(
    "python_fu_export_png",
    "Save As PNG",
    "Exports the current image to a PNG in the current folder.",
    "GeorgeSchafer",
    "Open source (BSD 3-clause license)",
    "2023",
    "<Image>/Doomify",
    "*",
    [],
    [],
    exportPNG)

main()
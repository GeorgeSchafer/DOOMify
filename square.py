#!/usr/bin/env python

from gimpfu import *

def NAME_OF_MAIN_FUNCTION(image, drawable):{
    pdb.gimp_image_scale(image, PF_RADIO[0], PF_RADIO[1])
}
    

register(
    "python-fu-DOOMify",
    "Adjusting large images to look pixelated for GZDoom",
    "Adjust one edge to 128px, resolution to 72x72 dpi, Apply Unsharp Mask(.32, .32, 32), Export to the equivalent folder",
    "George Schafer", "George 'Jadedrakerider' Schafer", "2023",
    "DOOMIFY",
    "*",
    [
        # basic parameters are: (UI_ELEMENT, "variable", "label", Default)
        (PF_IMAGE, "image", "takes current image", None),
        (PF_DRAWABLE, "drawable", "Input layer", None)
        # PF_SLIDER, SPINNER have an extra tuple (min, max, step)
        # PF_RADIO has an extra tuples within a tuple:
        # eg. (("radio_label", "radio_value), ...) for as many radio buttons
        # '2x2' 128x128
        # '2x4' 128x256
        # '2x4' 256x128
        (
            ("1x1", [64,64]),
            ("1x2", [64,128]),
            ("2x1", [128,64]),
            ("2x2", [128,128]),
            ("2x4", [128,256]),
            ("4x2", [256,128])
            
        )
        # PF_OPTION has an extra tuple containing options in drop-down list
        # eg. ("opt1", "opt2", ...) for as many options
        # see ui_examples_1.py and ui_examples_2.py for live examples
    ],
    [],
    NAME_OF_MAIN_FUNCTION, menu="<Image>")  # second item is menu location

main()
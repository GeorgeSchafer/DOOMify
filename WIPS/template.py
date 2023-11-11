#!/usr/bin/env python

from gimpfu import *

def FUNCTION_NAME(img, layer) :


register(
    "python_fu_FUNCTION_NAME",
    "TITLE",
    "SUMMARY",
    "AUTHOR",
    "LICENSE",
    "YEAR",
    "", # image types, leave blank for all
    [],
    [],
    FUNCTION_NAME, menu="<Image>/DESIRED/PATH")

main()
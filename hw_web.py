#!/usr/bin/env python3
from os import makedirs
from os.path import exists, join, expanduser

for pth in ("",
            "public",
            "public/img",
            "public/css",
            "public/js",
            "uploads",
            "etc"):
    pth = expanduser(join("~/web", pth))
    print(pth)
    if not exists(pth):
        makedirs(pth)

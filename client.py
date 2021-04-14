#!/usr/bin/env python3
#imports
import time
import tkinter
import requests

#own modules
import config as c


def load_mods(modulnames):
    global mods
    text = ""
    for i in modulnames:
        text += "import mods." + i + " as " + i + "\n"
    text += "def init():\n"
    text += "    modules = {}"
    for i in modulnames:
        text += "\n    modules[\""+ i +"\"]=" + i
    text += "\n    return modules"

    f = open("loadmodules.py","w")
    f.write(text)
    f.close()
    time.sleep(0.5)
    import loadmodules as l
    mods = l.init()
    for mod in mods:
        mods[mod].init()

load_mods(["testmod", "testmod2"])

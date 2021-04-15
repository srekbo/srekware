#!/usr/bin/env python3
#imports
import time
import tkinter
import requests
import os

#own modules
import config as c


def load_mods():
    global mods
    modulnames = []
    for file in os.listdir("mods/"):
        if file.endswith(".py") and not file.startswith(".py"):
            file = file.strip(".py")
            modulnames.append(file)
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

if __name__ == "__main__":
    load_mods()

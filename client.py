#!/usr/bin/env python3
#imports
import time
import asyncio
import tkinter
import requests
import os
import importlib

#own modules
#import config as c

active_modnames = []

async def load_all_mods():
    global mods, modnames, active_modnames
    modulnames = []
    for file in os.listdir("mods/"):
        if file.endswith(".py") and not file.startswith(".py"):
            file = file.strip(".py")
            modulnames.append(file)
    modules = {}
    for i in modulnames:
        modules[str(i)] = importlib.import_module("mods." + str(i))
    mods = modules
    modnames = modulnames
    active_modnames = []
    for mod in mods:
        mods[mod].init()
        active_modnames.append(mod)

async def add_mods():
    global mods, modnames, active_modnames
    modulnames = []
    for file in os.listdir("mods/"):
        if file.endswith(".py") and not file.startswith(".py"):
            file = file.strip(".py")
            if not str(file) in modulnames:
                modulnames.append(file)
                mods[str(file)] = importlib.import_module("mods." + str(file))
                mods[str(file)].init()
                active_modnames.append(str(file))

async def main():
    await load_all_mods()
    await asyncio.sleep(60)
    await add_mods()

if __name__ == "__main__":
    asyncio.run(main())
    print("Hi")

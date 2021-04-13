import yaml
import warnings

config = yaml.safe_load(open("config.yml"))

def get(key):
    keyARG = config
    keyA = key.split(".")
    for key in keyA:
        keyARG = keyARG.get(key)
    return keyARG
def reload():
    global config
    config = yaml.safe_load(open("config.yml"))

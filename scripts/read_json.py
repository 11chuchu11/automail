import json

def readJson(filename):
    with open(f"{filename}.json", encoding="utf-8") as info:
        data = json.load(info) 
    return data
        
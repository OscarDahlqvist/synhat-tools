import json
import simplejson
import os

def __init__():
    jsOut = {}
    jsOut["models"] = []
    cmData = -169;

    oldDat = open("old.txt").read().split("\n")
    for line in oldDat:
        if("§" in line):
            break
        [regName, dispName] = line.split("/")

        itemData = {
            "item":"minecraft:clock",
            "data":cmData,
            "model":"synhat/old/hat/"+regName,
        }
        if dispName:
            itemData["displayName"] = dispName
        else:
            makeName = " ".join([x.title() for x in regName.split("_")])
            itemData["displayName"] = makeName

        jsOut["models"].append(itemData)

        cmData+=1

    f = open(f"../source.json","w+")    
    f.write(simplejson.dumps(
        jsOut, indent=4, sort_keys=False
    ))
    f.close()
    f = open(f"../source.json","r+") 
    print(f.read())


__init__()
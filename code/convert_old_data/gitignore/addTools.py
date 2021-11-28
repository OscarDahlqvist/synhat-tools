import json

hatData = json.load(open(f"../source3.json"))
f = open(f"oldTools.txt","r")

itemIds = {}
for line in f.read().split("\n"):
    if line == "" or line[0] == "#": continue

    [path, material, name, ench] = line.split("+")
    regName = path.split("/")[-1]

    if(material in itemIds):
        itemIds[material]+=1
    else:
        itemIds[material]=1

    cmData = itemIds[material]

    if material in ["sword","axe","hoe","shovel"]: 
        material = "netherite_"+material
    elif material == "pick":
        material = "netherite_pickaxe"

    mcItem = "minecraft:"+material

    itemData = {    
        "item":mcItem,
        "data":cmData,
        "model":"synhat/old/held/"+path,
        "type":"held",
    }
    
    if name:
        itemData["displayName"] = name
    else:
        makeName = " ".join([x.title() for x in regName.split("_")])
        itemData["displayName"] = makeName

    hatData["models"].append(itemData)

jsonStr = json.dumps(hatData).replace("}, {","},\n\t{")
open(f"../source4.json","w+").write(jsonStr)

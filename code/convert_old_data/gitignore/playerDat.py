import json
import simplejson

hatData = json.load(open(f"../source.json"))
f = open(f"old_player.txt","r")

cmData = 0
for line in f.read().split("\n"):
    cmData += 1
    [uuid,lastKnownName,rank] = line.split("/")
    itemData = {
        "item":"minecraft:clock",
        "data":cmData,
        "uuid":uuid,
        "model":"synhat/player/player/"+uuid,
        "displayName":lastKnownName,
        "playerRank":rank
    }
    hatData["models"].append(itemData)

print(hatData)

f = open(f"../source2.json","w+")    
f.write(simplejson.dumps(
    hatData, indent=4, sort_keys=False
))
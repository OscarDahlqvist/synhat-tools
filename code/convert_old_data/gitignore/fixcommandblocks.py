import json

hatData = json.load(open(f"../source4.json"))

def clockFirst(str):
    if str == "minecraft:clock":
        return "AAA"
    return str

for x in hatData["models"]:
    if(x["item"] == "minecraft:command_block"):
        x["item"] = "minecraft:clock"
        num = int(x["data"])
        x["data"] = -183-num

hatData["models"].sort(
    key=lambda x: clockFirst(x["item"])
)

jsonStr = json.dumps(hatData).replace("}, {","},\n\t{")
jsonStr = jsonStr.replace("[{","[\n\t{")
open(f"../source5.json","w+").write(jsonStr)
    
import json

def clockFirst(str):
    if str == "minecraft:clock":
        return "AAA"
    return str

def xsort():
    file = "__master_models_table.json"

    inFile = open(file)
    hatData = json.load(inFile)
    inFile.close

    hatData["models"].sort(
        key=lambda x: (clockFirst(x["item"]), x["data"])
    )

    jsonStr = json.dumps(hatData).replace("}, {","},\n\t{")
    jsonStr = jsonStr.replace("[{","[\n\t{")
    open(file,"w+").write(jsonStr)

xsort()
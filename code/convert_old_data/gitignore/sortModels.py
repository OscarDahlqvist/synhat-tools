import json

def clockFirst(str):
    if str == "minecraft:clock":
        return "AAA"
    return str

def xsort():
    file = "../source5.json"

    inFile = open(file)
    hatData = json.load(inFile)
    inFile.close

    hatData["models"].sort(
        key=lambda x: clockFirst(x["item"])
    )

    jsonStr = json.dumps(hatData).replace("}, {","},\n\t{")
    jsonStr = jsonStr.replace("[{","[\n\t{")
    open(f"file","w+").write(jsonStr)
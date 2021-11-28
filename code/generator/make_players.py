import json
import requests
from requests.auth import HTTPDigestAuth
import base64
from PIL import Image, ImageDraw
import PIL as PIL

def run():
    file = "__master_models_table.json"

    inFile = open(file)
    hatData = json.load(inFile)

    for x in hatData["models"]:
        if(x["data"] <= 0): continue
        if(x["item"] != "minecraft:clock"): continue

        if(x["data"] == 1):
            uuid = x["uuid"]
            img = Image.open("temp/32xtest.png")
            (userName, path) = makeSkin(uuid)
            x["displayName"] = userName
            x["model"] = path

def makeSkin(uuid):         
    (userName, skinUrl, skinType) = getProfileData(uuid)
    img = downloadTextureFromURL(skinUrl)
    img = fixImage(img)  
    path = "synhat/player/player/"+uuid
    model = {"parent":f"synhat/player/{skinType}","textures":{"1":path}}

    modelFile = open(f"temp/out/model/{path}", "w+")
    modelFile.write(model)
    modelFile.close()
    img.save(f"temp/out/texture/{path}")

    return(userName, path)


def downloadTextureFromURL(url):
    img_data = requests.get(url, stream=True).content
    with open("temp/temp.png", 'wb') as handler:
        handler.write(img_data)    
    return Image.open("temp/temp.png")

def getProfileData(uuid):
    url = "https://sessionserver.mojang.com/session/minecraft/profile/" + uuid
    profileData = json.loads(downloadSite(url))
    userName = profileData["name"]
    skinDataStr = base64.b64decode(profileData["properties"][0]["value"])
    skinData = json.loads(skinDataStr)
    skinUrl = skinData["textures"]["SKIN"]["url"]
    skinType = "classic"
    try: 
        skinType = skinData["textures"]["SKIN"]["metadata"]["model"]
    except Exception: ""

    print(userName, skinUrl,skinType)
    return(userName, skinUrl, skinType)

def downloadSite(url):
    x = """{
  "id" : "133f9bff47f54277af2741e5eaab5902",
  "name" : "33333333333333",
  "properties" : [ {
    "name" : "textures",
    "value" : "ewogICJ0aW1lc3RhbXAiIDogMTYzMzIxNzc4NzM2MSwKICAicHJvZmlsZUlkIiA6ICIxMzNmOWJmZjQ3ZjU0Mjc3YWYyNzQxZTVlYWFiNTkwMiIsCiAgInByb2ZpbGVOYW1lIiA6ICIzMzMzMzMzMzMzMzMzMyIsCiAgInRleHR1cmVzIiA6IHsKICAgICJTS0lOIiA6IHsKICAgICAgInVybCIgOiAiaHR0cDovL3RleHR1cmVzLm1pbmVjcmFmdC5uZXQvdGV4dHVyZS85ZTBkMzRlNzRhZTE5NmU2NDQxYzc4ODFhMjY5ZjA2Y2QzMGQ5ZGRmMGQzN2IyYjVhYWVjMjYwZGMwM2FhZjhiIgogICAgfQogIH0KfQ=="
  } ]
}"""
    return x
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36"
    }
    get = requests.get(url, 
        allow_redirects=True, 
        headers=headers,
    )
    return get.content

def fixImage(img):
    if(img.height != 32): return img
    outImg = Image.new(mode="RGBA",size=[64,64])
    outImg.paste(im=img)

    imFlip = img.transpose(PIL.Image.FLIP_LEFT_RIGHT)
    #Legs
    region = cropSized(imFlip, 52, 20, 12, 12)
    outImg.paste(im=region,box=(16, 52))
    region = cropSized(imFlip, 48, 20, 4, 12)
    outImg.paste(im=region,box=(28, 52))
    region = cropSized(imFlip, 52, 16, 4, 4)
    outImg.paste(im=region,box=(24, 48))
    region = cropSized(imFlip, 56, 16, 4, 4)
    outImg.paste(im=region,box=(20, 48))
    #Arms
    region = cropSized(imFlip, 12, 20, 12, 12)
    outImg.paste(im=region,box=(32, 52))
    region = cropSized(imFlip, 8, 20, 4, 12)
    outImg.paste(im=region,box=(44, 52))
    region = cropSized(imFlip, 16, 16, 4, 4)
    outImg.paste(im=region,box=(36, 48))
    region = cropSized(imFlip, 12, 16, 4, 4)
    outImg.paste(im=region,box=(40, 48))

    #outImg.save("temp/out32test.png")
    return outImg

def cropSized(img, x, y, xsize, ysize):
    return img.crop((x, y, x+xsize, y+ysize))

run()
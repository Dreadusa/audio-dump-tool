import uuid
import json
import os
import re
import soundfile as sf
import audioread
import uuid
import shutil
from collections import OrderedDict
with open("config.txt") as f:
    config = json.load(f)
    yypDirectories = list(os.listdir(config["yypDirectory"]))
    yypThisDirectory = config["yypDirectory"]
    musDirectory = config['musDirectory']
    for pot in yypDirectories:
        if (pot.endswith(".yyp")):
            yypPath = yypThisDirectory + "\\" + pot
            yypFile = pot



def yy_load(filename):
    return json.load(open(filename), object_pairs_hook=OrderedDict)
def yy_save(data, filename):
    with open(filename, "w", newline='\r\n') as fp:
        json.dump(data, fp, indent=4)

path = os.getcwd()

viewsPath = re.sub(yypFile,"",yypPath) + "views"
viewDirectories = list(os.listdir(viewsPath))
for view_ in viewDirectories:
    with (open(viewsPath + "/" + view_)) as viewFile:
        viewJson = json.load(viewFile)
        if (viewJson['localisedFolderName'] == 'ResourceTree_Sounds'):
            soundFile = viewsPath + "/" + view_

viewJson = json.load(open(soundFile))
print(viewJson['children'])
yyp_data = yy_load(yypPath)
directories = list(os.listdir(musDirectory))
gmpath  = (re.sub(yypFile,"",yypPath)) + "sounds"
gmdirectory = list(os.listdir(gmpath))
print(gmpath)
oggs = list()
for file in directories:
    with open(musDirectory + "\\" + file) as f:
        if (f.read(3) == "Ogg"):
            oggs.append(file)
yys = list()
for ogg in oggs:
    print("yy path here" + gmpath + "/" + re.sub(".ogg","",ogg))
    if (os.path.exists(gmpath + "/" + re.sub(".ogg","",ogg))):
        continue
    else:
        #Make the folder for the set of files
        os.mkdir(gmpath + "\\" + re.sub(".ogg","",ogg))
        #Make a copy of the ogg file
        shutil.copy(musDirectory + "\\" + ogg, gmpath + "\\" + re.sub(".ogg","",ogg))
        #Strip the file format from the newly copied ogg file
        os.rename(gmpath + "\\" + re.sub(".ogg","",ogg) + "\\" + ogg, gmpath + "\\" + re.sub(".ogg","",ogg) + "\\" + re.sub(".ogg","",ogg))
        thisUuid = str(uuid.uuid4())
        sampleDict = {
            "id": str(thisUuid),
            "modelName": "GMSound",
            "mvc": "1.0",
            "name": re.sub(".ogg","",ogg),
            "audioGroupGuid": "7b2c4976-1e09-44e5-8256-c527145e03bb",
            "bitDepth": 1,
            "bitRate": 128,
            "kind": 0,
            "preload": 0,
            "sampleRate": sf.SoundFile(musDirectory + "\\" + ogg).samplerate,
            "type": 0,
            "volume": 1}
        yypDic = {
            "Value": {
            "id": str(uuid.uuid4()),
            "resourcePath": gmpath + "\\" + re.sub(".ogg","",ogg) + "\\" + (re.sub(".ogg","",ogg) + ".yy"),
            "resourceType": "GMSound"
            },
            "Key": str(thisUuid)}
       
        if sampleDict not in yyp_data['resources']:
            print("not in here!")
            yyp_data['resources'].append(yypDic)
            if os.path.exists(gmpath + sampleDict["name"] + "/" +  sampleDict["name"] + ".yy") == False:
                with (open(gmpath + "/" + sampleDict["name"] + "/" +  sampleDict["name"] + ".yy",'w')) as yyFile:
                    print("write here: " + gmpath + "/" + sampleDict["name"] + "/" +  sampleDict["name"] + ".yy",'w')
                    json.dump(sampleDict,yyFile,indent=4)

os.remove(yypPath)
yyp_data["resources"] = sorted(yyp_data["resources"])

with open(yypPath,'w') as newYypFile:
    json.dump(yyp_data,newYypFile,indent=4)

soundPath = gmpath
soundsDirectory = list(os.listdir(soundPath))
for file in soundsDirectory:
    thisYYFile = gmpath + "\\" + file + "\\" + file + ".yy"
    with open(thisYYFile) as f:
        newF = json.load(f)
        print(viewJson['children'])
        if newF['id'] not in viewJson['children']:
            viewJson['children'].append(str(newF['id']))

#with open(soundFile,'w') as newSoundFile:
#   json.dump(viewJson,newSoundFile,indent=4)
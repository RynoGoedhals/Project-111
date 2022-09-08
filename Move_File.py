import os
import shutil

fromDir = "C:/Users/rwgoe/Downloads"
toDir = "C:/Users/rwgoe/Desktop"

listOfFiles = os.listdir(fromDir)
#print(listOfFiles)

for fileName in listOfFiles:
    name, extension = os.path.splitext(fileName)

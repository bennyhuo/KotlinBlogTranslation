# coding=utf-8
import os
from datetime import datetime
from dateutils import dateutils
import urllib

os.chdir("original")
files = os.listdir(".")
fileMap = {}

for file in files:
    f = open(file, "r")
    f.readline()
    f.readline()
    datetimeString = f.readline().replace("date:", "").strip()
    time = dateutils.timeStampFromString(datetimeString, "%Y-%m-%d %H:%M:%S")
    fileMap[time] = [file, datetimeString]

sortedKeys = fileMap.keys()
sortedKeys.sort(reverse=True)

for key in sortedKeys:
    file = fileMap[key][0]
    name = file[:-3]
    encodedFile = urllib.quote(file)
    print "[" + name + "](original/" +  encodedFile + ") |" + fileMap[key][1] + "| [译文](translated/" + encodedFile +")| |"

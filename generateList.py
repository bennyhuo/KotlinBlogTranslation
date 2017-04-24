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


readme = open("README.md", "w")

head = """Kotliner.cn 计划同步翻译 Kotlin 官方博客，以下是经过处理的原文以及经过谷歌翻译的译文，如果愿意参加到翻译当中，请加 QQ 群讨论：162452394

翻译时直接修改对应译文，不要修改格式。另外，如需在发布后接受打赏，可以将 reward 设置为 true，并且提供微信和支付宝二维码图片的地址（可以外链，也可以直接上传到本仓库 /assets/文章名/ 目录，地址写绝对路径，比如 /assets/文章名/wechat.png）。


标题 | 发表时间 | 译文地址 | 译者
---|---|---|---\n"""

readme.write(head)

for key in sortedKeys:
    file = fileMap[key][0]
    name = file[:-3]
    encodedFile = urllib.quote(file)
    readme.write("[" + name + "](original/" +  encodedFile + ") |" + fileMap[key][1] + "| [译文](translated/" + encodedFile +")| |\n")

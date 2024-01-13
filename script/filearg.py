# 使用命令行语句自动化生成目标文档，由于一周内会多次提交文档，所以直接按照月份分类，时间倒序输出。 格式类似于
# `py filearg.py -new targetTitle`

import os
import sys
import argparse
from datetime import datetime, date, time, timezone


# get args
arguments = sys.argv[1:]

parser = argparse.ArgumentParser(description="create new posts ")
parser.add_argument('-t', '--title', type=str, help="new title name and no .md attribute")
args = parser.parse_args()

titleName = args.title

# warn the user if the working path is not in script:

script_directory = os.path.dirname(os.path.abspath(__file__))  # Get the directory of the script

if os.getcwd() != script_directory:
    raise NameError("hi, you should set working path to the script.")

# new post, the same name will make two markdown files

dirls = os.listdir("../post")
newName = "issue" + str(len(dirls)+1) + ".md"

with open("../post/"+newName, "w+", encoding="UTF-8") as f:
    f.write("# "+titleName+"\n\n")


##########################################################

# insert time and post list

nowtime = datetime.now(timezone.utc)
cy = nowtime.year
cm = nowtime.month

ry = ''
rm = ''


with open("../README.md", "r", encoding="UTF-8") as f:
    content = f.readlines()
    count = 0
    linecount = 0
    for line in content:
        linecount += 1
        if "#" in line and count == 0:
            count += 1
            continue
        if "#" in line and count == 1:
            count += 1
            ry = int(line[2:6])
            ryline = linecount
            continue
        if "#" in line and count == 2:
            count += 1
            rm = int(line[3:5])
            break

newPost = f"""- {newName}: [{titleName}](./post/{newName})\n"""
newPostInsertLine = ryline + 3

if ry != cy:
    content.insert(ryline-1, "# "+ str(cy)+"\n\n")
    content.insert(ryline, "## "+str(cm)+"\n\n")
    newPostInsertLine = ryline+1
    newPost += "\n"
    ry = cy
    rm = cm
# # 所有的文件操作系统都需要重新覆写整个文本文件从而在文本中间插入文本

if rm != cm:
    content.insert(ryline+1, "## "+str(cm)+"\n\n")
    newPostInsertLine = ryline+2
    rm = cm
    newPost += "\n"

if rm == cm and ry == cy:
    content.insert(newPostInsertLine, newPost)
    with open("../README.md", "w+", encoding="UTF-8") as f:
        f.writelines(content)

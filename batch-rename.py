# -*- coding = utf-8 -*-
# @Time : 2021/2/13 18:21
# @Author : 张宇
# @File : batch-rename.py
# @Software: PyCharm

import os
import re
import sys


def fileRename():
    filepath = r"C:\pythoncode\testtest\image"  # the directory of files need to rename

    currentpath = os.getcwd()  # the path where the files are
    print(currentpath)
    filelist = os.listdir(filepath)  # the list of files
    os.chdir(filepath)
    pat = r".+\.(jpg)"  # any type are support (XXX)
    print("before:" + str(filelist))

    num = 1
    for filename in filelist:
        pattern = re.findall(pat, filename)
        os.rename(filename, "周杰伦" + str(num) + ".jpg")  # rename the filename as "zhou" + str(num) + ".jpg"
        num += 1

    sys.stdin.flush()  # refresh the current directory
    filelist = os.listdir(filepath)
    print("after" + str(filelist))


if __name__ == '__main__':
    fileRename()
    print("~~~~~~~~~~rename is done!~~~~~~~~~~~~")

from Basic.dirOperation import *
import os
import subprocess

def getAPKPath(file_path):
    d = dirOperation()
    fileList = d.getAllFiles(file_path)
    return fileList

def getAPKName(file_path):
    d = dirOperation()
    fileNameList = d.getFileName(file_path)
    return fileNameList

def installAPKs(file_path):
    for i in range(0, len(getAPKPath(file_path))):
        Int = os.system('adb install -t ' + getAPKPath(file_path)[i])
        if Int == 0:
            print(getAPKName(file_path)[i] + ' install success')
        else:
            print(getAPKName(file_path)[i] + ' install fail')
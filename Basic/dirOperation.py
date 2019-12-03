#encoding:utf-8
__author__ = "GaoKun"

import os

class dirOperation(object):

    def getCWD(self):
        return os.getcwd()

    def getDIR(self, path):
        return os.listdir(path)

    def getFileName(self, path):
        fileNameList = []
        for root, dirs, files in os.walk(path):
            for file in files:
                fileNameList.append(file)
        return fileNameList

    def getAllFiles(self, path):
        fileList = []
        for root, dirs, files in os.walk(path):
            for file in files:
                fileList.append(os.path.join(root, file))
        return fileList

if __name__  ==  "__main__":
    d = dirOperation()
    for file in d.getAllFiles(r"G:\安全\Phone\testAPK"):
        print(file)

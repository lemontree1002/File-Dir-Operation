#encoding:utf-8
__author__ = "GaoKun"

from Basic.replaceContent import *
from Basic.dirOperation import *

def changeAll(file_path, old_str, new_str):
    d = dirOperation()
    r = replaceStrInFile()
    filleList = d.getAllFiles(file_path)
    for file in filleList:
        r.func1(file, old_str, new_str)

if __name__ == "__main__":
    changeAll(r"G:\hello\config", "com.zte.ajin.stockplus", "com.zte.test.stockplus")
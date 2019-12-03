#encoding:utf-8
__author__ = "GaoKun"

import sys
import os

#F:\security\phone\testAPK
path = os.path.dirname(os.getcwd())#'G:\FileAndDirOperation' 若不加，那么在cmd下运行，和运行bat时会报错
sys.path.append(path)

from Func.actionInstall import *

filePath = input("please input filePath:")

installAPKs(filePath)

os.system('pause')
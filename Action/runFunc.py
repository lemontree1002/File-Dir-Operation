#encoding:utf-8
__author__ = "GaoKun"

import sys
import os

path = os.path.dirname(os.getcwd())#'G:\FileAndDirOperation' 若不加，那么在cmd下运行，和运行bat时会报错
sys.path.append(path)

from Func.action import *

# pyFile = sys.argv[0]
# filePath = sys.argv[1]
# oldStr = sys.argv[2]
# newStr = sys.argv[3]

filePath = input("please input filePath:")
oldStr = input("please input oldStr:")
newStr = input("please input newStr:")

changeAll(filePath, oldStr, newStr)

os.system('pause')

# changeAll(r"G:\hello\config", "com.zte.test.stockplus", "com.zte.test.python.stockplus")
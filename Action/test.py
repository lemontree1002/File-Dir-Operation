#encoding:utf-8

__author__ = "GaoKun"

import sys
import os

dirname, filename = os.path.split(os.path.abspath(sys.argv[0]))
print(dirname)
print(filename)
# print(os.path.abspath(__file__))
# print(os.path.realpath(__file__))
# print(os.path.abspath(sys.argv[0]))
# print(os.path.realpath(sys.argv[0]))
print(os.getcwd())
print(os.path.dirname(os.getcwd()))#获取当前运行文件所在目录的上一级目录
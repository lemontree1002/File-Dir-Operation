#encoding:utf-8
__author__ = "GaoKun"

import string
import re
import os

class replaceStrInFile(object):

    def func1(self, file_path, old_str, new_str):
        """
        替换文件中的字符串
        :param file_path: 文件名
        :param old_str: 需要替换的字符串
        :param new_str: 替换的字符串
        :return: None
        """
        f = open(file_path, 'r+', encoding='utf-8')
        file_data = ''
        for res in f.readlines():
            if old_str in res:
                res = res.replace(old_str, new_str)
            file_data += res
        f = open(file_path, 'w', encoding='utf-8')
        f.write(file_data)
        f.close()

    def func2(self, file_path, old_str, new_str):
        """
        将替换的字符串写到一个新的文件中，然后将原文件删除，新文件改为原来文件的名字
        :param file_path: 文件名
        :param old_str: 需要替换的字符串
        :param new_str: 替换的字符串
        :return: None
        """
        f1 = open(file_path, 'r+', encoding='utf-8')
        f2 = open('%s.bak' % file_path, 'w', encoding='utf-8')
        for res in f1.readlines():
            if old_str in res:
                res = res.replace(old_str, new_str)
            f2.write(res)
        f1.close()
        f2.close()
        os.remove(file_path)
        os.rename('%s.bak' % file_path, file_path)

    def func3(self, file_path, old_str, new_str):
        """
        使用正则表达式替换文件内容re.sub方法替换
        :param file_path: 文件名
        :param old_str: 需要替换的字符串
        :param new_str: 替换的字符串
        :return: None
        """
        f1 = open(file_path, 'r+', encoding='utf-8')
        f2 = open('%s.bak' % file_path, 'w', encoding='utf-8')
        for res in f1.readlines():
            f2.write(re.sub(old_str, new_str, res))
        f1.close()
        f2.close()
        os.remove(file_path)
        os.rename('%s.bak' % file_path, file_path)

if __name__  ==  "__main__":
    r = replaceStrInFile()
    r.func3(r'G:\\AboutTestCases.xml', 'com.zte.stockplus', 'com.zte.test.stockplus')
#!/usr/bin/python
# -*- coding:utf-8 -*-

"""
dl.py
    URL先のオブジェクトをダウンロード
    シンプルな GET のみ
"""

__author__ = "tanjo"
__versoin__ = "0.0.1"
__date__ = "2014-05-20"

import sys 
import urllib
import os.path
from datetime import datetime as dt

def download(url):
    file_url = urllib.urlopen(url)
    localfile = open('file/' + os.path.basename(os.path.abspath(url)), 'wb')
    localfile.write(file_url.read())
    file_url.close()
    localfile.close()

def download_loop(urlprefix, urlsuffix, startNum, endNum):
    for var in range(startNum, endNum):
        print str(var)
        download(urlprefix + str(var) + urlsuffix)

def main():
    argvs = sys.argv;
    argc = len(argvs)
    if (argc == 2): # 単体ダウンロード
       download(argvs[1]) 
        
    elif (argc == 5): # 連番ダウンロード
        download_loop(argvs[1], argvs[2], argvs[3], argvs[4])
    else:
        print str(argc) + ' : 引数の数がおかしいです'
        for argv in argvs:
            print '    ' + argv
if __name__ == '__main__':
    main()

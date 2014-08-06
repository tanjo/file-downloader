#!/usr/bin/python
# -*- coding:utf-8 -*-

"""
dl.py
    URL先のオブジェクトをダウンロード
    シンプルな GET のみ
"""

__author__ = "tanjo"
__versoin__ = "0.0.1"
__date__ = "2014-08-06"

import sys
import urllib
import os.path
from datetime import datetime as dt
from invoke import run, task

@task
def dl(url="", prefix="", suffix="", start=0, end=0, help=False):
  if prefix:
    if suffix:
      if start < end:
        for var in range(start, end):
          print str(var)
          dl(prefix + str(var) + suffix)
        return


  if len(url) == 0 or help:
    print """
    [Usage]
      invoke dl --help
      invoke dl --url='url'
      invoke dl --prefix='http://www.sample.' --suffix='.jpg' --start=0 --end=5
    """
  else:
    file_url = urllib.urlopen(url)
    localfile = open('file/' + os.path.basename(os.path.abspath(url)), 'wb')
    localfile.write(file_url.read())
    file_url.close()
    localfile.close()

#coding:utf-8
__author__ = 'yuyc'

import os
import sys
import platform
from core import QueenBee

if platform.system() == 'Windows':
    BASE_DIR = '\\'.join(os.path.abspath(os.path.dirname(__file__)).split('\\')[:-1])
    print BASE_DIR
else:
     BASE_DIR = '/'.join(os.path.abspath(os.path.dirname(__file__)).split('/')[:-1])
     print BASE_DIR


if __name__ == '__main__':
    pass
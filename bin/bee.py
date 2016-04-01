#coding:utf-8
__author__ = 'yuyc'

import os
import sys
import platform


if platform.system() == 'Windows':
    BASE_DIR = '\\'.join(os.path.abspath(os.path.dirname(__file__)).split('\\')[:-1])
    print BASE_DIR
else:
     BASE_DIR = '/'.join(os.path.abspath(os.path.dirname(__file__)).split('/')[:-1])
sys.path.append(BASE_DIR)


from core import QueenBee

if __name__ == '__main__':
    QueenBee.ArgvHandler(sys.argv)
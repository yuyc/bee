#coding:utf-8


import os
print os.path.dirname(__file__)
print os.path.realpath(__file__)
print os.path.abspath(__file__)
print os.path.abspath(os.path.dirname(__file__)).split('\\')[:-1]
print os.path.realpath(os.path.dirname(__file__))
print os.path.abspath(os.path.dirname(__file__)).split('\\')[:-1]


print test
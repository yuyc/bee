#coding:utf-8
__author__ = 'yuyc'

import os
import sys
import datetime
import urllib
import urllib2
import json


class argv_handler(object):
    def __init__(self, argv_list):
        self.argvs = argv_list
        self.parse_argv()

    def parse_argv(self):
        if len(self.argvs) >1:
            if hasattr(self,self.argvs[1]):
                func = getattr(self,self.argvs[1])
                func()
            else:
                self.help_msg()
        else:
            self.help_msg()

    def help_msg(self):
        msg = '''
        collect_data
        run_forever
        get_asset_id
        report_asset
        '''
        print msg

    def collect_data(self):
        pass

    def run_forever(self):
        pass

    def get_asset_id(self):
        pass

    def report_asset(self):
        pass


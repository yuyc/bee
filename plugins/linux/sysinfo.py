#coding:utf-8
__author__ = 'yuyc'

import os
import re
import sys
import commands
import subprocess





class DiskPlugin(object):

    def linux(self):
        result = {'physical_disk_driver':[]}
        try:
            script_path = os.path.dirname(os.path.abspath(__file__))
            shell_command = 'sudo %s/Megacli -PDList -aALL' % script_path
            output = commands.getstatusoutput(shell_command)
            result['physical_disk_driver'] = self.parse(output[1])
        except Exception,e:
            result['error'] = e
        return result

    def parse(self,content):

        response = []
        result = []
        for row_line in content.split("\n\n\n\n"):
            result.append(row_line)
        for item in result:
            temp_dict = {}
            for row in item.split('\n'):
                if not row.strip():
                    continue
                if len(row.split(':')) != 2:
                    continue
                key,value = row.split(":")
                name = self.mega_patter_match(key)
                if name:
                    if key == 'Raw Size':
                        raw_size = re.search('(\d+\.\d+)',value.strip())
                        if raw_size:
                            temp_dict[name] = raw_size.group()
                        else:
                            raw_size = '0'
                    else:
                        temp_dict[name] = value.strip()
            if temp_dict:
                response.append(temp_dict)
        return response


    def mega_patter_match(self,needle):
        grep_pattern = {'Slot':'slot','Raw Size':'capacity','Inquiry':'model','PD Tyep':'iface_type'}
        for key,value in grep_pattern.items():
            if needle.startswitch(key):
                return value
        return False

if __name__=="__main__":
    print DiskPlugin().linux()



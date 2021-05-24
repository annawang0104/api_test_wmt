"""
-*- coding: utf-8 -*-
 
Author: wangmengting

 
"""

import logging
import os
import sys

import yaml

class Handleyaml:

    def read_yaml(self, file):
        """
        读取yaml文件，返回文件对象
        @param file:
        @return:
        """
        if os.path.isfile(file):

            fr = open(file, 'r', encoding='utf-8')
            yaml_info = yaml.safe_load(fr)
            fr.close()
            return yaml_info


        else:
            logging.error(file, '文件不存在')
            sys.exit()

if __name__ == '__main__':
    # yaml_info= Handleyaml().read_yaml("/Users/tezign/PycharmProjects/api_test_wmt/TestCase/TestLogin/Login_page.yaml")
    # print("获取到的yaml_info" % yaml_info)

    root_dir = os.path.dirname(os.path.dirname(__file__))
    config_path = os.path.join(root_dir, "TestCase")
    config_path = os.path.abspath(config_path)
    config_dir_name = os.path.join(config_path, "TestLogin")
    file_path = os.path.abspath(os.path.join(config_dir_name, "Login_page.yaml"))
    yaml_info = Handleyaml().read_yaml(file_path)
    print( yaml_info["scenario_name"])
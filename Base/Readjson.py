"""
-*- coding: utf-8 -*-
 
Author: wangmengting

 
"""

import json
import logging
import os
import sys


def read_json(file_name):
    """
    读取json文件，返回json对象
    :param file_name:
    :return:
    """


    # try:
    #     with open(file_name, "r", encoding="utf-8") as f:
    #         data = json.load(f)
    #     return data
    # except Exception:
    #     print("未找到json文件")
    #     return {}

    if os.path.isfile(file):

        fr = open(file, 'r', encoding='utf-8')
        yaml_info = json.load(fr)
        fr.close()
        return yaml_info

    else:
        logging.error(file, '文件不存在')
        sys.exit()






if __name__ == '__main__':
    file="/Users/tezign/PycharmProjects/api_test_wmt/TestCase/TestLogin/Login_page.json"
    info = read_json(file)
    for i in info["steps"]:
        print(i)


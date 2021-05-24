"""
-*- coding: utf-8 -*-
 
Author: wangmengting

 
"""
import json
import logging

import configparser
import yaml
from configparser import ConfigParser


class ReadFileData():


    def load_yaml(self,file_path):
        logging.info("加载 {} 文件......".format(file_path))
        with open(file_path, encoding='utf-8') as f:
            data = yaml.safe_load(f)
        logging.info("读到数据 ==>>  {} ".format(data))
        return data

    def load_json(self,file_path):
        logging.info("加载 {} 文件......".format(file_path))
        with open(file_path, encoding='utf-8') as f:
            data = json.load(f)
            logging.info("读到数据 ==>>  {} ".format(data))
        return data

    def load_ini(self,file_path):
        logging.info("加载 {} 文件......".format(file_path))
        cf = configparser.ConfigParser()
        cf.read(file_path, encoding="UTF-8")
        data = dict(cf._sections)
        # print("读到数据 ==>>  {} ".format(data))
        return data



if __name__ == '__main__':
    file="/Users/tezign/PycharmProjects/api_test_wmt/TestCase/TestLogin/Login_page.json"
    info = ReadFileData().load_json(file_path=file)
    for key,value in info["steps"][0].items():
        pass

    print()
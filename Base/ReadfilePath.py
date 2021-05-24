"""
-*- coding: utf-8 -*-
 
Author: wangmengting

 
"""
import os


def get_file_path(package_name,dir_name,file_name):
    root_dir = os.path.dirname(os.path.dirname(__file__))
    config_path = os.path.join(root_dir, package_name)
    config_dir_name = os.path.join(config_path, dir_name)
    file_path = os.path.abspath(os.path.join(config_dir_name, file_name))
    return file_path
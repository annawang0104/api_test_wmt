"""
-*- coding: utf-8 -*-
 
Author: wangmengting

 
"""
import os

from Base.ReadfilePath import get_file_path
from Config.readConf import Config
from Util.apiSend import send_request
from Util.assertResult import assertions
from Util.readDatamethod import ReadFileData


# conf_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config.yaml')
# print(conf_path)
root_dir = os.path.dirname(os.path.dirname(__file__))
config_path = os.path.join(root_dir, 'Config')
file_path = os.path.abspath(os.path.join(config_path, "config.yaml"))
config_info = ReadFileData().load_yaml(file_path=file_path)

def api_send_check(case_data):

    # host,port = Config().read_host_port()

    host = config_info["server_info"]["host"]
    port = config_info["server_info"]["port"]


    url= host+":"+ str(port)+ case_data["case_url"]


    result = send_request(case_data=case_data, url=url)

    assertions(case_data["case_name"], case_data, result)



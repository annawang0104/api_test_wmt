"""
-*- coding: utf-8 -*-
 
Author: wangmengting

 
"""
import cmd
import logging
import os
import sys

import allure
import pytest

from Base.ReadfilePath import get_file_path
from Util.apiSendCheck import api_send_check
from Util.readDatamethod import ReadFileData

file = get_file_path("TestCase","TestLogin","Login_page.json")

case_dict = ReadFileData().load_json(file_path=file)



@allure.feature(case_dict["scenarioName"])
class TestLogin:
    @pytest.mark.parametrize("case_data", case_dict["steps"])
    @allure.story("用户登录")
    # @pytest.mark.flaky(reruns=3, reruns_delay=3)
    def test_adminlogin(self,case_data):
        """

        :param case_data: 单个测试用例数据
        :return:
        """
        # 发送测试请求
        api_send_check(case_data)



if __name__ == '__main__':
    pytest.main('-s', '-q','--alluredir',"/Users/tezign/PycharmProjects/api_test_wmt/Result")
    md = 'allure generate ./Report/{}/allure-result -o ./Report/{}/allure-report --clean'
    logging.info("命令行执行cmd:{}".format(cmd))
    try:
        os.system(cmd)
    except Exception as e:
        logging.error('命令【{}】执行失败！'.format(cmd))
        sys.exit()

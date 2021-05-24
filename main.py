"""
-*- coding: utf-8 -*-
 
Author: wangmengting

 
"""
import logging
import os
import sys

import pytest

from Base.pubMethod import PubMethod

root_dir = os.path.dirname(__file__)

def run_all_case():

    # 测试结果文件存放目录
    result_dir = os.path.abspath("./Report/allure-result")
    # 测试报告文件存放目录
    report_dir = os.path.abspath("./Report/allure-report")
    # 本地测试历史结果文件存放目录，用于生成趋势图
    history_dir = os.path.abspath("./Report/history/")
    PubMethod.create_dirs(history_dir)
    # # 定义测试用例features集合
    # allure_features = ["--allure-features"]
    # allure_features_list = [
    #     'Register_page_case',
    #     'Login_page_case'
    # ]
    # allure_features_args = ",".join(allure_features_list)
    # # 定义stories集合
    # allure_stories = ["--allure-stories"]
    # allure_stories_args = ['']
    # allure_path_args = ['--alluredir', result_dir, '--clean-alluredir']
    # test_args = ['-s', '-q']
    # # 拼接运行参数
    # run_args = test_args + allure_path_args + allure_features + [
    #     allure_features_args] + allure_stories + allure_stories_args
    # 使用pytest.main
    run_args = ['-s', '-q', '--alluredir', result_dir]
    pytest.main(run_args)
    # 生成allure报告，需要系统执行命令--clean会清楚以前写入environment.json的配置
    cmd = 'allure generate ./Report/allure-result -o ./Report/allure-report --clean'
    logging.info("命令行执行cmd:{}".format(cmd))
    try:
        os.system(cmd)
    except Exception as e:
        logging.error('命令【{}】执行失败！'.format(cmd))
        sys.exit()

    # 打印url，方便直接访问
    url = '本地报告链接：http://127.0.0.1:63342/{}/Report/allure-report/index.html'.format(root_dir.split('/')[-1])
    print(url)

if __name__ == '__main__':
    run_all_case()





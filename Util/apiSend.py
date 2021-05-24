"""
-*- coding: utf-8 -*-
 
Author: wangmengting

 
"""
import logging
import os

import allure

from Base.requestMethod import BaseRequest as br
from Util.replaceParams import ComParams

from Util.readDatamethod import ReadFileData
import  json


response_info = {}




def send_request(case_data, url):
    """
    封装请求
    :param case_data: 单个用例数据
    :param url: 接口请求地址
    :return:
    """


    #一些需要关联的字段，比如头参数，请求参数等，首先替换关联值

    if "body" in case_data["request"]:

        body_para =ComParams().read_replace_params(response_info=response_info, data=case_data["request"]["body"])
    else:
        body_para = None

    headers_info = ComParams().read_replace_params(response_info=response_info, data=case_data["request"]["headers"])


    if case_data["request_type"].lower() == 'post':
        logging.info("请求方法: POST")

        with allure.step("POST请求接口"):
            allure.attach(name="请求接口", body=str(case_data["case_name"]))
            allure.attach(name="请求地址", body=url)
            allure.attach(name="请求头", body=str(headers_info))
            allure.attach(name="请求参数", body=str(body_para))

            if "application/x-www-form-urlencoded" in case_data["request"]["headers"]["Content-Type"]:
                result = br.post(br,header=headers_info,url=url,data=body_para["body"])
            else:

                result = br.post(br,header=headers_info,url=url,data=json.dumps(body_para))

        result[1]["response_code"] = result[0]
        response_info[case_data["case_name"]] = result[1]

        #dict格式存在每个接口的请求参数，参数名为key，接口请求结果为value



    elif case_data["request_type"].lower() == 'get':
        logging.info("请求方法: GET")
        with allure.step("GET请求接口"):
            allure.attach(name="请求接口", body=str(case_data["case_name"]))
            allure.attach(name="请求地址", body=url)
            allure.attach(name="请求头", body=str(headers_info))

            # allure.attach(name="请求参数", body=str(data["request"]["body"]))
            logging.info("请求方法: GET")

            result = br.get(br,header=headers_info, url=url, data=body_para)
        result[1]["response_code"] = result[0]
        response_info[case_data["case_name"] ] = result[1]

        # print(type(data["case_name"]))

    elif case_data["request_type"].lower() == 'put':
        logging.info("请求方法: PUT")
        with allure.step("PUT请求接口"):
            allure.attach(name="请求接口", body=str(case_data["case_name"]))
            allure.attach(name="请求地址", body=url)
            allure.attach(name="请求头", body=str(headers_info))
            allure.attach(name="请求参数", body=str(body_para))
        result = br.put(header=headers_info,url=url,data=body_para)
        result[1]["response_code"] = result[0]
        response_info[case_data["case_name"]] = result[1]


    elif case_data["request_type"].lower() == 'delete':
        logging.info("请求方法: POST")
        with allure.step("DELETE请求接口"):
            allure.attach(name="请求接口", body=str(case_data["case_name"]))
            allure.attach(name="请求地址", body=url)
            allure.attach(name="请求头", body=str(headers_info))
            allure.attach(name="请求参数", body=str(body_para))
        logging.info("请求方法: DELETE")

        result = br.delete(header=headers_info,url=url,data=body_para)
        result[1]["response_code"] = result[0]
        response_info[case_data["case_name"]] = result[1]

    else:
        result = {"code": False, "data": False}
        response_info[case_data["case_name"]] = result
    logging.info("请求接口结果：\n %s" % str(response_info))
    return response_info



if __name__ == '__main__':
    file="/Users/tezign/PycharmProjects/api_test_wmt/TestCase/TestLogin/Login_page.json"


    root_dir = os.path.dirname(os.path.dirname(__file__))
    config_path = os.path.join(root_dir, "TestCase")
    config_dir_name = os.path.join(config_path, "TestLogin")
    file_path = os.path.abspath(os.path.join(config_dir_name, "login_page.json"))

    info = ReadFileData().load_json(file_path=file_path)
    # url = "https://vms-stage-service.tezign.com"+info["steps"][0]["case_url"]
    # # print(url)
    # header = info["steps"][0]["request"]["headers"]
    # # print(header)
    # data = info["steps"][0]
    # Result = send_request(data=data,url=url)
    # print(Result)


    for n in info["steps"]:
        url = "http://10.80.82.191:30626" + n["case_url"]


        result = send_request(case_data=n, url=url)

    print(result)








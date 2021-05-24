"""
-*- coding: utf-8 -*-
 
Author: wangmengting

 
"""
import re

import allure
import json

import jsonpath

from Util.apiSend import send_request
from Util.readDatamethod import ReadFileData

success ={}


def assertions(test_name,case_data,response_info):
    """

    :param test_name: 用例名
    :param case_data: 用例测试数据
    :param response_info: 响应结果
    :return:
    """


    expect_assertion = case_data["assertions"]
    expect_code =expect_assertion["status"]

    actual_response=response_info[test_name]
    actual_code = response_info[test_name]["response_code"]


    if expect_assertion == {}:
        with allure.step("不校验结果"):
            pass

    else:

        with allure.step("第一步，校验接口http状态"):
             allure.attach("期望code", str(expect_code))
             allure.attach("实际code", str(actual_code))
        if int(actual_code) == expect_assertion["status"]:
            if expect_assertion["body"] =={} :
               allure.attach("http code校验完成")
               pass


            else:
                with allure.step("第二步，校验body内容"):
                    expect_body = expect_assertion["body"]
                   # allure.attach("期望data",str(expect_assertion["body"]))
                   # allure.attach("实际data",str(actual_response))


                # print(actual_response)

                for key, value in expect_body.items():

                    # 这种用法json路径需要用例名
                    # key_value_elem = jsonpath.jsonpath(actual_response, key)
                    # # print(key_value_elem)

                    # if str(key_value_elem[0]) == str(value):
                    #     allure.attach("body内容校验完成")
                    #     pass


                    if key in actual_response:
                        if str(actual_response[key])== str(value):

                           allure.attach("期望校验key",str(key))
                           allure.attach("期望校验的value",str(value))
                           allure.attach("实际校验的value",str(actual_response[key]))
                           pass

                    elif "$" in key:
                       key_assertions_elem = jsonpath.jsonpath(response_info, key)
                       if str(key_assertions_elem[0]) == str(value):
                           allure.attach("期望校验key", str(key))
                           allure.attach("期望校验的value", str(value))
                           allure.attach("实际校验的value", str(key_assertions_elem[0]))
                           pass
                       else:

                             raise Exception("内容校验失败！ %s ! = %s" % (key_assertions_elem[0], value))



                    # elif key =="assertion":
                    #     assertions_value = value.split(":")
                    #     assertions_elem = jsonpath.jsonpath(response_info,assertions_value[0])
                    #     if str(assertions_elem[0]) == str(assertions_value[1]):
                    #         allure.attach("body内容校验完成")
                    #         pass
                    #     else:
                    #
                    #         raise Exception("内容校验失败！ %s ! = %s" % (assertions_elem, assertions_value[1]))



                    else:
                        raise Exception("校验失败！ %s ! = %s" % (str(expect_assertion["body"]), str(actual_response)))



        else:

            raise Exception("http状态码错误！\n %s != %s" % (actual_code, expect_assertion["status"]))






















if __name__ == '__main__':
    file = "/Users/tezign/PycharmProjects/api_test_wmt/TestCase/TestLogin/Login_page.json"
    info = ReadFileData().load_json(file_path=file)

    for n in info["steps"]:
        url = "http://10.80.82.191:30626" + n["case_url"]


        result = send_request(case_data=n, url=url)

        assertions(n["case_name"],n,result)

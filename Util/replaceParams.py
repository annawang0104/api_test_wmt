"""
-*- coding: utf-8 -*-
 
Author: wangmengting

 
"""
import re

import jsonpath

# from Util.apiSend import send_request
from Util.readDatamethod import ReadFileData


class ComParams():



    def read_replace_params(self,response_info,data):
        """

        :param response_info:接口返回结果集
        :param data:存在需要取关联key的参数，比如头参数，para，及传入data["request"]["body"]数据即可
        :return:
        """

        if isinstance(data,dict):

          for key, value in data.items():
            if isinstance(value, dict):
                data[key] = self.read_replace_params(response_info=response_info, data=value)
            elif isinstance(value, list):
                for k, i in enumerate(value):
                    data[key][k] = self.read_replace_params(response_info=response_info, data=i)
            else:

                relevance_list = re.findall(r"\$\.{(.*?)}", str(value))  # 使用正则表达式取出需要关联的值

                # if len(relevance_list) == 0:
                #     pass
                # else:

                for n in relevance_list:

                        replace_elem = jsonpath.jsonpath(response_info, n)
                        data[key] = str(replace_elem[0])

        return data















if __name__ == '__main__':
    file="/Users/tezign/PycharmProjects/api_test_wmt/TestCase/TestLogin/Login_page.json"
    info = ReadFileData().load_json(file_path=file)



    result ={}
    # response_info = json.dumps(Result)
    #
    # n = info["steps"][0]
    # url = "http://10.80.82.191:30626" + n["case_url"]
    #
    # header = n["request"]["headers"]
    # Result = send_request(data=n, url=url)
    # i = info["steps"][1]["request"]["body"]
    #
    # ComParams().read_replace_params(response_info=Result, data=i)



















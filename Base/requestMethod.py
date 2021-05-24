"""
-*- coding: utf-8 -*-
 
Author: wangmengting

 
"""
import json
import logging

import simplejson

import requests


class BaseRequest:

    def post(self, header, url,  data):
        """
        post 请求
        :param header:  请求头
        :param url:  请求接口路径
        :param data: 请求参数
        :return:
        """
        response = requests.post(url=url, data=data, headers=header, timeout=8)
        try:
            if response.status_code !=200:
                return response.status_code,response.text
            else:
                return response.status_code, response.json(), response.headers
        except json.decoder.JSONDecodeError:
            return response.status_code, '', response.headers
        except simplejson.errors.JSONDecodeError:
            return response.status_code, '', response.headers
        except Exception as e:
            logging.exception('接口报错了')
            logging.error(e)
            return {}, {}, response.headers

    def get(self,header, url, data):
        """
        get 请求
        :param header:  请求头
        :param url:  请求接口路径
        :param data: 请求参数
        :return:
        """

        response = requests.get(url=url, params=data, headers=header, timeout=8)
        if response.status_code == 301:
            response = requests.get(url=response.headers["location"])
        try:
            return response.status_code, response.json(), response.headers
        except json.decoder.JSONDecodeError:
            return response.status_code, '', response.headers
        except simplejson.errors.JSONDecodeError:
            return response.status_code, '', response.headers
        except Exception as e:
            logging.exception('接口报错了')
            logging.error(e)
            return {}, {}, response.headers

    def put(self,header, url, data):
        """
        put 请求
        :param header:  请求头
        :param url:  请求接口路径
        :param data: 请求参数
        :return:
        """
        response = requests.put(url=url, data=data, headers=header, timeout=8)
        try:
            return response.status_code, response.json(), response.headers
        except json.decoder.JSONDecodeError:
            return response.status_code, '', response.headers
        except simplejson.errors.JSONDecodeError:
            return response.status_code, '', response.headers
        except Exception as e:
            logging.exception('接口报错了')
            logging.error(e)
            return {}, {}, response.headers

    def delete(self,header, url, data):
        """
        put 请求
        :param header:  请求头
        :param url:  请求接口路径
        :param data: 请求参数
        :return:
        """
        response = requests.delete(url=url, params=data, headers=header)
        try:
            return response.status_code, response.json(), response.headers
        except json.decoder.JSONDecodeError:
            return response.status_code, '', response.headers
        except simplejson.errors.JSONDecodeError:
            return response.status_code, '', response.headers
        except Exception as e:
            logging.exception('接口报错了')
            logging.error(e)
            return {}, {}, response.headers



if __name__ == '__main__':

    url = "https://vms-service.tezign.com/material/search/list"
    data = {
    "filterMap": {},
    "searchText": {
        "张三_30s": []
    },
    "startPoint": 0,
    "endPoint": 1000
}

    header={
           "Content-Type": "application/json",
           "origin": "https://vms-t13.tezign.com",
           "X-Token": "67ca7a6cb0a80dcf2edf5d6fe7db44f1",
           "X-User-Id": "1"
         }


    result=BaseRequest.post(BaseRequest,header=header,url=url,data=json.dumps(data))

    list = result[1]["result"]["list"]
    id_list={}

    for x in list:
        id_list[x["CORE_NAME"]]=x["CORE_ID"] ;
        print(x["CORE_NAME"])














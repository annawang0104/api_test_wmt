"""
-*- coding: utf-8 -*-
 
Author: wangmengting

 
"""
import logging
import os
import random
import string
import sys
import time
from _md5 import md5
from datetime import timedelta, datetime

import allure




class PubMethod:
    @staticmethod
    def get_rand_mac():
        mac = [0x00, 0x16, 0x3e,
               random.randint(0x00, 0x7f),
               random.randint(0x00, 0xff),
               random.randint(0x00, 0xff)]
        return ':'.join(map(lambda x: "%02x" % x, mac))

    @staticmethod
    def get_rand_num(min=10, max=200, type=1):
        """
        获取随机数
        :param min:最小值
        :param max: 最大值
        :param type: 类型，1为浮点型，2为布尔值，0为整型
        :return:
        """
        value = random.uniform(min, max)
        if type == 1:
            return float(round(value, 1))
        elif type == 0:
            return int(value)
        elif type == 2:
            return random.randint(0, 1)

    @staticmethod
    def empty_local_dir(local_file_dir):
        files = os.listdir(local_file_dir)
        if len(files) > 0:
            for file in os.listdir(local_file_dir):
                file_path = os.path.join(local_file_dir, file)
                if 'ovpn' in file or 'json' or 'test_result' or 'png' in file:
                    os.remove(file_path)
            print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), '本地文件夹清空成功！', local_file_dir)

        else:
            print('%s此文件夹没有待清除文件！' % local_file_dir)

    @staticmethod
    def get_time_stamp(delta=0, delta_type='h', time_format='%Y-%m-%dT%H:%M:%SZ'):
        """
        获取时间戳
        :param delta: 要增加或者减少的时间
        :param delta_type: 单位 d:天 h:小时 m:分钟 s:秒
        :param time_format: 显示格式
        :return:
        """
        if delta_type == 'h':
            delta_time = timedelta(hours=delta)
        elif delta_type == 'm':
            delta_time = timedelta(minutes=delta)
        elif delta_type == 's':
            delta_time = timedelta(seconds=delta)
        elif delta_type == 'd':
            delta_time = timedelta(days=delta)
        else:
            delta_time = 0
        time_stamp = datetime.utcnow() + delta_time
        return time_stamp.strftime(time_format)



    @staticmethod
    def transfer_md5(msg):
        hl = md5()
        hl.update(msg.encode('utf-8'))
        return hl.hexdigest().upper()










    @staticmethod
    def random_string(strings=string.ascii_letters, length=15):
        """
        获取随机字符串
        @param strings:
        @param length:
        @return:
        """
        values = ''.join(random.choices(strings, k=length))
        return values



    @staticmethod
    def create_file(file_path):
        """
        创建文件，当目录不存在时自动创建
        :param file_path:
        :return:
        """
        dir_path = os.path.split(file_path)[0]
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
        if not os.path.isfile(file_path):
            f = open(file_path, mode='w', encoding='utf-8')
            f.close()

    @staticmethod
    def create_dirs(file_dir):
        """
        创建文件路径,先判断目录是否存在
        :param file_dir:
        :return:
        """
        if not os.path.exists(file_dir):
            os.makedirs(file_dir)



    # @staticmethod
    # def screen_picture(driver):
    #     """
    #     截图操作
    #     @return:
    #     """
    #     try:
    #         logging.info("正在进行截图操作：")
    #         picture_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    #         file_path = "Report/picture"
    #         file_name = picture_time + ".png"
    #         FileOption.file_mkdir(file_path)
    #         res = driver.get_screenshot_as_file(file_path + '/' + file_name)
    #         picture_url = file_path + '/' + file_name
    #         allure.attach.file(picture_url, attachment_type=allure.attachment_type.PNG)
    #         logging.info("截图成功，picture_url为：{}".format(picture_url))
    #     except Exception as e:
    #         logging.error("截图失败，错误信息为：{}".format(e))
    #     finally:
    #         return picture_url

    # @staticmethod
    # def create_docker_hub_container(base_url, image, name, ports):
    #     """
    #     创建selenium的hub节点
    #     @param base_url:
    #     @param image:
    #     @param name:
    #     @param ports:
    #     @return:
    #     """
    #     client = docker.DockerClient(base_url=base_url)
    #     try:
    #         client.containers.run(
    #             image=image,
    #             detach=True,
    #             tty=True,
    #             stdin_open=True,
    #             restart_policy={'Name': 'always'},
    #             name=name,
    #             ports=ports,
    #             privileged=True
    #         )
    #     except Exception as e:
    #         print("创建容器失败，错误信息：{}".format(e))
    #
    # @staticmethod
    # def create_docker_node_container(base_url, image, name, ports, links):
    #     """
    #     在docker中创建selenium的node节点
    #     @param base_url: docker的URL
    #     @param image: 镜像
    #     @param name: 命名
    #     @param ports: 端口
    #     @param links: 连接
    #     @return:
    #     """
    #     client = docker.DockerClient(base_url=base_url)
    #     try:
    #         client.containers.run(
    #             image=image,
    #             detach=True,
    #             tty=True,
    #             stdin_open=True,
    #             restart_policy={'Name': 'always'},
    #             name=name,
    #             ports=ports,
    #             links=links,
    #             privileged=True
    #         )
    #     except Exception as e:
    #         print("创建容器失败，错误信息：{}".format(e))
    #
    #

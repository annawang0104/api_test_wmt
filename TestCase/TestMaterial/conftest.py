"""
-*- coding: utf-8 -*-
 
Author: wangmengting

 
"""

import pytest

from Base.ReadfilePath import get_file_path
from Util.apiSendCheck import api_send_check
from Util.readDatamethod import ReadFileData

file = get_file_path("TestCase","TestLogin","Login_page.json")

case_dict = ReadFileData().load_json(file_path=file)

@pytest.fixture(scope="function")

def login_in_load():

        # @pytest.mark.flaky(reruns=3, reruns_delay=3)

        case_data =case_dict["steps"][0]


        api_send_check(case_data)
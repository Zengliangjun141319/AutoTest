# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     LoginAPITest.py
   Description :
   Author :        曾良均
   QQ:             277099728
   Date：          8/27/2021 3:02 PM
-------------------------------------------------
   Change Activity:
                   8/27/2021:
-------------------------------------------------
"""
__author__ = 'ljzeng'

import unittest
import requests
from urllib import parse
from Common.excel import excel
import ddt
from Common.logger import Log
import os
import time

url = 'http://iron.soft.rz/login/Login.aspx?tp=dologin'

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

file_path = ".\TestData\loginData.xls"
testData = excel.get_list(file_path)
log = Log()
path = ".\\report"
isExists = os.path.exists(path)
if not isExists:
    os.mkdir(path)

@ddt.ddt
class LoginAPITest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        log.info("登录接口测试 ----")

    @classmethod
    def tearDownClass(cls) -> None:
        pass

    @ddt.data(*testData)
    def test_logins(self, data, expect=True):
        '''登录测试'''
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',
            'Content-Type': 'text/plain;charset=UTF-8'}

        log.info("测试 --  " + data["casename"])
        user = data["user"]
        pwd = data["pwd"]
        ss = user + 'ª' + pwd
        paydata = ss.encode('utf8')

        time.sleep(1)
        resut = requests.post(url=url, headers=headers, data=paydata)

        ms = []
        for a in resut.text.split(','):
            ms += [a]

        message = ms[1].split(':')[1]
        message = message[1:-1]

        ts = (message == data["mess"])
        if self.assertEqual(message, data["mess"], "ts is %s, expect is %s" %(message, data["mess"])):
            log.info("用例 %s 测试失败" %data["casename"])
        else:
            log.info("用例 %s 测试成功" %data["casename"])
            log.info("")

if __name__ == '__main__':
    unittest.main()

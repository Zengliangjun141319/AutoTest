# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     UserManageAPITest.py
   Description :
   Author :        曾良均
   QQ:             277099728
   Date：          9/7/2021 3:07 PM
-------------------------------------------------
   Change Activity:
                   9/7/2021:
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
from Common.loginsapi import login
from Common.queryMSSQL import *

log = Log()
path = ".\\report"
isExists = os.path.exists(path)
if not isExists:
    os.mkdir(path)

loginuser = 'admin@iicon001.com'
s = requests.session()
global iiabc,sites,useriid,appname
file_path = "TestData\\api-userdata.xls"
testData = excel.get_list(file_path)

@ddt.ddt
class UserManageAPITest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        log.info("用户管理接口测试 ----")
        global iiabc, sites, appname
        init = login(s, loginuser=loginuser)
        if init:
            iiabc = init[1]
            sites = init[2][:45]
            appname = sites[31:]
        else:
            exit()


    @classmethod
    def tearDownClass(cls) -> None:
        pass


    @ddt.data(*testData)
    def test01_adduser(self, data):
        log.info("测试： %s" % data["casename"])
        global iiabc,sites,useriid
        adduserurl = sites + '/Security/AddUser.aspx'
        addheaders = {
            'Accept':'application/json, text/javascript, */*; q=0.01',
            'X-Requested-With':'XMLHttpRequest',
            'Cookie': 'ir_lusname_=%s; iiabc_lang=en-us; iiabc_=%s; basemap=topo;' %(loginuser,iiabc),
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'user-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
        }

        id = data["userid"]
        displayname = data["username"]
        pwd = data["pwd"]

        ClientData = '{"UserInfo":{"ID":"%s","DisplayName":"%s","TextAddress":"","Mobile":"","BusinessPhone":"","Active":true,"UserType":"2","IsUser":true,"AllowLoginIntoPC":false,"AllowLoginIntoInspectMobile":false,"AllowLoginIntoFleetMobile":false,"AllowMobileBarcodeScanning":false,"ContactType":"100","ManagerIID":"","Notes":"","EmailOptOut":false,"InspectEmailList":false,"TeamIntelligenceUser":false,"FOB":"","HourlyRate":-1,"LandingPage":"MapView.aspx","PreferredLanguage":"","LocationIds":[],"DepartmentIds":[],"TransPass":"%s"},"Subscribe":null,"Features":[{"Key":100,"Value":["0"]},{"Key":220,"Value":["0"]},{"Key":600,"Value":["0"]},{"Key":601,"Value":["0"]},{"Key":602,"Value":["0"]},{"Key":1000,"Value":["0"]}],"Schedule":{"$type":"FI.FIC.EmailSchedule, FICBLC","ScheduleItems":{"$type":"FI.FIC.EmailScheduleItem[], FICBLC","$values":[]}}}' % (id, displayname, pwd)
        datas = 'MethodID=-1&MethodName=AddUser&ClientData=' + parse.quote(ClientData)    # 对参数内容进行URL编码

        time.sleep(1)
        adduserRes = s.post(url=adduserurl, headers=addheaders, data=datas)

        try:
            mess = adduserRes.text.split('","')[1]
            mess = str(mess)[:-2]
            useriid = adduserRes.text.split('","')[0]
            useriid = str(useriid)[2:]
            log.info("测试 新建用户 成功")
            log.info("新建的用户IID是： %s" % useriid)

        except:
            mess = adduserRes.text
            mess = mess[1:-1]

        # print(mess)
        self.assertEqual(mess, data["mess"], "实际：%s, 预期：%s" % (mess, data["mess"]))


    def test02_getuserlist(self):
        global iiabc,sites,useriid
        log.info("测试： 检查用户列表")

        # 查看用户列表
        headers = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'X-Requested-With': 'XMLHttpRequest',
            'Cookie': 'ir_lusname_=%s; iiabc_lang=en-us; iiabc_=%s; basemap=topo;' % (loginuser, iiabc),
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'user-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
        }

        usermanurl = sites + '/Security/UserManage.aspx'
        getuserres = s.post(url=usermanurl, headers=headers, data='MethodID=-1&MethodName=GetUsers&ClientData=')

        # assertIn(self, member, container,msg=None)
        self.assertIn(useriid, getuserres.text)


    def test03_edituser(self):
        global iiabc,sites,useriid
        log.info("测试： 编辑用户为 %s" %useriid)
        url = sites + 'Security/AddUser.aspx'
        headers = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'X-Requested-With': 'XMLHttpRequest',
            'Cookie': 'ir_lusname_=%s; iiabc_lang=en-us; iiabc_=%s; basemap=topo;' % (loginuser, iiabc),
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'user-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
        }

        ClientData = '{"UserInfo":{"ID":"apitest01@iicon001.com","DisplayName":"Api+Test01","TextAddress":"","Mobile":"","BusinessPhone":"","Active":true,"UserType":"1","IsUser":true,"AllowLoginIntoPC":true,"AllowLoginIntoInspectMobile":true,"AllowLoginIntoFleetMobile":false,"AllowMobileBarcodeScanning":false,"ContactType":"100","ManagerIID":"","Notes":"","EmailOptOut":true,"InspectEmailList":false,"TeamIntelligenceUser":false,"FOB":"","HourlyRate":-1,"LandingPage":"MapView.aspx","PreferredLanguage":"fr-fr","LocationIds":[],"DepartmentIds":[],"IID":"%s"},"Subscribe":{"$type":"FI.FIC.Contracts.DataObjects.BaseObject.SubscribeMessageByEmail,+FICIntfAdv","NeedSendMessages":[],"UserEmail":"","UserTextMessage":""},"Features":[{"Key":100,"Value":["99999"]},{"Key":220,"Value":["0"]},{"Key":600,"Value":["1"]},{"Key":601,"Value":["99999"]},{"Key":602,"Value":["0"]},{"Key":1000,"Value":["0"]}],"Schedule":{"$type":"FI.FIC.EmailSchedule,+FICBLC","ScheduleItems":{"$type":"FI.FIC.EmailScheduleItem[],+FICBLC","$values":[]}}}' % useriid
        datas = 'MethodID=-1&MethodName=EditUser&ClientData=' + parse.quote(ClientData)  # 对参数内容进行URL编码
        time.sleep(1)

        editres = s.post(url=url, headers=headers, data=datas)

        try:
            mess = editres.text.split('","')[1]
            mess = str(mess)[:-2]
        except:
            mess = editres.text
            mess = mess[1:-1]

        self.assertEqual(mess, 'Saved successfully.', "实际：%s, 预期：Saved successfully." % mess)


    def test04_deluser(self):
        global iiabc,sites,useriid
        log.info("测试： 删除用户 %s" % useriid)
        url = sites + 'Security/UserManage.aspx'
        headers = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'X-Requested-With': 'XMLHttpRequest',
            'Cookie': 'ir_lusname_=%s; iiabc_lang=en-us; iiabc_=%s; basemap=topo;' % (loginuser, iiabc),
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'user-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
        }

        datas = 'MethodID=-1&MethodName=DeleteUser&ClientData=' + useriid

        delres = s.post(url=url, headers=headers, data=datas)

        mess = delres.text[1:-1]
        self.assertEqual(mess, 'OK', "实际：%s, 预期：OK" % mess)


if __name__ == '__main__':
    unittest.main()

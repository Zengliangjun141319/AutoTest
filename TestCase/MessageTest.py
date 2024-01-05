# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     MessageTest.py
   Description :
   Author :        曾良均
   QQ:             277099728
   Date：          10/11/2021 9:52 AM
-------------------------------------------------
   Change Activity:
                   10/11/2021:
-------------------------------------------------
"""
__author__ = 'ljzeng'

import unittest
from Page.loginpage import LoginPage
from logger import Log
from operater import browser
import unittest
import time
import os

log = Log("MessageTest")

# path = '.\\report'
#
# if not os.path.exists(path):
#     os.mkdir(path)


class MessageTest(unittest.TestCase):
    # 元素
    messageIcon_loc = ('id', 'iconmessage')
    firstmessage_loc = ('xpath', '//*[@id="divmsgcontainer"]/div/div/div')  # 第一条message
    firstMessWO_loc = ('xpath', '//*[@id="divmsgcontainer"]/div/div/div[1]/div[1]/a')
    firstMessDel_loc = ('xpath', '//*[@id="divmsgcontainer"]/div/div/div[1]/div[3]/em[@class="spanbtn icondelete"]')
    Delyes_loc = ('xpath', '/html/body/div[@class="dialog popupmsg"]/div[@class="dialog-func"]/input[2]')
    # //*[@id="divmsgcontainer"]/div/div/div[@class="msgitem unreadmsg"]
    firstUnreadmessage_loc = ('xpath', '//*[@id="divmsgcontainer"]/div/div/div[@class="msgitem unreadmsg"]/div[1]')
    firstUnreadMeTitle_loc = ('xpath', '//*[@id="divmsgcontainer"]/div/div/div[@class="msgitem unreadmsg"]/div[2]')

    # Work Order页面元素
    commmets_loc = ('xpath', '//*[@id="communication_holder"]/div[2]/div[2]/textarea')  # ('id', 'dialog_comments')
    # //*[@id="divcontent"]/div/div[2]/div/div[2]/div[3]/div[1]/table/tbody/tr/td/div/div/span[2]
    sendComments_loc = ('xpath', '//*[@id="communication_holder"]/div[2]/div[2]/div/button[2]')
    sendResult_loc = ('xpath', '//*[@id="divcomments"]/div[1]/div[2]')

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = browser()
        cls.login = LoginPage(cls.driver)
        cls.login.login('atmessage@iicon004.com', 'Win.12345')
        log.info("开始测试Message相关功能 ---- ")
        cls.driver.implicitly_wait(60)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def messageManage(self):
        # 点击Message打开列表
        self.login.click(self.messageIcon_loc)
        try:
            self.login.find_element(self.firstUnreadmessage_loc)
        except:
            log.info("没有未读信息")
            res = False
        else:
            self.login.click(self.firstUnreadMeTitle_loc)  # //*[@id="divmsgs"]/div[3]/div[2]/div[4]/div[2]
            log.info("阅读消息成功！ ")

        try:
            self.login.find_element(self.firstmessage_loc)
        except:
            log.info("没有message信息")
            res = False
        else:
            self.login.click(self.firstMessDel_loc)
            time.sleep(1)
            self.login.click(self.Delyes_loc)
            res = True
            log.info("删除Message成功！")
        self.assertEqual(res, True)

    def openWO(self, comms):
        # 点击Message列表中的WO打开Work Order页面
        try:
            self.login.find_element(self.firstmessage_loc)
        except:
            log.info("没有Message")
            res = False
        else:
            self.login.click(self.firstMessWO_loc)
            time.sleep(2)
            self.driver.switch_to.window(self.driver.window_handles[1])
            self.driver.implicitly_wait(60)
            try:
                while True:
                    if self.login.pageload():
                        time.sleep(1)
                        break
                    else:
                        time.sleep(2)
                        log.info("页面未加载完，继续等待...")
                        continue
                time.sleep(5)
                self.login.find_element(self.commmets_loc)
            except:
                log.info("没找到Comments输入框")
                res = False
            else:
                time.sleep(3)
                log.info('发送内部交流： %s' % comms)
                self.login.send_keys(self.commmets_loc, comms)
                # 横向滚动条 content1
                self.login.js_execute("document.getElementById('content1').scrollLeft=300")
                time.sleep(5)
                self.login.click(self.sendComments_loc)
                time.sleep(3)
                els = self.driver.find_elements_by_xpath('//*[@id="communication_holder"]/div[2]/div[3]/div[@class="item-div"]')
                ms = []
                for ls in els:
                    txt = ls.find_element_by_xpath('./div[2]/span').text
                    ms += [txt]

                res = False
                for i in range(0, len(ms)):
                    log.info('Comments: %s' % ms[i])
                    if ms[i] == comms:
                        res = True
                        break
                # res = (txt == comms)
                if res:
                    log.info("回复内部交流成功! ")

            self.driver.switch_to.window(self.driver.window_handles[0])
        self.assertEqual(res, True)

    def test01_messagetest(self):
        '''测试点击阅读未读信息及删除第一条信息'''
        self.messageManage()

    def test02_WOtest(self):
        '''测试从Message打开WO并回复内部交流'''
        from datetime import datetime
        nowtime = datetime.now().strftime("%Y.%m.%d.%H%M%S.%f")[:-3]
        mess = 'reply at ' + nowtime
        self.openWO(mess)


if __name__ == '__main__':
    unittest.main()

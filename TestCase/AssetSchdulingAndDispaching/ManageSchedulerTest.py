# -*-coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     ManageSchedulerTest.py
   Description :   测试Scheduler的添加
   Author :        姜丽丽
   Change List:
    1、 下拉框元素位置变更 ------ zlj  2023.8.8
-------------------------------------------------
"""
from Page.loginpage import LoginPage
from Page.AssetSchdulingAndDispaching.ManageSchedulerPage import ManageSchedulerPage
from logger import Log
from operater import browser
import pymssql
import unittest
import time
import os
import random

log = Log()
path = '.\\report'

#判断报告目录是否存在
if not os.path.exists(path):
    os.mkdir(path)

class ManageSchedulerTest(unittest.TestCase):
    @classmethod
    def setUpClass(self) -> None:
        log.info('--------开始测试Scheduler Management--------')
        self.driver = browser()
        self.login = LoginPage(self.driver)
        self.login.login('atscheduler@iicon006.com','Win.12345')
        self.driver.implicitly_wait(60)
        log.info('--------成功登录--------')

    def to_iframe(self):
        # 登录用户起始页面为Schedule管理页
        self.scheduler = ManageSchedulerPage(self.driver)
        self.driver.implicitly_wait(60)
        time.sleep(5)
        self.scheduler.switch_to_iframe(self.scheduler.iframe_loc)

    def get_assetName(self):
        while True:
            if self.scheduler.pageload():
                time.sleep(1)
                break
            else:
                time.sleep(2)
                log.info("页面未加载完，继续等待...")
                continue
        try:
            self.scheduler.click(self.scheduler.refreshBtn_loc)
            time.sleep(1)
        except:
            log.info('列表刷新不成功，等待3秒')
            time.sleep(3)
        else:
            log.info('正在刷新列表')
            time.sleep(2)

        try:
            self.scheduler.click(self.scheduler.addBtn_loc)
            time.sleep(1)
            self.scheduler.switch_to_iframe(self.scheduler.schedulerIframe_loc)
            time.sleep(2)
        except:
            log.info('--------打开Scheduler添加页面失败！--------')
        else:
            log.info('--------成功打开Scheduler添加页面！--------')
            self.scheduler.click(self.scheduler.asset_loc)
            time.sleep(1)
            asset_sel = '//*[@id="dialog_machine"]/div/div[2]/ul/li[%d]' % random.randint(2, 7)
            self.driver.find_element_by_xpath(asset_sel).click()
            # 获取选择的机器名称
            self.assetName = self.driver.find_element_by_id('dialog_vin').text
            log.info('-------- Asset Name: %s' % self.assetName)
            log.info('--------开始输入信息--------')

    def input_scheduler_information(self):
        self.current_date = time.strftime('%m/%d/%Y')
        self.get_assetName()
        self.scheduler.select_by_index(self.scheduler.jobsite_loc, random.randint(1, 7))
        self.scheduler.clear(self.scheduler.beginDate_loc)
        self.scheduler.inputTo(self.scheduler.beginDate_loc, self.current_date)
        self.scheduler.inputTo(self.scheduler.endDate_loc, self.current_date)
        self.scheduler.inputTo(self.scheduler.notes_loc, 'As for the type of incidents you want to get')
        #保存scheduler
        try:
            self.scheduler.click(self.scheduler.saveBtn_loc)
        except:
            log.info('--------保存scheduler失败！--------')
        else:
            log.info('--------完成保存操作，是否添加成功待验证！--------')

    def get_Asset_Id(self, assetName, server='192.168.25.215\\ironintel',user='fi', pw='database', dt='[FORESIGHT_FLV_IICON_006].[dbo].[MACHINES]'):
        try:
            conn = pymssql.connect(server, user, pw)
            cur = conn.cursor()  # 获取光标
            sqlstr = "select MACHINEID from %s where MACHINENAME2='%s' or MACHINENAME='%s' or VIN='%s'" % (dt, assetName, assetName, assetName)
            # log.info('查询ID的SQL语句： %s' % sqlstr)
            cur.execute(sqlstr)
        except:
            log.info('--------从数据库执行查询AssetId失败！--------')
        else:
            data = cur.fetchone()
            assetId = str(data)[1:-2]
            # AssetId = str(data)
            return assetId

    def search_Scheduler(self, server='192.168.25.215\\ironintel', user='fi', pw='database', dt='[FORESIGHT_FLV_IICON_006].[dbo].[JOBSITEDISPATCH]'):
        try:
            conn = pymssql.connect(server, user, pw)
            cur = conn.cursor()  # 获取光标
            assetId = self.get_Asset_Id(self.assetName)
            sqlstr = "select assetId from %s where ASSETID=%s" % (dt, assetId)
            # log.info('搜索机器的SQL为： %s' % sqlstr)
            cur.execute(sqlstr)
        except:
            log.info('--------从数据库执行查询Scheduler失败！--------')
        else:
            data = cur.fetchone()
        if str(data):
            return True
        else:
            return False

    @classmethod
    def tearDownClass(self) -> None:
        self.driver.quit()

    def test_add_scheduler(self):
        self.to_iframe()
        self.input_scheduler_information()
        res = self.search_Scheduler()
        if res == False:
            log.info('-----添加Scheduler失败！----')
        else:
            log.info('-----已验证Scheduler添加成功！----')
        self.assertTrue(res)


if __name__ == '__main__':
    unittest.main()






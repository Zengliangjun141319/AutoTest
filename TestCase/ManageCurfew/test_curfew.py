# coding:utf-8

import os
from operater import browser
from logger import Log
from TestCase.ManageCurfew.curfew_pub import curfew_IronSite
import unittest
from skiptest import skip_dependon
from Page.loginpage import LoginPage
import time
from queryMSSQL import delSQL

log = Log()
path = ".\\report"

if not os.path.exists(path):
    os.mkdir(path)


class CurfewConfigTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = browser("chromeH")
        cls.loginer = LoginPage(cls.driver)
        cls.loginer.login("atcurfew@iicon004.com", "Win.12345")
        cls.driver.implicitly_wait(35)
        log.info('-----开始测试Curfew相关功能')
        # 初始化
        dt = 'FORESIGHT_FLV_IICON004'
        querystr = "delete from CURFEW where TITLE='Plan100'"
        delSQL(dt=dt, sqlstr=querystr)
        time.sleep(10)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def test01_addcurfew(self):
        '''添加Curfew'''
        log.info('测试添加Curfew------')
        time.sleep(5)
        text = curfew_IronSite(self.driver).open_addwindow()
        res = (text == 'Saved successfully.')
        if res:
            log.info('添加Curfew成功')
        else:
            log.info('添加Curfew失败')
        self.assertTrue(res)

    # 如果新增Curfew失败，则跳过搜索Curfew测试
    @skip_dependon(depend='test01_addcurfew')
    def test02_searchcurfew(self):
        '''搜索Curfew'''
        res = curfew_IronSite(self.driver).search_curfew()
        if res:
            log.info('搜索Curfew测试成功')
        else:
            log.info('搜索Curfew测试失败')
        self.assertTrue(res)

    # 如果新增Curfew失败，则跳过删除Curfew测试
    @skip_dependon(depend='test01_addcurfew')
    def test03_delCurfew(self):
        '''删除Curfew'''
        curfew_IronSite(self.driver).delete_curfew()
        res = curfew_IronSite(self.driver).search_curfew()
        if not res:
            log.info('删除Curfew成功')
        else:
            log.info('删除Curfew失败')
        self.assertFalse(res)


if __name__ == '__main__':
    unittest.main()
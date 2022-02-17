# encoding: utf-8
# Change Log：
#     1、 2.22.128版本，增加删除功能  ---- 曾良均
#

from Page.loginpage import LoginPage
from Page.TeamIntelligence.GlobalSectionPage import GlobalSectionPage
from Common.operater import browser
from Common.logger import Log
import unittest
import os
import time
from Common.skiptest import skip_dependon

log = Log()
path = '.\\report'

if not os.path.exists(path):
    os.mkdir(path)

currenttime = time.strftime('%Y%m%d%H%M%S')
gsname = 'GS' + currenttime

class GlobalSectionTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = browser()
        log.info('------开始测试Team Global Section------')
        cls.login = LoginPage(cls.driver)
        cls.login.login("autotester@foresight.com", "1")
        cls.driver.implicitly_wait(60)
        time.sleep(3)
        cls.open_customer(cls)
        cls.open_globalsection(cls)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def open_customer(self):
        self.gs = GlobalSectionPage(self.driver)
        self.gs.click(self.gs.customerlink_loc)
        time.sleep(5)
        self.gs.send_keys(self.gs.searchinput_loc, '004')
        self.gs.click(self.gs.searchbutton_loc)
        time.sleep(2)
        self.gs.click(self.gs.customeropen_loc)
        all_h = self.driver.window_handles
        self.driver.switch_to.window(all_h[1])

    def open_globalsection(self):
        try:
            self.gs.click(self.gs.fullmenu_loc)
            self.gs.click(self.gs.teamintel_loc)
            time.sleep(3)
            self.gs.click(self.gs.globalsection_loc)
        except:
            log.info("—————打开Global Section列表失败—————")
        else:
            log.info("—————打开Global Section列表成功—————")

    def add_globalsection(self):

        try:
            self.gs.click(self.gs.addbutton_loc)
        except:
            log.info("-----打开新增窗口失败-----")
        else:
            log.info("-----打开新增窗口成功-----")

            self.gs.send_keys(self.gs.nameinput_loc, gsname)
            self.gs.send_keys(self.gs.displayinput_loc, 'Global Section' + currenttime)
            self.gs.send_keys(self.gs.notesinput_loc, 'Notes of GS' + currenttime)
            self.gs.click(self.gs.savebutton_loc)
            mess = self.gs.get_text(self.gs.savemsg_loc)
            self.gs.click(self.gs.saveok_loc)
            self.gs.click(self.gs.withoutsave_loc)
            result = (mess == 'Saved successfully.')
            if result:
                return True
            else:
                return False

    def search_del_gs(self):
        self.driver.refresh()
        self.driver.implicitly_wait(60)
        lss = self.driver.find_elements_by_xpath('//*[@id="set_right"]/div/div[3]/div')
        for l in lss:
            name = l.find_element_by_xpath('./div/div[@class="section-cell section-name"]/input').get_attribute('value')
            if name == gsname:
                l.find_element_by_xpath(
                    './div/div[@class="section-cell section-func"]/em[@title="Delete Section"]').click()
                time.sleep(1)
                self.driver.find_element_by_xpath(
                    '/html/body/div[@class="dialog popupmsg"]/div[@class="dialog-func"]/input[@value="Yes"]').click()
                time.sleep(2)
                return True
        else:
            return False


    def test01_globalsection(self):
        '''测试新建Global Section'''
        res = self.add_globalsection()
        if res:
            log.info('-----新增Global Section成功-----')
        else:
            log.info('-----新增Global Section失败-----')
        self.assertTrue(res)

    @skip_dependon(depend='test01_globalsection')
    def test02_search(self):
        '''测试搜索并删除'''
        res = self.search_del_gs()
        if res:
            log.info('删除Global Section成功')
        else:
            log.info('删除Global Section失败')
        self.assertTrue(res)

if __name__ == '__main__':
    unittest.main()

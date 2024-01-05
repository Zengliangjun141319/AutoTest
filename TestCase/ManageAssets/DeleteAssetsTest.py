import unittest
from Page.ManageAssets.ManageAssetsPage import ManageAssetsPage
from Page.loginpage import LoginPage
from Page.TeamIntelligence.GlobalSectionPage import GlobalSectionPage
from operater import browser
from logger import Log
import os
import time
from loginsapi import addAsset

log = Log()
path = '.\\report'

if not os.path.exists(path):
    os.mkdir(path)


class DeleteAssetsTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = browser("chromeH")
        cls.login = LoginPage(cls.driver)
        cls.login.login("autotester@foresight.com", "1")
        cls.driver.implicitly_wait(60)
        log.info('------开始测试删除机器功能------')
        time.sleep(3)
        # 初始化机器数据
        addAsset()
        cls.open_customer(cls)


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
        self.toFrame(self)

    def toFrame(self):
        self.ma = ManageAssetsPage(self.driver)
        self.driver.implicitly_wait(60)
        time.sleep(5)
        # Open to Manage Assets Page
        self.ma.click(self.ma.ManageAssetBtn_loc)
        time.sleep(5)

        frameA = self.driver.find_element_by_xpath('//*[@id="set_right"]/iframe')
        self.driver.switch_to.frame(frameA)
        time.sleep(2)

    def deleteAsset(self):
        # 搜索初始化添加的机器，并删除
        self.ma.SearchAssets('autoTestDelAsset')
        time.sleep(1)

        # 判断是否有机器
        try:
            assets = self.driver.find_element_by_xpath('//*[@id="machinelist"]/div/div[1]/div/table/tbody/tr')
        except:
            log.info('没找到要删除的机器')
            return False
        else:
            try:
                self.ma.click(self.ma.deleteAsset_loc)
                time.sleep(1)
                try:
                    self.ma.click(self.ma.deleteYes_loc)
                    time.sleep(1)
                except:
                    self.driver.switch_to.default_content()
                    self.ma.click(self.ma.deleteYes_loc)
                    time.sleep(1)
                    self.ma.switch_to_iframe(self.ma.iframe)
            except:
                log.info('删除操作失败')
                return False
            else:
                log.info('删除操作成功，检查删除结果')

                datas = self.driver.find_element_by_class_name('data-grid-body-content')
                asset = datas.find_elements_by_class_name('data-grid-row')
                if not asset:
                    log.info('机器删除成功')
                    return True
                else:
                    return False

    def test01_deleteAsset(self):
        '''测试页面删除机器功能'''
        res = self.deleteAsset()
        self.assertTrue(res)

if __name__ == '__main__':
    unittest.main()

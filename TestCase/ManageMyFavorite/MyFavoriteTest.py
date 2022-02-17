# coding:utf-8

import unittest
from Page.MyFavorite.MyFavoritePage import MyFavoritePage
import time
from Common.operater import browser
from Page.loginpage import LoginPage
from selenium.webdriver.common.action_chains import ActionChains
from Common.logger import Log
import os
from Common.skiptest import skip_dependon

log = Log()
# 判断保存报告的目录是否存在
path = ".\\report"
isExists = os.path.exists(path)
if not isExists:
    os.mkdir(path)

class MyFavoriteTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        log.info("Start test MyFavoriteTest ......")
        cls.driver = browser()
        cls.login = LoginPage(cls.driver)
        cls.login.login('autotester@iicon004.com', 'Win.12345')
        cls.driver.implicitly_wait(60)
        time.sleep(10)
        log.info("Step 0: Clear data")
        cls.delete_favorite(cls)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def delete_favorite(self):
        self.favorite = MyFavoritePage(self.driver)
        self.favorite.click(self.favorite.favoritemenu_loc)
        while True:
            try:
                self.favorite.find_element(self.favorite.editfavoritemenu_loc)
            except:
                break
            else:
                self.favorite.click(self.favorite.editfavoritemenu_loc)
                self.favorite.click(self.favorite.deletebutton_loc)
                self.favorite.click(self.favorite.msgboxokbutton_loc)
                self.favorite.click(self.favorite.closebutton_loc)
                time.sleep(2)
                self.favorite.click(self.favorite.favoritemenu_loc)
        ActionChains(self.driver).move_by_offset(100, 500).click().perform()


    def test_addfavorite(self):
        log.info("Step 1: Test Add Favorite")
        # time.sleep(3)
        self.driver.refresh()
        self.driver.implicitly_wait(60)
        time.sleep(5)
        self.favorite.click(self.favorite.addfavorite_loc)
        self.driver.implicitly_wait(60)
        time.sleep(5)
        self.favorite.click(self.favorite.dispatch_loc)
        self.driver.implicitly_wait(60)
        time.sleep(5)
        self.favorite.click(self.favorite.addfavorite_loc)
        time.sleep(2)
        self.favorite.click(self.favorite.jobsites_loc)
        self.driver.implicitly_wait(60)
        time.sleep(5)
        self.favorite.click(self.favorite.addfavorite_loc)
        time.sleep(2)
        self.favorite.click(self.favorite.favoritemenu_loc)
        self.driver.implicitly_wait(60)
        time.sleep(5)
        text = self.favorite.get_text(self.favorite.favoritelistmenu_loc)
        if self.assertEqual(text, "Jobsite Requirements"):
            log.info("加入收藏夹失败！")
        else:
            log.info("加入收藏夹成功！")

    @skip_dependon(depend="test_addfavorite")
    def test_downorder(self):
        log.info("Step 2: Test move down the favorite")
        time.sleep(2)
        self.favorite.click(self.favorite.editfavoritemenu_loc)
        self.favorite.click(self.favorite.downmoverbotton_loc)
        textdown = self.favorite.get_text(self.favorite.favoritesecond_loc)
        if self.assertEqual(textdown, "Jobsite Requirements"):
            log.info("向下调整顺序失败！")
        else:
            log.info("向下调整顺序成功！")

    @skip_dependon(depend="test_addfavorite")
    def test_uporder(self):
        log.info("Step 3: Test move up the favorite")
        time.sleep(2)
        self.favorite.click(self.favorite.upmovebutton_loc)
        textup = self.favorite.get_text(self.favorite.favoritefirst_loc)

        if self.assertEqual(textup, "Jobsite Requirements"):
            log.info("向上调整顺序失败！")
        else:
            log.info("向上调整顺序成功！")

if __name__ == "__main__":
    unittest.main()
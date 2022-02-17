# -*- coding:utf8 -*-

from Common.operater import browser
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from Page.loginpage import LoginPage, login_url
from Common.logger import Log
import os
import unittest
import time
from Common.queryMSSQL import *

log = Log()
now_handle = ''

# 判断保存报告的目录是否存在
path = ".\\report"
isExists = os.path.exists(path)
if not isExists:
    os.mkdir(path)

class LoginTest(unittest.TestCase):
    # @classmethod
    url = ''
    ssid = ''
    @classmethod
    def setUpClass(cls):
        # 登录IronIntel站点
        log.info("Start test login/logout and forgot password ... ")
        cls.driver = browser()
        log.debug("打开地址 %s" % login_url)
        cls.login = LoginPage(cls.driver)
        cls.login.open(login_url)
        cls.driver.implicitly_wait(60)

    @classmethod
    def tearDownClass(cls):
        # self.driver.implicitly_wait(10)
        cls.driver.quit()

    def login_case(self, username, psw, expect=True):
        log.info("Part1: Test login ... ")
        self.login.input_username(username)
        time.sleep(2)
        self.login.input_password(psw)
        self.login.click_login()
        while True:
            if self.login.pageload():
                time.sleep(1)
                break
            else:
                time.sleep(2)
                log.info("页面未加载完，继续等待...")
                continue
        self.driver.implicitly_wait(20)

        # 等待所有元素都加载
        home_log = ('id', 'button_home')
        WebDriverWait(self.driver, timeout=20).until(EC.presence_of_element_located(home_log))

        self.login.click(home_log)
        time.sleep(2)

        btnuser = ('id', 'btnuser')
        self.login.click(btnuser)
        time.sleep(2)
        spanusername = self.driver.find_element_by_id('spanusername').text
        result = (spanusername == 'Auto Test')
        self.login.click(btnuser)
        time.sleep(2)

        if self.assertEqual(result, expect):
            log.info("login fail！")
            log.info("---------------------------")
        else:
            log.info("login successfully！")
            log.info("---------------------------")

    def logout_case(self, expect=True):
        # 定位元素
        leftmenu_loc = ('id', 'btnuser')
        # //*[@id="usermenu_panel"]/ul/li[3]/table/tbody/tr/td[2]/span
        logout_loc = ('xpath', '//*[@id="usermenu_panel"]/ul/li[3]/table/tbody/tr/td[2]/span')
        loginB_loc = ('id', 'btn_login')
        log.info("Part2: Test logout ... ")
        self.login.click(leftmenu_loc)
        self.driver.implicitly_wait(1)

        self.login.click(logout_loc)
        self.driver.implicitly_wait(5)

        #判断是否回到登录页
        result = self.login.is_text_in_value(loginB_loc, 'LOGIN')
        self.assertEqual(result, expect)
        if self.assertEqual(result, expect):
            log.info("Exit failed！ ")
            log.info("---------------------------")
        else:
            log.info("Exit successfully！")
            log.info("---------------------------")

    def test01_login(self):
        '''测试界面登录'''
        self.login_case('auto@iicon004.com', 'Win.12345', True)

    def test02_logout(self):
        '''测试退出'''
        self.logout_case(True)

    def test03_forgotpassword(self):
        log.info("Part3: Test forgot password ... ")
        forgotpw_loc = ('xpath', '//*[@id="form2"]/div[4]/div/div[2]/div/div[8]/a')

        # forgotpassword.aspx
        uid = 'testforgotpw@iicon004.com'
        uid_loc = ('id', 'txt_uid')
        submit_loc = ('id', 'Button1')

        # sendpassword.aspx
        here_loc = ('xpath', '//*[@id="contentWrapper"]/div/div[3]/a')

        # changepassword.aspx
        newpw_loc = ('id', 'txtNewPassword')
        confirmpw_loc = ('id', 'txtConfirmPassword')
        save_loc = ('xpath', '//*[@id="form2"]/div[4]/div/div[2]/div/table/tbody/tr[5]/td[2]/input[1]')

        self.driver.implicitly_wait(60)
        log.info("login page click forgot password")
        self.login.click(forgotpw_loc)
        time.sleep(1)

        self.driver.implicitly_wait(60)
        log.info("input user email,submit")
        self.login.send_keys(uid_loc, uid)
        self.login.click(submit_loc)
        time.sleep(2)

        log.info("From database copy temp password")
        newpw = getTempPassword(dt='FORESIGHT_SERVICES', type='Forgot Password', uid=uid)
        log.info("temp pwd is: %s" % str(newpw))

        log.info("click here to login page")
        self.login.click(here_loc)
        self.driver.implicitly_wait(60)
        time.sleep(2)

        log.info("login user")
        self.login.input_username(uid)
        self.login.input_password(str(newpw))
        self.login.click_login()
        self.driver.implicitly_wait(60)
        time.sleep(3)

        log.info("change password")
        self.login.send_keys(newpw_loc, 'Win.12345')
        self.login.send_keys(confirmpw_loc, 'Win.12345')
        time.sleep(1)
        self.login.click(save_loc)
        time.sleep(5)
        log.info("verify password expiration")
        ex = getPWExpiration(dt='ironintel', userid=uid)
        self.assertEqual(ex, '2050-12-31 00:00:00')

if __name__ == "__main__":
    unittest.main()


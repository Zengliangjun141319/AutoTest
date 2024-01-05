# -*- coding:utf8 -*-
"""
Change Log:
  1、 增加修改密码功能测试   ---- 曾良均 2022.7.12
  2、 增加验证码测试     ---- 曾良均  2022.7.15
"""

from operater import browser
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from Page.loginpage import LoginPage, login_url
from logger import Log
import os
import unittest
from queryMSSQL import *

log = Log()
now_handle = ''

# 判断保存报告的目录是否存在
path = ".\\report"
isExists = os.path.exists(path)
if not isExists:
    os.mkdir(path)

class LoginTest(unittest.TestCase):
    # 定位元素
    url = ''
    ssid = ''
    home_log = ('id', 'button_home')
    btnuser = ('id', 'btnuser')

    changePwBtn_loc = ('xpath', '//*[@id="usermenu_panel"]/ul/li[2]/table/tbody/tr/td[2]/span')
    oldpw_loc = ('id', 'txt_old_pass')
    newpw_loc = ('id', 'txt_new_pass')
    confirmpw_loc = ('id', 'txt_new_pass2')
    changeOk_loc = ('id', 'button_submit')

    logout_loc = ('xpath', '//*[@id="usermenu_panel"]/ul/li[3]/table/tbody/tr/td[2]/span')
    loginB_loc = ('id', 'btn_login')

    @classmethod
    def setUpClass(cls):
        # 登录IronIntel站点
        log.info("Start test login/logout and forgot password ... ")
        cls.driver = browser()
        log.debug("打开地址 %s" % login_url)
        cls.login = LoginPage(cls.driver)
        cls.login.open(login_url)
        cls.driver.implicitly_wait(3)

    @classmethod
    def tearDownClass(cls):
        # self.driver.implicitly_wait(10)
        cls.driver.quit()

    def login_case(self, username, psw, expect=True):
        log.info("Part1: Test login ... ")
        self.login.login(username, psw)

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
        WebDriverWait(self.driver, timeout=20).until(EC.presence_of_element_located(self.home_log))

        self.login.click(self.home_log)
        time.sleep(2)

        self.login.click(self.btnuser)
        time.sleep(2)
        spanusername = self.driver.find_element_by_id('spanusername').text
        result = (spanusername == 'Auto Test')
        self.login.click(self.btnuser)
        time.sleep(2)

        if self.assertEqual(result, expect):
            log.info("login fail！")
            log.info("---------------------------")
        else:
            log.info("login successfully！")
            log.info("---------------------------")

    def logout_case(self, expect=True):

        # //*[@id="usermenu_panel"]/ul/li[3]/table/tbody/tr/td[2]/span
        self.driver.refresh()
        self.driver.implicitly_wait(60)
        time.sleep(3)

        log.info("Part3: Test logout ... ")
        self.login.click(self.btnuser)
        self.driver.implicitly_wait(1)

        self.login.click(self.logout_loc)
        self.driver.implicitly_wait(5)

        #判断是否回到登录页
        result = self.login.is_text_in_value(self.loginB_loc, 'LOGIN')
        self.assertEqual(result, expect)
        if self.assertEqual(result, expect):
            log.info("Exit failed！ ")
            log.info("---------------------------")
        else:
            log.info("Exit successfully！")
            log.info("---------------------------")

    def changePw(self):
        self.driver.refresh()
        self.driver.implicitly_wait(60)
        time.sleep(3)

        log.info('Part2: Test Change Password')
        self.login.click(self.btnuser)
        self.driver.implicitly_wait(1)

        try:
            self.login.click(self.changePwBtn_loc)
            time.sleep(1)
        except:
            log.info('open change password failed')
            return False
        else:
            self.login.send_keys(self.oldpw_loc, 'Win.12345')
            time.sleep(1)
            self.login.send_keys(self.newpw_loc, 'Win.12345')
            self.login.send_keys(self.confirmpw_loc, 'Win.12345')
            time.sleep(1)

            try:
                self.login.click(self.changeOk_loc)
                time.sleep(2)
                self.driver.switch_to.alert.accept()
                time.sleep(1)
            except:
                log.info('change password complete failed.')
                return False
            else:
                log.info('change password successfully')
                return True

    def forgotpw(self):
        log.info("Part4: Test forgot password ... ")
        forgotpw_loc = ('xpath', '//*[@id="form2"]/div[4]/div/div[2]/div/div[8]/a')

        # forgotpassword.aspx
        uid = 'testforgotpw@iicon004.com'
        uid_loc = ('id', 'txt_uid')
        submit_loc = ('id', 'Button1')

        # sendpassword.aspx
        here_loc = ('xpath', '//*[@id="contentWrapper"]/div/div[3]/a')

        # changepassword.aspx
        # newpw_loc = ('id', 'txtNewPassword')
        newpw_loc = ('xpath', '//*[@id="panel_reset"]/div/div/div/input[@class="textbox password"]')
        confirmpw_loc = ('xpath', '//*[@id="panel_reset"]/div/div/div/input[@class="textbox password2"]')
        save_loc = ('xpath', '//*[@id="panel_reset"]/div/div/div/input[@class="loginbutton formbutton primarybutton"]')

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
        self.assertEqual(ex, '2030-12-31 00:00:00')

    def test01_login(self):
        '''测试界面登录'''
        self.login_case('auto@iicon004.com', 'Win.12345', True)

    def test02_changepw(self):
        '''测试修改密码'''
        res = self.changePw()
        self.assertTrue(res)

    def test03_logout(self):
        '''测试退出'''
        self.logout_case(True)

    def test04_forgotpassword(self):
        '''测试忘记密码'''
        self.forgotpw()


if __name__ == "__main__":
    unittest.main()


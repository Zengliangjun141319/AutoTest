# -*- coding:utf8 -*-

from Common.operater import *
from selenium.webdriver.support.wait import WebDriverWait

login_url = "http://iron.soft.rz/login/"
class LoginPage(Operater):
    # 定位器，定位页面元素
    username_loc = ('id', 'txt_uid')
    password_loc = ('id', 'txt_pwd')
    loginB_loc = ('id', 'btn_login')
    forget_loc = ('xpath', '/html/body/form/div[4]/div/div[2]/div/div[8]/a/span')

    def __init__(self, driver):
        """初始化driver"""
        self.driver = driver
        self.open(login_url)

    def input_username(self, username):
        '''输入账号框'''
        self.send_keys(self.username_loc, username)

    def input_password(self, password):
        '''输入密码框'''
        self.send_keys(self.password_loc, password)

    def click_login(self):
        '''登录按钮'''
        self.click(self.loginB_loc)

    def click_forget(self):
        '''忘记密码'''
        self.click(self.forget_loc)

    def login(self, username='auto@iicon004.com', password='Win.12345'):
        '''登录方法'''
        self.input_username(username)
        self.input_password(password)
        self.click_login()

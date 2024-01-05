# -*- coding:utf8 -*-

from operater import *
from queryMSSQL import *
login_url = "https://iron.soft.rz/login/"


class LoginPage(Operater):
    # 定位器，定位页面元素
    username_loc = ('id', 'txt_uid')
    password_loc = ('id', 'txt_pwd')
    loginB_loc = ('id', 'btn_login')
    forget_loc = ('xpath', '/html/body/form/div[4]/div/div[2]/div/div[8]/a/span')
    termAcc_loc = ('xpath', '//*[@id="panel_bottom"]/input[@value="Accept and continue"]')

    def __init__(self, driver, url=login_url):
        """初始化driver"""
        self.driver = driver
        self.open(url)
        sys.stderr.write('Test Site is: %s\n' % url)

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

        # 获取并在页面输入验证码
        time.sleep(1)
        time0 = time.time()
        try:
            v_Inbox = self.driver.find_element_by_xpath('//*[@id="panel_verifycode"]/div/div/div[2]/input[1]')
            v_Inbox.click()
        except:
            sys.stderr.write("异常耗时: %s \n" % (time.time()-time0))
            sys.stderr.write('------ 不需要验证码! \n')
        else:
            sys.stderr.write("正常耗时: %s \n" % (time.time() - time0))
            try:
                codes = getVerifyCode(loginuser=username)
                sys.stderr.write('------ 输入验证码： %s\n' % codes)
                v_Inbox.send_keys(codes)
                time.sleep(1)
                self.driver.find_element_by_xpath('//*[@id="panel_verifycode"]/div/div/div[2]/input[2]').click()
            except Exception:
                sys.stderr.write('------ 验证码输入失败!\n')
            else:
                sys.stderr.write('------ 验证码验证正确，正常登录!\n')

        # Terms
        try:
            time.sleep(2)
            t = self.driver.find_element_by_xpath('//*[@id="panel_bottom"]/input[@value="Accept and continue"]')
            t.click()
        except Exception:
            sys.stderr.write('------ 不需要用户协议!\n')
        else:
            sys.stderr.write('------ 同意用户协议! \n')

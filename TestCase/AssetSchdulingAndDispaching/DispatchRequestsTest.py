# -*-coding: utf-8 -*-
"""
--------------------------------------------------------------------------
   File Name：     Dispatch RequestsTest.py
   Description :   测试Dispatch Requests的Eamil、Print、删除、查看历史记录等功能
   Author :        姜丽丽
   Change list:
        1、 更改下拉框元素位置  ------ zlj  2023.8.8
--------------------------------------------------------------------------
"""
from Page.loginpage import LoginPage
from Page.AssetSchdulingAndDispaching.DispatchRequestsPage import DispatchRequestsPage
from logger import Log
from operater import browser
import random
import unittest
import time
import os

log = Log()
path = '.\\report'

#判断报告目录是否存在
if not os.path.exists(path):
    os.mkdir(path)


class DispatchRequestsTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = browser()
        cls.login = LoginPage(cls.driver)
        cls.login.login('atdispatch@iicon006.com', 'Win.12345')
        cls.driver.implicitly_wait(60)
        log.info('--------开始测试Dispatch Repuests--------')
        time.sleep(5)
        # log.info('--------成功登录--------')
        cls.to_iframe(cls)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def to_iframe(self):
        self.dispatch = DispatchRequestsPage(self.driver)
        self.driver.implicitly_wait(60)
        time.sleep(5)
        try:
            ex = ('id', 'nav_arrow')
            log.info('-----收折左侧菜单')
            if not self.dispatch.is_clickable(ex):
                log.info('元素不可点击，等待3秒重试')
                time.sleep(3)
            self.dispatch.click(ex)
            time.sleep(1)
        except:
            log.info('--------打开Dispatch Requests列表失败！--------')
        else:
            log.info('--------打开Dispatch Requests列表成功！--------')
            self.dispatch.click(ex)
            time.sleep(2)
            self.dispatch.switch_to_iframe(self.dispatch.iframe_loc)
            time.sleep(1)

    def refresh(self):
        time.sleep(2)
        ref = ('xpath', '//*[@id="contentctrl"]/div[@class="function_title"]/span[@class="sbutton iconrefresh"]')
        try:
            self.dispatch.click(ref)
        except:
            log.info('刷新数据异常，重新打开页面')
            self.driver.refresh()
            self.driver.implicitly_wait(60)
            time.sleep(5)
            self.dispatch.switch_to_iframe(self.dispatch.iframe_loc)
            time.sleep(2)
        else:
            log.info('刷新数据------')
            time.sleep(5)

    def is_have_records(self):
        time.sleep(3)
        try:
            table = self.driver.find_element_by_class_name('data-grid-body-content')
            table.find_elements_by_tag_name('tr')
        except:
            log.info('--------Dispatch Requests列表中无记录！--------')
            return False
        else:
            records = table.find_elements_by_tag_name('tr')
            rec = len(records)
            log.info('找到 %s 条记录' % rec)
            return True

    def email_dispatch(self):
        res = self.is_have_records()
        if res:
            try:
                self.dispatch.click(self.dispatch.asset1_loc)
                time.sleep(1)
                self.dispatch.click(self.dispatch.emailBtn_loc)
                time.sleep(1)
            except:
                log.info('--------打开Dispatch Assignment对话框失败！--------')
                return False
            else:
                try:
                    self.dispatch.click(self.dispatch.selectAssetList_loc)
                    time.sleep(1)
                    assets = ('xpath', '//*[@id="dialog_assignasset"]/div/div[2]/ul/li[%d]' % random.randint(1, 10))
                    self.dispatch.click(assets)
                    time.sleep(1)
                    self.dispatch.click(self.dispatch.continueBtn_loc)
                    time.sleep(1)
                    self.dispatch.send_keys(self.dispatch.emailAddress_loc, 'autoTest@test.com')
                except:
                    log.info('--------打开Send Dispatch Request页面失败！--------')
                    return False
                else:
                    try:
                        self.dispatch.click(self.dispatch.sendEmailOKBtn_loc)
                        try:  # 页面代码元素位置调整
                            self.dispatch.click(self.dispatch.sendEmailDialogOKBtn_loc)
                        except:
                            self.driver.switch_to.default_content()
                            self.dispatch.click(self.dispatch.sendEmailDialogOKBtn_loc)
                            self.dispatch.switch_to_iframe(self.dispatch.iframe_loc)
                    except:
                        log.info('--------Send Dispatch Request失败！--------')
                        return False
                    else:
                        log.info('--------Send Dispatch Request成功！--------')
                        return True
        else:
            return res

    def print_dispatch(self):
        res = self.is_have_records()
        if res:
            try:
                time.sleep(1)
                self.dispatch.click(self.dispatch.asset1_loc)
                time.sleep(1)
                self.dispatch.click(self.dispatch.printBtn_loc)
                time.sleep(1)
            except:
                log.info('--------打开Dispatch Assignment对话框失败！--------')
                return False
            else:
                try:
                    self.dispatch.click(self.dispatch.selectAssetList_loc)
                    time.sleep(1)
                    selasset = ('xpath', '//*[@id="dialog_assignasset"]/div/div[2]/ul/li[%d]' % random.randint(1, 10))
                    self.dispatch.click(selasset)
                    self.dispatch.click(self.dispatch.continueBtn_loc)
                except:
                    log.info('--------打开Dispatch打印页面失败！--------')
                    return False
                else:
                    try:
                        self.driver.switch_to.window(self.driver.window_handles[1])
                        self.dispatch.find_element(self.dispatch.printWindow_loc)
                        self.driver.close()
                    except:
                        log.info('--------打印Dispatchs失败！--------')
                        self.driver.switch_to.window(self.driver.window_handles[0])
                        time.sleep(1)
                        self.dispatch.switch_to_iframe(self.dispatch.iframe_loc)
                        time.sleep(1)
                        return False
                    else:
                        log.info('--------打印Dispatchs成功！--------')
                        self.driver.switch_to.window(self.driver.window_handles[0])
                        time.sleep(1)
                        self.dispatch.switch_to_iframe(self.dispatch.iframe_loc)
                        time.sleep(1)
                        return True
        else:
            return res

    def delete_dispatch(self):
        res = self.is_have_records()
        if res:
            try:
                self.dispatch.click(self.dispatch.deleteBtn_loc)
            except:
                log.info('--------打开Delete Dispatch对话框失败！--------')
                return False
            else:
                try:
                    try:  # element location changed
                        self.dispatch.click(self.dispatch.deleteDialogYesBtn_loc)
                    except:
                        self.driver.switch_to.default_content()
                        self.dispatch.click(self.dispatch.deleteDialogYesBtn_loc)
                        self.dispatch.switch_to_iframe(self.dispatch.iframe_loc)
                except:
                    log.info('--------删除Dispatch失败！--------')
                    return False
                else:
                    log.info('--------删除Dispatch成功！--------')
                    return True
        else:
            return res

    def view_dispatch_history(self):
        res = self.is_have_records()
        if res:
            try:
                self.dispatch.click(self.dispatch.viewChangeHistoryBtn_loc)
            except:
                log.info('--------打开View Change History页面失败！--------')
                return False
            else:
                time.sleep(1)
                try:
                    self.driver.switch_to.window(self.driver.window_handles[1])
                    # 增加延时  -- 曾良均 2021.10.22
                    time.sleep(2)
                    self.dispatch.find_element(self.dispatch.viewChangeHistoryTitle_loc)
                except:
                    log.info('--------查看Dispatch Change History失败！--------')
                    return False
                else:
                    log.info('--------查看Dispatch Change History成功！--------')
                    return True
        else:
            return res

    def test01_send_dispatch(self):
        '''发送Dispatch Email'''
        self.refresh()
        res = self.email_dispatch()
        self.assertTrue(res)

    def test02_print_dispatch(self):
        '''打开dispatch'''
        self.refresh()
        res = self.print_dispatch()
        self.assertTrue(res)

    def test03_delete_dispatch(self):
        '''删除Dispatch'''
        self.refresh()
        res = self.delete_dispatch()
        self.assertTrue(res)

    def test04_view_dispatch_history(self):
        '''查看Dispatch History'''
        self.refresh()
        res = self.view_dispatch_history()
        self.assertTrue(res)


if __name__ == '__main__':
    unittest.main()






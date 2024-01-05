# -*-coding: utf-8 -*-
"""
--------------------------------------------------------------------------
   File Name：    MaintenanceSchedulesTest.py
   Description :   测试schedule的Add、Delete、Manage schedule、Manage assets
   Author :        姜丽丽
--------------------------------------------------------------------------
"""
from Page.loginpage import LoginPage
from Page.AssetHealth.MaintenanceSchedulesPage import MaintenanceSchedulesPage
from logger import Log
from operater import browser
import unittest
import time
import os
from skiptest import skip_dependon

log = Log()
path = '.\\report'

#判断报告目录是否存在
if not os.path.exists(path):
    os.mkdir(path)

current_time = time.strftime('%H%M%S')
planName = 'AutoTest'+current_time


class MaintenanceSchedulesTest(unittest.TestCase):
    login = None
    driver = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = browser("chromeH")
        cls.login = LoginPage(cls.driver)
        cls.login.login('atpm@iicon006.com', 'Win.12345')
        cls.driver.implicitly_wait(60)
        log.info('--------开始测试Maintenance Schedules--------')
        time.sleep(5)
        log.info('--------成功登录--------')
        cls.to_frame(cls)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def to_frame(self):
        self.plan = MaintenanceSchedulesPage(self.driver)
        try:
            # self.plan.click(self.plan.assetHealth_loc)
            time.sleep(10)
            # self.plan.click(self.plan.maintenanceSchedules_loc)
            self.plan.switch_to_iframe(self.plan.iframe_loc)
        except:
            log.info('--------打开Maintenance Schedules列表失败！--------')
        else:
            log.info('--------打开Maintenance Schedules列表成功！--------')

    def input_and_save(self):
        try:
            while not self.plan.is_clickable(self.plan.addBtn_loc):
                log.info('元素还不能点击，等待3秒')
                time.sleep(3)
            self.plan.click(self.plan.addBtn_loc)
        except:
            log.info('--------打开Manage Maintenance Schedule页面失败！--------')
        else:
            log.info('--------打开Manage Maintenance Schedule页面成功！开始输入信息--------')
            self.plan.send_keys(self.plan.planName_loc, planName)
            self.plan.select_by_index(self.plan.planType_loc, 0)
            self.plan.send_keys(self.plan.description_loc, 'AutoTest')
            try:
                self.plan.click(self.plan.saveAndExitBtn_loc)
                time.sleep(1)
            except:
                log.info('-----保存Maintenance Schedule失败！！-----')
            else:
                time.sleep(2)
                log.info('-----完成保存操作，是否添加成功待验证！-----')

    def search_schedule(self, plan):
        time.sleep(1)
        self.plan.select_by_text(self.plan.planSelect_loc, plan)
        time.sleep(3)

    def search_and_verify(self, plan):
        try:
            try:
                self.driver.implicitly_wait(30)
                ref = ('xpath', '//*[@id="refresh_button"]')
                self.plan.click(ref)
            except:
                log.info('列表不能刷新，再等待3秒重试')
                time.sleep(3)
            else:
                time.sleep(3)
            self.search_schedule(plan)
        except:
            log.info('-----添加Maintenance Schedule失败！-----')
            return False
        else:
            log.info('-----添加Maintenance Schedule成功！-----')
            return True

    def add_interval(self, plan):
        try:
            self.search_schedule(plan)
        except:
            log.info('-----搜索目标Schedule失败！-----')
            return False
        else:
            time.sleep(3)
            try:
                self.plan.click(self.plan.manageSchedule_loc)
                time.sleep(1)
            except:
                log.info('-----打开Manage Maintenance Schedule页面失败！-----')
                return False
            else:
                log.info('-----打开Manage Maintenance Schedule页面成功！-----')
                try:
                    time.sleep(1)
                    self.plan.click(self.plan.addIntervalBtn_loc)
                except:
                    log.info('-----打开Add Interval页面失败！-----')
                    return False
                else:
                    log.info('-----打开Add Interval页面成功！-----')
                    self.plan.inputTo(self.plan.serviceName_loc,'AutoTest interval')
                    self.plan.inputTo(self.plan.interval_loc, '1000')
                    self.plan.inputTo(self.plan.notificationPeriod_loc, '100')
                    self.plan.click(self.plan.recurring_loc)
                    self.plan.inputTo(self.plan.serviceDescription_loc, 'AutoTest')
                    self.plan.inputTo(self.plan.expectedCost_loc, '66.6')
                    self.plan.inputTo(self.plan.priority_loc, '1')
                    try:
                        self.plan.click(self.plan.addIntervalOKBtn_loc)
                        time.sleep(1)
                        self.plan.click(self.plan.saveAndExitBtn_loc)
                    except:
                        log.info('-----添加interval失败！-----')
                        return False
                    else:
                        log.info('-----添加interval成功！-----')
                        return True

    def disable_schedules(self, plan):
        try:
            self.search_schedule(plan)
        except:
            log.info('-----搜索目标Schedule失败！-----')
            return False
        else:
            time.sleep(3)
            try:
                self.plan.click(self.plan.manageSchedule_loc)
                time.sleep(1)
            except:
                log.info('-----打开Manage Maintenance Schedule页面失败！-----')
                return False
            else:
                log.info('-----打开Manage Maintenance Schedule页面成功！-----')
                try:
                    time.sleep(1)
                    if self.plan.is_selected(self.plan.planEnable_loc):
                        self.plan.click(self.plan.planEnable_loc)  # 点击一次，取消勾选
                        time.sleep(1)
                except Exception:
                    log.info('------取消启用Schedule失败!')
                    return False
                else:
                    try:
                        time.sleep(1)
                        self.plan.click(self.plan.saveAndExitBtn_loc)
                    except:
                        log.info('-----设置Schedule失败！-----')
                        return False
                    else:
                        log.info('-----设置Schedule成功！ 待验证设置结果！！ ')
                        try:
                            self.search_schedule(plan)
                        except Exception:
                            log.info('-----搜索目标Schedule失败！-----')
                            return False
                        else:
                            try:
                                txt = self.plan.get_text(self.plan.sc_disable_loc)
                                if txt == "Disabled":
                                    return True
                            except Exception:
                                log.info('------禁用Schedule失败------')
                                return False

    def manage_assets(self, plan):
        try:
            time.sleep(3)
            self.search_schedule(plan)
        except:
            log.info('-----搜索目标Schedule失败！-----')
            return False
        else:
            try:
                time.sleep(2)
                self.plan.click(self.plan.manageAssetsBtn_loc)
            except:
                log.info('-----打开Manage Absolute Distance Maintenance Assets页面失败！-----')
                return False
            else:
                log.info('-----打开Manage Absolute Distance Maintenance Assets页面成功！-----')
                try:
                    self.plan.click(self.plan.addAssetsBtn_loc)
                    time.sleep(1)
                except:
                    log.info('-----打开Select Assets页面失败！-----')
                    return False
                else:
                    log.info('-----打开Select Assets页面成功！-----')
                    try:
                        self.plan.click(self.plan.firstAsset_loc)
                        self.plan.click(self.plan.selectAssetOKBtn_loc)
                        self.plan.click(self.plan.setAssetOKBtn_loc_loc)
                        self.plan.click(self.plan.saveAssetBtn_loc)
                        time.sleep(2)
                        self.driver.switch_to.default_content()
                        self.plan.click(self.plan.saveAssetDialogOKBtn_loc)
                        time.sleep(2)
                    except:
                        log.info('-----给计划添加Assets失败！-----')
                        return False
                    else:
                        self.plan.switch_to_iframe(self.plan.iframe_loc)
                        time.sleep(1)
                        self.plan.click(self.plan.backBtn_loc)
                        log.info('-----给计划添加Assets成功！-----')
                        return True

    def edit_interval(self, plan):
        try:
            self.search_schedule(plan)
        except:
            log.info('-----搜索目标Schedule失败！-----')
            return False
        else:
            try:
                self.plan.click(self.plan.expandIntervalsBtn_loc)
                time.sleep(1)
                self.plan.send_keys(self.plan.listServiceName_loc,'AutoTest interval 001')
                self.plan.click(self.plan.listSaveServiceBtn_loc)
                time.sleep(1)
            except:
                log.info('-----编辑interval失败！-----')
                return False
            else:
                log.info('-----编辑interval成功！-----')
                return True

    def delete_schedule(self, plan):
        try:
            self.search_schedule(plan)
        except:
            log.info('-----搜索目标Schedule失败！-----')
            return False
        else:
            try:
                time.sleep(2)
                self.plan.click(self.plan.deleteScheduleBtn_loc)
                time.sleep(2)
                try:
                    self.plan.click(self.plan.deleteScheduleYesBtn_loc)
                except:
                    self.driver.switch_to.default_content()
                    self.plan.click(self.plan.deleteScheduleYesBtn_loc)
                    self.plan.switch_to_iframe(self.plan.iframe_loc)
            except:
                log.info('-----删除schedule失败！-----')
                return False
            else:
                time.sleep(1)
                self.search_schedule(plan)
                time.sleep(2)
                txt = self.plan.get_text(self.plan.deleteResult_loc)
                if txt == 'No results.':
                    log.info('-----删除schedule成功！-----')
                    return True
                else:
                    log.info('-----删除schedule失败！-----')
                    return False

    def test01_add_plan(self):
        '''添加PM计划'''
        self.input_and_save()
        res = self.search_and_verify(planName)
        self.assertTrue(res)

    @skip_dependon(depend='test01_add_plan')
    def test02_add_interval(self):
        '''为PM添加Interval'''
        res = self.add_interval(planName)
        self.assertTrue(res)

    @skip_dependon(depend='test01_add_plan')
    def test03_manage_assets(self):
        '''为PM添加机器'''
        res = self.manage_assets(planName)
        self.assertTrue(res)

    @skip_dependon(depend='test02_add_interval')
    def test04_edit_interval(self):
        '''编辑PM计划'''
        res = self.edit_interval(planName)
        self.assertTrue(res)

    @skip_dependon(depend='test01_add_plan')
    def test05_disable_schedule(self):
        """测试禁用Schedule"""
        res = self.disable_schedules(planName)
        self.assertTrue(res)

    @skip_dependon(depend='test01_add_plan')
    def test06_delete_schedule(self):
        '''删除PM计划'''
        res = self.delete_schedule(planName)
        self.assertTrue(res)


if __name__ == '__main__':
    unittest.main()






# -*- coding: utf-8 -*-
"""
------------------------------------------------------------------------------
   File Name：     JobsiteRequirementsTest.py
   Description :   测试Jobsite Requirements的添加、删除、查看修改记录、查看删除记录
   Author :        姜丽丽
-------------------------------------------------------------------------------
"""
from Common.operater import browser
from Page.AssetSchdulingAndDispaching.JobsiteRequirementsPage import JobsiteRequirementsPage
from Page.loginpage import LoginPage
from Common.logger import Log
import os
import unittest
import time

log = Log()
path = '.\\report'
if not os.path.exists(path):
    os.mkdir(path)

currentDate = time.strftime('%Y%m%d',time.localtime(time.time()))
currentTime = time.strftime('%Y%m%d-%H%M%S',time.localtime(time.time()))
pointOfContact = 'test'+currentTime

class JobsiteRequirementsTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        log.info('----测试用例开始----')
        cls.driver = browser()
        cls.log = LoginPage(cls.driver)
        cls.log.login('atrequirement@iicon006.com','Win.12345')
        cls.to_frame(cls)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def to_frame(self):
        self.requirement = JobsiteRequirementsPage(self.driver)
        self.driver.implicitly_wait(60)
        time.sleep(5)
        # try:
        #     self.requirement.click(self.requirement.dispatchmenu_loc)
        #     time.sleep(3)
        #     self.requirement.click(self.requirement.requirementsManage_loc)
        #     time.sleep(2)
        # except:
        #     log.info('--------打开Jobsite Requirements列表失败！--------')
        # else:
        #     log.info('--------打开Jobsite Requirements列表成功！--------')
        self.requirement.switch_to_iframe(self.requirement.iframe_loc)
        time.sleep(5)

    def add_requirement(self):
        try:
            self.requirement.click(self.requirement.addBtn_loc)
            time.sleep(2)
            self.requirement.switch_to_iframe(self.requirement.requirementIframe_loc)
            time.sleep(1)
        except:
            log.info('----打开requirement添加页面失败!----')
        else:
            log.info('----打开requirement添加页面成功!----')
            self.requirement.select_by_index(self.requirement.jobsiteSelect_loc,1)
            time.sleep(1)
            self.requirement.send_keys(self.requirement.beginDate_loc, currentDate)
            self.requirement.send_keys(self.requirement.endDate_loc, currentDate)
            self.requirement.click(self.requirement.endDate_loc)
            time.sleep(1)
            try:
                self.requirement.click(self.requirement.assetTypeList_loc)
                time.sleep(1)
                self.requirement.click(self.requirement.assetType_loc)
                time.sleep(1)
            except:
                log.info('------未选择Asset Type------')
            else:
                self.requirement.send_keys(self.requirement.pointOfContact_loc, pointOfContact)
                self.requirement.click(self.requirement.applyBtn_loc)
                self.requirement.click(self.requirement.manageAssetBtn_loc)
                self.requirement.click(self.requirement.firstAsset_loc)
                self.requirement.click(self.requirement.selectAssetOKBtn_loc)
                try:
                    self.requirement.click(self.requirement.saveBtn_loc)
                    self.requirement.click(self.requirement.continueBtn_loc)
                except:
                    log.info('----保存requirement失败!----')
                else:
                    log.info('----完成保存操作，是否添加成功待验证！----')
                    self.driver.switch_to.default_content()
                    self.requirement.switch_to_iframe(self.requirement.iframe_loc)
                    time.sleep(1)

    def verify_add(self, contact):
        #  # 根据’pointOfContact‘的内容查找table中是否有刚才添加的记录
        # self.requirement.clear(self.requirement.latestDate_loc)
        # time.sleep(1)
        # self.requirement.click(self.requirement.latestDate_loc)
        time.sleep(1)
        self.requirement.click(self.requirement.unscheduledBox_loc)
        time.sleep(3)
        try:
            table = self.driver.find_element_by_class_name('data-grid-body-content')
            rows = table.find_elements_by_tag_name('tr')
        except:
            log.info('----列表中没有Jobsite Requirements记录！----')
            return False
        else:
            rowNum = len(rows)
            for i in range(0, rowNum):
                row = rows[i]
                cols = row.find_elements_by_tag_name('td')
                colNum = len(cols)
                for j in range(0, colNum):
                    txt = cols[j].text
                    if txt == contact:
                        return True
            return False

    def delete__requirment(self, contact):
        # 根据’pointOfContact‘的内容查找刚才添加的记录，然后删除
        self.driver.switch_to.window(self.driver.window_handles[0])
        self.requirement.switch_to_iframe(self.requirement.iframe_loc)
        time.sleep(2)
        try:
            table = self.driver.find_element_by_class_name('data-grid-body-content')
            rows = table.find_elements_by_tag_name('tr')
        except:
            log.info('-----列表中没有Requirements！----')
            return False
        else:
            rowNum = len(rows)
            for i in range(0, rowNum):
                row = rows[i]
                cols = row.find_elements_by_tag_name('td')
                colNum = len(cols)
                for j in range(0, colNum):
                    txt = cols[j].text
                    if txt == contact:
                        try:
                            self.requirement.js_execute("window.scrollTo(0,300)")
                            time.sleep(1)
                            cols[12].click()
                        except:
                            log.info('-----删除Requirement失败！----')
                            return False
                        else:
                            time.sleep(1)
                            self.requirement.click(self.requirement.deleteYesBtn_loc)
                            log.info('-----删除Requirement成功！----')
                            return True

    def view_deleted_records(self):
        try:
            time.sleep(1)
            self.requirement.click(self.requirement.viewDeletedRecordsBtn_loc)
            time.sleep(2)
        except:
            log.info('-----点击View Deleted Records按钮失败！----')
        else:
            try:
                self.driver.switch_to.window(self.driver.window_handles[1])
                time.sleep(2)
                self.requirement.find_element(self.requirement.deletedJobsiteRequirements_loc)
            except:
                log.info('-----打开Deleted Jobsite Requirements页面失败！----')
            else:
                log.info('-----打开Deleted Jobsite Requirements页面成功！----')


    def verify_delete_records(self, contact):
        # 根据’pointOfContact‘的内容查找table中是否有刚才删除的记录
        try:
            table = self.driver.find_element_by_class_name('data-grid-body-content')
            rows = table.find_elements_by_tag_name('tr')
        except:
            log.info('----列表中没有Requirements记录！----')
            return False
        else:
            rowNum = len(rows)
            for i in range(0, rowNum):
                row = rows[i]
                cols = row.find_elements_by_tag_name('td')
                colNum = len(cols)
                for j in range(0, colNum):
                    txt = cols[j].text
                    if txt == contact:
                        return True
            return False

    def view_change_history(self, contact):
        # 根据’pointOfContact‘的内容查找刚才添加的记录，然后删除
        try:
            table = self.driver.find_element_by_class_name('data-grid-body-content')
            rows = table.find_elements_by_tag_name('tr')
        except:
            log.info('-----列表中没有Requirements记录！----')
            return False
        else:
            rowNum = len(rows)
            for i in range(0, rowNum):
                row = rows[i]
                cols = row.find_elements_by_tag_name('td')
                colNum = len(cols)
                for j in range(0, colNum):
                    txt = cols[j].text
                    if txt == contact:
                        try:
                            self.requirement.js_execute("window.scrollTo(0,300)")
                            time.sleep(1)
                            cols[13].click()
                        except:
                            log.info('-----打开Requirement Change History页面失败！----')
                            return False
                        else:
                            log.info('-----打开Requirement Change History页面成功！----')
                            self.driver.switch_to.window(self.driver.window_handles[1])
                            self.driver.close()
                            return True

    def test01_add_requirment(self):
        '''添加Requirment'''
        self.add_requirement()
        res = self.verify_add(pointOfContact)
        if res == True:
            log.info('-----添加Requirement成功！----')
        else:
            log.info('-----添加Requirement失败！----')
        self.assertTrue(res)

    def test02_view_change_history(self):
        '''查看Change history'''
        res = self.view_change_history(pointOfContact)
        self.assertTrue(res)

    def test03_delete_requirment(self):
        '''删除Requirment'''
        res = self.delete__requirment(pointOfContact)
        self.assertTrue(res)

    def test04_view_deleted_records(self):
        '''查看删除记录'''
        time.sleep(3)
        self.view_deleted_records()
        res = self.verify_delete_records(pointOfContact)
        if res == True:
            log.info('-----查看Deleted Jobsite Requirements成功，页面记录正确！----')
        else:
            log.info('-----查看Deleted Jobsite Requirements失败！----')
        self.assertTrue(res)

if __name__ == "__main__":
    unittest.main()



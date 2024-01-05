# -*-coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     AssetGroypsTest.py
   Description :   测试机器组管理的添加、编辑、删除
   Author :        姜丽丽
-------------------------------------------------
"""
from Page.ManageAssets.AssetGroupsPage import AseetGroupsPage
from operater import browser
from Page.loginpage import LoginPage
from logger import Log
import unittest
import os
import time
from skiptest import skip_dependon

log = Log()
# 判断测试报告目录是否存在
path = '.\\report'
if not os.path.exists(path):
    os.mkdir(path)

current_time = time.strftime('%H%M%S', time.localtime(time.time()))
groupName = 'AutoTest001'+current_time
editGroupName = groupName+'Edit'


class AssetGroypsTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        #登录ironintel站点
        cls.driver = browser()
        cls.login = LoginPage(cls.driver)
        cls.login.login('atassetgroup@iicon006.com','Win.12345')
        cls.driver.implicitly_wait(60)
        log.info('------开始测试机器组管理------')
        cls.to_iframe(cls)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def to_iframe(self):
        self.assetGroup = AseetGroupsPage(self.driver)
        self.driver.implicitly_wait(40)
        time.sleep(3)
        self.assetGroup.switch_to_iframe(self.assetGroup.iframe_loc)
        time.sleep(1)

    def input_group_information(self):
        try:
            self.assetGroup.click(self.assetGroup.addBtn_loc)
            self.assetGroup.switch_to_iframe(self.assetGroup.iframeMachineGroup_loc)
        except:
            log.info('--------打开机器组添加页面失败！！--------')
        else:
            log.info('--------打开机器组添加页面，开始输入信息--------')
            self.assetGroup.inputTo(self.assetGroup.groupName_loc, groupName)
            self.assetGroup.inputTo(self.assetGroup.groupCode_loc, 'AutoTest001')
            self.assetGroup.inputTo(self.assetGroup.description_loc, 'AutoTest')
            self.assetGroup.click(self.assetGroup.addAssetsBtn_loc)
            self.assetGroup.click(self.assetGroup.firstAsset_loc)
            self.assetGroup.click(self.assetGroup.assetOkBtn_loc)

    def save_group(self):
        try:
            self.assetGroup.click(self.assetGroup.saveAndExitBtn_loc)
        except:
            log.info('-----保存机器组失败！！-----')
        else:
            log.info('-----完成保存操作，是否添加成功待验证！-----')
            self.driver.switch_to.default_content()
            self.assetGroup.switch_to_iframe(self.assetGroup.iframe_loc)

    def edit_group(self):
        try:
            time.sleep(1)
            self.assetGroup.search(groupName)
            self.assetGroup.click(self.assetGroup.editBtn_loc)
            time.sleep(1)
            self.assetGroup.switch_to_iframe(self.assetGroup.iframeMachineGroup_loc)
        except:
            log.info('--------打开机器组编辑页面失败！！--------')
        else:
            time.sleep(1)
            log.info('--------打开机器组编辑页面，开始编辑信息--------')
            self.assetGroup.inputTo(self.assetGroup.groupName_loc, editGroupName)
            self.assetGroup.inputTo(self.assetGroup.groupCode_loc, 'AutoTestEdit001')
            self.assetGroup.inputTo(self.assetGroup.description_loc, 'AutoTestEdit')
            time.sleep(1)

    def search_and_delete(self, assetGroup):
        '''搜索并删除已存在的记录'''
        self.assetGroup.search(assetGroup)
        try:
            table = self.driver.find_element_by_class_name('data-grid-body-content')
            trs = table.find_elements_by_tag_name('tr')
        except:
            pass
        else:
            trNum = len(trs)
            self.assetGroup.js_execute("window.scrollTo(0,300)")
            for i in range(trNum):
                self.assetGroup.click(self.assetGroup.deleteBtn_loc)
                try:
                    self.assetGroup.click(self.assetGroup.deleteDialogOkBtn_loc)
                except:
                    self.driver.switch_to.default_content()
                    self.assetGroup.click(self.assetGroup.deleteDialogOkBtn_loc)
                    self.assetGroup.switch_to_iframe(self.assetGroup.iframe_loc)
            log.info('----删除已存在的记录!----')

    def search_and_verify(self, groupName):
        # 搜索并遍历table查找刚才创建的机器组是否存在
        time.sleep(2)
        self.assetGroup.search(groupName)
        try:
            table = self.driver.find_element_by_class_name('data-grid-body-content')
            time.sleep(2)
            rows = table.find_elements_by_tag_name('tr')
        except:
            return False
        else:
            rowNum = len(rows)
            for i in range(0, rowNum):
                row = rows[i]
                cols = row.find_elements_by_tag_name('td')
                colNum = len(cols)
                for j in range(0, colNum):
                    txt = cols[j].text
                    if txt == groupName:
                        return True
                    else:
                        return False

    def test01_add_group(self):
        self.input_group_information()
        self.save_group()
        res = self.search_and_verify(groupName)
        if res:
            log.info('-----添加机器组成功！----')
        else:
            log.info('-----添加机器组失败！----')
        self.assertTrue(res)

    def test02_edit_group(self):
        self.edit_group()
        self.save_group()
        time.sleep(1)
        res = self.search_and_verify(editGroupName)
        if res:
            log.info('-----编辑机器组成功！----')
        else:
            log.info('-----编辑机器组失败！----')
        self.assertTrue(res)

    @skip_dependon(depend='test02_edit_group')
    def test03_delete_group(self):
        self.search_and_delete(editGroupName)
        res = self.search_and_verify(editGroupName)
        if not res:
            log.info('-----删除机器组成功！----')
        else:
            log.info('-----删除机器组失败！----')
        self.assertFalse(res)


if __name__ == '__main__':
    unittest.main()






# coding:utf-8

from Page.SystemSettings.ManageDepartment import DepartmentPage
from operater import browser
from Page.loginpage import LoginPage
from logger import Log
import unittest
import os
import time
from skiptest import skip_dependon

log = Log()
path = '.\\report'

if not os.path.exists(path):
    os.mkdir(path)

current_time = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))
dep_name = 'department'+current_time
dep_code = 'code'+current_time
edit_name = 'editdepartment' + current_time
childdep_name = 'childdepartment' + current_time


class DepartmentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = browser("chromeH")
        cls.login = LoginPage(cls.driver)
        cls.login.login("atdepartment@iicon001.com", "Win.12345")
        cls.driver.implicitly_wait(60)
        time.sleep(3)
        cls.switch_to_iframe(cls)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def switch_to_iframe(self):
        self.department = DepartmentPage(self.driver)
        self.driver.implicitly_wait(60)
        time.sleep(5)
        try:
            self.department.click(self.department.settingsbutton_loc)
            self.department.click(self.department.syssettings_loc)
            self.driver.implicitly_wait(60)
            time.sleep(5)
            arr_status = self.driver.find_element_by_xpath('//*[@id="nav_arrow"]/div').get_attribute('class')
            if arr_status == 'icn collapse':
                self.department.click(self.department.exButton_loc)
                time.sleep(1)
            self.department.click(self.department.department_loc)
            self.department.click(self.department.exButton_loc)
            time.sleep(1)
        except:
            log.info("-----打开Manage Departments页面失败-----")
        else:
            log.info("-----打开Manage Departments页面成功-----")
            self.department.switch_to_iframe(self.department.iframe_loc)
            time.sleep(3)

    def add_department(self):
        try:
            self.department.click(self.department.addbutton_loc)
            time.sleep(1)
            self.department.send_keys(self.department.departmentname_loc, dep_name)
            self.department.send_keys(self.department.code_loc, dep_code)
            self.department.send_keys(self.department.notes_loc, 'Notes of ' + dep_name)
            self.department.click(self.department.okbutton_loc)
        except:
            log.info("-----新增Department失败-----")
        else:
            time.sleep(2)
            log.info("-----新增Department完成-----")

    def add_child_department(self):
        try:
            self.department.click(self.department.addchild_loc)
        except:
            log.info("-----当前不存在Department，无法添加子department-----")
        else:
            time.sleep(1)
            try:
                self.department.send_keys(self.department.departmentname_loc, childdep_name)
                self.department.send_keys(self.department.code_loc, 'childdep_code')
                self.department.click(self.department.okbutton_loc)
            except:
                log.info("-----添加子Deprtment失败-----")
            else:
                time.sleep(3)
                log.info("-----添加子Department完成，结果待验证-----")

    def edit_department(self):
        try:
            self.department.click(self.department.editbutton_loc)
            time.sleep(1)
            self.department.clear(self.department.departmentname_loc)
            self.department.send_keys(self.department.departmentname_loc, edit_name)
            self.department.click(self.department.editokbutton_loc)
        except:
            log.info("-----编辑Department失败-----")
        else:
            time.sleep(3)
            log.info("-----编辑Department完成，结果待验证-----")

    def search_departments(self, comparename):
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="recordcontent"]/div[2]/span[2]').click()
        time.sleep(2)
        table = self.driver.find_element_by_xpath("//*[@id='departmentlist']/div/div/div/table")
        rows = table.find_elements_by_tag_name("tr")
        rownames = []
        for row in rows:
            col = row.find_element_by_xpath("./td[1]/span")
            rowtext = col.text
            rownames.append(rowtext)
        if comparename in rownames:
            return True
        else:
            return False

    def delete_department(self):
        try:
            self.department.click(self.department.delbutton_loc)
            time.sleep(1)
            try:
                self.department.click(self.department.delmsgok_loc)
            except:
                self.driver.switch_to.default_content()
                self.department.click(self.department.delmsgok_loc)
                self.department.switch_to_iframe(self.department.iframe_loc)
        except:
            log.info("-----删除Department失败-----")
        else:
            log.info("-----删除Department完成，结果待验证-----")
        time.sleep(2)

    def test01_verify_addsucess(self):
        self.add_department()
        time.sleep(2)
        self.assertTrue(self.search_departments(dep_name))

    @skip_dependon(depend='test01_verify_addsucess')
    def test02_veriry_addchildsucess(self):
        self.add_child_department()
        time.sleep(2)
        self.assertTrue(self.search_departments(childdep_name))

    @skip_dependon(depend='test01_verify_addsucess')
    def test03_verify_editsucess(self):
        self.edit_department()
        time.sleep(2)
        self.assertTrue(self.search_departments(edit_name))

    @skip_dependon(depend='test03_verify_editsucess')
    def test04_verify_delsucess(self):
        self.delete_department()
        time.sleep(2)
        self.assertFalse(self.search_departments(edit_name))


if __name__ == "__main__":
    unittest.main()




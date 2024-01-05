# conding: utf-8

from Page.loginpage import LoginPage
from Page.TeamIntelligence.DraftPage import DraftPage
import os
import time
from operater import browser
import unittest
from logger import Log
from skiptest import skip_dependon

current_time = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
templateName = 'AutoTest'+current_time
editTemplateName = templateName+'Edit'
copyTemplateName = editTemplateName+'Copy'

log = Log()

path = '.\\report'
if not os.path.exists(path):
    os.mkdir(path)


class DraftTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = browser()
        cls.login = LoginPage(cls.driver)
        cls.login.login('autotester@foresight.com', '1')
        log.info('--------测试Team Intelligence--------')
        cls.driver.implicitly_wait(60)
        cls.open_customer(cls)
        cls.open_drafttemplate(cls)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def open_customer(self):
        self.draft = DraftPage(self.driver)
        self.draft.click(self.draft.customerlink_loc)
        self.driver.implicitly_wait(60)
        time.sleep(3)
        self.draft.send_keys(self.draft.searchinput_loc, '004')
        self.draft.click(self.draft.searchbutton_loc)
        time.sleep(2)
        self.draft.click(self.draft.customeropen_loc)
        all_h = self.driver.window_handles
        self.driver.switch_to.window(all_h[1])

    def open_drafttemplate(self):
        try:
            self.draft.click(self.draft.fullmenu_loc)
            self.draft.click(self.draft.teamintel_loc)
            self.draft.click(self.draft.exButton_loc)
            time.sleep(3)
            self.draft.click(self.draft.draftmenu_loc)
        except:
            log.info("—————打开Draft Templates列表失败—————")
        else:
            self.draft.click(self.draft.exButton_loc)
            time.sleep(3)
            log.info("—————打开Draft Templates列表成功—————")

    def add_drafttemplate(self):
        currenttime = time.strftime('%Y%m%d%H%M%S')
        try:
            self.draft.click(self.draft.addbutton_loc)
        except:
            log.info('-----打开新增Draft Template窗口失败-----')
        else:
            log.info("-----打开Drart Template窗口成功-----")
            time.sleep(2)
            self.draft.send_keys(self.draft.nameinput_loc, templateName)
            self.draft.click(self.draft.location_loc)
            self.draft.click(self.draft.signature_loc)
            self.draft.send_keys(self.draft.notes_loc, templateName + " 's note.")
            try:
                self.draft.click(self.draft.pageadd_loc)
                self.draft.js_execute("document.getElementById('right_popup').scrollTop=1000")
                self.draft.send_keys(self.draft.pagename_loc, 'Page 1')
                self.draft.send_keys(self.draft.pagetext_loc, 'Page one')
            except:
                log.info('-----添加Page失败-----')
            else:
                log.info('-----添加Page成功-----')
                try:
                    self.draft.click(self.draft.sectionadd_loc)
                    self.draft.js_execute("document.getElementById('right_popup').scrollTop=1000")
                    self.draft.send_keys(self.draft.sectionname_loc, 'Section 1')
                    self.draft.send_keys(self.draft.sectiontext_loc, 'Section one')
                except:
                    log.info('-----添加Section失败-----')
                else:
                    log.info('-----添加Section成功-----')
                    try:
                        self.draft.js_execute("document.getElementById('right_popup').scrollLeft=1000")
                        for i in range(0,3):
                            self.draft.click(self.draft.questionadd_loc)
                        self.draft.js_execute("document.getElementById('right_popup').scrollLeft=0")
                        time.sleep(1)
                        self.draft.js_execute("document.getElementById('right_popup').scrollTop=1000")

                        self.draft.send_keys(self.draft.question1name_loc, 'Question 1')
                        self.draft.send_keys(self.draft.question1text_loc, 'Question one')
                        self.draft.select_by_index(self.draft.question1type_loc, 1)

                        self.draft.send_keys(self.draft.question2name_loc, 'Question 2')
                        self.draft.send_keys(self.draft.question2text_loc, 'Question two')
                        self.draft.select_by_index(self.draft.question2type_loc, 5)

                        self.draft.send_keys(self.draft.question3name_loc, 'Question 3')
                        self.draft.send_keys(self.draft.question3text_loc, 'Question three')
                        self.draft.select_by_index(self.draft.question3type_loc, 12)

                    except:
                        log.info('-----添加Question失败-----')
                    else:
                        log.info('-----添加Question成功-----')
                        self.draft.js_execute("document.getElementById('right_popup').scrollTop=0")
                        time.sleep(2)
                        self.draft.click(self.draft.saveexit_loc)
                        time.sleep(3)

    def search_template(self, templateName):
        # 查询目标template是否存在
        time.sleep(1)
        self.draft.search(templateName)
        time.sleep(1)
        try:
            self.draft.get_text(self.draft.tempname1_loc)
        except:
            return False
        else:
            return True

    def verify_template(self, templateName):
        # 查询刚才创建的template是否存在
        self.draft.search(templateName)
        time.sleep(3)
        try:
            template = self.draft.get_text(self.draft.tempname1_loc)
        except:
            return False
        else:
            if template == templateName:
                return True
            else:
                return False

    def edit_template(self, templateName):
        res = self.search_template(templateName)
        if res:
            try:
                self.draft.click(self.draft.editbutton_loc)
                self.driver.implicitly_wait(60)
            except:
                log.info('-----打开Template编辑页面失败！----')
            else:
                time.sleep(3)
                self.draft.send_keys(self.draft.nameinput_loc, editTemplateName)
                time.sleep(1)
                self.draft.click(self.draft.saveexit_loc)
                time.sleep(3)
                log.info('-----完成Template编辑操作！是否编辑成功待验证----')
        else:
            log.info('-----未找到待编辑的Template!----')

    def copy_template(self, templateName):
        res = self.search_template(templateName)
        if res:
            try:
                self.draft.click(self.draft.copybutton_loc)
            except:
                log.info('-----打开Template拷贝对话框失败！----')
            else:
                self.draft.send_keys(self.draft.copytemname_loc, copyTemplateName)
                time.sleep(1)
                self.draft.click(self.draft.copytemok_loc)
                log.info('-----完成Template拷贝操作！是否拷贝成功待验证----')
        else:
            log.info('-----未找到待拷贝的Template!----')

    def delete_template(self, templateName):
        res = self.search_template(templateName)
        if res:
            try:
                self.draft.click(self.draft.delbutton_loc)
            except:
                log.info('-----打开Templates删除对话框失败！----')
            else:
                time.sleep(1)
                self.draft.click(self.draft.delyes_loc)
                log.info('-----完成Template删除操作！是否删除成功待验证----')
        else:
            log.info('-----未找到待删除的Template!----')

    def publish_template(self, templateName):
        res = self.search_template(templateName)
        if res:
            try:
                self.draft.click(self.draft.publishbutton_loc)
            except:
                log.info('-----打开Templates发布对话框失败！----')
            else:
                time.sleep(1)
                self.draft.click(self.draft.publishyes_loc)
                time.sleep(2)
                log.info('-----完成Template发布操作！是否发布成功待验证----')
        else:
            log.info('-----未找到待发布的Template!----')

    def verify_publish(self, templatename):
        publish = ('xpath', '//*[@id="set_left"]/ul/li[@title="Published"]')
        coll = self.driver.find_element_by_xpath('//*[@id="nav_arrow"]/div').get_attribute("class")
        if coll == 'icn collapse':
            self.draft.click(self.draft.exButton_loc)
        self.draft.click(publish)
        time.sleep(3)
        self.draft.click(self.draft.exButton_loc)
        self.draft.search(templatename)
        time.sleep(2)
        try:
            self.draft.get_text(self.draft.tempname1_loc)
        except:
            return False
        else:
            return True

    def test01_add_team_draft_template(self):
        """新建Template"""
        self.add_drafttemplate()
        res = self.verify_template(templateName)
        if res:
            log.info('-----添加Template成功！----')
        else:
            log.info('-----添加Template失败！----')
        self.assertTrue(res)

    @skip_dependon(depend='test01_add_team_draft_template')
    def test02_edit_team_draft_template(self):
        """编辑Template"""
        self.edit_template(templateName)
        res = self.verify_template(editTemplateName)
        if res:
            log.info('-----编辑Template成功！----')
        else:
            log.info('-----编辑Template失败！----')
        self.assertTrue(res)

    @skip_dependon(depend='test02_edit_team_draft_template')
    def test03_copy_team_draft_template(self):
        """复制编辑的Template"""
        self.copy_template(editTemplateName)
        res = self.verify_template(copyTemplateName)
        if res:
            log.info('-----拷贝Template成功！----')
        else:
            log.info('-----拷贝Template失败！----')
        self.assertTrue(res)

    @skip_dependon(depend='test03_copy_team_draft_template')
    def test04_delete_team_draft_template(self):
        """删除复制的Template"""
        self.delete_template(copyTemplateName)
        res = self.search_template(copyTemplateName)
        if not res:
            log.info('-----删除Template成功！----')
        else:
            log.info('-----删除Template失败！----')
        self.assertFalse(res)

    @skip_dependon(depend='test02_edit_team_draft_template')
    def test05_publish_team_draft_template(self):
        """发布编辑后的Template"""
        self.publish_template(editTemplateName)
        res = self.verify_publish(editTemplateName)
        # 清除数据
        self.delete_template(editTemplateName)
        time.sleep(2)
        if res:
            log.info('-----发布Template成功！----')
        else:
            log.info('-----发布Template失败！----')
        self.assertTrue(res)


if __name__ == '__main__':
    unittest.main()

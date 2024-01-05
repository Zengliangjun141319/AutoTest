# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     WOWidgetTest.py
   Author :        曾良均
   QQ:             277099728
   Date：          9/21/2023 8:38 AM   
   Description :
-------------------------------------------------
   Change Activity:
                   
-------------------------------------------------
"""
__author__ = 'ljzeng'

import unittest
from Page.loginpage import LoginPage
from Page.AssetHealth.WorkOrderPage import WorkOrderPage
from logger import Log
from operater import browser
from Common.PubValue import PubValue
import time
from datetime import datetime,timedelta
import random
import os
import pyautogui as ui   # 引用第三方库实现上传附件功能
import pyperclip   # 利用 剪切板 库实现对中文的读写
import ddt
from excel import excel
from selenium.webdriver.common.action_chains import ActionChains as AC

log = Log()
path = '.\\report'
value = PubValue(None)
currentdate = time.strftime('%Y%m%d-%H%M%S')
desc = 'The work order add on ' + currentdate
nextfollowdate = datetime.now() + timedelta(days=random.randint(1, 7))
nextfollowdate = nextfollowdate.strftime('%m/%d/%Y')
file_path = ".\\TestData\\communication_att.xlsx"
testData = excel.get_list(file_path)
crcmsg = 'Send Customer Record Comments at ' + currentdate


@ddt.ddt
class WOWidgetTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = browser()  # 无头模式下有的测试不通过
        cls.lg = LoginPage(cls.driver)
        cls.lg.login('atwowidget@iicon004.com', 'Win.12345')
        cls.driver.implicitly_wait(10)
        log.info('开始测试Work Order Widget功能------')
        cls.switchto_iframe(cls)
        cls.add_workorder(cls)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def switchto_iframe(self):
        self.workorder = WorkOrderPage(self.driver)
        self.driver.implicitly_wait(50)
        time.sleep(5)
        self.workorder.switch_to_iframe(self.workorder.iframe_loc)  # 切换到work order列表iframe
        time.sleep(1)

    def refresh(self):
        self.driver.refresh()
        self.driver.implicitly_wait(60)
        self.driver.switch_to.default_content()
        time.sleep(5)
        self.workorder.switch_to_iframe(self.workorder.iframe_loc)
        time.sleep(1)

    def add_workorder(self):
        time.sleep(5)
        if not self.workorder.is_clickable(self.workorder.addbutton_loc):
            self.refresh()
        try:
            self.workorder.click(self.workorder.addbutton_loc)
        except:
            log.info("-----打开新增Work order窗口失败-----")
        else:
            log.info("-----打开新增Work order窗口成功-----")
            time.sleep(2)
            self.workorder.switch_to_iframe(self.workorder.iframeworkorder_loc)  # 切换到新增work order的iframe
            time.sleep(1)

            self.workorder.click(self.workorder.assetselect_loc)
            self.driver.implicitly_wait(60)
            time.sleep(3)
            a = time.strftime('%M')
            log.info('----- 选择机器 ')
            s = 1
            while s < 5:
                try:
                    self.workorder.send_keys(self.workorder.assetsearchinput_loc, a)
                    self.workorder.click(self.workorder.assetsearchbutton_loc)
                    self.driver.implicitly_wait(60)
                    time.sleep(3)
                    self.workorder.click(self.workorder.searchresult_loc)
                    self.workorder.click(self.workorder.assetokbutton_loc)
                except:
                    log.info('机器列表未加载完成，稍后重试')
                    time.sleep(3)
                    s += 1
                    continue
                else:
                    log.info('机器已选择')
                    time.sleep(3)
                    break

            log.info('----录入Contact Information')
            self.select_customer(self)
            time.sleep(2)

            try:
                log.info('----输入Summary')
                self.workorder.send_keys(self.workorder.description_loc, desc)
                log.info('Desc: %s' % desc)

                self.workorder.click(self.workorder.assignedto_loc)
                time.sleep(1)
                assignedto = ('xpath', '//*[@id="dialog_assignto"]/div/div[2]/ul/li[@title="admin4 - Technician"]')
                self.workorder.click(assignedto)

                try:
                    self.workorder.click(self.workorder.duedate_loc)
                    time.sleep(1)
                    self.workorder.send_keys(self.workorder.duedate_loc, nextfollowdate)
                    time.sleep(1)
                except:
                    log.info('Input Due Date failed!')

                self.workorder.click(self.workorder.metertype_loc)
                time.sleep(1)
                self.workorder.click(self.workorder.metertype)
                time.sleep(2)
                # 获取发动机小时数
                hour = self.workorder.get_text(self.workorder.hourmeter_loc)
                if hour:
                    hours = hour + random.randint(10, 50)
                    self.workorder.send_keys(self.workorder.hourmeter_loc, str(hours))
                else:
                    self.workorder.send_keys(self.workorder.hourmeter_loc, str(random.randint(200, 5000)))

                # 获取里程数
                odo = self.workorder.get_text(self.workorder.odometer_loc)
                if odo:
                    odos = odo + random.randint(200, 500)
                    self.workorder.send_keys(self.workorder.odometer_loc, odos)
                else:
                    self.workorder.send_keys(self.workorder.odometer_loc, str(random.randint(2000, 50000)))

                self.workorder.click(self.workorder.odometeruom_loc)
                odounit = ('xpath', '//*[@id="dig_odometeruom"]/div/div[2]/ul/li[1]')
                self.workorder.click(odounit)

                try:
                    self.workorder.click(self.workorder.wotypeicon_loc)
                    time.sleep(2)
                    self.workorder.click(self.workorder.wotype_loc)
                    wotype = ('xpath', '//*[@id="dialog_wotype"]/div/div[2]/ul/li[2]')
                    wotypevalue = self.driver.find_element_by_xpath('//*[@id="dialog_wotype"]/div/div[2]/ul/li[2]').get_attribute('title')
                    self.workorder.click(wotype)
                except:
                    log.info('input work order type failed!')
                else:
                    #  把获取到的WO Type值保存到字典
                    time.sleep(1)
                    log.info('input work order type passed')

                self.workorder.send_keys(self.workorder.partsnmumberinbox, 'PON01')

                try:
                    self.workorder.click(self.workorder.location_loc)
                    time.sleep(1)
                    self.workorder.click(self.workorder.locationsel)
                    time.sleep(1)
                except:
                    log.info('input location failed!')
                else:
                    log.info('input location pass')

                try:
                    self.workorder.click(self.workorder.component)
                    time.sleep(1)
                    self.workorder.send_keys(self.workorder.component, 'AutoC')
                except:
                    log.info('input component failed')
                else:
                    log.info('input component passed')

                try:
                    self.workorder.click(self.workorder.department_loc)
                    time.sleep(1)
                    self.workorder.click(self.workorder.departmentsel)
                    time.sleep(1)
                except:
                    log.info('input department failed!')
                else:
                    log.info('input department passed!')

                try:
                    self.workorder.click(self.workorder.partsexpecteddate_inbox)
                    time.sleep(1)
                    self.workorder.send_keys(self.workorder.partsexpecteddate_inbox, nextfollowdate)
                    time.sleep(1)
                except:
                    log.info('Input Parts Expected Date failed!')

                try:
                    self.workorder.click(self.workorder.advisor_loc)
                    time.sleep(1)
                    self.workorder.click(self.workorder.advisorsel)
                    time.sleep(1)
                except:
                    log.info('input advisor failed!')
                else:
                    log.info('input advisor passed')

                try:
                    self.workorder.click(self.workorder.salesperson_loc)
                    time.sleep(1)
                    self.workorder.click(self.workorder.salespersonsel)
                    time.sleep(1)
                except:
                    log.info('input salesperson falied!')
                else:
                    log.info('input salesperson passed!')

                try:
                    self.workorder.click(self.workorder.nextfollowup_inbox)
                    time.sleep(1)
                    self.workorder.send_keys(self.workorder.nextfollowup_inbox, nextfollowdate)
                    time.sleep(1)
                except:
                    log.info('input Next Follow Up Date failed!')


                try:
                    self.workorder.send_keys(self.workorder.alternatestatus, 'Doing')
                except:
                    log.info('input Alternate status failed')
                else:
                    log.info('input Alternate status passed')
            except:
                log.info('录入Summary信息失败')
            else:
                try:
                    self.workorder.click(self.workorder.partstatus)
                    time.sleep(1)
                    self.workorder.click(self.workorder.partsstatussel)
                    time.sleep(1)
                except:
                    log.info('input parts status failed')
                else:
                    log.info('input parts status passed')

            try:
                log.info('-----录入Cost')
                self.workorder.send_keys(self.workorder.othercost_loc, str(random.randint(20, 500)))
                self.workorder.send_keys(self.workorder.partscost_loc, str(random.randint(10, 300)))
                self.workorder.send_keys(self.workorder.traveltimecost_loc, str(random.randint(10, 100)))
                self.workorder.send_keys(self.workorder.timetocomplete_loc, str(random.randint(1, 10)))
                self.workorder.send_keys(self.workorder.invoicenum_loc, 'IN' + currentdate)

                self.workorder.send_keys(self.workorder.internalid_loc, 'InvoNo.' + currentdate)
                self.workorder.click(self.workorder.billablechx)

                try:
                    self.workorder.click(self.workorder.billtojobDg)
                    time.sleep(1)
                    objob = ('//*[@id="dialog_billtojob"]/div/div[2]/ul/li[%d]' % random.randint(2, 9))
                    self.driver.find_element_by_xpath(objob).click()
                    time.sleep(1)
                except:
                    log.info('set Bill to job failed')
                else:
                    log.info('set Bill to job passed')

                try:
                    self.workorder.send_keys(self.workorder.notes_loc, 'This work order is testing.')
                except:
                    log.info('input notes failed')
                else:
                    log.info('input notes passed')
                time.sleep(2)
            except:
                log.info('录入Cost信息失败')

            self.workorder.click(self.workorder.status_loc)
            time.sleep(1)
            status1 = ('xpath', '//*[@id="dialog_status"]/div/div[2]/ul/li[@value="15"]')
            self.workorder.click(status1)

            log.info('-----保存WO')
            self.workorder.click(self.workorder.savebotton_loc)
            # 729版本增加提示
            self.driver.find_element_by_id('dialog_chksendtextmsg').click()
            self.driver.find_element_by_id('dialog_textmsg').send_keys('Save Work Order and Send')
            time.sleep(1)
            self.workorder.click(self.workorder.saveStatusChange_loc)
            time.sleep(1)

            res = ''
            times = 1
            while times <= 3:
                try:
                    res = self.workorder.get_text(self.workorder.savedialogmessage_loc)
                except:
                    log.info('第 %s 次未取到保存结果' % times)
                    time.sleep(2)
                    times += 1
                else:
                    log.info(res)
                    self.workorder.click(self.workorder.savedialogokbotton_loc)
                    time.sleep(5)
                    break

            ts = 1
            while ts <= 3:
                try:
                    woid = self.driver.find_element_by_id('dialog_wonumber').text
                    log.info('新建的WO为： % s' % woid)
                    self.workorder.click(self.workorder.withoutsavebutton_lco)
                except:
                    log.info('第 %s 次不保存退出失败' % ts)
                    ts += 1
                    time.sleep(2)
                else:
                    self.driver.implicitly_wait(60)
                    time.sleep(1)
                    value.setvalue(woid)
                    break
            self.driver.switch_to.default_content()
            self.workorder.switch_to_iframe(self.workorder.iframe_loc)
            time.sleep(2)
            result = (res == 'Saved successfully.')
            return result

    # 选择customer
    def select_customer(self):
        self.workorder.click(self.workorder.customerselect_loc)
        time.sleep(3)
        self.workorder.click(self.workorder.allcustomer_loc)
        tims = 1
        while tims <= 3:
            try:
                self.workorder.find_element(self.workorder.customerinfo_loc)
            except:
                log.info('Customer数据未加载完成，继续等待')
                time.sleep(2)
                tims += 1
            else:
                # log.info('Customer列表已加载')
                time.sleep(1)
                break

        time.sleep(1)
        try:
            self.workorder.click(self.workorder.customerinfo_loc)
            self.workorder.click(self.workorder.customerok_loc)
            time.sleep(2)
        except:
            log.info('选择Customer失败')
            self.workorder.click(self.workorder.customerok_loc)
            time.sleep(2)
        else:
            log.info('选择Customer成功')
            time.sleep(1)

    def set_widgets(self, locator):
        won = value.getvalue()
        time.sleep(2)
        if not self.workorder.is_clickable(self.workorder.addbutton_loc):
            self.refresh()
        try:
            # 搜索创建的WO
            self.workorder.send_keys(self.workorder.inputtext_loc, won)
            self.workorder.click(self.workorder.searchbutton_loc)
            time.sleep(3)
            self.workorder.click(self.workorder.first_line_cell)
            time.sleep(1)
        except:
            log.info('搜索WO失败')
        else:
            # log.info('找到WO，设置显示Widget')
            time.sleep(1)
            try:
                self.workorder.click(self.workorder.widgets_btn)
                time.sleep(1)
                self.workorder.click(self.workorder.widget_select_all_chx)
                time.sleep(1)
                self.workorder.click(self.workorder.widget_select_all_chx)  # 取消全选
            except:
                log.info('打开Widgets设置失败')
                return False
            else:
                self.workorder.click(locator)
                time.sleep(1)
                self.workorder.click(self.workorder.widget_set_ok_btn)
                time.sleep(3)

    def add_attaments(self, file):
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        fpath = os.path.abspath(os.path.join(BASE_DIR, '..\\..'))
        file = os.path.join(fpath, file)
        time.sleep(1)
        # 方法1：
        # pyperclip.copy(file)  # 复制文件路径到剪贴板
        # time.sleep(3)
        # ui.hotkey('ctrl', 'v')  # 快捷键 Ctrl + V 实现 粘贴
        # time.sleep(1)
        # ui.press('enter', presses=2)

        # 方法2：
        exfile = os.path.join(fpath, 'upfile.exe')
        os.system("%s %s" % (exfile, file))
        time.sleep(2)

    def screenshot(self, filepath):
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        fpath = os.path.abspath(os.path.join(BASE_DIR, '..\\..'))
        file = os.path.join(fpath, filepath)
        self.driver.save_screenshot(file)

    def send_communication(self, data):
        self.set_widgets(self.workorder.customercommunication_chx)
        log.info(data["casename"])
        try:
            self.workorder.send_keys(self.workorder.entermessage_inbox, data["text"])
            if data["file"]:
                if data["casename"] == "test picture":
                    # 先截图
                    self.screenshot(data["file"])
                    time.sleep(2)
                # 选择附件
                self.workorder.click(self.workorder.communication_atta_link)
                time.sleep(1)
                self.add_attaments(data["file"])
            self.workorder.click(self.workorder.sendmessage_btn)
            time.sleep(1)
        except:
            log.info('send message failed')
        else:
            message = ''
            time.sleep(3)
            while True:
                try:
                    self.workorder.send_keys(self.workorder.entermessage_inbox, ' ')
                except:
                    time.sleep(2)
                    continue
                else:
                    self.workorder.click(self.workorder.last_message_time)
                    time.sleep(1)
                    message = self.workorder.get_text(self.workorder.last_message_txt)
                    break
            if data["text"] in message:
                return True
            else:
                return False

    def change_status(self, sets, view):
        '''
        1、 定位到要更改状态的最后一条消息位置
        2、 使鼠标悬停，调出Tooltip
        3、 点击Tooltip上的更改图标，弹出update status窗口
        4、 依次更改每个接收者的状态为指定值，点击OK
        5、 检查更改后的状态显示是否正确
        '''
        try:
            self.set_widgets(self.workorder.customercommunication_chx)
            self.workorder.click(self.workorder.last_message_status)
            time.sleep(1)
            ac = AC(self.driver)
            # 取第一条的状态
            lst = self.driver.find_element_by_xpath('//*[@id="workorderdetail"]/div/div/div[2]/div[1]/div/div[5]/div[1]/div[2]/div')
            # bt = lst.find_element_by_xpath('./div/div[3]/div/div[@class="tip-function-button"]/svg')
            # 方法一：
            # ac.move_to_element(lst).pause(3).click(bt).release(bt).perform()   # 鼠标链式操作
            ac.move_to_element(lst).perform()  # 鼠标悬停
            time.sleep(1)
            # 方法二：
            # bt.click()  #  点击Tooltip上的元素
            # 方法三：
            # 通过JS点击Tooltip上的元素
            self.workorder.js_execute("document.querySelector('.tip-function-button').click()")
            time.sleep(1)
        except:
            log.info('打开Tooltip失败')
            return False
        else:
            try:
                sts = self.driver.find_elements_by_xpath('/html/body/div[@class="ui-popup-mask"]/div/div[2]/div[1]/div/div/div[1]/div/table/tr')
                for st in sts:
                    # 找到界面上所有需要更改状态号码，点击，选择要更新为的状态，点击OK
                    st.find_element_by_xpath('./td[last()-1]').click()
                    st.find_element_by_xpath('./td[last()-1]').click()  # 再点一次，打开下拉列表
                    time.sleep(1)
                    va = './td[last()-1]/div/div[2]/ul/li[@title="%s"]' % sets
                    st.find_element_by_xpath(va).click()
                    time.sleep(1)
                self.workorder.click(self.workorder.upstatus_ok_btn)
                time.sleep(3)
            except:
                log.info('update status operating failed')
                return False
            else:
                while True:
                    try:
                        self.workorder.click(self.workorder.entermessage_inbox)
                    except:
                        time.sleep(2)
                        continue
                    else:
                        time.sleep(1)
                        break
                time.sleep(1)
                self.workorder.click(self.workorder.last_message_time)
                time.sleep(1)
                ut = self.workorder.get_text(self.workorder.last_message_status)
                if ut == view:
                    return True
                else:
                    return False

    def send_comments(self, methods, content):
        self.set_widgets(self.workorder.internalcomments_chx)
        time.sleep(1)
        try:
            if methods == 'Post':
                self.workorder.click(self.workorder.commentsatt_btn)
                # Post方式：截图发附件及文字
                self.screenshot('report\\screenshot.png')
                time.sleep(1)
                # 选择附件
                self.add_attaments('report\\screenshot.png')
                self.workorder.send_keys(self.workorder.entercomments_inbox, content)
                self.workorder.click(self.workorder.postnote_btn)
                time.sleep(1)
            elif methods == 'Send':
                # Send方式发文字及表情
                self.workorder.send_keys(self.workorder.entercomments_inbox, content)
                self.workorder.click(self.workorder.comments_send_message_btn)
                time.sleep(1)
                try:
                    self.workorder.send_keys(self.workorder.sic_search_inbox, 'jack')
                    time.sleep(1)
                except:
                    log.info('打开Send Internal Comments窗口失败')
                    return False
                else:
                    self.workorder.click(self.workorder.sic_result_first_text_chx)
                    self.workorder.click(self.workorder.sic_result_first_mail_chx)
                    self.workorder.send_keys(self.workorder.sic_phonenumber_inbox, '15082852339;8442620940')
                    time.sleep(1)
                    self.workorder.click(self.workorder.sic_OK_btn)
                    while True:
                        try:
                            time.sleep(1)
                            self.workorder.send_keys(self.workorder.entercomments_inbox, ' ')
                        except:
                            time.sleep(2)
                            continue
                        else:
                            break
        except Exception as e:
            log.info(e)
            return False
        else:
            message = ''
            while True:
                try:
                    message = self.workorder.get_text(self.workorder.last_comments_txt)
                except:
                    time.sleep(2)
                    continue
                else:
                    break
            if message == content:
                return True
            else:
                return False

    def send_CustomerRecordComments(self):
        self.set_widgets(self.workorder.CRComments_chx)
        time.sleep(1)
        try:
            self.workorder.send_keys(self.workorder.crc_enter_comments_inbox, crcmsg)
            self.workorder.click(self.workorder.crc_post_btn)
            time.sleep(1)
        except Exception as e:
            log.info(e)
            return False
        else:
            while True:
                try:
                    self.workorder.send_keys(self.workorder.crc_enter_comments_inbox, ' ')
                except:
                    time.sleep(2)
                    continue
                else:
                    break
            text = self.workorder.get_text(self.workorder.crc_last_comments_txt)
            if text == crcmsg:
                return True
            else:
                return False

    # 以下为DDT带固定参数
    @ddt.data({'sets': 'Unknown', 'view': 'Unknown'},
              {'sets': 'Pending', 'view': 'Pending'},
              {'sets': 'Failed', 'view': 'Failed'},
              {'sets': 'Sent', 'view': 'Sent'},
              {'sets': 'Resent', 'view': 'Resent'},
              {'sets': 'Delivery Confirmed', 'view': 'Delivery Confirmed'})
    @ddt.unpack  # 分解多组数组
    def test01_changestatus(self, sets, view):
        '''测试更新消息状态'''
        res = self.change_status(sets, view)
        if res:
            log.info('测试修改状态为: %s  成功!' % sets)
        else:
            log.info('测试修改状态为: %s  失败!' % sets)
        self.assertTrue(res)

    @ddt.data(*testData)
    def test02_customCommunication(self, data):
        '''测试Customer Communication 小部件发送功能'''
        res = self.send_communication(data)
        if res:
            log.info('%s 测试成功！' % data["casename"])
        else:
            log.info('%s 测试失败!' % data["casename"])
        self.assertTrue(res)

    @ddt.data({"methods": "Post", "content": "Post note and attachment"},
              {"methods": "Send", "content": "Send message to mail and mobile"})
    @ddt.unpack
    def test03_internalcomments(self, methods, content):
        '''测试Internal Comments功能'''
        res = self.send_comments(methods, content)
        if res:
            log.info('%s Internal Comments 模式测试成功！' % methods)
        else:
            log.info('%s Internal Comments 模式测试失败！' % methods)
        self.assertTrue(res)

    def test04_CustomerRecordComments(self):
        '''测试Customer Record Comments小部件'''
        res = self.send_CustomerRecordComments()
        if res:
            log.info('Customer Record Comments小部件测试成功！')
        else:
            log.info('Customer Record Comments小部件测试失败！')
        self.assertTrue(res)


if __name__ == '__main__':
    unittest.main()

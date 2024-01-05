# coding: utf-8
'''
Change log:
    1、 1021版本改了对象的位置,已注释的是原位置 -- 曾良均 2021.10.22
    2、 2.22版本，列表上不可直接修改，须先点击再进入编辑模式  ---- 曾良均
    3、 2.25版本，列表上控件更改 ---- 曾良均
    4、 5.11版本，取消设置Contact及Following ---- 曾良均
    5、 6.7版本，增加新建WO时先遍历各Tab    ---- 普良均
    6、 727版本，把新建的WO Number保存到公共函数中，需要的模块自己再根据函数中方式取值   ---- 曾良均
    7、 911版本，增加对WO列表相关字段的测试
        a. WO编辑时取需要验证的字段值，保存到字典 fileds中
        b. 应用DDT，从Excel中取出要测试的字段，设置相应的Layout
        c. 验证各字段的值是否与保存在字典中的值相等
                                ------ 曾良均   2023.9.12
'''

from selenium.webdriver.support.select import Select
from Page.loginpage import LoginPage
from Page.AssetHealth.WorkOrderPage import WorkOrderPage
from logger import Log
from operater import browser
import unittest
import time
import os
import random
from skiptest import skip_dependon
from Common.PubValue import PubValue
import pyautogui as ui   # 引用第三方库实现上传附件功能
import pyperclip   # 利用 剪切板 库实现对中文的读写
from excel import excel
import ddt
from datetime import datetime, timedelta

log = Log()
path = '.\\report'

values = PubValue(None)

if not os.path.exists(path):
    os.mkdir(path)

currentdate = time.strftime('%Y%m%d-%H%M%S')
desc = 'The work order add on ' + currentdate
nextfollowdate = datetime.now() - timedelta(days=1)
nextfollowdate = nextfollowdate.strftime('%m/%d/%Y')
crrenttime = time.strftime('%Y%m%d%H%M%S')
statusname = 'Status-' + crrenttime
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

file_path = ".\\TestData\\TestWorkOrderList.xlsx"
testData = excel.get_list(file_path)
file_path1 = ".\\TestData\\TestWorkOrderList_Date.xlsx"
testData1 = excel.get_list(file_path1)
fileds = {}


@ddt.ddt
class ManageWorkOrderTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = browser()   # 无头模式下有的测试不通过
        cls.login = LoginPage(cls.driver)
        cls.login.login('autotestwo@iicon004.com', 'Win.12345')
        cls.driver.implicitly_wait(10)
        log.info('开始测试Work Order功能------')
        cls.switchto_iframe(cls)

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
        log.info('页面加载异常，刷新页面')
        self.driver.refresh()
        self.driver.implicitly_wait(60)
        self.driver.switch_to.default_content()
        time.sleep(5)
        self.workorder.switch_to_iframe(self.workorder.iframe_loc)
        time.sleep(1)

    def add_workorder(self):
        log.info('开始测试新增WO...')
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

            # 输入内容前先遍历各Tab
            try:
                self.workorder.click(self.workorder.alertstab_loc)
                time.sleep(2)

                self.workorder.click(self.workorder.segmentstab_loc)
                time.sleep(2)

                self.workorder.click(self.workorder.attachmentstab_loc)
                time.sleep(2)

                self.workorder.click(self.workorder.workortab_loc)
                time.sleep(1)
            except:
                log.info('加载各Tab内容失败')
                result = False

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
            self.select_customer()
            time.sleep(2)
            # 把公司名称、Code 保存到字典
            fileds["Company Name"] = self.workorder.get_text(self.workorder.companyName)
            fileds["Customer Code"] = self.workorder.get_text(self.workorder.companyCode)
            fileds["Contacts"] = 'Activer – T – 456-987-3179'

            try:
                log.info('----输入Summary')
                self.workorder.send_keys(self.workorder.description_loc, desc)
                log.info('Desc: %s' % desc)
                #  把描述字段内容保存到字典
                fileds["Description"] = desc
                self.workorder.click(self.workorder.assignedto_loc)
                time.sleep(1)
                assignedto = ('xpath', '//*[@id="dialog_assignto"]/div/div[2]/ul/li[@title="admin4 - Technician"]')
                self.workorder.click(assignedto)
                #  把Assigned to写入字典
                fileds["Assigned To"] = "admin4 - Technician"

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
                # self.workorder.js_execute("document.getElementById('divcontent').scrollTop=1000")
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
                    fileds["Work Order Type"] = wotypevalue
                    log.info('input work order type passed')

                self.workorder.send_keys(self.workorder.partsnmumberinbox, 'PON01')
                fileds["Parts Order Number"] = 'PON01'

                try:
                    self.workorder.click(self.workorder.location_loc)
                    time.sleep(1)
                    self.workorder.click(self.workorder.locationsel)
                    time.sleep(1)
                    fileds["Location"] = self.workorder.get_text(self.workorder.location_loc)
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
                    fileds["Component"] = 'AutoC'
                    log.info('input component passed')

                try:
                    self.workorder.click(self.workorder.department_loc)
                    time.sleep(1)
                    self.workorder.click(self.workorder.departmentsel)
                    time.sleep(1)
                    fileds["Department"] = self.workorder.get_text(self.workorder.department_loc)
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
                    fileds["Advisor"] = self.workorder.get_text(self.workorder.advisor_loc)
                except:
                    log.info('input advisor failed!')
                else:
                    log.info('input advisor passed! --> %s' % fileds["Advisor"])

                try:
                    self.workorder.click(self.workorder.salesperson_loc)
                    time.sleep(1)
                    self.workorder.click(self.workorder.salespersonsel)
                    time.sleep(1)
                    fileds["Salesperson"] = self.workorder.get_text(self.workorder.salesperson_loc)
                except:
                    log.info('input salesperson falied!')
                else:
                    log.info('input salesperson passed!  %s' % fileds["Salesperson"])

                try:
                    self.workorder.click(self.workorder.nextfollowup_inbox)
                    time.sleep(1)
                    self.workorder.send_keys(self.workorder.nextfollowup_inbox, nextfollowdate)
                    time.sleep(1)
                except:
                    log.info('input Next Follow Up Date failed!')


                try:
                    self.workorder.send_keys(self.workorder.alternatestatus, 'Doing')
                    fileds["Alternate Status"] = 'Doing'
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
                    # self.workorder.send_keys(self.workorder.partstatus, 'Pending')
                    self.workorder.click(self.workorder.partsstatussel)
                    time.sleep(1)
                except:
                    log.info('input parts status failed')
                else:
                    fileds["Parts Status"] = 'Pending'
                    log.info('input parts status passed')

            try:
                log.info('-----录入Cost')
                self.workorder.send_keys(self.workorder.othercost_loc, str(random.randint(20, 500)))
                self.workorder.send_keys(self.workorder.partscost_loc, str(random.randint(10, 300)))
                self.workorder.send_keys(self.workorder.traveltimecost_loc, str(random.randint(10, 100)))
                self.workorder.send_keys(self.workorder.timetocomplete_loc, str(random.randint(1, 10)))
                self.workorder.send_keys(self.workorder.invoicenum_loc, 'IN' + currentdate)
                fileds["Invoice #:"] = 'IN' + currentdate
                self.workorder.send_keys(self.workorder.internalid_loc, 'InvoNo.' + currentdate)
                # 1207版本新增PO Number
                self.workorder.send_keys(self.workorder.ponumber_loc, 'PN' + currentdate)
                fileds["PO Number"] = 'PN' + currentdate
                self.workorder.click(self.workorder.billablechx)
                fileds["Billable"] = 'Yes'
                try:
                    self.workorder.click(self.workorder.billtojobDg)
                    time.sleep(1)
                    objob = ('//*[@id="dialog_billtojob"]/div/div[2]/ul/li[%d]' % random.randint(2, 9))
                    self.driver.find_element_by_xpath(objob).click()
                    time.sleep(1)
                    fileds["Bill to job"] = self.workorder.get_text(self.workorder.billjobsel)
                except:
                    log.info('set Bill to job failed')
                else:
                    log.info('set Bill to job passed')

                try:
                    self.workorder.send_keys(self.workorder.notes_loc, 'This work order is testing.')
                except:
                    log.info('input notes failed')
                else:
                    fileds["Notes"] = 'This work order is testing.'
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

                    duedate = self.workorder.get_attribute(self.workorder.duedate_loc, 'value')
                    fileds['Due Date'] = duedate
                    time.sleep(1)
                    nextdate = self.workorder.get_attribute(self.workorder.nextfollowup_inbox, 'value')
                    fileds['Next Follow Up Date'] = nextdate
                    time.sleep(1)
                    partsexpecteddate = self.workorder.get_attribute(self.workorder.partsexpecteddate_inbox, 'value')
                    fileds['Parts Expected Date'] = partsexpecteddate

                    self.workorder.click(self.workorder.withoutsavebutton_lco)
                except:
                    log.info('第 %s 次不保存退出失败' % ts)
                    ts += 1
                    time.sleep(2)
                else:
                    self.driver.implicitly_wait(60)
                    time.sleep(1)
                    values.setvalue(woid)
                    break
            self.driver.switch_to.default_content()
            self.workorder.switch_to_iframe(self.workorder.iframe_loc)
            time.sleep(2)
            result = (res == 'Saved successfully.')
            return result

    # 选择customer
    def select_customer(self):
        log.info('----- 选择Customer')
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
                log.info('Customer列表已加载')
                time.sleep(1)
                break
        # while not self.workorder.is_visibility(self.workorder.customerinfo_loc):
        #     log.info('Customer数据未加载完成，继续等待')
        #     time.sleep(2)
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

    # 新增contact
    def add_contact(self):
        try:
            self.workorder.click(self.workorder.addcontact_loc)
            time.sleep(2)
        except:
            log.info("-----打开新增Contact窗口失败-----")
        else:
            log.info("-----打开新增Contact窗口成功-----")
            self.workorder.send_keys(self.workorder.contactname_loc, "Contact " + time.strftime('%Y%m%d%H%M%S'))
            # 228版本更改下拉控件 ---- 曾良均
            self.workorder.click(self.workorder.preferences_loc)
            time.sleep(1)
            self.workorder.click(self.workorder.preferencesE_loc)

            self.workorder.send_keys(self.workorder.email_loc, "contactxx@costline.com")
            self.workorder.send_keys(self.workorder.mobile_loc, "12345678999")
            self.workorder.send_keys(self.workorder.contactnotes_loc, "add new contact test.")
            self.workorder.click(self.workorder.contactok_loc)

    def setting_status(self):
        log.info('开始测试State设置...')
        # if not self.workorder.is_clickable(self.workorder.addbutton_loc):
        #     self.refresh()
        try:
            self.workorder.click(self.workorder.refreshbutton_loc)
            while True:
                if self.workorder.pageload():
                    time.sleep(1)
                    break
                else:
                    time.sleep(2)
                    log.info("页面未加载完，继续等待...")
                    continue
            time.sleep(5)
        except:
            log.info('页面未加载完，等待3秒')
            time.sleep(3)
        finally:
            time.sleep(3)

        try:
            self.workorder.click(self.workorder.statussetting_loc)
            time.sleep(3)
        except:
            log.info("-----打开Status列表失败-----")
        else:
            log.info("-----打开Status列表成功-----")
            self.workorder.switch_to_iframe(self.workorder.iframestatus_loc)
            self.add_status(statusname)
        return statusname

    def add_status(self, statusname):
        try:
            time.sleep(2)    # 等待Status列表加载
            self.workorder.click(self.workorder.statusaddbutton_loc)
            time.sleep(3)
        except:
            log.info("-----打开新增Status窗口失败-----")
        else:
            log.info("-----打开新增Status窗口成功-----")
            self.workorder.send_keys(self.workorder.statusnameinput_loc, statusname)
            self.workorder.clear(self.workorder.statuscolorinput_loc)
            self.workorder.send_keys(self.workorder.statuscolorinput_loc, '#9900FF')
            self.workorder.click(self.workorder.statusokbutton_loc)
            time.sleep(5)
            self.workorder.click(self.workorder.statusrefresh_loc)
            time.sleep(5)

    def search_status(self):
        table = self.driver.find_element('xpath', ".//*[@id='statuslist']/div/div[1]/div/table/tbody")
        rows = table.find_elements_by_tag_name('tr')
        # time.sleep(5)
        rownames = []
        for row in rows:
            col = row.find_element_by_xpath(".//td[1]/span")
            rowtext = col.text
            rownames.append(rowtext)
        time.sleep(2)
        return rownames

    def delete_status(self):
        try:
            self.workorder.click(self.workorder.statusrefresh_loc)
            time.sleep(2)
        except:
            log.info('刷新Status列表失败')
            return False
        finally:
            log.info('准备测试删除Status')
            time.sleep(5)
            table = self.driver.find_element('xpath', ".//*[@id='statuslist']/div/div[1]/div/table/tbody")
            rows = table.find_elements_by_tag_name('tr')

            for row in rows:
                col = row.find_element_by_xpath(".//td[1]/span")
                rowtext = col.text
                # log.info('Status: %s' % rowtext)
                if rowtext == statusname:
                    # //*[@id="statuslist"]/div/div[1]/div/table/tbody/tr[22]/td[9]
                    # 119版本增加了Status Code字段，删除按钮位置变更，改为用Title定位
                    row.find_element_by_xpath('./td/a[@title="Delete"]').click()
                    time.sleep(2)
                    # 确认删除 /html/body/div[4]/div[3]/input[2]
                    dele_ok = ('xpath', '/html/body/div[@class="dialog popupmsg"]/div[@class="dialog-func"]/input[2]')
                    self.workorder.click(dele_ok)
                    time.sleep(3)
                    log.info('删除Status： %s 成功' % rowtext)
                    self.workorder.click(self.workorder.statusexit_loc)
                    self.driver.implicitly_wait(60)
                    time.sleep(2)
                    self.driver.switch_to.default_content()
                    self.workorder.switch_to_iframe(self.workorder.iframe_loc)
                    return True
            else:
                self.workorder.click(self.workorder.statusexit_loc)
                self.driver.implicitly_wait(60)
                time.sleep(2)
                self.driver.switch_to.default_content()
                self.workorder.switch_to_iframe(self.workorder.iframe_loc)
                return False

    def add_segment(self):
        time.sleep(2)
        if not self.workorder.is_clickable(self.workorder.addbutton_loc):
            self.refresh()
        log.info('测试新建Segment')
        time.sleep(2)
        wonum = values.getvalue()
        try:
            self.workorder.send_keys(self.workorder.inputtext_loc, wonum)
            self.workorder.click(self.workorder.searchbutton_loc)
            time.sleep(3)
            self.workorder.click(self.workorder.wo_first_edit_btn)
            time.sleep(1)
            self.workorder.switch_to_iframe(self.workorder.iframeworkorder_loc)  # 切换到新增work order的iframe
            time.sleep(1)
            self.workorder.click(self.workorder.segmentstab_loc)
            time.sleep(1)
        except:
            log.info('打开到Segment Tab失败')
            return False
        else:
            log.info('开始Add Segment')
            self.workorder.click(self.workorder.addsegmentBtn_loc)
            time.sleep(1)
            try:
                self.workorder.send_keys(self.workorder.segmentHoursInbox_loc, str(random.randint(5, 20)))
                self.workorder.send_keys(self.workorder.segmentCostInbox_loc, str(random.randint(100, 300)))
                self.workorder.click(self.workorder.segmentBillable_chx_loc)
                self.workorder.send_keys(self.workorder.segmentDescInbox_loc, 'Segment Desc: ' + desc)
                self.workorder.click(self.workorder.segmentBtnOK_loc)
                time.sleep(2)
            except:
                log.info('录入Segment信息失败')
                return False
            else:
                log.info('检查Segment保存结果')
                title = self.workorder.get_text(self.workorder.segmenttitle_lab)
                # 不保存退出
                try:
                    self.workorder.click(self.workorder.withoutsavebutton_lco)
                    time.sleep(3)
                    self.driver.switch_to.default_content()
                    self.workorder.switch_to_iframe(self.workorder.iframe_loc)
                except:
                    log.info('不保存退出失败')
                    return False
                if title == 'Segment 1':
                    return True
                else:
                    return False

    def add_attachments(self):
        time.sleep(2)
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        fpath = os.path.abspath(os.path.join(BASE_DIR, '..\..'))
        file = os.path.join(fpath, 'TestData\\atts.jpg')
        if not self.workorder.is_clickable(self.workorder.addbutton_loc):
            self.refresh()
        log.info('测试附件功能')
        time.sleep(2)
        wonum = values.getvalue()
        try:
            self.workorder.send_keys(self.workorder.inputtext_loc, wonum)
            self.workorder.click(self.workorder.searchbutton_loc)
            time.sleep(3)
            self.workorder.click(self.workorder.wo_first_edit_btn)
            time.sleep(1)
            self.workorder.switch_to_iframe(self.workorder.iframeworkorder_loc)  # 切换到新增work order的iframe
            time.sleep(1)
            self.workorder.click(self.workorder.attachmentstab_loc)  # 打开附件Tab
            time.sleep(1)
            self.workorder.click(self.workorder.addattachmentsBtn_loc)  # 点击 Add File
            time.sleep(2)
            '''
            # 此方法执行时容易出异常
            pyperclip.copy(file)  # 复制文件路径到剪贴板
            time.sleep(2)
            # ui.write(file)  # 注意，此时输入法需改为英文，否则会出错
            ui.hotkey('ctrl', 'v')  # 快捷键 Ctrl + V 实现 粘贴
            time.sleep(1)
            ui.press('enter', presses=2)  # 多按次回车
            time.sleep(3)
            '''
            # 使用旧方法
            exfile = os.path.join(fpath, 'upfile.exe')
            os.system("%s %s" % (exfile, file))
            time.sleep(2)
        except:
            log.info('上传附件失败')
            return False
        else:
            log.info('附件上传操作成功，结果待验证......')
            self.driver.implicitly_wait(10)
            self.workorder.click(self.workorder.attachmentViewChx_loc)
            time.sleep(1)
            attname = self.workorder.get_attribute(self.workorder.attachmentNameInbox_loc, 'data-ori')
            # 不保存退出
            try:
                self.workorder.click(self.workorder.withoutsavebutton_lco)
                time.sleep(3)
                self.driver.switch_to.default_content()
                self.workorder.switch_to_iframe(self.workorder.iframe_loc)
            except:
                log.info('不保存退出失败')
                return False
            if attname == 'atts.jpg':
                return True
            else:
                return False

    def add_estimates(self):
        time.sleep(2)
        if not self.workorder.is_clickable(self.workorder.addbutton_loc):
            self.refresh()
        log.info('测试新建Estimate')
        time.sleep(2)
        wonum = values.getvalue()
        try:
            self.workorder.send_keys(self.workorder.inputtext_loc, wonum)
            self.workorder.click(self.workorder.searchbutton_loc)
            time.sleep(3)
            self.workorder.click(self.workorder.wo_first_edit_btn)
            time.sleep(1)
            self.workorder.switch_to_iframe(self.workorder.iframeworkorder_loc)  # 切换到新增work order的iframe
            time.sleep(1)
            self.workorder.click(self.workorder.estimatestab_loc)
            time.sleep(1)
        except:
            log.info('打开新建Estimate失败')
            return False
        else:
            log.info('开始点击Add Estimate')
            self.workorder.click(self.workorder.addestBtn_loc)
            time.sleep(1)
            try:
                self.workorder.send_keys(self.workorder.addest_Number, 'Es001')
                self.workorder.send_keys(self.workorder.addest_othercost_inbox, random.randint(30, 100))
                self.workorder.send_keys(self.workorder.addest_partcost_inbox, random.randint(50, 120))
                self.workorder.send_keys(self.workorder.addest_travelcost_inbox, random.randint(20, 200))
                self.workorder.send_keys(self.workorder.addest_laborcost_inbox, random.randint(10, 100))
                self.workorder.send_keys(self.workorder.addest_timetocomp_inbox, random.randint(1, 10))
                self.workorder.send_keys(self.workorder.addest_taxes_inbox, random.randint(30, 200))
                self.workorder.click(self.workorder.addest_porequired_chx)
                time.sleep(1)
                self.workorder.click(self.workorder.addest_totalcost_Btn)
                time.sleep(1)
                self.workorder.send_keys(self.workorder.addest_technotes_inbox, 'Technician Notes: ' + desc)
                self.workorder.click(self.workorder.addest_OK_btn)
                time.sleep(2)
            except:
                log.info('Estimate信息录入失败!')
                return False
            else:
                log.info('Estimate已保存，保存结果待验证......')
                title = self.workorder.get_text(self.workorder.addest_title_label)
                # 不保存退出
                try:
                    self.workorder.click(self.workorder.withoutsavebutton_lco)
                    time.sleep(3)
                    self.driver.switch_to.default_content()
                    self.workorder.switch_to_iframe(self.workorder.iframe_loc)
                except:
                    log.info('不保存退出失败')
                    return False
                if title == 'Es001':
                    return True
                else:
                    return False

    def publist_estimates(self):
        time.sleep(2)
        if not self.workorder.is_clickable(self.workorder.addbutton_loc):
            self.refresh()
        log.info('测试发布Estimates')
        time.sleep(2)
        wonum = values.getvalue()
        try:
            self.workorder.send_keys(self.workorder.inputtext_loc, wonum)
            self.workorder.click(self.workorder.searchbutton_loc)
            time.sleep(3)
            self.workorder.click(self.workorder.wo_first_edit_btn)
            time.sleep(1)
            self.workorder.switch_to_iframe(self.workorder.iframeworkorder_loc)  # 切换到新增work order的iframe
            time.sleep(1)
            self.workorder.click(self.workorder.estimatestab_loc)
            time.sleep(1)
        except:
            log.info('打开Estimates页失败')
            return False
        else:
            log.info('开始发布 Estimates')
            if self.workorder.get_attribute(self.workorder.pub_est_ex_btn, 'class') == 'sbutton iconchevronright':
                self.workorder.click(self.workorder.pub_est_ex_btn)
                time.sleep(1)
            try:
                self.workorder.click(self.workorder.pub_est_publish_btn)
                time.sleep(3)
                if not self.workorder.is_selected(self.workorder.pub_est_sendto_chx):
                    self.workorder.click(self.workorder.pub_est_sendto_chx)
                self.workorder.click(self.workorder.pub_est_publish_publish_btn)
                time.sleep(2)
            except:
                log.info('发布Estimates操作失败')
                return False
            else:
                log.info('发布操作成功，结果待验证...')
                status = ''
                times = 1
                while times < 60:
                    try:
                        status = self.workorder.get_text(self.workorder.pub_est_status_label)
                        self.workorder.click(self.workorder.pub_est_ex_btn)
                    except:
                        log.info('页面未加载完，第 %s 次重试！' % times)
                        time.sleep(3)
                        times += 1
                        continue
                    else:
                        log.info('已获取Estimate状态！')
                        break

                # 不保存退出
                try:
                    self.workorder.click(self.workorder.withoutsavebutton_lco)
                    time.sleep(3)
                    self.driver.switch_to.default_content()
                    self.workorder.switch_to_iframe(self.workorder.iframe_loc)
                except:
                    log.info('不保存退出失败')
                    return False
                if status == 'Awaiting Customer Approval':
                    return True
                else:
                    return False

    def add_pub_estimates(self):
        time.sleep(2)
        if not self.workorder.is_clickable(self.workorder.addbutton_loc):
            self.refresh()
        log.info('测试新建并发布Estimate')
        time.sleep(2)
        wonum = values.getvalue()
        try:
            self.workorder.send_keys(self.workorder.inputtext_loc, wonum)
            self.workorder.click(self.workorder.searchbutton_loc)
            time.sleep(3)
            self.workorder.click(self.workorder.wo_first_edit_btn)
            time.sleep(1)
            self.workorder.switch_to_iframe(self.workorder.iframeworkorder_loc)  # 切换到新增work order的iframe
            time.sleep(1)
            self.workorder.click(self.workorder.estimatestab_loc)
            time.sleep(1)
        except:
            log.info('打开新建Estimate失败')
            return False
        else:
            log.info('开始点击Add Estimate')
            self.workorder.click(self.workorder.addestBtn_loc)
            time.sleep(1)
            try:
                self.workorder.send_keys(self.workorder.addest_Number, 'Es002')
                self.workorder.send_keys(self.workorder.addest_technotes_inbox, 'Publish Estimates: ' + desc)
                self.workorder.click(self.workorder.addest_publish_btn)
                time.sleep(1)
                self.workorder.click(self.workorder.pub_est_publish_publish_btn)
                time.sleep(3)
            except:
                log.info('Estimate信息录入发布失败!')
                return False
            else:
                log.info('Estimate已发布，结果待验证......')
                status = ''
                times = 1
                while times < 60:
                    try:
                        status = self.workorder.get_text(self.workorder.addest_publish_status_label)
                        self.workorder.click(self.workorder.pub_est_ex_btn)
                    except:
                        log.info('页面未加载完，第 %s 次重试！' % times)
                        time.sleep(3)
                        times += 1
                        continue
                    else:
                        log.info('已获取Estimate状态！')
                        break

                # 不保存退出
                try:
                    self.workorder.click(self.workorder.withoutsavebutton_lco)
                    time.sleep(3)
                    self.driver.switch_to.default_content()
                    self.workorder.switch_to_iframe(self.workorder.iframe_loc)
                except:
                    log.info('不保存退出失败')
                    return False
                if status == 'Awaiting Customer Approval':
                    fileds["Estimate Status"] = 'Awaiting Customer Approval'
                    fileds["Pending Estimates"] = '2'
                    return True
                else:
                    return False

    def add_Invoice(self):
        time.sleep(2)
        if not self.workorder.is_clickable(self.workorder.addbutton_loc):
            self.refresh()
        log.info('测试新建Invoice')
        time.sleep(2)
        wonum = values.getvalue()
        try:
            self.workorder.send_keys(self.workorder.inputtext_loc, wonum)
            self.workorder.click(self.workorder.searchbutton_loc)
            time.sleep(3)
            self.workorder.click(self.workorder.wo_first_edit_btn)
            time.sleep(1)
            self.workorder.switch_to_iframe(self.workorder.iframeworkorder_loc)  # 切换到新增work order的iframe
            time.sleep(1)
            self.workorder.click(self.workorder.invoicestab_loc)
            time.sleep(1)
        except:
            log.info('打开新建Invoice失败')
            return False
        else:
            log.info('开始点击Add Invoice')
            self.workorder.click(self.workorder.addinvBtn)
            time.sleep(1)
            try:
                self.workorder.send_keys(self.workorder.addinv_number_inbox, 'Inv001')
                self.workorder.send_keys(self.workorder.addinv_notes_inbox, 'Invoice Notes: ' + desc)
                self.workorder.click(self.workorder.addinv_OK_btn)
                time.sleep(2)
            except:
                log.info('录入Invoice信息失败')
                return False
            else:
                log.info('Invoice已保存，保存结果待验证......')
                title = ''
                times = 1
                while times < 60:
                    try:
                        title = self.workorder.get_text(self.workorder.addinv_title_label)
                    except:
                        log.info('页面未加载完，第 %s 次重试！' % times)
                        time.sleep(3)
                        times += 1
                        continue
                    else:
                        log.info('已获取Invoice标题！')
                        break

                # 不保存退出
                try:
                    self.workorder.click(self.workorder.withoutsavebutton_lco)
                    time.sleep(3)
                    self.driver.switch_to.default_content()
                    self.workorder.switch_to_iframe(self.workorder.iframe_loc)
                except:
                    log.info('不保存退出失败')
                    return False
                if title == 'Inv001':
                    return True
                else:
                    return False

    def publish_invoices(self):
        time.sleep(2)
        if not self.workorder.is_clickable(self.workorder.addbutton_loc):
            self.refresh()
        log.info('测试Publish Invoice')
        time.sleep(2)
        wonum = values.getvalue()
        try:
            self.workorder.send_keys(self.workorder.inputtext_loc, wonum)
            self.workorder.click(self.workorder.searchbutton_loc)
            time.sleep(3)
            self.workorder.click(self.workorder.wo_first_edit_btn)
            time.sleep(1)
            self.workorder.switch_to_iframe(self.workorder.iframeworkorder_loc)  # 切换到新增work order的iframe
            time.sleep(1)
            self.workorder.click(self.workorder.invoicestab_loc)
            time.sleep(1)
        except:
            log.info('打开Publish Invoice失败')
            return False
        else:
            log.info('开始Publish Invoice')
            self.workorder.click(self.workorder.inv_ex_btn)
            time.sleep(1)
            # 添加附件
            BASE_DIR = os.path.dirname(os.path.abspath(__file__))
            fpath = os.path.abspath(os.path.join(BASE_DIR, '..\..'))
            file = os.path.join(fpath, 'TestData\\invoiceAttachment.jpg')
            try:
                self.workorder.click(self.workorder.inv_addAtt_btn)
                time.sleep(1)
                self.workorder.click(self.workorder.inv_add_att_upload_btn)
                # 此方法不稳定
                # pyperclip.copy(file)  # 复制文件路径到剪贴板
                # time.sleep(2)
                # ui.hotkey('ctrl', 'v')  # 快捷键 Ctrl + V 实现 粘贴
                # time.sleep(1)
                # ui.press('enter', presses=2)  # 多按次回车
                # time.sleep(3)

                # 使用upfile方法上传附件
                exfile = os.path.join(fpath, 'upfile.exe')
                os.system("%s %s" % (exfile, file))
                time.sleep(2)
                self.workorder.send_keys(self.workorder.inv_add_att_caption_inbox, 'invoice Attachment')
                self.workorder.click(self.workorder.inv_add_att_save_btn)
                time.sleep(2)
            except:
                log.info('加载附件失败')

            # Publish
            try:
                self.workorder.click(self.workorder.inv_pub_btn)
                time.sleep(3)
                if not self.workorder.is_selected(self.workorder.inv_pub_sendto_chx):
                    self.workorder.click(self.workorder.inv_pub_sendto_chx)

                self.workorder.click(self.workorder.inv_pub_sendAtt_chx)  # 点击勾选后自动加载附件
                time.sleep(1)
                self.workorder.click(self.workorder.inv_pub_publish_btn)
                time.sleep(2)
            except:
                log.info('Publish操作失败')
                return False
            else:
                log.info('Publish操作已完成，结果待验证...')
                inv_status = ''
                times = 1
                while times < 60:
                    try:
                        inv_status = self.workorder.get_text(self.workorder.inv_status_label)
                        self.workorder.click(self.workorder.inv_ex_btn)
                    except:
                        log.info('页面未加载完，第 %s 次重试！' % times)
                        time.sleep(3)
                        times += 1
                        continue
                    else:
                        log.info('已获取Invoice状态！')
                        break

                # 不保存退出
                try:
                    self.workorder.click(self.workorder.withoutsavebutton_lco)
                    time.sleep(3)
                    self.driver.switch_to.default_content()
                    self.workorder.switch_to_iframe(self.workorder.iframe_loc)
                except:
                    log.info('不保存退出失败')
                    return False
                if inv_status == 'Awaiting Payment':
                    return True
                else:
                    return False

    def add_pub_invoice(self):
        time.sleep(2)
        if not self.workorder.is_clickable(self.workorder.addbutton_loc):
            self.refresh()
        log.info('测试新建并发布Invoice')
        time.sleep(2)
        wonum = values.getvalue()
        try:
            self.workorder.send_keys(self.workorder.inputtext_loc, wonum)
            self.workorder.click(self.workorder.searchbutton_loc)
            time.sleep(3)
            self.workorder.click(self.workorder.wo_first_edit_btn)
            time.sleep(1)
            self.workorder.switch_to_iframe(self.workorder.iframeworkorder_loc)  # 切换到新增work order的iframe
            time.sleep(1)
            self.workorder.click(self.workorder.invoicestab_loc)
            time.sleep(1)
        except:
            log.info('打开新建Invoice失败')
            return False
        else:
            log.info('开始点击Add Invoice')
            self.workorder.click(self.workorder.addinvBtn)
            time.sleep(1)
            try:
                self.workorder.send_keys(self.workorder.addinv_number_inbox, 'Inv002')
                Select(self.driver.find_element_by_id('dialog_invoice_status')).select_by_value('1')
                time.sleep(1)
                self.workorder.click(self.workorder.addinv_OK_btn)  # 点击 OK
                time.sleep(1)
                self.workorder.click(self.workorder.inv_pub_publish_btn)  # 点击弹出窗口中的 Publish
                time.sleep(1)
                self.workorder.click(self.workorder.inv_pub_markCustomVisible_btn)  # 点击 Mark按钮
                time.sleep(3)
            except:
                log.info('录入Invoice并发布失败')
                return False
            else:
                log.info('Invoice已发布，结果待验证......')
                inv_status = ''
                times = 1
                while times < 60:
                    try:
                        inv_status = self.workorder.get_text(self.workorder.inv_pub_status_label)
                        self.workorder.click(self.workorder.inv_ex_btn)
                    except:
                        log.info('页面未加载完，第 %s 次重试！' % times)
                        time.sleep(3)
                        times += 1
                        continue
                    else:
                        log.info('已获取Invoice状态！')
                        break

                # 不保存退出
                try:
                    self.workorder.click(self.workorder.withoutsavebutton_lco)
                    time.sleep(3)
                    self.driver.switch_to.default_content()
                    self.workorder.switch_to_iframe(self.workorder.iframe_loc)
                except:
                    log.info('不保存退出失败')
                    return False
                if inv_status == 'Awaiting Payment':
                    return True
                else:
                    return False

    def del_workorder(self):
        time.sleep(2)
        if not self.workorder.is_clickable(self.workorder.addbutton_loc):
            self.refresh()
        log.info('测试删除Work Order')
        time.sleep(2)
        wonum = values.getvalue()
        try:
            self.workorder.send_keys(self.workorder.inputtext_loc, wonum)
            self.workorder.click(self.workorder.searchbutton_loc)
            time.sleep(3)
            self.workorder.click(self.workorder.wo_first_del_btn)
            time.sleep(1)
            try:
                self.workorder.click(self.workorder.saveoverwriteYes_loc)
            except:
                self.driver.switch_to.default_content()
                self.workorder.click(self.workorder.saveoverwriteYes_loc)
                time.sleep(1)
                self.workorder.switch_to_iframe(self.workorder.iframe_loc)
        except:
            log.info('删除Work Order操作失败')
            return False
        else:
            log.info('删除WO操作成功，删除结果待验证......')
            time.sleep(1)
            self.workorder.click(self.workorder.refreshbutton_loc)
            time.sleep(1)
            wolist = self.driver.find_element_by_xpath('//*[@id="workorderlist"]/div/div[1]/div/table/tbody')
            val = wolist.find_elements_by_xpath('./tr')
            if len(val) == 0:
                return True
            else:
                return False

    def restore_workorder(self):
        time.sleep(2)
        if not self.workorder.is_clickable(self.workorder.addbutton_loc):
            self.refresh()
        log.info('测试恢复Work Order')
        time.sleep(2)
        wonum = values.getvalue()
        try:
            self.workorder.send_keys(self.workorder.inputtext_loc, wonum)
            self.workorder.click(self.workorder.searchbutton_loc)
            time.sleep(3)
            try:
                mess = self.workorder.get_text(self.workorder.savemessage_loc)
                self.workorder.click(self.workorder.saveoverwriteYes_loc)
            except:
                self.driver.switch_to.default_content()
                mess = self.workorder.get_text(self.workorder.savemessage_loc)
                self.workorder.click(self.workorder.saveoverwriteYes_loc)
                time.sleep(2)
                self.workorder.switch_to_iframe(self.workorder.iframe_loc)
        except:
            log.info('恢复WO操作失败')
            return False
        else:
            if wonum in mess:
                log.info('恢复操作成功，恢复结果待验证......')
                time.sleep(1)
                firstwo = self.workorder.get_text(self.workorder.first_wo_number)
                if firstwo == wonum:
                    return True
                else:
                    return False
            else:
                return False

    def verify_somedate(self, casename, location):
        time.sleep(2)
        if not self.workorder.is_clickable(self.workorder.addbutton_loc):
            self.refresh()
        log.info('-----开始测试WO字段： %s' % casename)
        time.sleep(2)
        wo = values.getvalue()
        self.set_layout(casename)
        time.sleep(2)
        try:
            self.workorder.click(self.workorder.refreshbutton_loc)
            time.sleep(2)
        except:
            log.info('------Refresh页面失败')
            return False
        else:
            self.workorder.send_keys(self.workorder.inputtext_loc, wo)
            self.workorder.click(self.workorder.searchbutton_loc)
            time.sleep(3)
            wos = self.driver.find_element_by_xpath('//*[@id="workorderlist"]/div/div[1]/div/table/tbody/tr')
            filed_value = wos.find_element_by_xpath('./' + location).text
            style = wos.find_element_by_xpath('./' + location).get_attribute('style')
            log.info('%s 的值为： %s' % (casename, filed_value))
            log.info('%s 样式： %s' % (casename, style))
            time.sleep(2)
            if style == 'background-color: red;':  # 未完成的WO，背景颜色才是红色
                if filed_value == fileds["%s" % casename]:
                    return True
                else:
                    return False
            else:
                return False

    def modify_completed(self):
        # self.reset_layout()
        self.driver.refresh()
        self.workorder.switch_to_iframe(self.workorder.iframe_loc)
        time.sleep(2)
        if not self.workorder.is_clickable(self.workorder.addbutton_loc):
            self.refresh()
        log.info('-----测试修改Status')
        time.sleep(2)
        wo = values.getvalue()
        while True:
            try:
                self.workorder.send_keys(self.workorder.inputtext_loc, wo)
                self.workorder.click(self.workorder.searchbutton_loc)
                time.sleep(3)
                self.workorder.js_execute("document.querySelector('#workorderlist .data-grid-body').scrollLeft = 10")
                time.sleep(1)
                self.workorder.click(self.workorder.wonumber_loc)
                self.workorder.click(self.workorder.wonumber_loc)
                time.sleep(1)
                # 2.22版本，列表上不可直接修改，须先点击再进入编辑模式  ---- 曾良均
                self.workorder.click(self.workorder.searchresultWO_loc)
                time.sleep(1)
                # 2.25版本，列表上控件更改 ---- 曾良均
                self.workorder.click(self.workorder.statuslistBtn_loc)
                time.sleep(1)
                self.workorder.click(self.workorder.statuscol_loc)
                time.sleep(3)
                # 获取当前完成时间
                compltedate = self.workorder.get_attribute(self.workorder.completeddateinbox, 'value')
                # 格式化日期:09/01/2023  --> 9/1/2023
                cd = compltedate.split('/')
                cd[0] = str(int(cd[0]))
                cd[1] = str(int(cd[1]))
                log.info('WO 完成时间为： %s' % '/'.join(cd))
                fileds["Completed Date"] = '/'.join(cd)

                self.workorder.click(self.workorder.statuschangeok_loc)
            except:
                log.info("-----修改Completed状态失败-----")
                break
            else:
                log.info("-----修改Completed状态完成，结果待验证-----")
                time.sleep(2)
                # 复选框改为下拉选择
                # self.workorder.click(self.workorder.displaycompleteChx_loc)
                displays = self.driver.find_element_by_id('selcompleted')
                Select(displays).select_by_value('1')
                time.sleep(2)
                times = 1
                while times < 60:
                    try:
                        self.workorder.click(self.workorder.refreshbutton_loc)
                        time.sleep(3)
                        log.info('数据已加载！')
                        break
                    except:
                        log.info('数据未加载完，第 %s 次重试！' % times)
                        time.sleep(3)
                        times += 1
                        continue

                self.workorder.click(self.workorder.searchbutton_loc)
                time.sleep(3)
                self.workorder.click(self.workorder.searchresultWO_loc)
                time.sleep(1)

                # //*[@id="workorderlist"]/div/div[1]/div/table/tbody/tr/td[4]/span/div/div/div/label[1]
                loc = "//*[@id='workorderlist']/div/div[1]/div/table/tbody/tr/td[4]/span/div/div/div/label[1]"
                element = self.driver.find_element_by_xpath(loc)
                select_value = element.text
                self.driver.switch_to.default_content()
                self.workorder.switch_to_iframe(self.workorder.iframe_loc)
                time.sleep(2)

                if select_value == 'Completed':
                    fileds["Status"] = 'Completed'
                    return True
                else:
                    return False

    def set_layout(self, fileds):
        self.workorder.click(self.workorder.refreshbutton_loc)
        time.sleep(1)
        # 点击Layout,Update Layout
        try:
            self.workorder.click(self.workorder.layout_loc)
            time.sleep(1)
            self.workorder.click(self.workorder.uplayout_loc)
            time.sleep(1)
        except:
            log.info('-----打开Layout设置界面失败')
        else:
            # log.info('-----开始设置Layout')
            self.workorder.click(self.workorder.showdefaultlayout)
            time.sleep(1)
            self.workorder.click(self.workorder.selectAllChx_loc)
            # 再点击进行反选
            self.workorder.click(self.workorder.selectAllChx_loc)
            # 勾选显示第一个：Work Order Number
            self.workorder.click(self.workorder.firstlayoutcolumnChx_loc)
            # 根据字段名称来判断要显示的列
            layoutlist = '//*[@id="dialog_layouts"]/div[5]/div[2]/table/tr'
            lists = self.driver.find_elements_by_xpath(layoutlist)
            for li in lists:
                column = li.find_element_by_xpath('./td[2]/span').text
                if column == fileds:
                    li.find_element_by_xpath('./td[1]/input').click()  # 勾选要显示的字段
            self.workorder.click(self.workorder.layoutOK_loc)
            time.sleep(1)
            self.workorder.send_keys(self.workorder.savelayoutname_loc, 'verifyWoFiled')
            self.workorder.click(self.workorder.savelayoutBtn_loc)
            # 覆盖已有Layout
            try:
                self.workorder.click(self.workorder.saveoverwriteYes_loc)
            except:
                self.driver.switch_to.default_content()
                self.workorder.click(self.workorder.saveoverwriteNo_loc)
                self.workorder.switch_to_iframe(self.workorder.iframe_loc)

    def verify_wo_filed(self, casename, location):
        time.sleep(2)
        if not self.workorder.is_clickable(self.workorder.addbutton_loc):
            self.refresh()
        log.info('-----开始测试WO字段： %s' % casename)
        time.sleep(2)
        wo = values.getvalue()
        # log.info('------设置Layout')
        self.set_layout(casename)
        time.sleep(2)
        try:
            self.workorder.click(self.workorder.refreshbutton_loc)
            time.sleep(2)
        except:
            log.info('------Refresh页面失败')
            return False
        else:
            self.workorder.send_keys(self.workorder.inputtext_loc, wo)
            self.workorder.click(self.workorder.searchbutton_loc)
            time.sleep(3)
            wos = self.driver.find_element_by_xpath('//*[@id="workorderlist"]/div/div[1]/div/table/tbody/tr')
            filed_value = wos.find_element_by_xpath('./' + location).text
            log.info('%s 的值为： %s' % (casename, filed_value))
            if filed_value == fileds["%s" % casename]:
                return True
            else:
                return False

    def view_wo_history(self):
        # 打开WO history页面
        time.sleep(2)
        if not self.workorder.is_clickable(self.workorder.addbutton_loc):
            self.refresh()
        log.info('-----测试查看WO 历史记录')
        time.sleep(2)
        self.driver.switch_to.default_content()
        self.workorder.click(self.workorder.wohis_menu)
        h = 0
        while h < 10:
            try:
                self.workorder.switch_to_iframe(self.workorder.iframe_loc)
                time.sleep(1)
            except:
                log.info('History 页面未加载完成，稍后重试')
                self.driver.refresh()
                time.sleep(3)
                h += 1
                continue
            else:
                time.sleep(1)
                break

        # 输入WO Number搜索历史记录
        wo = values.getvalue()
        try:
            self.workorder.click(self.workorder.wohis_number_inbox)
            time.sleep(1)
            self.workorder.send_keys(self.workorder.wohis_search_inbox, wo)  # 搜索框中输入WO Number
            time.sleep(1)
            self.workorder.click(self.workorder.wohis_searchresult)  # 选择第一个
            time.sleep(1)
            self.workorder.click(self.workorder.wohis_search_btn)
            time.sleep(3)
        except:
            log.info('搜索WO操作失败')
            return False
        else:
            log.info('WO操作成功，验证WO历史记录')
            his = self.driver.find_element_by_id('wohlist').find_elements_by_xpath('./tr')
            # if len(his) > 5:
            #     # 增加Update Type值的测试
            #     typer = False
            types = []
            updates = []
            for line in his:
                ut = line.find_element_by_xpath('./td[3]').text
                types.append(ut)
                up = line.find_element_by_xpath('./td[2]').text
                updates.append(up)
            exp = ['Created', 'Modified', 'Closed']
            if 'Manually' not in types and 'Automatically' not in types and exp not in updates:
                log.info(types)
                log.info(updates)
                return False
            else:
                return True
            # else:
            #     return False

    def test01_add_status(self):
        '''添加Status'''
        name = self.setting_status()
        names = self.search_status()
        if self.assertIn(name, names):
            log.info("新增Status失败！")
        else:
            log.info("新增Status成功！")

    @skip_dependon(depend='test01_add_status')
    def test02_del_status(self):
        '''删除添加的Status'''
        res = self.delete_status()
        if res:
            log.info('status删除成功')
        else:
            log.info('Status删除失败')
        self.assertTrue(res)

    def test03_add_workorder(self):
        '''添加WorkOrder'''
        result = self.add_workorder()
        if result:
            log.info("新增Work Order成功！")
        else:
            log.info("新增Work Order失败！")
        self.assertTrue(result)

    @skip_dependon(depend='test03_add_workorder')
    def test04_edit_segments(self):
        '''测试编辑WO之添加Segments'''
        res = self.add_segment()
        if res:
            log.info('新建Segment测试成功！')
        else:
            log.info('新建Segment测试失败！！')
        self.assertTrue(res)

    @skip_dependon(depend='test03_add_workorder')
    def test05_edit_attachments(self):
        '''测试编辑WO之附件管理'''
        res = self.add_attachments()
        if res:
            log.info('添加附件功能测试成功！')
        else:
            log.info('添加附件功能测试失败！')
        self.assertTrue(res)

    @skip_dependon(depend='test03_add_workorder')
    def test06_edit_estimates(self):
        '''测试WO之Estimates功能'''
        res = self.add_estimates()
        if res:
            log.info('新建Estimated测试成功！')
        else:
            log.info('新建Estimated测试失败！！')
        self.assertTrue(res)

    @skip_dependon(depend='test06_edit_estimates')
    def test07_publish_estimates(self):
        '''测试WO之Publish Estimates功能'''
        res = self.publist_estimates()
        if res:
            log.info('Publish Estimates测试成功！')
        else:
            log.info('Publish Estimates测试失败！')
        self.assertTrue(res)

    @skip_dependon(depend='test06_edit_estimates')
    def test08_add_pub_estimates(self):
        '''测试WO之新建并发布Estimates'''
        res = self.add_pub_estimates()
        if res:
            log.info('测试新建并发布评估成功！')
        else:
            log.info('测试新建并发布评估失败！')
        self.assertTrue(res)

    @skip_dependon(depend='test03_add_workorder')
    def test09_edit_invoices(self):
        '''测试WO之Invoice功能'''
        res = self.add_Invoice()
        if res:
            log.info('新建Invoice测试成功！')
        else:
            log.info('新建Invoice测试失败！')
        self.assertTrue(res)

    @skip_dependon(depend='test09_edit_invoices')
    def test10_publish_invoices(self):
        '''测试Publish Invoices'''
        res = self.publish_invoices()
        if res:
            log.info('Publish Invoices测试成功！')
        else:
            log.info('Publish Invoices测试失败！')
        self.assertTrue(res)

    @skip_dependon(depend='test09_edit_invoices')
    def test11_add_pub_invoices(self):
        '''测试新建并发布发票'''
        res = self.add_pub_invoice()
        if res:
            log.info('测试新建并发布发票成功！')
        else:
            log.info('测试新建并发布发票失败！')
        self.assertTrue(res)

    @skip_dependon(depend='test03_add_workorder')
    def test12_delete_wo(self):
        '''测试删除WO功能'''
        res = self.del_workorder()
        if res:
            log.info('删除WO测试成功！')
        else:
            log.info('删除WO测试失败！')
        self.assertTrue(res)

    @skip_dependon(depend='test12_delete_wo')
    def test13_restore_wo(self):
        '''测试恢复WO功能'''
        res = self.restore_workorder()
        if res:
            log.info('恢复WO测试成功！')
        else:
            log.info('恢复WO测试失败！')
        self.assertTrue(res)

    @ddt.data(*testData1)
    def test14_somedate(self, data):
        '''测试WO相关日期字段及背景颜色'''
        res = self.verify_somedate(data['CaseName'], data['Location'])
        if res:
            log.info('测试 ' + data['CaseName'] + ' 成功！')
        else:
            log.info('测试 ' + data['CaseName'] + ' 失败！')
        self.assertTrue(res)

    @skip_dependon(depend='test13_restore_wo')
    def test15_changestatus(self):
        '''更改WorkOrder状态'''
        res = self.modify_completed()
        if res:
            log.info("完成Work Order测试成功！")
        else:
            log.info("完成Work Order测试失败!")
        self.assertTrue(res)

    @ddt.data(*testData)
    def test16_verify_wo_filed(self, data):
        '''测试WO各字段值'''
        res = self.verify_wo_filed(data['CaseName'], data['Location'])
        if res:
            log.info('测试 ' + data['CaseName'] + ' 成功！')
        else:
            log.info('测试 ' + data['CaseName'] + ' 失败！')
        self.assertTrue(res)

    @skip_dependon(depend='test15_changestatus')
    def test17_view_history(self):
        '''测试查看WO历史记录功能'''
        res = self.view_wo_history()
        if res:
            log.info('查询WO历史记录成功！')
        else:
            log.info('查询WO历史记录失败！')
        self.assertTrue(res)


if __name__ == '__main__':
    unittest.main()

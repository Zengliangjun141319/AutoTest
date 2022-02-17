# coding: utf-8

from Page.loginpage import LoginPage
from Page.AssetHealth.WorkOrderPage import WorkOrderPage
from Common.logger import Log
from Common.operater import browser
import unittest
import time
import os
from Common.skiptest import skip_dependon

log = Log()
path = '.\\report'

if not os.path.exists(path):
    os.mkdir(path)

currentdate = time.strftime('%Y%m%d-%H%M%S')
desc = 'The work order add on ' + currentdate
crrenttime = time.strftime('%Y%m%d%H%M%S')
statusname = 'Status-' + crrenttime

class ManageWorkOrderTest(unittest.TestCase):


    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = browser()
        cls.login = LoginPage(cls.driver)
        cls.login.login('autotestwo@iicon004.com', 'Win.12345')
        cls.driver.implicitly_wait(60)
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
            self.workorder.switch_to_iframe(self.workorder.iframeworkorder_loc) # 切换到新增work order的iframe
            time.sleep(1)
            self.workorder.click(self.workorder.assetselect_loc)
            self.driver.implicitly_wait(60)
            time.sleep(10)
            a = time.strftime('%M')
            log.info('----- 选择机器 ')
            self.workorder.send_keys(self.workorder.assetsearchinput_loc, a)
            self.workorder.click(self.workorder.assetsearchbutton_loc)
            self.driver.implicitly_wait(60)
            time.sleep(10)
            # while not self.workorder.is_clickable(self.workorder.searchresult_loc):
            #     log.info('Assets list not display, waiting 3s')
            #     time.sleep(3)
            self.workorder.click(self.workorder.searchresult_loc)
            self.workorder.click(self.workorder.assetokbutton_loc)
            time.sleep(3)

            log.info('----录入Contact Information')
            self.select_customer()
            time.sleep(2)
            self.add_contact()
            time.sleep(2)

            log.info('----输入Summary')
            self.workorder.send_keys(self.workorder.description_loc, desc)
            log.info('Desc: %s' % desc)
            self.workorder.select_by_value(self.workorder.status_loc, '15')
            self.workorder.select_by_index(self.workorder.assignedto_loc, 2)
            self.workorder.send_keys(self.workorder.duedate_loc, currentdate)
            self.workorder.select_by_value(self.workorder.metertype_loc, 'Both')
            time.sleep(2)
            self.workorder.js_execute("document.getElementById('divcontent').scrollTop=1000")
            time.sleep(2)
            self.workorder.send_keys(self.workorder.hourmeter_loc, '1000')
            self.workorder.send_keys(self.workorder.odometer_loc, '2000')
            self.workorder.select_by_value(self.workorder.odometeruom_loc, 'Mile')
            self.workorder.click(self.workorder.wotypeicon_loc)
            time.sleep(2)
            self.workorder.click(self.workorder.wotypeselect_loc)
            self.workorder.clear(self.workorder.followupdate_loc)
            self.workorder.send_keys(self.workorder.followupdate_loc, currentdate)
            time.sleep(3)

            log.info('-----录入Cost')
            self.workorder.send_keys(self.workorder.othercost_loc, '23')
            self.workorder.send_keys(self.workorder.partscost_loc, '30')
            self.workorder.send_keys(self.workorder.traveltimecost_loc, '60')
            self.workorder.send_keys(self.workorder.timetocomplete_loc, '3.2')
            self.workorder.send_keys(self.workorder.internalid_loc, 'InvoNo.' + currentdate)
            self.workorder.send_keys(self.workorder.notes_loc, 'This work order is testing.')
            time.sleep(2)

            log.info('-----保存WO')
            self.workorder.click(self.workorder.savebotton_loc)
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

            # while not self.workorder.is_clickable(self.workorder.savedialogokbotton_loc):
            #     log.info('正在保存中......')
            #     time.sleep(3)
            # result = self.workorder.get_text(self.workorder.savedialogmessage_loc)
            # self.workorder.click(self.workorder.savedialogokbotton_loc)

            log.info('-----退出')
            ts = 1
            while ts <= 3:
                try:
                    self.workorder.click(self.workorder.withoutsavebutton_lco)
                except:
                    log.info('第 %s 次不保存退出失败' % ts)
                    ts += 1
                    time.sleep(2)
                else:
                    self.driver.implicitly_wait(60)
                    time.sleep(1)
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
            self.workorder.select_by_value(self.workorder.preferences_loc, '1')
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

    def reset_layout(self):
        # self.driver.switch_to.default_content()
        time.sleep(3)
        # self.workorder.switch_to_iframe(self.workorder.iframe_loc)
        r = 1
        while r <= 3:
            # 重试3次
            try:
                self.workorder.click(self.workorder.resetlayout_loc)
            except:
                log.info("第 %s 次点击Reset layout失败" % r)
                time.sleep(2)
                r += 1
            else:
                self.workorder.click(self.workorder.resetcheck_loc)
                time.sleep(3)
                break


    def layout_setting(self):
        log.info('开始测试Layout设置......')
        time.sleep(2)
        if not self.workorder.is_clickable(self.workorder.addbutton_loc):
            self.refresh()
        self.reset_layout()
        time.sleep(3)
        s = 1
        while s <= 3:
            try:
                self.workorder.click(self.workorder.layout_loc)
            except:
                log.info("第 %s 次打开Layout设置窗口失败，重试" % s)
                time.sleep(2)
                s += 1
            else:
                log.info("第 %s 次打开Layout设置窗口成功-----" % s)
                time.sleep(3)
                self.workorder.click(self.workorder.firstcolumn_loc)
                self.workorder.send_keys(self.workorder.firstcolumninput_loc, 'WO No.')
                self.workorder.click(self.workorder.secondcolumnselect_loc)
                self.workorder.click(self.workorder.layoutokbutton_loc)
                time.sleep(3)
                break

        '''
        1021版本改了对象的位置,已注释的是原位置 -- 曾良均 2021.10.22
        headers = self.driver.find_elements_by_xpath(".//*[@id='workorderlist']/div/div/table/tr[1]/th")
        '''

    def verify_layoutset(self):
        self.layout_setting()
        headers = self.driver.find_elements_by_xpath(".//*[@id='workorderlist']/div/table/tbody/tr[1]/th")
        columnnames = []
        for header in headers:
            if header.get_attribute('textContent') == '':
                pass
            else:
                columnnames.append(header.get_attribute('textContent'))

        if columnnames[0] == 'WO No.' and columnnames[1] == 'Assigned To':
            return True
        else:
            return False


    def view_maintenancerecord(self):
        self.reset_layout()
        time.sleep(2)
        if not self.workorder.is_clickable(self.workorder.addbutton_loc):
            self.refresh()
        log.info('-----测试Maintenance Record显示')
        time.sleep(2)
        self.workorder.click(self.workorder.maintenancerecord_loc)
        time.sleep(5)
        wonumber = self.workorder.get_text(self.workorder.firstcell_loc)
        descrip = self.workorder.get_text(self.workorder.fifthcell_loc)

        if wonumber == '' and descrip != '':
            self.workorder.click(self.workorder.maintenancerecord_loc)
            time.sleep(3)
            return True
        else:
            self.workorder.click(self.workorder.maintenancerecord_loc)
            time.sleep(3)
            return False

    def modify_completed(self):
        self.reset_layout()
        time.sleep(2)
        if not self.workorder.is_clickable(self.workorder.addbutton_loc):
            self.refresh()
        log.info('-----测试修改Status')
        time.sleep(2)
        while True:
            try:
                self.workorder.send_keys(self.workorder.inputtext_loc, desc)
                self.workorder.click(self.workorder.searchbutton_loc)
                time.sleep(3)
                self.workorder.click(self.workorder.wonumber_loc)
                self.workorder.click(self.workorder.wonumber_loc)
                self.workorder.select_by_text(self.workorder.statuscol_loc, 'Completed')
                self.workorder.click(self.workorder.statuschangeok_loc)
            except:
                log.info("-----修改Completed状态失败-----")
                break
            else:
                log.info("-----修改Completed状态完成，结果待验证-----")

                loc = "//*[@id='workorderlist']/div/div[1]/div/table/tbody/tr[1]/td[4]/span/div/select"
                element = self.driver.find_element_by_xpath(loc)
                select_value = element.get_attribute('value')
                self.driver.switch_to.default_content()
                self.workorder.switch_to_iframe(self.workorder.iframe_loc)
                time.sleep(2)

                if select_value == '100':
                    return True
                else:
                    return False
                # res = element.value_of_css_property('background-color')
                # if res == 'rgba(34, 195, 73, 1)':
                #    return True
                #else:
                #    return False

    def revert_companylayout(self):
        log.info('-----开始测试重置默认布局')
        if not self.workorder.is_clickable(self.workorder.addbutton_loc):
            self.refresh()
        time.sleep(3)
        try:
            self.workorder.click(self.workorder.layout_loc)
        except:
            log.info("-----打开Layout设置窗口失败-----")
        else:
            log.info("-----打开Layout设置窗口成功-----")
            time.sleep(3)
            self.workorder.click(self.workorder.firstcolumnselect_loc)
            self.workorder.click(self.workorder.secondcolumnselect_loc)
            self.workorder.click(self.workorder.thirdcolumnselect_loc)
            self.workorder.click(self.workorder.fourthcolumnselect_loc)
            self.workorder.click(self.workorder.fifthcolumnselect_loc)
            self.workorder.click(self.workorder.layoutokbutton_loc)
            while True:
                if self.workorder.pageload():
                    time.sleep(1)
                    break
                else:
                    time.sleep(2)
                    log.info("页面未加载完，继续等待...")
                    continue
            time.sleep(3)

            loc1 = '//*[@id="workorderlist"]/div/table/tbody/tr/th[1]/div[1]/span'
            res1 = self.driver.find_element_by_xpath(loc1).get_attribute('textContent')

            if res1 == 'Asset':
                log.info("-----修改Layout设置成功-----")
                tis = 1
                while tis <= 3:
                    try:
                        self.workorder.js_execute("document.getElementById('recordcontent').scrollLeft=1000")
                        self.workorder.click(self.workorder.defaultlayout_loc)
                        time.sleep(1)
                        self.workorder.click(self.workorder.resetdefault_loc)
                        time.sleep(2)
                    except:
                        log.info("第 %s 次revert company default layout失败-----" % tis)
                        time.sleep(1)
                        tis += 1
                    else:
                        log.info("第 %s 次revert company default layout完成，结果待验证-----" % tis)
                        self.workorder.js_execute("document.getElementById('recordcontent').scrollLeft=0")
                        time.sleep(2)
                        break

                loc2 = '//*[@id="workorderlist"]/div/table/tbody/tr/th[1]/div[1]/span'
                res2 = self.driver.find_element_by_xpath(loc2).get_attribute('textContent')

                if res2 == 'Work Order Number':
                    log.info("revert company default layout结果验证正确-----")
                    return True
                else:
                    return False
            else:
                log.info("-----修改Layout设置失败-----")
        self.driver.switch_to.default_content()


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


    def test04_layoutsetting(self):
        '''设置layout'''
        res = self.verify_layoutset()
        if res:
            log.info("Layout设置测试成功！")
        else:
            log.info("Layout设置测试失败！")
        self.assertTrue(res)


    def test05_viewrecords(self):
        '''查看Maintenance Record'''
        if self.assertTrue(self.view_maintenancerecord()):
            log.info("View Maintenance Record测试失败！")
        else:
            log.info("View Maintenance Record测试成功！")


    @skip_dependon(depend='test03_add_workorder')
    def test06_changestatus(self):
        '''更改WorkOrder状态'''
        if self.assertTrue(self.modify_completed()):
            log.info("完成Work Order测试失败！")
        else:
            log.info("完成Work Order测试成功")



    def test07_revertdefaultlayout(self):
        '''恢复默认Layout'''
        if self.assertTrue(self.revert_companylayout()):
            log.info("完成revert company default layout测试失败！")
        else:
            log.info("完成revert company default layout测试成功！")




if __name__ == '__main__':
    unittest.main()


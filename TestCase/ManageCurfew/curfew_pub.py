# coding:utf-8

import time
from selenium.webdriver.support.select import Select
import sys
from Page.comms import *


class curfew_IronSite():
    """curfew信息封装"""
    def __init__(self, driver):
        """初始化driver"""
        self.driver = driver

    def delete_curfew(self):
        time.sleep(3)
        self.driver.find_element_by_id("searchinputtxt").clear()
        time.sleep(1)
        self.driver.find_element_by_id("searchinputtxt").send_keys("Plan100")
        self.driver.find_element_by_xpath(".//*[@id='content1']/div/div[2]/input[@value='Search']").click()

        # self.driver.exceute_script("window.scrollTo(0,300)")
        time.sleep(2)
        try:
            self.driver.find_element_by_xpath(".//*[@id='curfewlist']/div/div/div/table/tbody/tr[1]/td[5]")
        except:
            sys.stderr.write('没找到可删除的记录')
        else:
            self.driver.find_element_by_xpath(".//*[@id='curfewlist']/div/div/div/table/tbody/tr[1]/td[5]").click()
            time.sleep(2)
            try:
                del_yes = '/html/body/div[@class="dialog popupmsg"]/div[@class="dialog-func"]/input[@value="Yes"]'
                self.driver.find_element_by_xpath(del_yes).click()
            except:
                self.driver.switch_to.default_content()
                del_yes = '/html/body/div[@class="dialog popupmsg"]/div[@class="dialog-func"]/input[@value="Yes"]'
                self.driver.find_element_by_xpath(del_yes).click()
                iframe = self.driver.find_element_by_xpath(".//*[@id='set_right']/iframe")
                self.driver.switch_to.frame(iframe)

            time.sleep(1)


    def open_addwindow(self):
        time.sleep(3)
        iframe = self.driver.find_element_by_xpath(".//*[@id='set_right']/iframe")
        self.driver.switch_to.frame(iframe)
        self.driver.find_element_by_xpath(".//*[@id='content1']/div/div[3]/span[1]").click()
        # sys.stderr.write('打开添加页面\n')
        iframecurfew = self.driver.find_element_by_id("iframecurfew")
        self.driver.switch_to.frame(iframecurfew)
        self.driver.find_element_by_id("dialog_title").send_keys('Plan100')
        self.driver.find_element_by_id("chkMo").click()
        self.driver.find_element_by_id("chkTu").click()
        sh = self.driver.find_element_by_id("starttimehour_2")
        Select(sh).select_by_index(1)
        sm = self.driver.find_element_by_id("starttimeminute_2")
        Select(sm).select_by_value("17")
        seh =self.driver.find_element_by_id("endtimehour_2")
        Select(seh).select_by_value("07")
        sem = self.driver.find_element_by_id("endtimeminute_2")
        Select(sem) .select_by_value("00")
        self.driver.find_element_by_xpath(".//*[@id='tr_addtimepreiod']/td[2]/span").click()
        sh1 = self.driver.find_element_by_id("starttimehour_3")
        Select(sh1).select_by_index(9)
        sm1 = self.driver.find_element_by_id("starttimeminute_3")
        Select(sm1).select_by_value("17")
        seh1 = self.driver.find_element_by_id("endtimehour_3")
        Select(seh1).select_by_value("17")
        sem1 = self.driver.find_element_by_id("endtimeminute_3")
        Select(sem1).select_by_value("00")
        time.sleep(3)
        self.driver.find_element_by_xpath(".//*[@id='content1']/div[2]/div[1]/span[1]").click()
        text = self.driver.find_element_by_xpath("html/body/div[3]/div[2]").text


        self.driver.find_element_by_xpath("html/body/div[3]/div[3]/input").click()
        self.driver.find_element_by_xpath(".//*[@id='content1']/div[2]/div[1]/span[2]").click()
        self.driver.switch_to.default_content()
        time.sleep(1)
        self.driver.switch_to.frame(iframe)
        return text

    def search_curfew(self):
        # sys.stderr.write('搜索Curfew\n')
        time.sleep(2)
        self.driver.find_element_by_id("searchinputtxt").clear()
        self.driver.find_element_by_id("searchinputtxt").send_keys("Plan100")
        time.sleep(2)
        self.driver.find_element_by_xpath(".//*[@id='content1']/div/div[2]/input[@value='Search']").click()
        time.sleep(2)
        try:
            self.driver.find_element_by_xpath(".//*[@id='curfewlist']/div/div/div/table/tbody/tr")
        except:
            return False
        else:
            return True







from operater import browser
from time import sleep
from logger import Log
import os,time
import unittest
from Page.AdminSite.AdminHomePage import AdminHomePage
from Page.AdminSite.CustomerPage import CustomerPage
from Page.AdminSite.Con004DetailPage import Con004DetailPage as C4
from Page.loginpage import LoginPage as LG
from queryMSSQL import *

log = Log()
# 判断保存报告的目录是否存在
path = ".\\report"
isExists = os.path.exists(path)
if not isExists:
    os.mkdir(path)

class AdminDetailTest(unittest.TestCase):
    locationName = 'A1-Loc'

    def time_format(self):
        current_time = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        return current_time

    @classmethod
    def setUpClass(cls):
        # 登录IronIntel站点
        log.info("------开始测试Admin站点相关功能------")
        try:
            n = 0
            while n < 3:
                cls.driver = browser()
                cls.lg = LG(cls.driver)
                if cls.lg.is_visibility(cls.lg.loginB_loc):
                    break
                n += 1
        except:
            log.info('浏览器打开失败')
        else:
            cls.lg.login('zlj@foresight.com', 'Win.12345')  # foresight用户，登录到Admin站点
            # cls.lg.login()   默认为Contractor站点用户 auto@iicon004.com
            cls.driver.implicitly_wait(60)


    @classmethod
    def tearDownClass(cls):
        cls.driver.implicitly_wait(10)
        cls.driver.quit()

    def customerToDetail(self, expect=True):
        log.info("测试登录Admin站点，打开Customer，打开某站点的Detail页")
        sleep(2)
        self.homepage = AdminHomePage(self.driver)
        self.homepage.click_Customers()
        self.driver.implicitly_wait(50)

        # 判断当前页面是不是正确，检查 Manage Customers 是否存在
        self.custpage = CustomerPage(self.driver)
        # self.custpage.SearchSite("00")
        self.custpage.send_keys(self.custpage.SearchInputBox_loc, '00')
        self.custpage.click(self.custpage.SearchButton_loc)
        sleep(3)
        # 截图查看搜索结果
        # self.driver.get_screenshot_as_file(".\\report\\" + self.time_format() + "_Search.png")
        self.driver.implicitly_wait(5)

        result = self.custpage.is_text_in_value(self.custpage.SearchButton_loc, 'Search')
        self.assertEqual(result, expect)
        if self.assertEqual(result, expect):
            log.info("打开Customers页面失败！ ")
            log.info("")
        else:
            log.info("打开Customers页面成功！")
            log.info("")

    def detailSummery(self, expect=True):
        self.custpage = CustomerPage(self.driver)
        self.custpage.SearchSite("001")
        sleep(2)
        self.custpage.click(self.custpage.Search004Detail_loc)
        self.driver.implicitly_wait(60)

        # 跳转到004站点Detail页面
        self.driver.switch_to.window(self.driver.window_handles[1])
        sleep(2)
        self.c004 = C4(self.driver)
        sleep(3)
        log.info("点击收折左边主菜单")
        # //*[@id="nav_arrow"]
        self.driver.find_element_by_xpath('//*[@id="nav_arrow"]').click()
        # self.c004.click(self.c004.ExpButton_loc)
        sleep(1)
        log.info("跳到Summary页面")
        set_frame = self.driver.find_element_by_xpath('//*[@id="set_right"]/iframe')
        self.driver.switch_to.frame(set_frame)
        sleep(2)
        txt = 'Test Add Comments at ' + self.time_format()
        # self.c004.send_keys(self.c004.CommentsInputBox_loc, txt)
        log.info("输入Comments并提交")
        self.c004.inputTo(self.c004.CommentsInputBox_loc, txt)
        self.c004.click(self.c004.CommitComments_loc)
        sleep(2)

        #检查输入的Comments是否正确保存
        comments = self.driver.find_element_by_xpath('//*[@id="divcomments"]/div[1]/div[2]')
        result = (comments.text == txt)
        # self.assertEqual(result, expect) //*[@id="divcomments"]/div[1]/div[2]
        if self.assertEqual(result, expect):
            log.info("测试失败！ ")
            log.info("")
        else:
            log.info("测试成功！")
            log.info("")

    def managelocation(self, expect=True):
        self.c004 = C4(self.driver)
        sleep(3)
        self.driver.switch_to.default_content()
        sleep(2)
        # 点击manage Locations
        self.c004.click(self.c004.locations_loc)
        sleep(2)
        set_frame = self.driver.find_element_by_xpath('//*[@id="set_right"]/iframe')
        self.driver.switch_to.frame(set_frame)
        sleep(2)

        log.info("添加Location")
        self.c004.click(self.c004.Addlocation_loc)
        sleep(2)
        # self.locationName = 'A1-Loc'     # + self.time_format()
        self.c004.inputTo(self.c004.locationnameinbox_loc, self.locationName)
        self.c004.inputTo(self.c004.longinbox_loc, '-85.861413')
        self.c004.inputTo(self.c004.latinbox_loc, '37.254868')
        sleep(1)
        self.c004.click(self.c004.locOkbutton_loc)
        sleep(1)

        self.c004.js_execute("document.getElementById('locationlist').scrollLeft=0")
        sleep(2)
        sortname = self.driver.find_element_by_xpath('//*[@id="locationlist"]/div/table/tbody/tr/th[1]/div')
        sortname.click()
        sleep(2)
        addloc = self.driver.find_element_by_xpath('//*[@id="locationlist"]/div/div/div/table/tbody/tr[1]/td[1]/span')
        result = (addloc.text == self.locationName)
        # self.assertEqual(result, expect)
        if self.assertEqual(result, expect):
            log.info("添加Location失败！ ")
            log.info("---------------------------")
        else:
            log.info("添加Location成功！")
            log.info("---------------------------")

    def deletelocation(self):
        self.c004 = C4(self.driver)
        sleep(3)
        self.driver.switch_to.default_content()
        sleep(2)
        self.c004.click(self.c004.locations_loc)
        self.driver.implicitly_wait(60)
        sleep(2)
        set_frame1 = self.driver.find_element_by_xpath('//*[@id="set_right"]/iframe')
        self.driver.switch_to.frame(set_frame1)
        sleep(2)

        log.info("清除脏数据")
        # 当前因为有 确认删除 窗口，导致只能清除1条数据，
        locations = self.driver.find_elements_by_class_name('data-grid-row')
        for local in locations:
            local1 = local.find_element_by_xpath('.//td[1]/span')
            if local1.text == self.locationName:
                del_loc = local.find_element_by_xpath('.//td[6]')
                del_loc.click()
                delyes_loc = self.driver.find_element_by_xpath('/html/body/div[3]/div[3]/input[2]')
                delyes_loc.click()
                sleep(1)

    def clearTestData(self):
        log.info("清除自动化测试产生的Comments数据")
        dt = 'ironintel'
        sqls = "delete  from SYS_COMPANY_COMMENTS where COMPANYID='IICON_001' and USERIID='20775ABB-0495-4D82-9335-EA03BA25489C'"

        delSQL(dt=dt, sqlstr=sqls)

    def test01_AdminDetail(self):
        '''打开Customer页面，并搜索'''
        log.info("执行测试 - test01_AdminDetail")
        log.info("")
        self.clearTestData()
        time.sleep(2)
        self.customerToDetail()


    def test02_detailSummery(self):
        '''在Summary中添加Comments'''
        log.info("执行测试 - test02_detailSummery")
        log.info("")
        self.detailSummery()


    def test03_ManageLocation(self):
        '''添加一个Location'''
        log.info("执行测试 - test03_ManageLocation")
        log.info("")
        self.deletelocation()
        sleep(3)
        self.managelocation()


if __name__ == "__main__":
    unittest.main()
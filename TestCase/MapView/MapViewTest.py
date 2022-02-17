# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     MapViewTest.py
   Description :
   Author :        曾良均
   QQ:             277099728
   Date：          8/25/2021 10:54 AM
-------------------------------------------------
   Change Activity:
                   8/25/2021: add
                   9/28/2021: 增加不同TestCase间独立性，增强脚本运行容错性
-------------------------------------------------
"""
__author__ = 'ljzeng'

import unittest
from Common.operater import browser
from Page.loginpage import LoginPage as LG
from Page.Maps.MapView import MapView
from Common.logger import Log
import os
from selenium.webdriver.support.ui import WebDriverWait
from Common.skiptest import skip_dependon
from Common.queryMSSQL import *
import datetime


log = Log()
path = ".\\report"
isExists = os.path.exists(path)
if not isExists:
    os.mkdir(path)


class MapViewTest(unittest.TestCase):
    def time_format(self):
        current_time = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        return current_time

    @classmethod
    def setUpClass(cls):
        # 登录IronIntel站点
        cls.driver = browser()
        cls.lg = LG(cls.driver)
        cls.lg.login('autotestmap@iicon004.com', 'Win.12345')  # foresight用户，登录到Admin站点
        # cls.lg.login()   # 默认为Contractor站点用户 auto@iicon004.com
        cls.mv = MapView(cls.driver)
        log.info("Start test Map View functions ... ")
        cls.driver.implicitly_wait(60)
        time.sleep(5)

    @classmethod
    def tearDownClass(cls):
        cls.driver.implicitly_wait(10)
        cls.driver.quit()

    def assetDisplay(self, txt, AsName):
        '''地图机器列表搜索'''
        # log.info("打开地图")
        try:
            times = 0
            while times < 4:
                times += 1
                time.sleep(5)
                log.info("打开地图页面")
                self.mv.click(self.mv.ExButton_loc)
                time.sleep(3)

                if self.mv.is_visibility(self.mv.firstAssetLink_loc):
                    break
                else:
                    log.info('页面元素未加载完成，第 %d 次重试' % times)
                    self.driver.refresh()
                    self.driver.implicitly_wait(60)
        except:
            log.info("打开机器列表失败")
            result = False
        else:
            log.info('开始搜索机器')
            try:
                self.mv.send_keys(self.mv.searchInbox_loc, txt)
                self.mv.click(self.mv.searchButton_loc)
                self.driver.implicitly_wait(60)
                time.sleep(5)
            except:
                log.info("搜索操作失败")
                result = False
            else:
                time.sleep(2)
                assetname = self.mv.get_text(self.mv.firstAssetLink_loc)
                log.info('搜索到第一台机器： %s' % assetname)
                result = (assetname == AsName)

        if result:
            log.info("搜索机器成功")
        else:
            log.info("搜索机器失败")
        self.assertTrue(result)

    def editAsset(self, Assetname):
        '''编辑机器'''
        # log.info("编辑列表中第一台机器")
        self.mv = MapView(self.driver)
        try:
            self.mv.click(self.mv.firstAssetLink_loc)
        except:
            log.info("点击搜索第一台机器失败")
        else:
            self.mv.click(self.mv.editAsset_loc)
            time.sleep(2)
        # 打开机器编辑界面
        try:
            AssetFrame = self.driver.find_element_by_id('iframemachine')
            self.driver.switch_to.frame(AssetFrame)
            time.sleep(2)
        except:
            res = False
            log.info("跳转机器编辑界面失败")
        else:
            time.sleep(4)
            self.mv.send_keys(self.mv.AssetCustomName_loc, Assetname)  #
            self.mv.click(self.mv.AssetSave_loc)
            time.sleep(1)
            txt = self.mv.get_text(self.mv.SaveAssetTxt_loc)
            # log.info("保存提示： %s" % txt)
            res = (txt == 'Saved successfully.')
            self.mv.click(self.mv.SaveAssetOK_loc)
            time.sleep(1)

            self.mv.click(self.mv.AssetSaveandexit_loc)  # 保存并退出
            self.driver.switch_to.default_content()  # 切换回主界面

        if res:
            log.info("编辑机器成功")
        else:
            log.info("编辑机器失败")
        self.assertTrue(res)

    def editJobsite(self):
        # log.info("编辑Jobsite")
        try:
            self.mv.click(self.mv.mapmenu_loc)
            self.driver.implicitly_wait(60)
        except:
            log.info('地图菜单不可点击，刷新再试')
            self.driver.refresh()
            self.driver.implicitly_wait(60)
            time.sleep(5)
            self.mv.click(self.mv.mapmenu_loc)
            self.driver.implicitly_wait(60)
        while True:
            if self.mv.pageload():
                time.sleep(1)
                break
            else:
                time.sleep(2)
                log.info("页面未加载完，继续等待...")
                continue
        time.sleep(2)
        self.driver.implicitly_wait(60)
        self.mv.click(self.mv.ExButton_loc)
        time.sleep(1)
        self.mv.click(self.mv.tabJobsite_loc)  # click Jobsites
        time.sleep(2)

        self.mv.click(self.mv.firstJobsiteLink_loc)

        self.mv.click(self.mv.editJobsite_loc)  # 点击编辑Jobsite
        self.driver.implicitly_wait(60)
        time.sleep(1)

        # log.info("打开编辑Jobsite界面")
        jobsiteFrame = self.driver.find_element_by_id('iframejobsite')
        self.driver.switch_to.frame(jobsiteFrame)
        self.driver.implicitly_wait(60)
        time.sleep(2)

        self.mv.send_keys(self.mv.jobsitecode_loc, self.time_format())
        time.sleep(1)

        self.mv.click(self.mv.jobsiteSave_loc)
        self.driver.implicitly_wait(60)
        time.sleep(1)
        # while not self.mv.is_clickable(self.mv.editjobsiteOK_loc):
        #     time.sleep(2)
        txt = self.mv.get_text(self.mv.editjobsitetxt_loc)
        # log.info("保存Jobsite： %s" %txt)
        self.mv.click(self.mv.editjobsiteOK_loc)
        time.sleep(1)

        self.mv.click(self.mv.jobsiteExit_loc)
        self.driver.switch_to.default_content()
        res = (txt == 'Saved successfully.')
        if res:
            log.info("编辑Jobsite成功")
        else:
            log.info("编辑Jobsite失败")
        self.assertTrue(res)

    def sendJobsiteLocation(self, Mail):
        # log.info("发送Jobsite位置邮件")
        try:
            self.mv.click(self.mv.mapmenu_loc)
            self.driver.implicitly_wait(60)
        except:
            log.info('地图菜单不可点击，刷新再试')
            self.driver.refresh()
            self.driver.implicitly_wait(60)
            time.sleep(5)
            self.mv.click(self.mv.mapmenu_loc)
            self.driver.implicitly_wait(60)
        while True:
            if self.mv.pageload():
                time.sleep(1)
                break
            else:
                time.sleep(2)
                log.info("页面未加载完，继续等待...")
                continue
        time.sleep(2)
        self.driver.implicitly_wait(60)
        self.mv.click(self.mv.ExButton_loc)
        time.sleep(1)
        self.mv.click(self.mv.tabJobsite_loc)  # click Jobsites
        time.sleep(2)

        ci = 1
        while ci <= 3:
            try:
                self.mv.click(self.mv.firstJobsiteLink_loc)
                self.mv.click(self.mv.jobsiteSendmail_loc)
                time.sleep(2)
            except:
                log.info('第 %s 次打开邮件发送窗口失败，重试' % ci)
                ci += 1
            else:
                if self.mv.is_clickable(self.mv.jobsitesendOK_loc):
                    break
        try:
            self.mv.send_keys(self.mv.jobsitesendothermail_loc, Mail)
            self.mv.send_keys(self.mv.jobsitesendDesc_loc, "send Jobsite Location at " + self.time_format())
            self.mv.click(self.mv.jobsitesendOK_loc)

            # 此处的时间为UTC时间，如果当前时区为 +8,则需要减去8小时
            sendtime = datetime.datetime.now()
            sendtime = sendtime - datetime.timedelta(hours=8, minutes=1)
            totime = sendtime + datetime.timedelta(minutes=2)
            sendtime = sendtime.strftime("%Y-%m-%d %H:%M")
            totime = totime.strftime("%Y-%m-%d %H:%M")
            category = 'Asset-LocationMessage'
            time.sleep(2)
            # checksendmail方法用于检查发送的邮件是否正确发送，category为邮件类型，toadd为接收邮件地址
            sqlres = checksendmail(category=category, toadd=Mail, st=sendtime, tt=totime)
        except:
            log.info('邮件发送操作失败')
            return False
        else:
            time.sleep(1)
            txt = self.mv.get_text(self.mv.sendjobsitetxt_loc)
            self.mv.click(self.mv.sendjobsiteOK_loc)
            res = (txt == 'Message sent.')
            return sqlres and res

    def importShape(self, file, expect=True):
        log.info("导入Shape文件")
        try:
            self.mv.click(self.mv.mapmenu_loc)
            self.driver.implicitly_wait(60)
        except:
            log.info('地图菜单不可点击，刷新再试')
            self.driver.refresh()
            self.driver.implicitly_wait(60)
            time.sleep(5)
            self.mv.click(self.mv.mapmenu_loc)
            self.driver.implicitly_wait(60)
        while True:
            if self.mv.pageload():
                time.sleep(1)
                break
            else:
                time.sleep(2)
                log.info("页面未加载完，继续等待...")
                continue
        time.sleep(2)
        self.driver.implicitly_wait(60)
        self.mv.click(self.mv.ExButton_loc)
        time.sleep(1)
        self.mv.click(self.mv.tabShape_loc)  # click Shapes
        time.sleep(2)

        # log.info("点击打开导入Shape窗口")
        self.mv.click(self.mv.importshapefileBtn_loc)
        time.sleep(2)

        # log.info("输入Shape相关信息")
        name = 'TestImportShape' + self.time_format()
        self.mv.send_keys(self.mv.importshapefilename_loc, name)
        # log.info("选择shape文件")
        # 因Input类型的，直接用send keys
        # self.mv.send_keys(self.mv.importshapeButton_loc, file)
        # 也可调用自定义方法
        self.mv.click(self.mv.importshapeButton_loc)
        # 确定可执行文件的绝对路径
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        fpath = os.path.abspath(os.path.join(BASE_DIR, '..\..'))
        time.sleep(3)
        exfile = os.path.join(fpath,'upfile.exe')
        os.system("%s %s" % (exfile, file))
        time.sleep(2)
        self.mv.click(self.mv.importshapefileOK_loc)
        time.sleep(1)

        # 搜索刚导入的Shape，看是否成功导入
        self.mv.send_keys(self.mv.searchShapeinbox_loc, name)
        self.mv.click(self.mv.searchShapeBtn_loc)
        time.sleep(1)

        shapename = self.driver.find_element_by_xpath('//*[@id="shapeList"]/div/a')
        target = shapename.get_attribute("title")  # 获取元素的Title属性值
        res = (target == name)
        if self.assertEqual(res, expect):
            log.info("Import Failer")
        else:
            log.info("Import successfully")

    def clearImShape(self):
        # log.info("清除导入Shape的文件")
        try:
            self.mv.click(self.mv.mapmenu_loc)
            self.driver.implicitly_wait(60)
        except:
            log.info('地图菜单不可点击，刷新再试')
            self.driver.refresh()
            self.driver.implicitly_wait(60)
            time.sleep(5)
            self.mv.click(self.mv.mapmenu_loc)
            self.driver.implicitly_wait(60)
        time.sleep(2)
        self.driver.implicitly_wait(60)
        self.mv.click(self.mv.ExButton_loc)
        time.sleep(1)
        self.mv.click(self.mv.tabShape_loc)  # click Shapes
        time.sleep(2)

        self.mv.send_keys(self.mv.searchShapeinbox_loc, 'TestImportShape')
        self.mv.click(self.mv.searchShapeBtn_loc)
        time.sleep(2)

        try:
            # log.info("开始清除")
            shapelist = self.driver.find_element_by_id('shapeList')
            tmp = 0
            shapes = shapelist.find_elements_by_class_name('machineitem')

            # 用while判断是否有Shape文件，有则删除，并统计删除的文件
            while shapes:
                shapes[0].find_element_by_xpath('./span').click()
                time.sleep(1)
                self.driver.find_element_by_xpath('/html/body/div[@class="dialog popupmsg"]/div[3]/input[2]').click()
                time.sleep(1)
                tmp += 1
                # log.info("清除第 %d 个导入的测试Shape文件。" % tmp)
        except:
            log.info('已清空导入的Shape文件')

    def routeNavigation(self, expect=True):
        try:
            self.mv.click(self.mv.mapmenu_loc)
            self.driver.implicitly_wait(60)
        except:
            log.info('地图菜单不可点击，刷新再试')
            self.driver.refresh()
            self.driver.implicitly_wait(60)
            time.sleep(5)
            self.mv.click(self.mv.mapmenu_loc)
            self.driver.implicitly_wait(60)
        while True:
            if self.mv.pageload():
                time.sleep(1)
                break
            else:
                time.sleep(2)
                log.info("页面未加载完，继续等待...")
                continue
        self.driver.implicitly_wait(60)
        time.sleep(2)

        log.info("Test Route Navigation")
        try:
            self.mv.click(self.mv.routenaviBg_loc)
            time.sleep(1)
        except:
            res = False
            log.info("没有路径优化功能")
        else:
            # log.info("open Route Navigation Successfully")
            try:
                self.mv.click(self.mv.addlocation_loc)
                time.sleep(2)
                retry = 0
                # log.info("input start location")
                while retry <= 3:
                    self.mv.send_keys(self.mv.startlocation_loc, 'Riverside')
                    time.sleep(2)
                    self.mv.click(self.mv.startFir_loc)
                    time.sleep(1)

                    # log.info("input middle location")
                    self.mv.send_keys(self.mv.midlocation_loc, 'Perris, California')
                    time.sleep(2)
                    self.mv.click(self.mv.midFir_loc)
                    time.sleep(1)

                    # log.info("input end location")
                    self.mv.send_keys(self.mv.endlocation_loc, 'Escondido, California')
                    time.sleep(2)
                    self.mv.click(self.mv.endFir_loc)
                    time.sleep(1)

                    # log.info("click get directions")
                    self.mv.click(self.mv.getDirection_loc)
                    self.driver.implicitly_wait(30)
                    time.sleep(5)

                    ExcpOk = ('xpath', '/html/body/div[@class="dialog popupmsg"]/div[@class="dialog-func"]/input')
                    if self.mv.is_invisibility(ExcpOk):    #  如果对象不存在，则走下一步流程
                        break
                    else:
                        self.mv.click(ExcpOk)
                        retry += 1

            except:
                log.info("input location fail")
                res = False
            else:
                # log.info("send route")
                try:
                    time.sleep(2)
                    self.mv.click(self.mv.routefaMail_loc)
                except:
                    log.info("Open Send Route Fail")
                    res = False
                else:
                    time.sleep(2)
                    # log.info("input other address")
                    self.mv.send_keys(self.mv.SROAddress_loc, 'zljun8210@live.cn')
                    time.sleep(1)
                    self.mv.send_keys(self.mv.SRDescription_loc, 'Send Route Navigations at %s' % self.time_format())
                    time.sleep(1)
                    # log.info("click OK , send route information")
                    self.mv.click(self.mv.SROKButton_loc)
                    time.sleep(1)

                    # log.info("send route result")
                    txt = self.mv.get_text(self.mv.SRMessage_loc)
                    self.mv.click(self.mv.SRMessageOk_loc)
                    res = (txt == 'Message sent.')
                    if res:
                        log.info("Route Navigation Test Successfully!")
            self.mv.click(self.mv.routenaviBg_loc)
        self.assertEqual(res, expect)

    def search_asset(self, txt, AName):
        try:
            self.mv.click(self.mv.mapmenu_loc)
            self.driver.implicitly_wait(60)
        except:
            log.info('地图菜单不可点击，刷新再试')
            self.driver.refresh()
            self.driver.implicitly_wait(60)
            time.sleep(5)
            self.mv.click(self.mv.mapmenu_loc)
            self.driver.implicitly_wait(60)
        while True:
            if self.mv.pageload():
                time.sleep(1)
                break
            else:
                time.sleep(2)
                log.info("页面未加载完，继续等待...")
                continue
        self.driver.implicitly_wait(60)
        try:
            self.mv.waitClick(self.mv.ExButton_loc)
        except:
            log.info("打开机器列表失败")
            return False
        else:
            self.mv.click(self.mv.ExButton_loc)
            time.sleep(1)
            try:
                self.mv.waitClick(self.mv.firstAssetLink_loc)
                time.sleep(2)
            except:
                log.info('没有机器数据')
                return False
            else:
                self.mv.send_keys(self.mv.searchInbox_loc, txt)     #  '176415'
                self.mv.click(self.mv.searchButton_loc)
                time.sleep(5)
                assetname = self.mv.get_text(self.mv.firstAssetLink_loc)

            if assetname == AName:
                return True

    def Asset_Trip_Report(self):
        time.sleep(1)
        self.mv.click(self.mv.firstAssetLink_loc)
        time.sleep(1)
        try:
            self.mv.click(self.mv.firstAssetLocationHistory_loc)
            time.sleep(1)
        except:
                log.info('打开History')
                res = False
        else:
            try:
                self.mv.send_keys(self.mv.dateFrom_loc, '10/20/2021')
                self.mv.send_keys(self.mv.dateTo_loc, '10/27/2021')
                time.sleep(1)
                self.mv.click(self.mv.TripReport_loc)
                time.sleep(1)
            except:
                log.info('录入时间及打开TripReport操作失败')
                res = False
            else:
                reports = self.mv.find_elements(self.mv.TripReports_loc)
                time.sleep(2)
                if reports:
                    res = True
                else:
                    log.info("没有Report记录数据")
                    res = False
                self.mv.click(self.mv.closeTrip_loc)
        return res



    def test01_SearchanddisplayAssets(self):
        '''测试在左侧机器列表中搜索机器'''
        serchtxt = "josh's"
        AssetName = "Josh's Truck - CalAmp"
        self.assetDisplay(txt=serchtxt, AsName=AssetName)

    @skip_dependon(depend="test01_SearchanddisplayAssets")
    def test02_editAssets(self):
        '''编辑Assets'''
        AssetName = "Josh's Truck - CalAmp"
        self.editAsset(Assetname=AssetName)

    def test03_editJobsites(self):
        '''编辑Jobsite'''
        self.editJobsite()

    def test04_sendjobsitelocation(self):
        '''发送Jobsite位置邮件测试'''
        email = 'zljun8210@163.com'
        result = self.sendJobsiteLocation(Mail=email)
        if result:
            log.info('发送Jobsite位置邮件成功')
        else:
            log.info('发送Jobsite位置失败')
        self.assertTrue(result)

    def test05_importshapefile(self):
        '''测试导入Shape文件'''
        # 清除脏数据
        self.clearImShape()
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        fpath = os.path.abspath(os.path.join(BASE_DIR, '..\..'))
        file = os.path.join(fpath, 'TestData\\testkmzs.kmz')
        time.sleep(1)
        self.importShape(file=file)

    def test06_routeNavigation(self):
        '''测试路径优化功能'''
        self.routeNavigation()

    def test07_AssetTripReport(self):
        '''测试查看机器历史轨迹及TripReport'''
        asset = '176415'
        assetname = 'CHARGEWAGON'
        searchs = self.search_asset(asset,assetname)
        if searchs:
            re = self.Asset_Trip_Report()
        else:
            re = False
        self.assertTrue(re)

if __name__ == '__main__':
    unittest.main()

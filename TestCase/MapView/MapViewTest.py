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

import time
import unittest
from operater import browser
from Page.loginpage import LoginPage as LG
from Page.Maps.MapView import MapView
from logger import Log
import os
from selenium.webdriver.support.ui import WebDriverWait
from skiptest import skip_dependon
from queryMSSQL import *
import datetime

log = Log()
path = ".\\report"
isExists = os.path.exists(path)
if not isExists:
    os.mkdir(path)


class MapViewTest(unittest.TestCase):
    lg = None
    driver = None

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

    def loadPages(self):
        try:
            self.mv.click(self.mv.mapmenu_loc)
            self.driver.implicitly_wait(60)
        except Exception as e:
            log.info('地图菜单不可点击，刷新再试')
            self.driver.refresh()
            time.sleep(3)
            while True:
                try:
                    self.mv.click(self.mv.mapmenu_loc)
                    time.sleep(2)
                except Exception as e:
                    time.sleep(2)
                    continue
                else:
                    break

    def assetDisplay(self, txt, AsName):
        """地图机器列表搜索"""
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
        except Exception as e:
            log.info("打开机器列表失败")
            result = False
        else:
            log.info('开始搜索机器')
            try:
                self.mv.send_keys(self.mv.searchInbox_loc, txt)
                self.mv.click(self.mv.searchButton_loc)
                self.driver.implicitly_wait(60)
                time.sleep(5)
            except Exception as e:
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
        """编辑机器"""
        self.loadPages()
        while True:
            try:
                self.mv.click(self.mv.ExButton_loc)
                time.sleep(3)
            except Exception as e:
                log.info('展开失败，1秒后重试')
                time.sleep(1)
                continue
            else:
                break
        try:
            log.info('搜索指定机器')
            self.mv.send_keys(self.mv.searchInbox_loc, "Josh's Truck - CalAmp")
            self.mv.click(self.mv.searchButton_loc)
            time.sleep(2)
            self.mv.click(self.mv.firstAssetLink_loc)
            time.sleep(3)
            self.mv.click(self.mv.firstAssetLink_loc)
        except Exception as e:
            log.info("点击第一台机器失败")
        else:
            self.mv.click(self.mv.editAsset_loc)
            time.sleep(2)
        # 打开机器编辑界面
        time.sleep(3)
        try:
            assetframe = self.driver.find_element_by_id('iframemachine')
            self.driver.switch_to.frame(assetframe)
            time.sleep(2)
            self.mv.click(self.mv.AssetCustomName_loc)
            time.sleep(2)
        except Exception as e:
            res = False
            log.info("跳转机器编辑界面失败")
        else:
            time.sleep(1)
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
        self.loadPages()
        while True:
            try:
                self.mv.click(self.mv.ExButton_loc)
                time.sleep(1)
            except Exception as e:
                time.sleep(2)
                continue
            else:
                break
        try:
            self.mv.click(self.mv.tabJobsite_loc)  # click Jobsites
            time.sleep(2)
            self.mv.click(self.mv.firstJobsiteLink_loc)
        except Exception as e:
            log.info('click first jobsite failed')
        else:
            self.mv.click(self.mv.editJobsite_loc)  # 点击编辑Jobsite
            time.sleep(1)

            # log.info("打开编辑Jobsite界面")
            jobsiteFrame = self.driver.find_element_by_id('iframejobsite')
            self.driver.switch_to.frame(jobsiteFrame)
            self.driver.implicitly_wait(60)
            time.sleep(2)

            self.mv.send_keys(self.mv.jobsitecode_loc, self.time_format())
            time.sleep(1)
        r = 0
        txt = ''
        while r < 3:
            try:
                self.mv.click(self.mv.jobsiteSave_loc)
                self.driver.implicitly_wait(60)
                time.sleep(1)
                txt = self.mv.get_text(self.mv.editjobsitetxt_loc)
                self.mv.click(self.mv.editjobsiteOK_loc)
                time.sleep(1)
                break
            except Exception as e:
                r += 1
                log.info('编辑操作失败，第%d 次重试！' % r)
                time.sleep(2)
                continue

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
        self.loadPages()
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
            except Exception as e:
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
        except Exception as e:
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
        self.loadPages()
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
        exfile = os.path.join(fpath, 'upfile.exe')
        os.system("%s %s" % (exfile, file))
        time.sleep(2)
        self.mv.click(self.mv.importshapefileOK_loc)
        time.sleep(1)

        # 搜索刚导入的Shape，看是否成功导入
        res = False
        t = 0
        while t < 3:
            try:
                self.mv.send_keys(self.mv.searchShapeinbox_loc, name)
                self.mv.click(self.mv.searchShapeBtn_loc)
                time.sleep(1)
            except Exception:
                t += 1
                time.sleep(2)
                continue
            else:
                shapename = self.driver.find_element_by_xpath('//*[@id="shapeList"]/div/a')
                target = shapename.get_attribute("title")  # 获取元素的Title属性值
                res = (target == name)
                break
        if self.assertEqual(res, expect):
            log.info("Import Failer")
        else:
            log.info("Import successfully")

    def clearImShape(self):
        # log.info("清除导入Shape的文件")
        self.loadPages()
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
        except Exception as e:
            log.info('已清空导入的Shape文件')

    def routeNavigation(self, n=3, expect=True):
        self.loadPages()
        time.sleep(2)
        res = False

        try:
            self.mv.click(self.mv.routenaviBg_loc)
            time.sleep(1)
            log.info("Test Route Navigation")
        except Exception as e:
            res = False
            log.info("没有路径优化功能")
        else:
            # log.info("open Route Navigation Successfully")
            try:
                retry = 0
                # log.info("input start location")
                while retry <= 3:
                    self.mv.click(self.mv.addlocation_loc)
                    time.sleep(2)

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
                    if self.mv.is_invisibility(ExcpOk):  # 如果对象不存在，则走下一步流程
                        break
                    else:
                        self.mv.click(ExcpOk)
                        retry += 1

            except Exception as e:
                if n == 0:
                    res = False
                else:
                    log.info("input location fail, try agin...")
                    num = n - 1
                    self.routeNavigation(n=num)
            else:
                # log.info("send route")
                try:
                    time.sleep(2)
                    self.mv.click(self.mv.routefaMail_loc)
                except Exception as e:
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
        self.loadPages()
        time.sleep(1)
        try:
            self.mv.waitClick(self.mv.ExButton_loc)
        except Exception as e:
            log.info("打开机器列表失败")
            return False
        else:
            self.mv.click(self.mv.ExButton_loc)
            time.sleep(1)
            try:
                self.mv.waitClick(self.mv.firstAssetLink_loc)
                time.sleep(2)
            except Exception as e:
                log.info('没有机器数据')
                return False
            else:
                self.mv.send_keys(self.mv.searchInbox_loc, txt)  # '176415'
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
        except Exception as e:
            log.info('打开History失败')
            res = False
        else:
            try:
                self.mv.send_keys(self.mv.dateFrom_loc, '10/20/2021')
                self.mv.send_keys(self.mv.dateTo_loc, '10/27/2021')
                time.sleep(1)
                self.mv.click(self.mv.TripReport_loc)
                time.sleep(1)
            except Exception as e:
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

    def theft_mode(self):
        time.sleep(1)
        self.mv.click(self.mv.firstAssetLink_loc)
        time.sleep(1)
        try:
            self.mv.click(self.mv.firstAssetLocationHistory_loc)
            time.sleep(1)
        except Exception as e:
            log.info('打开History失败')
            return False
        else:
            try:
                self.mv.send_keys(self.mv.dateFrom_loc, '12/24/2023')
                self.mv.send_keys(self.mv.dateTo_loc, '12/25/2023')
                time.sleep(1)
                self.mv.click(self.mv.theft_mode_btn)
                time.sleep(1)
            except Exception as e:
                log.info('录入时间及打开Theft Mode操作失败')
                return False
            else:
                if self.mv.is_selected(self.mv.theft_sec_checkbox_loc):
                    return True
                time.sleep(1)
                self.mv.click(self.mv.theft_mode_close_btn)

    def viewTimelines(self):
        # 查看TimeLine功能
        self.loadPages()
        time.sleep(2)
        self.mv.click(self.mv.ExButton_loc)
        time.sleep(1)
        log.info('开始测试TimeLine功能')
        # 页面加载完成后，设置Map Layer为None,左侧搜索界面点击 Show All，再点击打开TimeLine界面
        self.mv.select_by_text(self.mv.mapLayer_loc, '(None)')
        time.sleep(1)
        self.mv.click(self.mv.showAll_loc)
        time.sleep(3)
        try:
            self.mv.click(self.mv.timeLineBtn_loc)
            time.sleep(2)
            timelineframe = self.driver.find_element_by_id('iftimelineview')
            self.driver.switch_to.frame(timelineframe)
        except Exception as e:
            log.info('打开TimeLine失败')
            return False
        else:
            self.mv.send_keys(self.mv.timeSelect_loc, '10/21/2018')
            self.mv.click(self.mv.timeRefreshBtn_loc)
            self.driver.implicitly_wait(60)
            time.sleep(5)

            datas = self.driver.find_element_by_id('asset-ids')
            data = datas.find_elements_by_xpath('tr')
            dataCount = len(data)
            if data:
                log.info('当前日期有 %d 台机器' % dataCount)
                return True
            else:
                log.info('没有机器数据')
                return False

    def exportTimeline(self):
        # 导出操作须在 ViewTimeLine通过后执行
        time.sleep(3)
        log.info('测试导出TimeLine功能')
        self.mv.click(self.mv.utilizationTab)
        # 获取有多少条数据
        assetgrid = self.driver.find_element_by_xpath('//*[@id="tab_grid"]/div/div[1]/div/table/tbody')
        assets = assetgrid.find_elements_by_xpath('tr')
        assetcounts = len(assets) - 1
        log.info('页面显示有 %d 条数据' % assetcounts)
        # 下载
        try:
            self.mv.click(self.mv.timeLineExport_loc)
            time.sleep(10)
            # 判断下载的文件是否存在
            import pathlib
            BASE_DIR = os.path.dirname(os.path.abspath(__file__))
            fpath = os.path.abspath(os.path.join(BASE_DIR, '..\\..'))
            exfile = os.path.join(fpath, r'.\report\Time+Line.xlsx')
            exportfile = pathlib.Path(exfile)
            log.info('下载文件： %s' % exportfile)
            if exportfile.exists():
                # 调用读取数据
                from excel import excel
                datas = excel.get_rows(exportfile)
                # 有效数据须减去前3行（标题行）和最后一行（合计行）
                datas = datas - 4
                # 保留下载的文件
                # os.system('del %s' % exportfile)
                if datas == assetcounts:
                    log.info('导出TimeLine数据到Excel正确')
                    return True
                else:
                    log.info('导出后数据不正确')
                    return False
            else:
                log.info('导出文件不存在')
                return False
        except Exception as e:
            log.info('导出失败')
            return False
        finally:
            # 关闭TimeLine
            log.info('关闭TimeLine，恢复Map layer')
            self.driver.refresh()
            time.sleep(2)
            self.mv.select_by_text(self.mv.mapLayer_loc, 'AutoTests')
            time.sleep(1)

    def test01_SearchanddisplayAssets(self):
        """测试在左侧机器列表中搜索机器"""
        serchtxt = "Josh's Truck - CalAmp"
        AssetName = "Josh's Truck - CalAmp"
        self.assetDisplay(txt=serchtxt, AsName=AssetName)

    @skip_dependon(depend="test01_SearchanddisplayAssets")
    def test02_editAssets(self):
        """编辑Assets"""
        AssetName = "Josh's Truck - CalAmp"
        self.editAsset(Assetname=AssetName)

    def test03_editJobsites(self):
        """编辑Jobsite"""
        self.editJobsite()

    def test04_sendjobsitelocation(self):
        """发送Jobsite位置邮件测试"""
        email = 'zljun8210@163.com'
        result = self.sendJobsiteLocation(Mail=email)
        if result:
            log.info('发送Jobsite位置邮件成功')
        else:
            log.info('发送Jobsite位置失败')
        self.assertTrue(result)

    def test05_importshapefile(self):
        """测试导入Shape文件"""
        # 清除脏数据
        self.clearImShape()
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        fpath = os.path.abspath(os.path.join(BASE_DIR, '..\..'))
        file = os.path.join(fpath, 'TestData\\testkmzs.kmz')
        time.sleep(1)
        self.importShape(file=file)

    def test06_routeNavigation(self):
        """测试路径优化功能"""
        self.routeNavigation()

    def test07_AssetTripReport(self):
        """测试查看机器历史轨迹及TripReport"""
        asset = 'CANDICED2018'  # '176415'
        assetname = 'CHARGEWAGON'
        searchs = self.search_asset(asset, assetname)
        if searchs:
            log.info('已找到机器，开始验证Trip Report功能。')
            re = self.Asset_Trip_Report()
        else:
            re = False
            log.info('没有找到机器.')
        self.assertTrue(re)

    def test08_test_theft_mode(self):
        """测试Theft Mode功能"""
        asset = '1FTEW1EP3GKF833212'
        assetname = '33212-Theft Mode'
        if self.search_asset(asset, assetname):
            log.info('已找到机器，开始测试Theft Mode功能！')
            res = self.theft_mode()
        else:
            log.info('没找到机器！')
            res = False
        self.assertTrue(res)

    def test09_ViewTimeLines(self):
        """测试TimeLine功能"""
        res = self.viewTimelines()
        if res:
            log.info('TimeLine功能测试成功')
        else:
            log.info('TimeLine功能测试失败')
        self.assertTrue(res)

    @skip_dependon(depend='test09_ViewTimeLines')
    def test10_ExportTimeline(self):
        """测试导出TimeLine功能"""
        res = self.exportTimeline()
        if res:
            log.info('Timeline导出成功')
        else:
            log.info('TimeLine导出失败')
        self.assertTrue(res)


if __name__ == '__main__':
    unittest.main()

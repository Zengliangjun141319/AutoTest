# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     ManageJobSitesTest.py
   Description :   测试Jobsite的添加、导入、Layout设置
   Author :        姜丽丽
-------------------------------------------------
"""
from Common.operater import browser
from Page.AssetSchdulingAndDispaching.ManageJobsitePage import ManageJobsitePage
from Page.loginpage import LoginPage
from Common.logger import Log
from ddt import ddt,data
from Common.excel import excel
import os
import unittest
import time

log = Log()
path = '.\\report'
if not os.path.exists(path):
    os.mkdir(path)

file_path = "TestData\JobSitesData.xls"
testData = excel.get_list(file_path)

@ddt
class ManageJobSitesTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        log.info('----开始测试Jobsite管理----')
        cls.driver = browser()
        cls.log = LoginPage(cls.driver)
        cls.log.login('atjobsite@iicon006.com','Win.12345')
        cls.to_frame(cls)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def to_frame(self):
        #
        try:
            n = 0
            while n < 3:
                self.jobsite = ManageJobsitePage(self.driver)
                self.driver.implicitly_wait(60)
                time.sleep(5)
                # 已设置此测试用户只有Jobsite权限，且登录页默认为Jobsite
                # self.jobsite.click(self.jobsite.dispatchmenu_loc)
                # time.sleep(2)
                # self.jobsite.click(self.jobsite.jobsiteManage_loc)
                # time.sleep(2)
                if self.jobsite.is_visibility(self.jobsite.iframe_loc):
                    break
                n += 1
        except:
            log.info('--------打开Jobsites列表失败！--------')
        else:
            log.info('--------打开Jobsites列表成功！--------')
            self.jobsite.switch_to_iframe(self.jobsite.iframe_loc)
            time.sleep(3)

    def search_and_delete(self):
        '''搜索并删除已存在的Jobsites'''
        log.info("搜索并删除带有AutoTest的测试数据")
        self.reset_layout()
        self.jobsite.search('AutoTest')
        try:
            table = self.driver.find_element_by_class_name('data-grid-body-content')
        except:
            log.info('没找到对象')
            return False
        else:
            trs = table.find_elements_by_tag_name('tr')
            trNum = len(trs)
            self.jobsite.js_execute("window.scrollTo(0,300)")
            for i in range(1, trNum+1):
                time.sleep(1)
                try:
                    self.jobsite.click(self.jobsite.deleteBtn_loc)    #  //*[@id="jobsitelist"]/div/div[1]/div/table/tbody/tr[2]/td[26]/a
                    time.sleep(1)
                except:
                    log.info('没有可删除的数据')
                else:
                    self.jobsite.click(self.jobsite.deleteDialogOkBtn_loc)
                    time.sleep(1)
                    log.info('---已删除第 %s 条记录' % i)
            log.info('----删除已存在的相同记录！----')
            return True

    def input_jobsite_information(self, data):
        if not self.jobsite.is_clickable(self.jobsite.addBtn_loc):
            log.info('添加按钮不可点击，刷新页面！')
            self.driver.refresh()
            self.driver.implicitly_wait(60)
            time.sleep(2)
            self.jobsite.switch_to_iframe(self.jobsite.iframe_loc)
        log.info('----测试：  %s' % data['casename'])
        try:
            self.jobsite.click(self.jobsite.addBtn_loc)
            self.jobsite.switch_to_iframe(self.jobsite.jobsiteiframe_loc)
        except:
            log.info('--------打开Jobsite添加页面失败！！--------')
        else:
            # log.info('--------打开Jobsite添加页面，开始输入信息--------')
            time.sleep(5)
            self.jobsite.send_keys(self.jobsite.name_loc, data['name'])
            self.jobsite.select_by_text(self.jobsite.type_loc, data['type'])
            # Region改为下拉方式,取消Region输入
            self.jobsite.select_by_text(self.jobsite.region_loc,  data['region'])
            self.jobsite.send_keys(self.jobsite.number_loc, data['number'])
            self.jobsite.send_keys(self.jobsite.code_loc, data['code'])
            self.jobsite.send_keys(self.jobsite.latitude_loc, str(data['Latitude']))
            self.jobsite.send_keys(self.jobsite.longitude_loc, str(data['Longitude']))
            self.jobsite.send_keys(self.jobsite.radius_loc, str(data['Radius']))
            time.sleep(3)

    def save_jobsite(self):
        try:
            self.jobsite.click(self.jobsite.saveBtn_loc)
            time.sleep(3)
            self.msg = self.jobsite.get_text(self.jobsite.saveDialog_loc)
            self.jobsite.click(self.jobsite.saveDialogOkBtn_loc)
        except:
            log.info('-----保存Jobsite失败！！-----')
        else:
            # log.info('-----完成保存操作，是否添加成功待验证！-----')
            time.sleep(1)
            self.jobsite.click(self.jobsite.exitWithoutSavingBtn_loc)
            time.sleep(1)
            self.driver.switch_to.default_content()
            time.sleep(1)
            self.jobsite.switch_to_iframe(self.jobsite.iframe_loc)

    def import_jobsite(self,file):
        self.driver.refresh()
        self.driver.implicitly_wait(60)
        time.sleep(5)
        self.driver.switch_to.default_content()
        while True:
            if self.jobsite.pageload():
                time.sleep(1)
                break
            else:
                time.sleep(2)
                log.info("页面未加载完，继续等待...")
                continue
        time.sleep(1)
        self.jobsite.switch_to_iframe(self.jobsite.iframe_loc)
        time.sleep(2)
        try:
            self.jobsite.click(self.jobsite.importBtn_loc)
        except:
            log.info('--------打开Import Jobsite窗口失败！--------')
        else:
            log.info('--------成功打开Import Jobsite窗口！--------')
            time.sleep(2)
            # 确定可执行文件的绝对路径
            BASE_DIR = os.path.dirname(os.path.abspath(__file__))
            fpath = os.path.abspath(os.path.join(BASE_DIR, '..\..'))
            time.sleep(3)
            exfile = os.path.join(fpath, 'upfile.exe')
            try:
                os.system("%s %s" % (exfile, file))
                # os.system("upfile.exe %s" %file)
            except:
                log.info('--------上传附件失败！--------')
            else:
                # log.info('--------上传附件成功！--------')
                self.jobsite.click(self.jobsite.matchOKBtn_loc)
                time.sleep(1)
                self.jobsite.click(self.jobsite.importOKBtn_loc)
                time.sleep(1)

        # # 搜索刚导入的jobsite，看是否成功导入
        # self.jobsite.send_keys(self.jobsite.searchInbox_loc, 'AutoTest001')
        # self.jobsite.click(self.jobsite.searchButton_loc)
        # time.sleep(1)
        #
        # target = self.jobsite.get_text(self.jobsite.td1_loc) # 获取元素的Title属性值
        #
        # if target == 'AutoTest001':
        #     return True
        # else:
        #     return False

    def search_and_verify(self, jobsite):
        # 搜索并遍历table查找jobsite是否存在
        time.sleep(1)
        self.jobsite.search(jobsite)
        try:
            table = self.driver.find_element_by_class_name('data-grid-body-content')
            time.sleep(1)
        except:
            return False
        else:
            rows = table.find_elements_by_tag_name('tr')
            rowNum = len(rows)
            for i in range(0, rowNum):
                row = rows[i]
                cols = row.find_elements_by_tag_name('td')
                colNum = len(cols)
                for j in range(0, colNum):
                    txt = cols[j].text
                    if txt == jobsite:
                        return True
                    else:
                        return False

    def set_layout(self):
        self.driver.refresh()
        self.driver.implicitly_wait(60)
        time.sleep(3)
        self.jobsite.switch_to_iframe(self.jobsite.iframe_loc)
        # 先刷新页面
        try:
            time.sleep(3)
            self.jobsite.click(self.jobsite.refreshBtn_loc)
        except:
            log.info('页面不能刷新，等待3秒')
            time.sleep(3)
        else:
            log.info('正在刷新列表数据')
            time.sleep(2)
        try:

            self.jobsite.click(self.jobsite.layoutBtn_loc)
            time.sleep(2)
        except:
            log.info('--------打开Select Columns页面失败！--------')
            return False
        else:
            try:
                self.jobsite.click(self.jobsite.codeLayout_loc)
                self.jobsite.click(self.jobsite.typesLayout_loc)
                self.jobsite.click(self.jobsite.latitudeLayout_loc)
                self.jobsite.click(self.jobsite.longitudeLayout_loc)
                self.jobsite.click(self.jobsite.colorLayout_loc)
                self.jobsite.click(self.jobsite.radiusLayout_loc)
                self.jobsite.click(self.jobsite.bindingtoAssetLayout_loc)
                self.jobsite.click(self.jobsite.foremanLayout_loc)
                self.jobsite.click(self.jobsite.startDateLayout_loc)
                self.jobsite.click(self.jobsite.endDateLayout_loc)
            except:
                log.info('--------选择Layout列失败！--------')
                return False
            else:
                time.sleep(1)
                self.jobsite.click(self.jobsite.layoutOKBtn_loc)
                time.sleep(1)
                nameColText = self.jobsite.get_text(self.jobsite.nameCol_loc)
                regionColText = self.jobsite.get_text(self.jobsite.regionCol_loc)
                numberColText = self.jobsite.get_text(self.jobsite.numberCol_loc)
                if nameColText == 'Name' and regionColText == 'Region' and numberColText == 'Number':
                    log.info('-----设置Layout成功！----')
                    return True
                else:
                    log.info('-----设置Layout失败！----')
                    return False

    def reset_layout(self):
        try:
            self.jobsite.click(self.jobsite.resetLayoutBtn_loc)
            time.sleep(2)
        except:
            self.driver.refresh()
            self.driver.implicitly_wait(60)
            while True:
                if self.jobsite.pageload():
                    time.sleep(1)
                    break
                else:
                    time.sleep(2)
                    log.info("页面未加载完，继续等待...")
                    continue
            self.jobsite.switch_to_iframe(self.jobsite.iframe_loc)
            time.sleep(1)
            self.jobsite.click(self.jobsite.resetLayoutBtn_loc)
            time.sleep(2)
        finally:
            self.jobsite.click(self.jobsite.resetLayoutOKBtn_loc)

    def configuration(self):
        self.driver.refresh()
        self.driver.implicitly_wait(60)
        self.jobsite.switch_to_iframe(self.jobsite.iframe_loc)
        time.sleep(2)
        try:
            time.sleep(2)
            self.jobsite.click(self.jobsite.configurationBtn_loc)
            self.jobsite.switch_to_iframe(self.jobsite.configIframe_loc)
            time.sleep(1)
        except:
            log.info('--------打开Configuration页面失败！--------')
        else:
            log.info('--------打开Configuration页面成功！--------')
            try:
                assetTable = self.driver.find_element('xpath','//*[@id="selectedmachinelist"]/div/div/div/table')
                assetTrs = assetTable.find_elements_by_tag_name('tr')
                if assetTrs:
                    log.info("--------删除已有Assets -------- ")
                    self.jobsite.click(self.jobsite.selectAllAssets_loc)
                    self.jobsite.click(self.jobsite.deleteAssetBtn_loc)
                    time.sleep(3)
                    self.jobsite.click(self.jobsite.deleteAssetYesBtn_loc)
                    time.sleep(1)
                    self.jobsite.click(self.jobsite.deleteAssetDilogOKBtn_loc)
                    time.sleep(2)
                typeTable = self.driver.find_element('xpath','//*[@id="selectedassettypelist"]/div/div/div/table')
                typeTrs = typeTable.find_elements_by_tag_name('tr')
                if typeTrs:
                    log.info("--------删除Asset Types --------")
                    self.jobsite.click(self.jobsite.selectAllAssetTypes_loc)
                    time.sleep(1)
                    self.jobsite.click(self.jobsite.deleteAssetTypeBtn_loc)
                    time.sleep(3)
                    self.jobsite.click(self.jobsite.deleteAssetTypeYesBtn_loc)
                    time.sleep(1)
                    self.jobsite.click(self.jobsite.deleteAssetTypeDilogOKBtn_loc)
                    time.sleep(1)
            except:
                log.info('--------删除已有Configuration设置失败！--------')
            else:
                log.info('--------删除已有Configuration设置成功！--------')
                try:
                    log.info("--------准备添加Assets --------")
                    self.jobsite.click(self.jobsite.addAssetBtn_loc)
                    self.jobsite.click(self.jobsite.assetLoc_loc)
                    self.jobsite.click(self.jobsite.addAssetOKBtn_loc)
                    time.sleep(2)
                    self.jobsite.click(self.jobsite.addAssetDilogOKBtn_loc)
                    time.sleep(1)
                except:
                    log.info('--------在Configuration页面添加机器失败！--------')
                else:
                    log.info('--------在Configuration页面添加机器成功！--------')
                    try:
                        log.info("--------准备添加Asset Type --------")
                        self.jobsite.click(self.jobsite.addAssetTypeBtn_loc)
                        self.jobsite.click(self.jobsite.assetTypeLoc_loc)
                        self.jobsite.click(self.jobsite.addAssetTypeOKBtn_loc)
                        time.sleep(1)
                        self.jobsite.click(self.jobsite.addAssetTypeDilogOKBtn_loc)
                        time.sleep(1)
                    except:
                        log.info('--------在Configuration页面添加机器类型失败！--------')
                    else:
                        log.info('--------在Configuration页面添加机器类型成功！--------')
                        try:
                            self.jobsite.click(self.jobsite.exitBtn_loc)
                        except:
                            log.info('--------Configuration设置失败！--------')
                            return False
                        else:
                            log.info('--------Configuration设置成功！--------')
                            return True

    @data(*testData)
    def test01_add_jobsite(self, data):
        '''测试添加Jobsite'''
        self.input_jobsite_information(data)
        self.save_jobsite()
        if self.msg == data['errmsg']:
            log.info('----已验证Jobsite添加成功！----')
        else:
            log.info('----Jobsite添加失败！----')
        self.assertEqual(self.msg, data['errmsg'])

    def test02_import_jobsite(self):
        '''测试Import功能'''
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        fpath = os.path.abspath(os.path.join(BASE_DIR, '..\..'))
        filename = os.path.join(fpath, r'TestData\importJobsites.xlsx')
        self.import_jobsite(filename)
        res = self.search_and_verify('AutoTestImport001')
        if res == True:
            log.info('-----导入Jobsite成功！----')
        else:
            log.info('-----导入Jobsite失败！----')
        self.assertTrue(res)

    def test03_delete_jobsite(self):
        '''删除添加的Jobsite'''
        res = self.search_and_delete()
        self.assertTrue(res)

    def test04_layout(self):
        '''测试Layout功能'''
        self.reset_layout()
        res = self.set_layout()
        self.assertTrue(res)

    def test05_configuration(self):
        '''测试Configuration功能'''
        res = self.configuration()
        self.assertTrue(res)

if __name__ == "__main__":
    unittest.main()



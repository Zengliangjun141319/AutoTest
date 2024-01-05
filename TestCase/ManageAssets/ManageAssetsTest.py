from Page.ManageAssets.ManageAssetsPage import ManageAssetsPage
from Page.loginpage import LoginPage
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from logger import Log
from operater import browser
from time import sleep
import os
import time
import unittest
import random
from queryMSSQL import delSQL


log = Log()

# 判断保存报告的目录是否存在
path = ".\\report"
isExists = os.path.exists(path)
if not isExists:
    os.mkdir(path)

current_time = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
vin = 'sn' + current_time

class ManageAssetsTest(unittest.TestCase):
    def time_format(self):
        current_time = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        return current_time

    @classmethod
    def setUpClass(cls) -> None:
        # 登录IronIntel站点
        cls.driver = browser()
        cls.logina = LoginPage(cls.driver)
        cls.logina.login('atasset@iicon001.com', 'Win.12345')
        cls.driver.implicitly_wait(10)
        log.info("------ Start test Assets management ------")
        cls.to_frame(cls)

    def to_frame(self):
        sleep(3)
        self.manageassetpage = ManageAssetsPage(self.driver)
        self.driver.implicitly_wait(60)
        sleep(3)
        coll = self.driver.find_element_by_xpath('//*[@id="nav_arrow"]/div').get_attribute("class")
        while True:
            if coll != 'icn collapse':
                self.driver.find_element_by_id('nav_arrow').click()
                continue
            else:
                log.info('菜单已收折')
                break

        # iframe = self.driver.find_element_by_xpath('//*[@id="set_right"]/iframe')  # 机器管理主体页面是内嵌的iframe
        # self.driver.switch_to.frame(iframe)
        self.manageassetpage.switch_to_iframe(self.manageassetpage.iframe)
        '''
        如果要退出iframe，则：
        driver.switch_to.default_content()
        '''

    def reset_layout(self):
        try:
            self.manageassetpage.waitClick(self.manageassetpage.ResetLayout_loc)
        except Exception as e:
            log.info(e.args)
        else:
            self.manageassetpage.click(self.manageassetpage.ResetLayout_loc)
            self.manageassetpage.click(self.manageassetpage.ResetLayoutOk_loc)
            self.driver.implicitly_wait(60)
            time.sleep(3)

    def ManageAssets(self, expect=True):
        log.info("Test add assets")
        # 添加机器
        self.driver.implicitly_wait(60)
        sleep(5)
        # log.info("click Add to open page")
        self.manageassetpage.click(self.manageassetpage.AddButton_loc)
        sleep(2)

        name = 'an' + self.time_format()
        cn = 'cn' + self.time_format()
        desc = 'The New Asset is ' + 'sn' + self.time_format()
        year = 2010 + random.randint(1, 10)

        iframemachine = self.driver.find_element_by_id('iframemachine')  # 机器编辑界面
        # log.info("jump to edit assets page")
        self.driver.switch_to.frame(iframemachine)

        # log.info("input assets informations")
        self.manageassetpage.InputTo(self.manageassetpage.SNInbox_loc, vin)
        self.manageassetpage.InputTo(self.manageassetpage.NameInbox_loc, name)
        self.manageassetpage.InputTo(self.manageassetpage.CustomNameInbox_loc, cn)
        self.manageassetpage.InputTo(self.manageassetpage.YearInbox_loc, str(year))
        # 选择框选择值
        Select(self.driver.find_element_by_id('dialog_make')).select_by_index(6)
        Select(self.driver.find_element_by_id('dialog_model')).select_by_index(0)
        sleep(1)
        # Select(self.driver.find_element_by_id('dialog_type')).select_by_index(random.randint(1, 9))
        # 因元素方法改变，更改点击方式
        type_inbox = ('id', 'dialog_type')
        type_value = ('xpath', '//*[@id="dialog_type"]/div/div[2]/ul/li[4]')
        self.manageassetpage.click(type_inbox)
        sleep(1)
        self.manageassetpage.click(type_value)

        self.manageassetpage.InputTo(self.manageassetpage.DescInbox_loc, desc)
        sleep(1)

        # 保存退出
        # log.info("save and exit")
        self.manageassetpage.click(self.manageassetpage.SaveExitButton_loc)
        sleep(2)

        # 搜索机器
        try:
            self.manageassetpage.click(self.manageassetpage.RefreshBt_loc)
            time.sleep(5)
        except:
            self.driver.refresh()
            self.driver.implicitly_wait(60)
            time.sleep(5)
            self.driver.switch_to.default_content()
            iframe = self.driver.find_element_by_xpath('//*[@id="set_right"]/iframe')  # 机器管理主体页面是内嵌的iframe
            self.driver.switch_to.frame(iframe)
            sleep(1)
        # log.info("search added asset")
        self.manageassetpage.SearchAssets(vin)
        self.driver.implicitly_wait(60)
        time.sleep(5)

        result = self.manageassetpage.is_text_in_element(self.manageassetpage.searchvin_loc, vin)
        # log.info("Check whether the machine is added successfully")
        if self.assertEqual(result, expect):
            log.info("Failed to add machine！ ")
            # log.info("")
        else:
            log.info("Adding a machine succeeded！")
            # log.info("")

    def SearchHideAsset(self):
        # log.info("")
        if not self.manageassetpage.is_clickable(self.manageassetpage.AddButton_loc):
            log.info('界面不可操作，刷新页面')
            self.driver.refresh()
            self.driver.implicitly_wait(30)
            self.to_frame()
            time.sleep(5)

        log.info("Test Search hidden assets")
        # self.reset_layout()
        try:
            self.manageassetpage.waitClick(self.manageassetpage.ShowHiddenCheck_loc)
        except Exception as e:
            log.info(e.args)
        else:
            sleep(1)
            self.manageassetpage.click(self.manageassetpage.ShowHiddenCheck_loc)
            sleep(2)
            self.manageassetpage.send_keys(self.manageassetpage.SearchInbox_loc, 'hide')
            time.sleep(2)
            self.manageassetpage.click(self.manageassetpage.SearchButton_loc)    # //*[@id="recordcontent"]/div[2]/input[2]
            time.sleep(2)
        hide = False

        try:
            self.manageassetpage.find_element(('xpath', '//*[@id="machinelist"]/div/div/div/table/tbody/tr'))
        except:
            log.info("No data is available!!")
        else:
            # 方法一： 检查数据中hide复选框是否勾上
            # js = "document.querySelector('#machinelist .data-grid-body').scrollLeft = 2000"
            # self.driver.execute_script(js)
            # time.sleep(1)
            # hide = self.manageassetpage.is_selected(self.manageassetpage.ListHideck_loc)

            # 方法二： 取消Show Hidden后数据是否还存在
            sleep(1)
            self.manageassetpage.click(self.manageassetpage.ShowHiddenCheck_loc)
            sleep(2)
            res = ('xpath', '//*[@id="machinelist"]/div/div/div/table/tbody/tr')
            if self.manageassetpage.is_located(res):
                hide = False
            else:
                hide = True

        self.assertEqual(hide, True)

    def SetLayout(self):
        log.info("Test set layout")
        if not self.manageassetpage.is_clickable(self.manageassetpage.AddButton_loc):
            log.info('界面不可操作，刷新页面')
            self.driver.refresh()
            self.driver.implicitly_wait(30)
            self.to_frame()
            time.sleep(5)
        self.reset_layout()
        self.driver.implicitly_wait(30)
        sleep(5)

        # log.info("click Layout")
        try:
            self.manageassetpage.waitClick(self.manageassetpage.Layout_loc, timeout=40)
        except Exception as e:
            log.info(e.args)
        else:
            sleep(2)
            self.manageassetpage.click(self.manageassetpage.Layout_loc)
            sleep(5)
            # 取消全选 ---- 鼠标操作
            checkAll = self.driver.find_element_by_xpath('//*[@id="dialog_layouts"]/div[2]/div/div/table/tr[1]/th[3]/div/label/layer')
            ActionChains(self.driver).click(checkAll).perform()
            time.sleep(1)
            ActionChains(self.driver).click(checkAll).perform()
            time.sleep(1)

            lists = self.driver.find_elements_by_xpath('//*[@id="dialog_layouts"]/div[2]/div/div/div/div/table/tr')
            for list in lists:
                txt = list.find_element_by_xpath('.//td[1]')
                if txt.text == 'VIN/SN':
                    loc = list.find_element_by_xpath('.//td[2]')
                    # 因为输入框对象还没有产生，需要先用鼠标点击
                    ActionChains(self.driver).click(loc).perform()
                    sleep(1)
                    list.find_element_by_xpath('.//td[2]/content/span/input').send_keys('VIN')
                    # pass
                elif txt.text == 'Asset Name':
                    loc = list.find_element_by_xpath('.//td[2]')
                    # 因为输入框对象还没有产生，需要先用鼠标点击
                    ActionChains(self.driver).click(loc).perform()
                    sleep(1)
                    list.find_element_by_xpath('.//td[2]/content/span/input').send_keys('AssetName')
                    # pass
                elif txt.text == 'Hide':
                    pass
                else:
                    list.find_element_by_xpath('.//td[3]/label/layer').click()

            self.manageassetpage.click(self.manageassetpage.LayoutOKBT_loc)

        sleep(2)

        # log.info("get header")
        headers = self.driver.find_elements_by_xpath('//*[@id="machinelist"]/div/table/tr/th')
        headername = []
        for header in headers:
            if header.text == '':
                pass
            else:
                headername += [header.text]
        # log.info("Determine if the column header is correct")
        res = ('VIN' == headername[0]) and ('AssetName' == headername[1])

        sleep(5)
        self.reset_layout()
        self.assertEqual(res, True)

    def importAssets(self):
        try:
            self.manageassetpage.click(self.manageassetpage.RefreshBt_loc)
            time.sleep(3)
        except:
            log.info('页面元素还未加载完，等待3秒')
            time.sleep(3)
        finally:
            time.sleep(1)

        # 开始导入操作
        log.info('Start test import Assets')
        try:
            self.manageassetpage.click(self.manageassetpage.importBtn_loc)
            time.sleep(2)
        except:
            log.info('点击导入失败')
            return False
        else:
            BASE_DIR = os.path.dirname(os.path.abspath(__file__))
            fpath = os.path.abspath(os.path.join(BASE_DIR, '..\..'))
            time.sleep(3)
            exfile = os.path.join(fpath, 'upfile.exe')
            file = os.path.join(fpath, 'TestData\\Importmachines.xlsx')
            os.system("%s %s" % (exfile, file))
            time.sleep(2)
            try:
                self.manageassetpage.click(self.manageassetpage.importMappingOk_loc)
                time.sleep(1)
            except:
                log.info('选择映射关系失败')
                return False
            else:
                try:
                    self.manageassetpage.click(self.manageassetpage.importImp_loc)
                    time.sleep(3)
                    try:
                        self.manageassetpage.click(self.manageassetpage.importOk_loc)
                    except:
                        self.driver.switch_to.default_content()
                        self.manageassetpage.click(self.manageassetpage.importOk_loc)
                        self.manageassetpage.switch_to_iframe(self.manageassetpage.iframe)
                except:
                    log.info('import Ok not click')
                log.info('已完成导入操作，待验证导入数据正确性')
                time.sleep(3)
                return True

    def searchAssets(self, vins):
        try:
            self.manageassetpage.click(self.manageassetpage.RefreshBt_loc)
            time.sleep(3)
        except:
            log.info('页面元素还未加载完，等待3秒')
            time.sleep(3)
        finally:
            time.sleep(1)

        # 搜索导入机器
        log.info('搜索机器')
        try:
            self.manageassetpage.send_keys(self.manageassetpage.SearchInbox_loc, vins)
            self.manageassetpage.click(self.manageassetpage.SearchButton_loc)
            time.sleep(3)
        except:
            log.info('搜索操作失败')
            return False
        else:
            # 获取搜索结果的VIN
            try:
                self.manageassetpage.find_element(('xpath', '//*[@id="machinelist"]/div/div/div/table/tbody/tr'))
            except:
                log.info("No data is available!!")
                return False
            else:
                search_vin = self.manageassetpage.get_text(self.manageassetpage.searchvin_loc)
                if search_vin == vins:
                    return True

    def delAssets(self):
        log.info('从数据库删除机器')
        dta = 'ironintel_admin'
        dtm = 'IICON_001_FLVMST'
        sqlstr = "delete from machines where machinename like '%an%' "
        delSQL(dtm, sqlstr)
        delSQL(dta, sqlstr)
        time.sleep(10)

    def exportToExcel(self):
        try:
            self.manageassetpage.click(self.manageassetpage.RefreshBt_loc)
            time.sleep(3)
        except:
            log.info('数据未加载完，等待3秒')
            self.driver.refresh()
            self.driver.implicitly_wait(60)
            self.to_frame()
            time.sleep(3)
        finally:
            self.manageassetpage.clear(self.manageassetpage.SearchInbox_loc)
            time.sleep(1)
            self.manageassetpage.click(self.manageassetpage.SearchButton_loc)
            time.sleep(3)

        grids = self.driver.find_element_by_xpath('//*[@id="machinelist"]/div/div[1]/div')
        hei = grids.size["height"]
        counts = int(hei) / 27
        log.info('当前有 %d 条数据' % counts)

        try:
            self.manageassetpage.click(self.manageassetpage.exportToBtn_loc)
            time.sleep(10)
            # 判断下载的文件是否存在
            import pathlib
            BASE_DIR = os.path.dirname(os.path.abspath(__file__))
            fpath = os.path.abspath(os.path.join(BASE_DIR, '..\..'))
            exfile = os.path.join(fpath, r'.\report\Manage+Assets.xlsx')
            exportfile = pathlib.Path(exfile)
            log.info('下载文件： %s' % exportfile)
            if exportfile.exists():
                # 调用读取数据
                from excel import excel
                datas = excel.get_rows(exportfile)
                # 有效数据须减去第1行（标题行）
                datas = datas - 1
                os.system('del %s' % exportfile)
                if datas == counts:
                    log.info('导出数据到Excel正确')
                    return True
                else:
                    log.info('导出后数据不正确')
                    return False
            else:
                log.info('导出文件不存在')
                return False
        except:
            log.info('导出失败')
            return False

    def test01_addAssets(self):
        '''新建机器'''
        self.ManageAssets()
        # pass

    def test02_searchHideAsset(self):
        '''搜索隐藏机器'''
        self.SearchHideAsset()
        # pass

    # def test03_setLayout(self):
    #     '''重置布局'''
    #     self.SetLayout()

    def test04_import(self):
        '''测试导入机器'''
        res = False
        if self.importAssets():
            res = self.searchAssets('imautotest')
            if res:
                log.info('导入机器成功')
            else:
                log.info('导入机器失败')
        self.assertTrue(res)

    def test05_delAssets(self):
        '''删除添加及导入的机器'''
        self.delAssets()
        res = self.searchAssets('imautotest')
        if not res:
            log.info('删除成功')
        else:
            log.info('删除失败')
        self.assertFalse(res)

    def test06_exportAssets(self):
        '''测试导出到Excel'''
        res = self.exportToExcel()
        if res:
            log.info('导出Assets测试成功')
        else:
            log.info('导出Assets测试失败')
        self.assertTrue(res)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.implicitly_wait(10)
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()
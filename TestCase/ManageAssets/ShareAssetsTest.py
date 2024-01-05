import unittest
from Page.ManageAssets.ShareAssetsPage import ShareAssetsPage
from Page.loginpage import LoginPage
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from logger import Log
from operater import browser
from time import sleep
import os
from queryMSSQL import *
import datetime
from skiptest import skip_dependon

log = Log()

# 判断保存报告的目录是否存在
path = ".\\report"
isExists = os.path.exists(path)
if not isExists:
    os.mkdir(path)


class ShareAssetsTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        # 登录IronIntel站点
        cls.driver = browser("chromeH")
        cls.logina = LoginPage(cls.driver)
        cls.logina.login('atshareasset@iicon004.com', 'Win.12345')
        log.info("Start test ShareAssets")
        cls.driver.implicitly_wait(60)
        cls.to_frame(cls)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.implicitly_wait(10)
        cls.driver.quit()

    def to_frame(self):
        sleep(3)
        self.shareassetpage = ShareAssetsPage(self.driver)
        # 打开机器管理页面：点击左侧主菜单之Manage Assets
        # self.manageassetpage.click(self.manageassetpage.ManageAssetBtn_loc)
        self.driver.implicitly_wait(60)
        sleep(3)
        self.shareassetpage.click(self.shareassetpage.ExButton_loc)
        self.shareassetpage.click(self.shareassetpage.ShareAssets_loc)

        sleep(10)
        # 收折左侧菜单
        self.shareassetpage.click(self.shareassetpage.ExButton_loc)
        sleep(2)

        self.shareassetpage.switch_to_iframe(self.shareassetpage.iframe_loc)
        '''
        如果要退出iframe，则：
        driver.switch_to.default_content()
        '''

    def unshareDeleteDT(self, mid):
        dta = 'ironintel_admin'
        dtm = 'IICON_001_FLVMST'
        sqlstr = "delete from machines where machineid='%s'" % mid
        delSQL(dtm, sqlstr)
        delSQL(dta, sqlstr)
        time.sleep(3)

    def getMachineid(self):
        sleep(3)
        dt = 'IICON_001_FLVMST'
        sqls = "select machineid from machines where vin='7627701'"
        mid = commQuery(dt, sqls)
        for i in mid:
            if i:
                m = i
                # print(m)
        # mid = mid[0]
        return m

    def setShare(self):
        # 搜索机器，并把它Share
        try:
            self.shareassetpage.click(self.shareassetpage.Refresh_loc)
            time.sleep(3)
        except:
            log.info('页面元素还未加载完，等待3秒')
            time.sleep(3)
        finally:
            time.sleep(1)

        log.info('测试设置共享')
        self.shareassetpage.search('7627701')
        sleep(2)
        try:
            self.shareassetpage.click(self.shareassetpage.fullSelect_loc)
            sleep(1)
        except:
            log.info("没有机器可共享")
        else:
            self.shareassetpage.click(self.shareassetpage.ShareBtn_loc)
            sleep(1)
            try:
                Select(self.driver.find_element_by_id('dialog_sharewith')).select_by_value('IICON_001')
                sleep(1)
            except:
                log.info('共享到IICON_001失败')
            else:
                self.shareassetpage.click(self.shareassetpage.OKBtn_loc)
                sleep(1)
                try:
                    self.shareassetpage.click(self.shareassetpage.confirmYes_loc)
                    sleep(3)
                except:
                    self.driver.switch_to.default_content()
                    self.shareassetpage.click(self.shareassetpage.confirmYes_loc)
                    self.shareassetpage.switch_to_iframe(self.shareassetpage.iframe_loc)
                    sleep(1)
                log.info('共享操作成功，待数据库确认')

                id = self.getMachineid()
                log.info('共享过来的机器ID是: %s' % id)
                if id:
                    return True
                else:
                    return False

    def editShare(self):
        endtime = (datetime.datetime.now() + datetime.timedelta(days=2)).strftime("%#m/%#d/%Y")

        try:
            self.shareassetpage.click(self.shareassetpage.Refresh_loc)
            time.sleep(3)
        except:
            log.info('页面元素还未加载完，等待3秒')
            time.sleep(3)
        finally:
            time.sleep(1)

        log.info('测试编辑共享设置')
        self.shareassetpage.search('7627701')
        sleep(2)
        try:
            self.shareassetpage.click(self.shareassetpage.ShareAsset_loc)
            sleep(1)
        except:
            log.info('打开编辑共享失败')
        else:
            self.shareassetpage.send_keys(self.shareassetpage.enddate_loc, endtime)
            log.info('设置结束日期： %s' % endtime)
            sleep(2)
            self.shareassetpage.click(self.shareassetpage.shareText_loc)
            sleep(1)

            self.shareassetpage.click(self.shareassetpage.OKBtn_loc)
            sleep(1)
            try:
                self.shareassetpage.click(self.shareassetpage.confirmYes_loc)
            except:
                self.driver.switch_to.default_content()
                self.shareassetpage.click(self.shareassetpage.confirmYes_loc)
                self.shareassetpage.switch_to_iframe(self.shareassetpage.iframe_loc)
            sleep(3)

        log.info('验证编辑结果')
        exdate = self.shareassetpage.get_text(self.shareassetpage.ExpectedDate_loc)
        log.info('获取结束日期： %s' % exdate)
        if exdate == endtime:
            return True
        else:
            return False

    def unShare(self):
        try:
            self.shareassetpage.click(self.shareassetpage.Refresh_loc)
            time.sleep(3)
        except:
            log.info('页面元素还未加载完，等待3秒')
            time.sleep(3)
        finally:
            time.sleep(1)

        log.info('测试取消共享设置')
        self.shareassetpage.search('7627701')
        sleep(2)

        try:
            self.shareassetpage.click(self.shareassetpage.unshareAsset_loc)
            sleep(1)
        except:
            log.info('打开Unshare失败')
            return False
        else:
            try:
                self.shareassetpage.click(self.shareassetpage.confirmYes_loc)
                sleep(3)
            except:
                self.driver.switch_to.default_content()
                self.shareassetpage.click(self.shareassetpage.confirmYes_loc)
                sleep(1)
                self.shareassetpage.switch_to_iframe(self.shareassetpage.iframe_loc)
            return True

    def test01_ShareAsset(self):
        '''设置共享机器'''
        res = self.setShare()
        if res:
            log.info('机器共享成功')
        else:
            log.info('机器共享失败')
        self.assertTrue(res)

    @skip_dependon(depend='test01_ShareAsset')
    def test02_EditShare(self):
        '''编辑共享'''
        res = self.editShare()
        if res:
            log.info('编辑共享成功')
        else:
            log.info('编辑共享失败')
        self.assertTrue(res)

    @skip_dependon(depend='test01_ShareAsset')
    def test03_Unshare(self):
        '''Unshare机器'''
        res = self.unShare()
        if res:
            log.info('UnShare操作成功')
        else:
            log.info('UnShare操作失败')
        # 清除测试数据
        id = self.getMachineid()
        sleep(2)
        self.unshareDeleteDT(id)
        self.assertTrue(res)

if __name__ == '__main__':
    unittest.main()

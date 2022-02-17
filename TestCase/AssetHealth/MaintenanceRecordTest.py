from Common.operater import Operater
import time
from Page.AssetHealth.MaintenanceRecordPage import MaintenanceRecordPage
from Page.loginpage import LoginPage
import unittest
from Common.operater import browser
import os
from Common.excel import excel
import ddt
from Common.logger import Log

log = Log()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

file_path = ".\\TestData\\maintenance.xls"
testData = excel.get_list(file_path)

@ddt.ddt
class ManageMaintenanceRecordTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = browser()
        cls.login = LoginPage(cls.driver)
        cls.login.login('atrecord@iicon004.com', 'Win.12345')
        cls.driver.implicitly_wait(60)
        time.sleep(5)
        cls.to_frame(cls)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def to_frame(self):
        self.maintenance = MaintenanceRecordPage(self.driver)
        time.sleep(5)
        self.maintenance.switch_to_iframe(self.maintenance.iframe_loc)

    @ddt.data(*testData)
    def test_add_record(self, data):
        if not self.maintenance.is_clickable(self.maintenance.addbutton_loc):
            log.info('添加按钮不能点击，刷新页面')
            self.driver.refresh()
            self.driver.implicitly_wait(60)
            time.sleep(5)
            self.maintenance.switch_to_iframe(self.maintenance.iframe_loc)

        self.maintenance.click(self.maintenance.addbutton_loc)
        log.info('测试添加Maintenance Record之   %s' % data['casename'])
        time.sleep(2)
        self.maintenance.select_by_value(self.maintenance.type_loc, "327")
        self.maintenance.send_keys(self.maintenance.searchinput1_loc, "1152600")
        self.maintenance.click(self.maintenance.searchbotton1_loc)

        self.maintenance.click(self.maintenance.addrecordbutton_loc)
        self.maintenance.switch_to_iframe(self.maintenance.mriframe_loc)

        self.maintenance.clear(self.maintenance.maintenacedate_loc)
        self.maintenance.send_keys(self.maintenance.maintenacedate_loc, data['Date'])
        self.maintenance.select_by_value(self.maintenance.maintenancetype_loc, "Undercarriage")
        self.maintenance.send_keys(self.maintenance.maintenancehour_loc, data['Hours'])
        self.maintenance.send_keys(self.maintenance.cost_loc, "200")
        self.maintenance.send_keys(self.maintenance.invoicenum_loc, "IN" + time.strftime("%Y%m%d%H%M%S"))
        self.maintenance.send_keys(self.maintenance.completedby_loc, "xdh10")
        self.maintenance.send_keys(self.maintenance.descrip_loc, data['Description'])
        self.maintenance.click(self.maintenance.savebotton_loc)
        time.sleep(3)
        result = self.maintenance.get_text(self.maintenance.savemsg_loc)

        self.maintenance.click(self.maintenance.saveok_loc)
        self.maintenance.click(self.maintenance.withoutsave_loc)
        self.driver.switch_to.default_content()
        self.maintenance.switch_to_iframe(self.maintenance.iframe_loc)
        reback = ('xpath', '//*[@id="content1"]/div[1]/div[1]/span[1]')
        self.maintenance.click(reback)
        time.sleep(2)

        self.assertEqual(result, data['mess'])



if __name__ == "__main__":
    unittest.main()


from operater import Operater
import time


class SurveyManagementPage(Operater):
    # 左侧滑块大图标
    assetHealth_loc = ('xpath', '//*[@id="divLeftTitle"]/div[@title="Asset Health"]/div')

    # Survey templates菜单元素
    exButton_loc = ('xpath', '//*[@id="nav_arrow"]')  # 左边菜单收折按钮
    surveyManagement_loc = ('xpath', '//*[@id="nav_surveymanagementresult"]/a/span')  # Survey Management/Result菜单

    # Survey Management/Result列表元素
    iframe_loc = ('xpath', '//*[@id="set_right"]/iframe')
    beginDateSearchText_loc = ('id', 'startdatetxt')  # Begin Date搜索文本框
    wobeginDate_loc = ('id', 'wostartdatetxt')
    # 1229调整位置： //*[@id="content1"]/div[1]/div[3]/input[@value="Search"]
    search_Inbox = ('id', 'searchinputtxt')
    searchBtn_loc = ('xpath', '//*[@id="content1"]/div/div[3]/input[@value="Search"]')  # search按钮
    surveyIframe_loc = ('id', 'iframesurveydetail')  # survey详情页面
    closeSurveyIframe_loc = ('xpath', '//*[@id="content1"]/div[1]/div[@class="function_title"]/span[@class="sbutton icondelete"]')  # survey详情页面的关闭按钮
    refresh_btn = ('xpath', '//*[@id="content1"]/div[1]/div[4]/span[@class="sbutton iconrefresh"]')

    # Status 过滤
    status_filter_btn = ('xpath', '//*[@id="surveylist"]/div/table/tr/th[@data-key="Status"]/div[2]')
    status_input = ('xpath', '/html/body/div[@class="data-column-header-filter-panel active"]/div[1]/input')
    status_check = ('xpath', '//*[@id="filter_value_0"]')
    status_filter_OK = ('xpath', '/html/body/div[@class="data-column-header-filter-panel active"]/div[3]/input[2]')

    def search(self):
        self.clear(self.beginDateSearchText_loc)
        time.sleep(1)
        self.clear(self.wobeginDate_loc)
        time.sleep(1)
        self.click(self.searchBtn_loc)
        time.sleep(2)

    def inputTo(self, Inboxloc, text):
        self.send_keys(Inboxloc, text)
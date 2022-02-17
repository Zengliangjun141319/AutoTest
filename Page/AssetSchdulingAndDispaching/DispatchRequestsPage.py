from Common.operater import Operater
from time import sleep

class DispatchRequestsPage(Operater):

    # 左侧滑块大图标
    dispatchmenu_loc = ('xpath', '//div[@title="Asset Scheduling and Dispatching"]')

    # Dispatch Requests菜单元素
    exButton_loc = ('xpath', '//*[@id="nav_arrow"]')    # 左边菜单收折按钮
    dispatchRequests_loc = ('id', 'nav_dispatchrequests')    # Dispatch Requests菜单

    # Dispatch Requests列表元素
    iframe_loc = ('xpath', '//*[@id="set_right"]/iframe')
    latestStartDate_loc = ('id', 'latesdatetxt') # Latest Start Date搜索条件
    searchBtn_loc = ('xpath', '//*[@id="contentctrl"]/div[2]/input[3]')  # 搜索按钮

    # Email功能相关元素
    asset1_loc = ('xpath','//*[@id="dispatchlist"]/div/div/div/table/tbody/tr[1]/td[1]/input') #列表中的第一个机器
    asset2_loc = ('xpath', '//*[@id="dispatchlist"]/div/div/div/table/tbody/tr[2]/td[1]/input')  # 列表中的第二个机器
    emailBtn_loc = ('xpath', '//*[@id="contentctrl"]/div[@class="function_title"]/span[1]') # Email按钮
    selectAssetList_loc = ('xpath','//*[@id="dialog_assignasset"]/div/div') # Dispatch Assignment对话框中的下拉按钮
    firstAsset_loc = ('xpath','//*[@id="dropdowndiv"]/ul/li[1]') # Dispatch Assignment对话框中机器列表中的第一个机器
    continueBtn_loc = ('xpath','//*[@id="dialog_assignment"]/div[@class="dialog-func"]/input[1]') # Dispatch Assignment对话框中的continue按钮
    emailAddress_loc = ('id','sendmail_otheremailaddress')  # Other Email Address文本框
    sendEmailOKBtn_loc = ('xpath','//*[@id="dialog_sendmail"]/div[@class="dialog-func"]/input[2]')   # Send Dispatch Request页面的OK按钮
    sendEmailDialogOKBtn_loc = ('xpath','/html/body/div[@class="dialog popupmsg"]/div[@class="dialog-func"]/input') # Send Dispatch Request对话框上的OK按钮

    # Print功能相关元素
    printBtn_loc = ('xpath', '//*[@id="contentctrl"]/div[@class="function_title"]/span[2]') # Print按钮
    printWindow_loc = ('xpath','//*[@id="form1"]/div[3]/h1') # 打印窗口的Dispatch Requests标题

    # delete功能相关元素
    deleteBtn_loc = ('xpath','//*[@id="dispatchlist"]/div/div/div/table/tbody/tr[1]/td[13]/a')  # Delete按钮
    deleteDialogYesBtn_loc = ('xpath','/html/body/div[@class="dialog popupmsg"]/div[@class="dialog-func"]/input[2]') # Delete对话框Yes按钮

    # delete功能相关元素
    viewChangeHistoryBtn_loc = ('xpath','//*[@id="dispatchlist"]/div/div/div/table/tbody/tr[1]/td[14]/a')  # View Change History按钮
    viewChangeHistoryTitle_loc = ('id','div_title') # View Change History页面Title


    def inputTo(self, Inboxloc, text):
        self.send_keys(Inboxloc, text)






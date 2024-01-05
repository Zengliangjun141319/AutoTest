# coding:utf-8

from operater import Operater
from Page.comms import *

login_url = "http://iron.soft.rz/login/"


class UserPage(Operater):
    #  进入用户管理页面前的元素
    settings_loc = ('id', "button_menu") # 左侧滑块列表中的Settings按钮
    usersetup_loc = ('xpath', ".//*[@id='menu_panel']/ul/li[1]/a/span") # Settings面板中的User Setup按钮
    usersmenu_loc = ('xpath', ".//*[@id='nav_users']/a/span") # Users菜单按钮

    # 用户管理页面元素
    iframe_loc = ('xpath', ".//*[@id='set_right']/iframe") # 用户主体页面嵌入的iframe

    searchinput_loc = ('id', "searchinputtxt") # 用户管理查询输入框
    searchbutton_loc = ('xpath', './/*[@id="content1"]/div/div[2]/input[@value="Search"]') # 用户管理查询按钮
    addbutton_loc = ('xpath', ".//*[@id='content1']/div/div[3]/span[1]") # 添加用户按钮
    # 搜索结果中右侧功能入口
    editfun_loc = ('xpath', '//*[@id="userlist"]/div/div[1]/div/table/tbody/tr/td/a[@title="Edit"]')    # 编辑当前用户
    assetass_loc = ('xpath', '//*[@id="userlist"]/div/div[1]/div/table/tbody/tr/td/a[@title="Assets Assignment"]')    #分配机器
    assetgroup_loc = ('xpath', '//*[@id="userlist"]/div/div[1]/div/table/tbody/tr/td/a[@title="Asset Groups Assignment"]')
    assettype_loc = ('xpath', '//*[@id="userlist"]/div/div[1]/div/table/tbody/tr/td/a[@title="Asset Type Assignment"]')
    jobsiteass_loc = ('xpath', '//*[@id="userlist"]/div/div[1]/div/table/tbody/tr/td/a[@title="Jobsites Assignment"]')
    deletebutton_loc = ('xpath', "//*[@id='userlist']/div/div[1]/div/table/tbody/tr/td/a[@title='Delete']")  # 用户删除按钮
    resetpw_loc = ('xpath', '//*[@id="userlist"]/div/div[1]/div/table/tbody/tr/td/a[@title="Reset Password"]')

    yesbutton_loc = ('xpath', yes_btn)  # 提示信息框Yes按钮
    user_loc = ('xpath', ".//*[@id='userlist']/div/div/div/table/tbody/tr[1]/td[1]/span")

    # 分配机器窗口元素
    allselect_loc = ('id', "header_checkbox_column_0")  # 机器列表全选CheckBox
    delectass_loc = ('xpath', ".//*[@id='dialog_managemahchine']/div[4]/span[2]")
    infoyes_loc = ('xpath', yes_btn)
    firstcheckbox_loc = ('id', "body_checkbox_row_0")  # 机器列表第一台机器的CheckBox
    addasset_loc = ('xpath', ".//*[@id='dialog_managemahchine']/div[4]/span[1]")
    searchassetinput_loc = ('xpath', "//*[@id='dialog_machines']/div[2]/div[1]/input")
    searchassetbutton_loc = ('xpath', "//*[@id='dialog_machines']/div[2]/div[1]/div")
    assetcheckbox_loc = ('id', "body_checkbox_row_0")
    assetok_loc = ('xpath', "//*[@id='dialog_machines']/div[3]/input[2]")
    assetwindowclose_loc = ('xpath', "//*[@id='dialog_managemahchine']/div[6]/input[1]")
    assetinfo_loc = ('xpath', '//*[@id="selectedmachinelist"]/div/div[1]/div/table/tbody/tr/td[2]/span')

    # 分配机器组窗口元素
    availablegroup_loc = ('xpath', '//*[@id="availableassetgrouplist"]/div/div[1]/div/table/tbody/tr[7]/td[1]/span')
    groupaddedbutton_loc = ('xpath', '//*[@id="dialog_machinegroup"]/div[2]/table/tbody/tr/td[2]/input[1]')
    selectedgourp_loc = ('xpath', '//*[@id="selectedassetgrouplist"]/div/div[1]/div/table/tbody/tr/td[1]/span')
    groupok_loc = ('xpath', '//*[@id="dialog_machinegroup"]/div[3]/input[2]')
    allgroupremove_loc = ('xpath', '//*[@id="dialog_machinegroup"]/div[2]/table/tbody/tr/td[2]/input[4]')

    # 分配机器类型窗口元素
    availabletype_loc = ('xpath', '//*[@id="availableassettypelist"]/div/div[1]/div/table/tbody/tr[1]/td[1]')
    typeaddedbuttion_loc = ('xpath', '//*[@id="dialog_manageassettype"]/div[3]/table/tbody/tr/td[2]/input[1]')
    selectedtype_loc = ('xpath', '//*[@id="selectedassettypelist"]/div/div[1]/div/table/tbody/tr/td[1]/span')
    typeok_loc = ('xpath', '//*[@id="dialog_manageassettype"]/div[4]/input[2]')
    alltyperemove_loc = ('xpath', '//*[@id="dialog_manageassettype"]/div[3]/table/tbody/tr/td[2]/input[4]')

    # 重置密码窗口元素
    randomcheckbox_loc = ('id', "dialog_user_randompass")
    pwinput_loc = ('id', "dialog_user_password")
    conpwinput_loc = ('id', "dialog_user_password1")
    okbutton_loc = ('xpath', ".//*[@id='dialog_password']/div[3]/input[2]")
    resetok_loc = ('xpath', ok_btn)

    # 用户详细信息页面元素
    iframeuser_loc = ('id', "iframeuser")  # 添加用户弹窗iframe
    userid_loc = ('id', "dialog_user_id")  # 用户ID输入框
    randompsw_loc = ('id', "dialog_user_randompass")  # 随机密码复选框
    psw_loc = ('id', "dialog_user_password")  # 密码输入框
    confirmpsw_loc = ('id', "dialog_user_password1")  # 确认密码输入框
    username_loc = ('id', "dialog_user_name")  # 用户名输入框
    usertype_loc = ('id', "dialog_user_type")  # 用户类型下拉选择框
    textadress_loc = ('id', "dialog_textaddress")  # 文本地址输入框
    mobile_loc = ('id', "dialog_mobile")  # 手机输入框
    businessphone_loc = ('id', "dialog_business_phone")  # 商务电话输入框
    isuser_loc = ('id', "dialog_isuser")  # is user复选框
    browser_loc = ('id', "dialog_allowloginintopc")  # 通过PC端浏览器访问复选框
    inspectapp_loc = ('id', "dialog_allowloginintoinspectmobile")  # 通过inspect app访问复选框
    fleetapp_loc = ('id', "dialog_allowloginintofleetmobile")  # 通过fleet app访问复选框
    barcodeapp_loc = ('id', "dialog_mobileappbarcodescanner")  # barcode app 复选框
    contacttype_loc = ('id', "dialog_contacttype")  # contact type下拉选择框
    fob_loc = ('id', "dialog_fob")  # employee id or fob 输入框
    manager_loc = ('id', "dialog_manager")  # manager下拉选择框
    emailoutopt_loc = ('id', "dialog_emailoptout")  # opt out of email复选框
    inspectemail_loc = ('id', "dialog_inspectemaillist")  # inspect email复选框
    teamuser_loc = ('id', "dialog_teamintelligenceuser")  # team intelligence user复选框
    language_loc = ('id', "dialog_languages")  # 语言下拉选择框
    landingpage_loc = ('id', "dialog_landingpage")  # 登录页下拉选择框
    notes_loc = ('id', "dialog_notes")  # notes输入框
    savebutton_loc = ('xpath', '//*[@id="content1"]/div[1]/div[@class="function_title"]/span[1]')  # 保存按钮
    saveexitbotton_loc = ('xpath', '//*[@id="content1"]/div[1]/div[@class="function_title"]/span[2]')  # 保存并退出按钮
    withoutsavebutton_loc = ('xpath', '//*[@id="content1"]/div[1]/div[@class="function_title"]/span[@class="sbutton iconexit"]')  # 直接退出按钮
    # boxmsg_loc = ('xpath', '/html/body/div[@class="dialog"]/div[@class="alert-message-box"]/div')  # 消息体内容
    boxmsg_loc = ('xpath', msg_content)
    # boxokbutton_loc = ('xpath', '/html/body/div[@class="dialog"]/div[@class="dialog-one-function"]/input[@value="OK"]')  # OK按钮
    boxokbutton_loc = ('xpath', ok_btn)

    # 定义输入用户ID方法
    def input_userid(self,  userid):
        # 输入用户ID
        self.send_keys(self.userid_loc, userid)

    def uncheck_randompsw(self):
        # 取消勾选随机密码
        self.click(self.randompsw_loc)





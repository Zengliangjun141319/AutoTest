# coding:utf-8

from Common.operater import  Operater

login_url = "http://iron.soft.rz/login/"

class UserPage(Operater):

    #  进入用户管理页面前的元素
    settings_loc = ('id', "button_menu") # 左侧滑块列表中的Settings按钮
    usersetup_loc = ('xpath', ".//*[@id='menu_panel']/ul/li[1]/a/span") # Settings面板中的User Setup按钮
    usersmenu_loc = ('xpath', ".//*[@id='nav_users']/a/span") # Users菜单按钮

    # 用户管理页面元素
    iframe_loc = ('xpath', ".//*[@id='set_right']/iframe") # 用户主体页面嵌入的iframe

    searchinput_loc = ('id', "searchinputtxt") # 用户管理查询输入框
    searchbutton_loc = ('xpath', ".//*[@id='content1']/div/div[2]/input[2]") # 用户管理查询按钮
    addbutton_loc = ('xpath', ".//*[@id='content1']/div/div[3]/span[1]") # 添加用户按钮
    # 搜索结果中右侧功能入口
    editfun_loc = ('xpath', '//*[@id="userlist"]/div/div[1]/div/table/tbody/tr/td/a[@title="Edit"]')    # 编辑当前用户
    assetass_loc = ('xpath', '//*[@id="userlist"]/div/div[1]/div/table/tbody/tr/td/a[@title="Assets Assignment"]')    #分配机器
    assetgroup_loc = ('xpath', '//*[@id="userlist"]/div/div[1]/div/table/tbody/tr/td/a[@title="Asset Groups Assignment"]')
    assettype_loc = ('xpath', '//*[@id="userlist"]/div/div[1]/div/table/tbody/tr/td/a[@title="Asset Type Assignment"]')
    jobsiteass_loc = ('xpath', '//*[@id="userlist"]/div/div[1]/div/table/tbody/tr/td/a[@title="Jobsites Assignment"]')
    deletebutton_loc = ('xpath', "//*[@id='userlist']/div/div[1]/div/table/tbody/tr/td/a[@title='Delete']")  # 用户删除按钮
    resetpw_loc = ('xpath', '//*[@id="userlist"]/div/div[1]/div/table/tbody/tr/td/a[@title="Reset Password"]')

    yesbutton_loc = ('xpath', "html/body/div[@class='dialog popupmsg']/div[@class='dialog-func']/input[2]")  # 提示信息框Yes按钮
    user_loc = ('xpath', ".//*[@id='userlist']/div/div/div/table/tbody/tr[1]/td[1]/span")

    # 用户详细信息页面元素
    iframeuser_loc = ('id', "iframeuser") # 添加用户弹窗iframe
    userid_loc = ('id', "dialog_user_id") # 用户ID输入框
    randompsw_loc = ('id', "dialog_user_randompass") # 随机密码复选框
    psw_loc = ('id', "dialog_user_password") # 密码输入框
    confirmpsw_loc = ('id', "dialog_user_password1") # 确认密码输入框
    username_loc = ('id', "dialog_user_name") # 用户名输入框
    usertype_loc = ('id', "dialog_user_type") # 用户类型下拉选择框
    textadress_loc = ('id', "dialog_textaddress") # 文本地址输入框
    mobile_loc = ('id', "dialog_mobile") # 手机输入框
    businessphone_loc = ('id', "dialog_business_phone") # 商务电话输入框
    isuser_loc = ('id', "dialog_isuser") # is user复选框
    browser_loc = ('id', "dialog_allowloginintopc") # 通过PC端浏览器访问复选框
    inspectapp_loc = ('id', "dialog_allowloginintoinspectmobile") # 通过inspect app访问复选框
    fleetapp_loc = ('id', "dialog_allowloginintofleetmobile") # 通过fleet app访问复选框
    barcodeapp_loc = ('id', "dialog_mobileappbarcodescanner") # barcode app 复选框
    contacttype_loc = ('id', "dialog_contacttype") # contact type下拉选择框
    fob_loc = ('id', "dialog_fob") # employee id or fob 输入框
    manager_loc = ('id', "dialog_manager") # manager下拉选择框
    emailoutopt_loc = ('id', "dialog_emailoptout") # opt out of email复选框
    inspectemail_loc = ('id', "dialog_inspectemaillist") # inspect email复选框
    teamuser_loc = ('id', "dialog_teamintelligenceuser") # team intelligence user复选框
    language_loc = ('id', "dialog_languages") # 语言下拉选择框
    landingpage_loc = ('id', "dialog_landingpage") # 登录页下拉选择框
    notes_loc = ('id', "dialog_notes") # notes输入框
    savebutton_loc = ('xpath', ".//*[@id='content1']/div[2]/div[2]/span[1]") # 保存按钮
    saveexitbotton_loc = ('xpath', ".//*[@id='content1']/div[2]/div[2]/span[2]") # 保存并退出按钮
    withoutsavebutton_loc = ('xpath', ".//*[@id='content1']/div[2]/div[2]/span[3]") # 直接退出按钮
    boxmsg_loc = ('xpath', "html/body/div[3]/div[2]/div")
    boxokbutton_loc = ('xpath', "html/body/div[3]/div[3]/input")


    # 定义输入用户ID方法
    def input_userid(self,  userid):
        # 输入用户ID
        self.send_keys(self.userid_loc, userid)

    def uncheck_randompsw(self):
        # 取消勾选随机密码
        self.click(self.randompsw_loc)





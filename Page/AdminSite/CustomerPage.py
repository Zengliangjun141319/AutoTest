from Common.operater import Operater

class CustomerPage(Operater):
    # 元素定位
    # 搜索框及按钮位置
    SearchInputBox_loc = ('id', 'searchinputtxt')
    SearchButton_loc = ('xpath', '//*[@id="recordcontent"]/div[2]/input[3]')
    mc_loc = ('xpath', '//*[@id="recordcontent"]/div[1]')

    # 搜索后的位置会根据结果不同，如搜索00时004站点Detail位置：//*[@id="customerlist"]/div/div/div/table/tbody/tr[4]/td[4]/a
    # 默认IRONDEALERS站点Detail和打开位置
    DealerDetail_loc = ('xpath', '//*[@id="customerlist"]/div/div/div/table/tbody/tr[3]/td[4]/a')
    DealerOpen_loc = ('xpath', '//*[@id="customerlist"]/div/div/div/table/tbody/tr[3]/td[5]/a')

    # 默认IICON004站点Detail和打开位置
    Con004Detail_loc = ('xpath', '//*[@id="customerlist"]/div/div/div/table/tbody/tr[7]/td[4]/a')
    Con004Open_loc = ('xpath','//*[@id="customerlist"]/div/div/div/table/tbody/tr[7]/td[5]/a')
    Search004Detail_loc = ('xpath', '//*[@id="customerlist"]/div/div/div/table/tbody/tr[2]/td[4]')

    # 搜索过滤
    def SearchSite(self, Texts):
        '''输入搜索内容，并点击Search'''
        self.send_keys(self.SearchInputBox_loc, Texts)
        self.click(self.SearchButton_loc)

    # 打开Detail
    def click_sites(self, loc):
        '''
        根据传入的Detail位置打开指定站点的Detail页面
        Usage：
        click_sites(DealerDetail_loc)     打开Dealer站点的Detail页
        click_sites(Con004Open_loc)    打开IICON004站点
        '''
        self.click(self, loc)

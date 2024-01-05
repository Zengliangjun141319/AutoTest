from operater import Operater

class AdminHomePage(Operater):
    # 定位器
    Customers_loc = ('xpath', '//*[@id="modules"]/div[1]/div/div')
    Styles_loc = ('xpath', '//*[@id="modules"]/div[2]/div/div')
    AlertView_loc = ('xpath', '//*[@id="modules"]/div[3]/div/div')

    def click_Customers(self):
        '''点击Customers'''
        self.click(self.Customers_loc)

    def click_Styles(self):
        '''打开样式管理'''
        self.click(self.Styles_loc)

    def click_AlertView(self):
        '''打开Alert View设置'''
        self.click(self.AlertView_loc)
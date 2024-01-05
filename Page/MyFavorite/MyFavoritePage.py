# coding:utf-8

from operater import Operater
from Page.comms import *


class MyFavoritePage(Operater):
    # 添加收藏按钮
    addfavorite_loc = ('id', "divfavadd")

    # 取消收藏按钮
    cancelfavorite_loc = ('id', "divfav")

    # 收藏夹菜单按钮
    favoritemenu_loc = ('id', "divfavmenu")

    # 收藏夹内容菜单列表
    favoritelistmenu_loc = ('xpath', ".//*[@id='favorite_panel']/div[1]/ul/li[1]/a/span")

    # 收藏夹内容编辑菜单
    editfavoritemenu_loc = ('xpath', ".//*[@id='favorite_panel']/div[2]/span")

    # 删除按钮
    deletebutton_loc = ('xpath', ".//*[@id='favoritelist']/div/div/div/table/tbody/tr[1]/td[2]/a")

    # 收藏内容顺序调整向上移动按钮
    upmovebutton_loc = ('xpath', ".//*[@id='favoritelist']/div/div/div/table/tbody/tr[1]/td[3]/a")

    # 收藏内容顺序调整向下移动按钮
    downmoverbotton_loc = ('xpath', ".//*[@id='favoritelist']/div/div/div/table/tbody/tr[1]/td[4]/a")

    # 删除提示信息确认按钮
    msgboxokbutton_loc = ('xpath', yes_btn)

    # 列表框关闭按钮
    closebutton_loc = ('xpath', ".//*[@id='dialog_favorite']/div[1]/em")

    # Dispatch Requests菜单
    dispatch_loc = ('id', "nav_dispatchrequests")

    # Jobsites菜单
    jobsites_loc = ('id', "nav_jobsitemanage")

    # favorite列表第一和第二个元素
    favoritefirst_loc = ('xpath', ".//*[@id='favoritelist']/div/div/div/table/tbody/tr[1]/td[1]")
    favoritesecond_loc = ('xpath', ".//*[@id='favoritelist']/div/div/div/table/tbody/tr[2]/td[1]")
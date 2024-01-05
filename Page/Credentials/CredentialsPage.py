# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     CredentialsPage.py
   Author :        曾良均
   QQ:             277099728
   Date：          7/25/2023 10:39 AM   
   Description :
-------------------------------------------------
   Change Activity:
                   
-------------------------------------------------
"""
__author__ = 'ljzeng'


from operater import Operater
from Page.comms import *

class CredentialsPage(Operater):
    # 左侧菜单
    exp_btn = ('id', 'nav_arrow')
    credentials_menu = ('id', 'nav_credential')
    johndeere_menu = ('id', 'nav_jdlink')
    apicred_menu = ('id', 'nav_apicredential')

    # Credentials页面
    right_iframe = ('xpath', '//*[@id="set_right"]/iframe')

    cred_add_btn = ('xpath', '//*[@id="content1"]/div[1]/div[2]/span[@class="sbutton iconadd"]')
    cred_refresh_btn = ('xpath', '//*[@id="content1"]/div[1]/div[2]/span[@class="sbutton iconrefresh"]')
    cred_list_edit_btn = ('xpath', '//*[@id="credentiallist"]/div/div/div/table/tbody/tr/td/a[@title="Edit"]')
    cred_list_del_btn = ('xpath', '//*[@id="credentiallist"]/div/div/div/table/tbody/tr/td/a[@title="Delete"]')
    lists = ('xpath', '//*[@id="credentiallist"]/div/div[1]/div/table/tbody/tr')
    cred_del_yes_btn = ('xpath', yes_btn)  # '/html/body/div[19]/div[3]/input[2]'
    # 新建窗口
    cred_add_urlkey_inbox = ('id', 'dialog_urlkey')
    cred_add_username_inbox = ('id', 'dialog_username')
    cred_add_passwd_inbox = ('id', 'dialog_password')
    cred_add_enabled_chx = ('id', 'dialog_enabled')
    cred_add_notes_inbox = ('id', 'dialog_notes')
    cred_add_ok_btn = ('xpath', '//*[@id="dialog_credential"]/div[3]/input[@value="OK"]')

    # John Deere页面
    jdlink_add_btn = ('xpath', '//*[@id="content1"]/div[1]/div[2]/span[@class="sbutton iconadd"]')
    # 跳转新页面
    # jdlink_page_signin_lable = ('xpath', '//*[@id="form32"]/div[1]/h2')  # Sign In
    jdlink_page_signin_lable = ('xpath', '//*[@id="okta-sign-in"]/div[2]/div/div/form/div/h2')

    # API页面
    api_add_btn = ('xpath', '//*[@id="content1"]/div[1]/div[2]/span[@class="sbutton iconadd"]')
    api_refresh_btn = ('xpath', '//*[@id="content1"]/div[1]/div[2]/span[@class="sbutton iconrefresh"]')

    api_name_chelist = ('id', 'dialog_apiname')  # value=43  JCB
    api_username_inbox = ('id', 'dialog_username')
    api_pwd_inbox = ('id', 'dialog_password')
    api_key_inbox = ('id', 'dialog_apikey')
    api_secret_inbox = ('id', 'dialog_apisecret')
    api_ok_btn = ('xpath', '//*[@id="dialog_credential"]/div[3]/input[@value="OK"]')

    api_list_edit_btn = ('xpath', '//*[@id="credentiallist"]/div/div[1]/div/table/tbody/tr/td/a[@title="Edit"]')
    api_list_del_btn = ('xpath', '//*[@id="credentiallist"]/div/div[1]/div/table/tbody/tr/td/a[@title="Delete"]')

    api_del_yes_btn = ('xpath', yes_btn)  # /html/body/div[19]/div[3]/input[2]
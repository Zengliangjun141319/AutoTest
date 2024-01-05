# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     Pyload.py
   Author :        曾良均
   QQ:             277099728
   Date：          7/21/2023 10:30 AM   
   Description :
-------------------------------------------------
   Change Activity:
                   
-------------------------------------------------
"""
__author__ = 'ljzeng'

import pywinauto
import time
from pywinauto.keyboard import send_keys

def Pyload(files):
    # 通过Pywinauto工具上传附件，需要提供文件跟径
    # app = Application
    # try:
    #     app = app.connect(title_re='Open', class_name='#32770')
    #     app['Open']['Edit1'].set_edit_text(files)
    #     app['Open']['Button1'].click()
    #     time.sleep(2)
    # except:
    #     app = app.connect(title_re='打开', class_name='#32770')
    #     app['打开']['Edit1'].set_edit_text(files)
    #     app['打开']['Button1'].click()
    #     time.sleep(2)

    app = pywinauto.Desktop()
    try:
        # 窗口为英文标题
        dlg = app['Open']
        dlg['Edit1'].click()
        dlg['Edit1'].type_keys(files)
        # send_keys(files)
        time.sleep(1)
        dlg['Button1'].click()
        time.sleep(3)
    except:
        # 窗口为中文标题
        dlg = app['打开']
        # dlg['Edit1'].type_keys(files)
        dlg['Edit1'].click()
        send_keys(files)
        time.sleep(1)
        dlg['Button1'].click()
        time.sleep(3)
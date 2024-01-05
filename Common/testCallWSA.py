# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     testCallWSA.py
   Author :        曾良均
   QQ:             277099728
   Date：          2/27/2023 10:45 AM   
   Description :
-------------------------------------------------
   Change Activity:
                   
-------------------------------------------------
"""
__author__ = 'ljzeng'
import os
from pynput.keyboard import Key, Controller
import time

kb = Controller()
with kb.pressed(Key.cmd_l):
    kb.press('r')
    kb.release('r')

os.system('net start wsaservice')

time.sleep(3)

# 控制键盘 按压释放、键入字符串、按下组合键
with kb.pressed(Key.cmd_l):  # Key.cmd_l 即为Win键
    kb.press('r')
    kb.release('r')
kb.type('wsa://com.android.settings')    # 输入命令
kb.press(Key.enter)
kb.release(Key.enter)
time.sleep(5)

# 连接设备
os.system('adb connect 127.0.0.1:58526')
time.sleep(2)
os.system('adb devices')
time.sleep(3)

# 启动APP
os.system('adb shell am start com.ForesightIntelligence.FleetIntelligence/crc64a7ba8be028210fcc.MainActivity')
time.sleep(5)

# 运行 界面直接启动APP包
# 须把wsaClient命令路径加入环境变量
# WsaClient.exe  /launch wsa://com.ForesightIntelligence.FleetIntelligence

# 安装WSA后，已把windowsapp路径加入环境变量，要运行程序，可直接在运行界面输入
# wsa://com.ForesightIntelligence.FleetIntelligence

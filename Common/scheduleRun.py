# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     scheduleRun.py
   Description :
   Author :        曾良均
   QQ:             277099728
   Date：          9/13/2021 3:07 PM
-------------------------------------------------
   Change Activity:
                   9/13/2021:
-------------------------------------------------
"""
__author__ = 'ljzeng'

from queryMSSQL import *
import os

# 检查IronIntel版本
dt = 'ironintel'
sqls = "select appver from SYS_CUSTSITES where COMPANYID='iicon004'"
vers = commQuery(dt=dt, sqlstr=sqls)
# print(vers)
cver = vers[0][0]
cver = str(cver)
print("cver: %s" % cver)

# 获取上次测试版本
file = '.\\TestData\\ver.xml'
isExists = os.path.exists(file)
if not isExists:
    # print("run auto tests!")
    os.system("python run_testcase.py")
    # print("文件不存在")
else:
    with open(file, 'r', encoding='utf-8') as fp:
        v = fp.read()
        # print("文件存在，上次测试版本为： %s" % v)
        if v != cver:
            print("diff version")
            print("run auto tests! ")
            os.system("python run_testcase.py")

with open(file, 'w+', encoding='utf-8') as fp:
    fp.write(cver)
    fp.flush()

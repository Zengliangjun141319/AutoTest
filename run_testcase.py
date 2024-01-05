# -*- coding:utf8 -*-
# 调用运行测试用例
import unittest
from HTMLTestRunner import HTMLTestRunner
from sendemail import *
from queryMSSQL import commQuery
from queryMSSQL import updateSQL
from Common.updateResultToDB import getresult
import sys


def all_testcase():
    # 待执行测试用例的目录
    case_dir = ".\\TestCase"
    testcase = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(case_dir, pattern="*.py", top_level_dir=None)
    # discover筛选出来的用例，添加到测试套件中
    for test_suite in discover:
        for test_case in test_suite:
            # 添加测试用例到 testcase
            testcase.addTest(test_case)
    print(testcase)
    return testcase


def checkver():
    # 检查IronIntel版本
    dt = 'ironintel'
    sqls = "select appver from SYS_CUSTSITES where COMPANYID='iicon004'"
    vers = commQuery(dt=dt, sqlstr=sqls)
    ver = vers[0][0]
    return ver


def setTerm(val):
    # 设置Terms
    dt = 'ironintel'
    sqls = "update TERMOFUSE set STATUS=%d" % val
    updateSQL(dt=dt, sqlstr=sqls)
    time.sleep(3)


if __name__ == "__main__":
    path = ".\\report"
    isExists = os.path.exists(path)
    if not isExists:
        os.mkdir(path)

    # 设置Terms为0
    setTerm(0)

    nowtime = datetime.now().strftime("%Y.%m.%d.%H%M%S.%f")[:-3]
    rtime = datetime.now().strftime("%Y.%m.%d %H:%M")
    report_path = ".\\report\\result_%s" % nowtime
    os.mkdir(report_path)
    report_file = report_path + "\\result_%s.html" % nowtime
    fp = open(report_file, "wb")
    runner = HTMLTestRunner(stream=fp, title=u'测试报告', description=u'用例执行情况：')
    # 运行用例
    runner.run(all_testcase())
    fp.close()
    # 设置Terms为1
    setTerm(1)

    # 发送邮件
    try:
        vers = checkver()
        # sendEmail(ver=vers, report=report_file, runtime=rtime)
        # getresult(report_file,vers)
    except Exception:
        sys.stderr.write("Email delivery report failed!!")
    finally:
        os.system('move .\\report\\*.* ' + report_path)

# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     runTestcases.py
   Description :
   Author :        曾良均
   QQ:             277099728
   Date：          9/27/2021 11:28 AM
-------------------------------------------------
   Change Activity:
                   9/27/2021:
-------------------------------------------------
"""
__author__ = 'ljzeng'


from HTMLTestRunners import *
from sendemail import *
from queryMSSQL import commQuery
import threadpool

global all_result

def all_testcase():
    # 待执行测试用例的目录
    case_dir = ".\\TestCase"
    discover = unittest.defaultTestLoader.discover(case_dir, pattern="*.py", top_level_dir=None)
    return discover


def checkver():
    # 检查IronIntel版本
    dt = 'ironintel'
    sqls = "select appver from SYS_CUSTSITES where COMPANYID='iicon004'"
    vers = commQuery(dt=dt, sqlstr=sqls)
    ver = vers[0][0]
    return ver


def run(case, report, nth=0):
    global all_result
    fp_temp = open(report, "wb")
    runner = HTMLTestRunner(stream=fp_temp,description=u'测试用例结果' + report)
    res = runner.run(case)
    all_result.append(res)
    fp_temp.close()
    sys.stderr.write("run: %s \n" % str(len(all_result)))
    os.system("del %s" % report)


if __name__ == "__main__":
    path = ".\\report"
    isExists = os.path.exists(path)
    if not isExists:
        os.mkdir(path)
    nowtime = datetime.now().strftime("%Y.%m.%d.%H%M%S.%f")[:-3]
    rtime = datetime.now().strftime("%Y.%m.%d %H:%M")
    start_time = datetime.now()
    time_stamp = int(time.time())
    report_path = ".\\report\\result_%s" % nowtime
    os.mkdir(report_path)

    all_result = []
    cases = all_testcase()
    task_pool = threadpool.ThreadPool(5)
    count = 0
    lst = []
    for i, j in zip(cases, range(len(list(cases)))):
        file_path = report_path + '\\' + nowtime + '_' + str(count) + '.html'
        file_path = file_path.replace("\r", r"\r").replace('\n', r'\n')
        count += 1
        # sys.stderr.write("\ncase: %s" % i)
        lst.append(([i, file_path, j], None))
    rqs = threadpool.makeRequests(run, lst)

    [task_pool.putRequest(req) for req in rqs]
    task_pool.wait()

    end_time = datetime.now()

    report_file = report_path + "\\result_%s.html" % nowtime

    fp = open(report_file, "wb")
    merge_html = MergeResult(fp=fp,result_list=all_result,start_time=start_time,end_time=end_time, title=u'多线程测试报告', description=u'用例执行情况：')
    merge_html.make_html()
    fp.close()

    # 发送邮件
    try:
        vers = checkver()
        # sendEmail(ver=vers, report=report_file, runtime=rtime)
    except:
        sys.stderr.write("Email delivery report failed!!")
    finally:
        sys.stderr.write(os.popen('move .\\report\\*.* ' + report_path).read())

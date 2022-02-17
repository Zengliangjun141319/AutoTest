# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     AutoRunTest.py
   Description :    本程序是实现Win服务，在晚上20点到23：59之间执行测试
   Author :        曾良均
   QQ:             277099728
   Date：          10/8/2021 9:58 AM
-------------------------------------------------
   Change Activity:
                   10/8/2021:
-------------------------------------------------
"""
__author__ = 'ljzeng'

from datetime import datetime
import win32serviceutil
import win32service
import win32event
import os
import servicemanager
import sys
import win32api

class AutoRunTest(win32serviceutil.ServiceFramework):
    _svc_name_ = "AutoRunTestService"    # 服务名
    _svc_display_name_ = "AutoTestService"    # Win服务上显示的名称
    _svc_description_ = "IronIntel Automate testing services"    # 服务描述

    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)
        self.log('init')

    def log(self, msg):
        '''日志记录'''
        servicemanager.LogInfoMsg(str(msg))

    def start(self):
        '''执行脚本'''
        stime = datetime.strptime(str(datetime.now().date()) + '11:20', '%Y-%m-%d%H:%M')
        endtime = datetime.strptime(str(datetime.now().date()) + '23:50', '%Y-%m-%d%H:%M')
        now = datetime.now()

        if stime < now < endtime:
            self.log('running ... ')
            re = os.popen("D:\\SVN\\IronIntel\\Doc\\AutoTest\\run.bat").read()
            self.log(re)
        else:
            self.log('Not run time, wait ...')

            # os.system("C:\\AutoTest\\run.bat")


    def stop(self):
        pass

    def SvcDoRun(self):
        while True:
            self.ReportServiceStatus(win32service.SERVICE_START_PENDING)
            nowtime = datetime.now().strftime("%Y.%m.%d %H:%M:%S.%f")[:-3]
            try:
                self.ReportServiceStatus(win32service.SERVICE_RUNNING)
                self.log('%s -- start run' % nowtime)
                self.start()
                # win32event.WaitForSingleObject(self.hWaitStop, win32event.INFINITE)    # 手动停止服务
                self.log('%s -- done' % nowtime)
            except Exception as e:
                self.log('Exception: %s' % e)
                self.SvcStop()
            # 延时再检查
            win32api.Sleep(600000, True)

    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        nowtime = datetime.now().strftime("%Y.%m.%d %H:%M:%S.%f")[:-3]
        self.log('%s -- stopping' % nowtime)
        self.stop()
        self.log('%s -- stopped' % nowtime)
        win32event.SetEvent(self.hWaitStop)
        self.ReportServiceStatus(win32service.SERVICE_STOPPED)


if __name__ == "__main__":
    if len(sys.argv) == 1:
        servicemanager.Initialize()
        servicemanager.PrepareToHostSingle(AutoRunTest)
        servicemanager.StartServiceCtrlDispatcher()
    else:
        win32serviceutil.HandleCommandLine(AutoRunTest)
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     setPermissions.py
   Description :
   Author :        曾良均
   QQ:             277099728
   Date：          10/27/2021 3:45 PM
-------------------------------------------------
   Change Activity:
                   10/27/2021:
-------------------------------------------------
"""
__author__ = 'ljzeng'

import requests
from urllib import parse
import time
import sys

s = requests.session()

def setPermission(Cdata):
    url = 'http://iron.soft.rz/login/Login.aspx?tp=dologin'
    username = 'admin@iicon004.com'
    password = 'Win.12345'
    ss = username + 'ª' + password
    payload = ss.encode('utf8')
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',
        'Content-Type': 'text/plain;charset=UTF-8'}

    req = s.post(url=url, data=payload, headers=headers)
    iiabc = str(req.cookies.get_dict()).split("'")[3]

    list = []
    for a in req.text.split(','):
        list += [a]

    resu = list[0].split(':')[1]

    if resu != str(0):
        mess = list[1].split(':')[1]
        mess = mess[1:-1]
        print(mess)
        return False
    else:
        # jumpurl = list[2][11:-1]
        # print(jumpurl)
        # sys.stderr.write("登录成功！ ")

        # 登录成功，则继续编辑用户
        time.sleep(2)
        adduserurl = 'http://iron.soft.rz/custsites/5ZSAMRFPL4YAWA/Security/AddUser.aspx'
        addheaders = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'X-Requested-With': 'XMLHttpRequest',
            'Cookie': 'ir_lusname_=%s; iiabc_lang=en-us; iiabc_=%s; basemap=topo;' % (username, iiabc),
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'user-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
        }

        data = 'MethodID=-1&MethodName=EditUser&ClientData=' + parse.quote(Cdata)

        edituserRes = s.post(url=adduserurl, headers=addheaders, data=data, timeout=5)
        try:
            res = edituserRes.text.split(',')[1][1:-2]
            if res == 'Saved successfully.':
                # sys.stderr.write('\n权限设置成功\n')
                return True
            else:
                return False
        except:
            return False

if __name__ == "__main__":
    cda = '{"UserInfo":{"ID":"atpermission@iicon004.com","DisplayName":"Auto+Test+Permissions","TextAddress":"","Mobile":"","BusinessPhone":"","Active":true,"UserType":"1","IsUser":true,"AllowLoginIntoPC":true,"AllowLoginIntoInspectMobile":false,"AllowLoginIntoFleetMobile":false,"AllowMobileBarcodeScanning":false,"ContactType":"100","ManagerIID":"","Notes":"","AssignedWorkOrders":false,"EmailOptOut":false,"InspectEmailList":false,"TeamIntelligenceUser":false,"FOB":"","HourlyRate":-1,"LandingPage":"MapView.aspx","PreferredLanguage":"","IID":"5AB99F30-4CC9-4C74-98C0-57A426A72114"},"Subscribe":{"$type":"FI.FIC.Contracts.DataObjects.BaseObject.SubscribeMessageByEmail,+FICIntfAdv","NeedSendMessages":[],"UserEmail":"","UserTextMessage":""},"Features":[{"Key":100,"Value":["99999"]},{"Key":110,"Value":["0"]},{"Key":120,"Value":["0"]},{"Key":130,"Value":["0"]},{"Key":140,"Value":["0"]},{"Key":200,"Value":["99999"]},{"Key":210,"Value":["0"]},{"Key":220,"Value":["0"]},{"Key":230,"Value":["0"]},{"Key":235,"Value":["0"]},{"Key":237,"Value":["0"]},{"Key":245,"Value":["0"]},{"Key":300,"Value":["0"]},{"Key":600,"Value":["99999"]},{"Key":601,"Value":["0"]},{"Key":602,"Value":["0"]},{"Key":800,"Value":["99999"]},{"Key":900,"Value":["99999"]},{"Key":1000,"Value":["0"]},{"Key":1100,"Value":["0"]},{"Key":1101,"Value":["0"]}],"Schedule":{"$type":"FI.FIC.EmailSchedule,+FICBLC","ScheduleItems":{"$type":"FI.FIC.EmailScheduleItem[],+FICBLC","$values":[]}}}'
    print(setPermission(cda))

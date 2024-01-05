# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     loginsapi.py
   Description :
   Author :        曾良均
   QQ:             277099728
   Date：          9/8/2021 10:11 AM
-------------------------------------------------
   Change Activity:
                   9/8/2021:
-------------------------------------------------
"""
__author__ = 'ljzeng'


import requests
from urllib import parse
import json
import urllib3


def login(s, loginuser='admin@iicon004.com', pwd='Win.12345'):
    url = 'https://iron.soft.rz/login/Login.aspx?tp=dologin'
    password = pwd
    ss = loginuser + 'ª' + password
    payload = ss.encode('utf8')
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',
        'Content-Type': 'text/plain;charset=UTF-8'}

    urllib3.disable_warnings()
    print(payload)
    req = s.post(url=url, data=payload, headers=headers, verify=False)

    list = []
    for a in req.text.split(','):
        list += [a]

    resu = list[0].split(':')[1]

    if resu != str(0):
        mess = list[1].split(':')[1]
        mess = mess[1:-1]
        print("登录失败！ ")
        print(mess)
        return False
    else:
        iiabc = str(req.cookies.get_dict()).split("'")[3]
        jumpurl = list[2][11:-1]
        # print("登录成功！ ")
        # print('跳转到： ', jumpurl)
        return True, iiabc, jumpurl


def addAsset():
    sess = requests.session()
    tk = login(sess)

    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'X-Requested-With': 'XMLHttpRequest',
        'Cookie': 'ir_lusname_=admin@iicon004.com; iiabc_lang=en-us; iiabc_=%s; basemap=topo;' % tk[1],
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'user-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
    }
    aurl = 'https://iron.soft.rz/custsites/5ZSAMRFPL4YAWA/MachineDeviceManagement/AddMachine.aspx'
    sour = '{"VIN":"autoTestDelAsset","Name":"autoTestDelAsset","Name2":"autoTestDelAsset","MakeYear":"2011","MakeID":"2","MakeName":"KOMATSU","ModelID":"249","ModelName":"PC88","TypeID":"7","EngineHours":-1,"ContractorID":"","ODOMeter":-1,"OdometerUnits":"","UnderCarriageHours":null,"OnSiteJobsiteIDs":[],"ContactIDs":[],"MachineGroupIDs":[],"AquisitionType":"Leased","Hidden":false,"OnRoad":true,"TelematicsEnabled":false,"Attachment":false,"CostCenter":"","EQClass":"","Description":"API+add","ID":-1,"MachineAttributes":[{"ID":67,"DisplayText":"Always+On","Format":"VARCHAR(30)","Description":"Select+Yes+to+notify+that+asset+has+been+turned+off.++Must+subscribe+to+alert.","DataType":0,"Multiline":false,"Length":30,"Precision":0,"Value":null,"Dropdown":true,"DataSource":"No;Yes"},{"ID":93,"DisplayText":"Current+Jobsite+Completion","Format":"DATETIME2","Description":"Jobsite+Complete+Date","DataType":4,"Multiline":false,"Length":100,"Precision":0,"Value":"","Dropdown":false,"DataSource":""},{"ID":69,"DisplayText":"Next+Jobsite+Assignment","Format":"VARCHAR(100)","Description":"Next+Jobsite+Assignment","DataType":0,"Multiline":false,"Length":100,"Precision":0,"Value":"","Dropdown":false,"DataSource":""},{"ID":70,"DisplayText":"Future+Assignment+Date","Format":"DATETIME2","Description":"Future+Assignment+Date","DataType":4,"Multiline":false,"Length":100,"Precision":0,"Value":"","Dropdown":false,"DataSource":""},{"ID":71,"DisplayText":"Custom+Status","Format":"VARCHAR(100)","Description":"Custom+Status","DataType":0,"Multiline":false,"Length":100,"Precision":0,"Value":"","Dropdown":false,"DataSource":""},{"ID":31,"DisplayText":"Fuel+Cost","Format":"DECIMAL(18,2)","Description":"GENERAL+ATTRIBUTES","DataType":3,"Multiline":false,"Length":18,"Precision":2,"Value":"","Dropdown":false,"DataSource":""},{"ID":32,"DisplayText":"Fuel+Cost+UOM","Format":"VARCHAR(10)","Description":"GENERAL+ATTRIBUTES","DataType":0,"Multiline":false,"Length":10,"Precision":0,"Value":"","Dropdown":false,"DataSource":""},{"ID":33,"DisplayText":"Machine+Rate","Format":"DECIMAL(18,2)","Description":"GENERAL+ATTRIBUTES","DataType":3,"Multiline":false,"Length":18,"Precision":2,"Value":"","Dropdown":false,"DataSource":""},{"ID":36,"DisplayText":"Work+Type","Format":"VARCHAR(100)","Description":"GENERAL+ATTRIBUTES","DataType":0,"Multiline":false,"Length":100,"Precision":0,"Value":"","Dropdown":false,"DataSource":""},{"ID":58,"DisplayText":"Fuel+Type","Format":"VARCHAR(50)","Description":"GENERAL+ATTRIBUTES","DataType":0,"Multiline":false,"Length":50,"Precision":0,"Value":null,"Dropdown":true,"DataSource":"Diesel;Gas"},{"ID":61,"DisplayText":"Fuel+Card+ID","Format":"VARCHAR(20)","Description":"GENERAL+ATTRIBUTES","DataType":0,"Multiline":false,"Length":20,"Precision":0,"Value":"","Dropdown":false,"DataSource":""},{"ID":68,"DisplayText":"Fuel+Tank+Size","Format":"DECIMAL(18,2)","Description":"GENERAL+ATTRIBUTES","DataType":3,"Multiline":false,"Length":18,"Precision":2,"Value":"","Dropdown":false,"DataSource":""},{"ID":74,"DisplayText":"Load+Capacity+(tons)","Format":"int","Description":"GENERAL+ATTRIBUTES","DataType":1,"Multiline":false,"Length":100,"Precision":0,"Value":"","Dropdown":false,"DataSource":""},{"ID":39,"DisplayText":"Lease+Start+Date","Format":"datetime2","Description":"LEASE+MANAGEMENT","DataType":4,"Multiline":false,"Length":100,"Precision":0,"Value":"","Dropdown":false,"DataSource":""},{"ID":40,"DisplayText":"Lease+End+Date","Format":"datetime2","Description":"LEASE+MANAGEMENT","DataType":4,"Multiline":false,"Length":100,"Precision":0,"Value":"","Dropdown":false,"DataSource":""},{"ID":42,"DisplayText":"Lease+Term","Format":"int","Description":"LEASE+MANAGEMENT","DataType":1,"Multiline":false,"Length":100,"Precision":0,"Value":"","Dropdown":false,"DataSource":""},{"ID":59,"DisplayText":"Lease+Term+UOM","Format":"VARCHAR(50)","Description":"LEASE+DETAILS","DataType":0,"Multiline":false,"Length":50,"Precision":0,"Value":null,"Dropdown":true,"DataSource":"Hours;Miles;Kilometers"},{"ID":60,"DisplayText":"Overage+per+unit","Format":"DECIMAL(18,2)","Description":"LEASE+DETAILS","DataType":3,"Multiline":false,"Length":18,"Precision":2,"Value":"","Dropdown":false,"DataSource":""},{"ID":1,"DisplayText":"Acquisition+Cost","Format":"DECIMAL(18,2)","Description":"THIS+IS+CAPTURE+ACQUISITION+COST+FOR+MACHINES+FOR+LIFECYCLE+MANAGEMENT","DataType":3,"Multiline":false,"Length":18,"Precision":2,"Value":"","Dropdown":false,"DataSource":""},{"ID":2,"DisplayText":"Vendor","Format":"VARCHAR(100)","Description":"CAPTURE+VENDOR+EQUIPMENT+WAS+AQUIRED+FROM+","DataType":0,"Multiline":false,"Length":100,"Precision":0,"Value":"","Dropdown":false,"DataSource":""},{"ID":3,"DisplayText":"Acquisition+Date","Format":"DATETIME2","Description":"CAPTURE+AQUISITION+DATE","DataType":4,"Multiline":false,"Length":100,"Precision":0,"Value":"","Dropdown":false,"DataSource":""},{"ID":37,"DisplayText":"Retirement+Hours","Format":"DECIMAL(18,2)","Description":"LIFECYCLE+MANAGEMENT","DataType":3,"Multiline":false,"Length":18,"Precision":2,"Value":"","Dropdown":false,"DataSource":""},{"ID":5,"DisplayText":"Sale+Value","Format":"DECIMAL(18,2)","Description":"CAPTURE+SALE+VALUE","DataType":3,"Multiline":false,"Length":18,"Precision":2,"Value":"","Dropdown":false,"DataSource":""},{"ID":7,"DisplayText":"Sold+To","Format":"VARCHAR(100)","Description":"CAPTURE+WHO+EQUIPMENT+WAS+SOLD+TO","DataType":0,"Multiline":false,"Length":100,"Precision":0,"Value":"","Dropdown":false,"DataSource":""},{"ID":8,"DisplayText":"Sale+Date","Format":"DATETIME2","Description":"CAPTURE+SALE+DATE","DataType":4,"Multiline":false,"Length":100,"Precision":0,"Value":"","Dropdown":false,"DataSource":""},{"ID":9,"DisplayText":"Acquisition+Hours","Format":"DECIMAL(18,2)","Description":"CAPTURE+HOURS+AT+TIME+OF+ACQUISITION","DataType":3,"Multiline":false,"Length":18,"Precision":2,"Value":"","Dropdown":false,"DataSource":""},{"ID":10,"DisplayText":"Acquisition+Odometer","Format":"DECIMAL(18,2)","Description":"CAPTURE+ODOMETER+READING+AT+TIME+OF+ACQUISITION","DataType":3,"Multiline":false,"Length":18,"Precision":2,"Value":"","Dropdown":false,"DataSource":""},{"ID":64,"DisplayText":"Hourly+Cost+of+Idle","Format":"DECIMAL(18,2)","Description":"Hourly+Cost+of+Idle","DataType":3,"Multiline":false,"Length":18,"Precision":2,"Value":"","Dropdown":false,"DataSource":""},{"ID":65,"DisplayText":"Target+Idle+Percent","Format":"DECIMAL(18,2)","Description":"Target+Idle+Percent","DataType":3,"Multiline":false,"Length":18,"Precision":2,"Value":"","Dropdown":false,"DataSource":""},{"ID":87,"DisplayText":"Error+Message","Format":"VARCHAR(300)","Description":"Error+Message","DataType":0,"Multiline":false,"Length":300,"Precision":0,"Value":"","Dropdown":false,"DataSource":""},{"ID":90,"DisplayText":"Telematic+Comments","Format":"VARHCAR(300)","Description":"Telematics+Comments","DataType":0,"Multiline":false,"Length":1000,"Precision":0,"Value":"","Dropdown":false,"DataSource":""},{"ID":51,"DisplayText":"License+Tag","Format":"VARCHAR(30)","Description":"OTR+ATTRIBUTES","DataType":0,"Multiline":false,"Length":30,"Precision":0,"Value":"","Dropdown":false,"DataSource":""},{"ID":52,"DisplayText":"License+Tag+Date","Format":"DATETIME2","Description":"OTR+ATTRIBUTES","DataType":4,"Multiline":false,"Length":100,"Precision":0,"Value":"","Dropdown":false,"DataSource":""},{"ID":53,"DisplayText":"Inspection+Date","Format":"DATETIME2","Description":"OTR+ATTRIBUTES","DataType":4,"Multiline":false,"Length":100,"Precision":0,"Value":"","Dropdown":false,"DataSource":""},{"ID":54,"DisplayText":"DOT+ID+1","Format":"VARCHAR(30)","Description":"OTR+ATTRIBUTES","DataType":0,"Multiline":false,"Length":30,"Precision":0,"Value":"","Dropdown":false,"DataSource":""},{"ID":55,"DisplayText":"DOT+ID+2","Format":"VARCHAR(30)","Description":"OTR+ATTRIBUTES","DataType":0,"Multiline":false,"Length":30,"Precision":0,"Value":"","Dropdown":false,"DataSource":""},{"ID":56,"DisplayText":"GVWR","Format":"DECIMAL(18,2)","Description":"Gross+Vehicle+Weight+Rating","DataType":3,"Multiline":false,"Length":18,"Precision":2,"Value":"","Dropdown":false,"DataSource":""},{"ID":57,"DisplayText":"Toll+Pass","Format":"VARCHAR(20)","Description":"OTR+ATTRIBUTES","DataType":0,"Multiline":false,"Length":20,"Precision":0,"Value":"","Dropdown":false,"DataSource":""},{"ID":63,"DisplayText":"Asset+Size","Format":"VARCHAR(20)","Description":"This+determines+classification+for+thresholds+for+Driver+Behavior+alerts/charts.","DataType":0,"Multiline":false,"Length":20,"Precision":0,"Value":"","Dropdown":true,"DataSource":";Passenger;Small+Truck/Van;Large+Truck"},{"ID":95,"DisplayText":"Sales+Tax","Format":"DECIMAL(18,2)","Description":"Sales+Tax","DataType":3,"Multiline":false,"Length":18,"Precision":2,"Value":"","Dropdown":false,"DataSource":""},{"ID":96,"DisplayText":"Property+Tax","Format":"DECIMAL(18,2)","Description":"Property+Tax","DataType":3,"Multiline":false,"Length":18,"Precision":2,"Value":"","Dropdown":false,"DataSource":""}],"IgnoreDuplicate":false}'
    cdata = 'MethodID=-1&MethodName=SaveMachine&ClientData=' + parse.quote(sour)

    # addassets = sess.post(url=aurl, headers=headers, data=cdata)
    # result = addassets.text
    # print('***', result)

    try:
        addassets = sess.post(url=aurl, headers=headers, data=cdata, verify=False)
    except:
        return False
    else:
        res = json.loads(addassets.text)
        if res["Result"] == 1:
            # print('添加的机器ID为： ', res["Data"][0])
            return True


if __name__ == '__main__':
    s = requests.session()
    r = login(s=s)
    # print(r)
    print("token: %s" % r[1])
    print("URL: %s" % r[2][:45])

    # addAsset()


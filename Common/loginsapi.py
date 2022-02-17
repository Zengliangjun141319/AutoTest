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


def login(s, loginuser='admin@iicon004.com', pwd='Win.12345'):
    url = 'http://iron.soft.rz/login/Login.aspx?tp=dologin'
    password = pwd
    ss = loginuser + 'ª' + password
    payload = ss.encode('utf8')
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',
        'Content-Type': 'text/plain;charset=UTF-8'}

    req = s.post(url=url, data=payload, headers=headers)

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



if __name__ == '__main__':
    s = requests.session()
    r = login(s=s)
    # print(r)
    print("token: %s" % r[1])
    print("URL: %s" % r[2][:45])


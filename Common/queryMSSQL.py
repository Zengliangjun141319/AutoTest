# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     queryMSSQL.py
   Description :
   Author :        曾良均
   QQ:             277099728
   Date：          8/24/2021 11:22 AM
-------------------------------------------------
   Change Activity:
                   8/24/2021:
-------------------------------------------------
"""
__author__ = 'ljzeng'

import pymssql
from bs4 import BeautifulSoup
import time
import datetime

def getTempPassword(dt, type,uid, server='192.168.25.215\\ironintel', user='fi', pw='database'):
    conn = pymssql.connect(server, user, pw, dt)
    cur = conn.cursor()  # 获取光标
    if not cur:
        raise (NameError, "数据库连接失败")

    sqlstr = "select mailbody from SYS_APPMAILS_BODY where mailid in(select top 1 mailid from SYS_APPMAILS where title='%s' and TOADDRESS='%s' order by ADDEDON desc)" % (type,uid)
    cur.execute(sqlstr)

    data = cur.fetchone()
    data = str(data)[2:-3]
    # print(data)

    soup = BeautifulSoup(data, 'lxml')

    elemnet = soup.find('h3')
    if elemnet is None:
        elemnet = soup.find_all('span', limit=5)
        temppw = elemnet[4].text
    else:
        temppw = str(elemnet).split(':')[1][1:-5]


    cur.close()
    conn.close()
    return temppw


def getUserIID(dt, userid, server='192.168.25.215\\ironintel', user='fi', pw='database'):
    conn = pymssql.connect(server, user, pw, dt)
    cur = conn.cursor()  # 获取光标
    if not cur:
        raise (NameError, "数据库连接失败")

    sqlstr = "select useriid from sys_users where userid='%s'" %userid
    cur.execute(sqlstr)

    data = cur.fetchone()
    useriid = str(data)[2:-3]

    cur.close()
    conn.close()
    return useriid

def getPWExpiration(dt, userid, server='192.168.25.215\\ironintel', user='fi', pw='database'):
    conn = pymssql.connect(server, user, pw, dt)
    cur = conn.cursor()  # 获取光标
    if not cur:
        raise (NameError, "数据库连接失败")

    sqlstr = "select convert(varchar(100),PWDEXPIRATION,120) from sys_users where userid='%s'" % userid
    cur.execute(sqlstr)

    data = cur.fetchone()
    # print(data)
    ExpTime = str(data)[2:-3]

    cur.close()
    conn.close()
    return ExpTime

def checksendmail(category, toadd, st, tt, server='192.168.25.215\\ironintel', user='fi', pw='database', dt='FORESIGHT_SERVICES'):
    conn = pymssql.connect(server, user, pw, dt)
    cur = conn.cursor()  # 获取光标
    if not cur:
        raise (NameError, "数据库连接失败")

    sqlstr = "select mailid from SYS_APPMAILS where CATEGORY='%s' and (ADDEDON between '%s' and '%s') and TOADDRESS='%s'" %(category, st, tt, toadd)
    cur.execute(sqlstr)

    data = cur.fetchone()
    # print(data[0])
    if data:
        # data = str(data)[2:-3]
        data = data[0]
        print('sent mail sucessfuly, mailid is ', data)

        cur.close()
        conn.close()
        return True
    else:
        print('send falier')

        cur.close()
        conn.close()
        return False

def commQuery(dt, sqlstr, server='192.168.25.215\\ironintel', user='fi', pw='database'):
    conn = pymssql.connect(server, user, pw, dt)
    cur = conn.cursor()  # 获取光标
    if not cur:
        raise (NameError, "数据库连接失败")

    cur.execute(sqlstr)
    data = cur.fetchall()

    cur.close()
    conn.close()
    return data

def delSQL(dt, sqlstr, server='192.168.25.215\\ironintel', user='fi', pw='database'):
    conn = pymssql.connect(server, user, pw, dt)
    cur = conn.cursor()
    if not cur:
        raise (NameError, "数据库连接失败")

    if 'delete' or 'update' in sqlstr:
        sqlstr += ";commit"

    try:
        cur.execute(sqlstr)
    except:
        conn.rollback()

    cur.close()
    conn.close()

def updateSQL(dt, sqlstr, server='192.168.25.215\\ironintel', user='fi', pw='database'):
    conn = pymssql.connect(server, user, pw, dt)
    cur = conn.cursor()
    if not cur:
        raise (NameError, "数据库连接失败")

    if 'delete' or 'update' in sqlstr:
        sqlstr += ";commit"

    try:
        cur.execute(sqlstr)
    except:
        conn.rollback()

    cur.close()
    conn.close()


if __name__ == "__main__":
    '''
    # 测试 getTempPassword
    sqls = "Forgot Password"
    ss = getTempPassword('FORESIGHT_SERVICES', type=sqls)
    print("Temp Password is :", ss)

    # 测试getUserIID
    userid = 'zljun8210@live.cn'
    ds = getUserIID('ironintel', userid=userid)
    print("userIID is: ", ds)
    '''
    # 测试 getPWExpiration
    # sqls = 'testforgotpw@iicon004.com'
    # times = getPWExpiration('ironintel', userid=sqls)
    # print("Password Expiration Time is： ", times)

    '''
    # 测试 checksendmail
    sendtime = datetime.datetime.now()
    sendtime = sendtime - datetime.timedelta(hours=8)
    totime = sendtime + datetime.timedelta(minutes=1)
    sendtime = sendtime.strftime("%Y-%m-%d %H:%M")
    totime = totime.strftime("%Y-%m-%d %H:%M")
    category = 'Asset-LocationMessage'
    toaddress = 'zljun8210@live.cn'
    checksendmail(category=category, toadd=toaddress, st=sendtime, tt=totime)

    category = 'Jobsite-AlertMessage'
    checksendmail(category=category, st=sendtime, tt=totime)


    # 测试commQuery:多字段、多记录
    dt = 'FORESIGHT_FLV_IICON004_New'
    sqlstr = "select attribute,datasource from PrimaryDataSource group by Attribute,DataSource order by Attribute"
    res = commQuery(dt, sqlstr)
    for d in res:
        print(d)
    
    
    # test delSQL
    dt = 'ironintel'
    sql = "delete  from SYS_COMPANY_COMMENTS where COMPANYID='IICON004' and USERIID='FFC597D3-BDA5-4B5D-8250-7C253BDE4409'"

    delSQL(dt, sql)

    time1 = '2030-12-31 00:00:00.000'
    userid = 'admin@iron001.com'
    dt = 'ironintel'
    sqlu = "update sys_users set PWDEXPIRATION='%s' where userid='%s'" %(time1, userid)
    sqlq = "select * from sys_users where userid='%s'" %userid
    updateSQL(dt=dt, sqlstr=sqlu)
    res = commQuery(dt=dt, sqlstr=sqlq)
    for r in res:
        print(r)
    '''

    #
    # dt = 'ironintel'
    # sqls = "select appver from SYS_CUSTSITES where COMPANYID='iicon004'"
    # vers = commQuery(dt=dt, sqlstr=sqls)
    # ver = vers[0]
    # print("ver: %s" % ver)


    dta = 'ironintel_admin'
    dtm = 'IICON_001_FLVMST'
    sqlstr = "delete from machines where machinename like '%an%' "
    delSQL(dtm, sqlstr)
    delSQL(dta, sqlstr)

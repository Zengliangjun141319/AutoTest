# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     execProduce.py
   Author :        曾良均
   QQ:             277099728
   Date：          6/25/2023 2:37 PM   
   Description :
-------------------------------------------------
   Change Activity:
                   
-------------------------------------------------
"""
__author__ = 'ljzeng'

import random
from queryMSSQL import *
import sys


def getdatedays(start):
    '''
    计算到现在相差几天，入参为结束日期，返回值为数值
    '''

    start = datetime.datetime.strptime(start, "%Y-%m-%d")
    nowtime = time.strftime("%Y-%m-%d")  # 获取当前时间，格式为年－月－日 时：分：秒
    now = datetime.datetime.strptime(nowtime, "%Y-%m-%d")  # 转换当前日期为指定格式，以便于计算
    d = now - start
    return d.days


class ExecProduce:
    def updateenghours(self):
        '''
        查询AssetEngineHours数据，并判断具体数据后调用存储过程来更新数据
        '''
        dt = 'FORESIGHT_FLV_IICON004_New'
        sqlstr = "select AssetId,Datasource,RefId,convert(varchar(100),AsofTime,120),ResetTime,Amount,UOM,MsgUID,Subsource from AssetEngineHours where Datasource='calamp' and AsofTime is not NULL and UOM='Hour'"
        res = commQuery(dt, sqlstr)
        count = 0
        for data in res:
            asoftime = data[3].split(" ")[0]  # 截取字符串前半部分即 年－月－日
            days = getdatedays(asoftime)
            rands = random.randint(5, 8)
            if days > rands:
                assetid = data[0]
                sys.stderr.write('update assetid: %s \n' % assetid)
                refid = data[2]
                amount = data[5]
                works = random.randint(1, 8)
                result = amount + (days * works)
                msguid = data[7]
                curentdate = str(time.strftime("%Y-%m-%d %H:%M:%S")) + '.243'
                sql = []
                sql.append("exec [dbo].[pro_updateassetenginehours] @assetid=%d,@datasrc = N'Calamp',@refid = N'%s',@asoftime =N'%s',@resettime = NULL,@amount = %d,@uom = N'Hour',@msgid = N'%s',@subsrc = ''")
                sql = '\n' .join(sql) % (assetid, refid, curentdate, result, msguid)
                execproce(dt=dt, sqlstr=sql)
                count += 1
        sys.stderr.write('Asset Engine Hours updated asset: %d pcs! \n' % count)

    def updateodo(self):
        '''
        查询AssetEngineOdometer数据，并判断具体数据后调用存储过程来更新数据
        '''
        dt = 'FORESIGHT_FLV_IICON004_New'
        sqlstr = "select AssetId,Datasource,RefId,convert(varchar(100),AsofTime,120),ResetTime,Odometer,UOM,MsgUID,Subsource,State from AssetOdometer where Datasource='calamp' and AsofTime is not NULL"
        res = commQuery(dt, sqlstr)
        count = 0
        for data in res:
            asoftime = data[3].split(" ")[0]  # 截取字符串前半部分即 年－月－日
            days = getdatedays(asoftime)
            rands = random.randint(5, 8)
            if days > rands:
                assetid = data[0]
                sys.stderr.write('update assetid: %s \n' % assetid)
                refid = data[2]
                odo = data[5]
                works = random.randint(1, 8)
                result = odo + (days * works * 60)
                UOM = data[6]
                msguid = data[7]
                subs = data[8]
                curentdate = str(time.strftime("%Y-%m-%d %H:%M:%S")) + '.243'
                sql = []
                sql.append("exec [dbo].[pro_updateassetodometer] @assetid=%d,@datasrc = N'Calamp',@refid = N'%s',@asoftime =N'%s',@resettime = NULL,@odo = %d,@uom = N'%s',@msgid = N'%s',@subsrc = N'%s',@state=''")
                sql = '\n' .join(sql) % (assetid, refid, curentdate, result, UOM, msguid, subs)
                execproce(dt=dt, sqlstr=sql)
                count += 1
        sys.stderr.write('Asset Odometer updated asset: %d pcs! \n' % count)


if __name__ == "__main__":
    ExecProduce.updateenghours(None)
    ExecProduce.updateodo(None)
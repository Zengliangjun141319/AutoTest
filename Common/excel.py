# -*- coding:utf-8 -*-

'''
@author: 曾良均
@file: excel.py
@time: 2017/12/19 13:12
'''

import xlrd
import os
'''
最新版的xlrd不支持读取xlsx，需安装旧版本
#卸载已安装的
pip uninstall xlrd 

#下载对应的版本
pip install xlrd==1.2.0
'''

class excel:
    def open_excel(excelfile):
        u'''读取Excel文件'''
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        # print(BASE_DIR)
        excelfile = os.path.join(BASE_DIR, excelfile)
        try:
            data = xlrd.open_workbook(excelfile)
            return data
        except Exception as e:
            raise e

    def excel_table(excelfile, sheetName):
        u'''加载数据到List'''
        data = excel.open_excel(excelfile)
        # data = xlrd.open_workbook(excelfile)
        # 通过工作表名称，获取到一个工作表
        table = data.sheet_by_name(sheetName)
        # table = data.sheet_by_index(0)
        # 获取行数
        Trows = table.nrows
        # 获取第一行数据
        Tcolnames = table.row_values(0)
        #　print('第一行数据为： %s ' % Tcolnames)
        lister = []
        for rownumber in range(1, Trows):
            row = table.row_values(rownumber)
            if row:
                app = {}
                for i in range(len(Tcolnames)):
                    app[Tcolnames[i]] = row[i]
                lister.append(app)
        return lister

    def get_list(excelfile, sheetname=u'Sheet1'):
        try:
            data_list = excel.excel_table(excelfile, sheetname)
            assert len(data_list)>0, u'Excel标签页：' + sheetname + u'为空'
            return data_list
        except Exception as e:
            raise e

if __name__ == '__main__':
    root = None
    files = u'./TestCase/API/loginData.xlsx'
    datas = excel.get_list(files, 'Sheet1')
    for line in datas:
        print(line)

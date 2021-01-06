"""  -*- coding:utf-8 -*-
 @File      :get_exceldata.py
 @Time      :2020/12/1617:37
 @Autor     :张娟娜
 @Email     :1136189505@qq.com
 @Software  :PyCharm
 """
import xlrd
import pprint
import json

def get_excel(sheetname):
    """
    :param sheetname: sheet页名称
    :return:
    """
    # formatting_info = True 保持表样式
    workbook=xlrd.open_workbook('../datas/外卖系统接口测试用例.xls',formatting_info=True)
    worksheet=workbook.sheet_by_name(sheetname)
    testdata=[]
    for i in range(1,worksheet.nrows):
        reqdata=worksheet.cell_value(i,9)
        respdata=worksheet.cell_value(i,11)
        testdata.append((reqdata,respdata))

    return testdata

# 根据用例编码获取执行用例的数据,返回数据为json
def get_exceldata2(sheetname,casename):
    # 数据列表
    datalist=[]
    workbook=xlrd.open_workbook('../datas/外卖系统接口测试用例.xls',formatting_info=True)
    worksheet=workbook.sheet_by_name(sheetname)
    for one in range(1,worksheet.nrows):
        name=worksheet.cell_value(one,0)
        # print(one)
        # print(name)
        if casename in name:
            # 转化输出字典格式的数据
            reqdata=json.loads(worksheet.cell_value(one,9))
            respdata=json.loads(worksheet.cell_value(one,11))
            num=worksheet.cell_value(one,0)
            # reqdata=worksheet.cell_value(one,9)
            # respdata=worksheet.cell_value(one,11)
            datalist.append((reqdata,respdata,num))
            print(worksheet.cell_value(one,0))
            print(reqdata)
            print(respdata)

    return datalist

if __name__ == '__main__':
    print(type(get_exceldata2("我的商铺","listshopping")[0][0]))
    print(type(get_exceldata2("食品管理","Addfoodkind")[0][0]))
    print(get_exceldata2("我的商铺", "listshopping")[0][0])
    print(get_exceldata2("食品管理", "Addfoodkind"))

"""  -*- coding:utf-8 -*-
 @File      :test_foodmanage.py
 @Time      :2021/1/418:45
 @Autor     :张娟娜
 @Email     :1136189505@qq.com
 @Software  :PyCharm
 """
import pytest
from tools.get_exceldata import get_exceldata2
from apiLib.foodManage import foodManage

class Test_foodmanage():
    @pytest.mark.parametrize("indata,respdata,num",get_exceldata2("食品管理","Addfoodkind"))
    def test_addfoodkind(self,indata,respdata,num,get_token,get_image):
        res=foodManage(get_token,get_image).add_foodkind(indata)
        print(num)
        print(res)
        if 'error' in res:
            assert res['error'] == respdata['error']
        else:
            assert res['code'] == respdata['code']

    @pytest.mark.parametrize("indata,respdata,num",get_exceldata2('食品管理',"Addfood0"))
    def test_addfood(self,indata,respdata,num,get_token,get_image):
        res=foodManage(get_token,get_image).add_food(indata)
        print(num)
        print(res)
        if 'error' in res:
            assert res['error']==respdata['error']
        else:
            assert res['code']==respdata['code']

    @pytest.mark.parametrize("indata,respdata,num",get_exceldata2('食品管理',"listfood"))
    def test_listfood(self,indata,respdata,num,get_token,get_image):
        res=foodManage(get_token,get_image).list_food(indata)
        print(num)
        print(res)
        if 'error' in res:
            assert res['error']==respdata['error']
        else:
            assert res['code']==respdata['code']

    @pytest.mark.parametrize('indata,respdata,num',get_exceldata2("食品管理","updatefood"))
    def test_updatefood(self,indata,respdata,num,get_token,get_image):
        res=foodManage(get_token,get_image).updtate_food(indata)
        print(num)
        print(res)
        if 'error' in res:
            assert res['error']==respdata['error']
        else:
            assert res['code']==respdata['code']

    @pytest.mark.parametrize("indata,respdata,num",get_exceldata2("食品管理","deletefood"))
    def test_deletefood(self,indata,respdata,num,get_token,get_image):
        res=foodManage(get_token,get_image).delete_food(indata)
        print(num)
        print(res)
        if 'error' in res:
            assert res['error'] == respdata['error']
        else:
            assert res['code'] == respdata['code']


if __name__ == '__main__':
    pytest.main(['test_foodmanage.py','-s'])
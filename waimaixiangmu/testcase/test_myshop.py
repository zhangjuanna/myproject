"""  -*- coding:utf-8 -*-
 @File      :test_myshop.py
 @Time      :2020/12/2119:49
 @Autor     :张娟娜
 @Email     :1136189505@qq.com
 @Software  :PyCharm
 """
from apiLib.MyShop import Myshop
import pytest
import os
from tools.get_exceldata import get_exceldata2
import allure

from apiLib.Login import Login
class Test_myshop():
    # def setup_class(self):#每一个类下面所有的方法调用只运行一次
    #     self.token = Login().login({"username":"sq0777","password":"xintian"})

    @pytest.mark.parametrize("indata,respdata",get_exceldata2("我的商铺","listshopping"))
    def test_listshopping(self,indata,respdata,get_token):
        res=Myshop(get_token).shopping_list(indata)
        if 'code' in res:
            assert res["code"]==respdata["code"]
        else:
            assert res["error"]==respdata["error"]

    @pytest.mark.parametrize("indata,respdata",get_exceldata2('我的商铺','update'))
    def test_updateshopping(self,indata,respdata,get_token,get_image):
        res=Myshop(get_token).shop_update(indata,get_image[0],get_image[1])
        assert res['code']==respdata['code']




if __name__ == '__main__':
    # pytest.main(["test_myshop.py","-s", '--alluredir', '../report/tmp'])
    for one in os.listdir('../report/tmp'):  # 列出对应文件夹的数据
        if 'json' in one:
            os.remove(f'../report/tmp/{one}')
    pytest.main(["test_myshop.py", "-s", '--alluredir', '../report/tmp'])
    os.system('allure serve ../report/tmp')

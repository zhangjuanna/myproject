"""  -*- coding:utf-8 -*-
 @File      :test_login.py
 @Time      :2020/12/1815:21
 @Autor     :张娟娜
 @Email     :1136189505@qq.com
 @Software  :PyCharm
 """
from apiLib.Login import Login
from tools.get_exceldata import get_exceldata2
import pytest
import json

class Test_login():
    @pytest.mark.parametrize("indata,respdata",get_exceldata2("登录模块","Login"))
    def test_Login001(self,indata,respdata):
        resp=Login.login(indata,gettoken=False)
        assert resp["msg"]==respdata["msg"]

if __name__ == '__main__':
    pytest.main(["test_login.py","-s"])
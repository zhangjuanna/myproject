"""  -*- coding:utf-8 -*-
 @File      :login.py
 @Time      :2020/12/1410:17
 @Autor     :张娟娜
 @Email     :1136189505@qq.com
 @Software  :PyCharm
 """

from configs.config import HOST
import requests
import hashlib
import json

# md5加密函数，用作加密密码
def get_md5(paswd):
    md5=hashlib.md5()
    md5.update(paswd.encode("utf-8"))
    return md5.hexdigest()

# 登录类，登录函数
class Login():
    def login(self,indate,gettoken=True):
        indate['password']=get_md5(indate['password'])
        paylod=indate
        res=requests.post(url=f'{HOST}/account/sLogin',params=paylod)
        if gettoken==True:
            return res.json()['data']['token']
        else:
            return res.json()

if __name__ == '__main__':
    print(Login().login({"username":"sq0777","password":"xintian"}))
"""  -*- coding:utf-8 -*-
 @File      :conftest.py
 @Time      :2020/12/2417:36
 @Autor     :张娟娜
 @Email     :1136189505@qq.com
 @Software  :PyCharm
 """

import pytest
from apiLib.Login import Login
from apiLib.MyShop import Myshop
from configs.config import logindate
from tools.get_exceldata import get_exceldata2
from apiLib.foodManage import foodManage

@pytest.fixture(scope='session')
def get_token():
    token=Login().login({"username":"sq0777","password":"xintian"},gettoken=True)
    print(token)
    return token

@pytest.fixture(scope='function')
def get_image():
    token = Login().login({"username": "sq0777", "password": "xintian"}, gettoken=True)
    image=Myshop(token).file_upload('123.png','../datas/123.png')
    shopid=Myshop(token).shopping_list({'page':1,'limit':20})['data']['records'][0]['id']
    # print("--------------我的商铺-----------------")
    return shopid,image

# @pytest.fixture(scop='session')
# def updtate_food_init():
#     token=Login().login(logindate,gettoken=True)
#     image=Myshop(token).file_upload("123.png","../datas/123.png")
#     indate=get_exceldata2('食品管理','Addfood010')[0]
#     res=foodManage.add_food(indate)
#     yield image






if __name__ == '__main__':
    print(get_image)
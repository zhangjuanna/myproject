"""  -*- coding:utf-8 -*-
 @File      :foodManage.py
 @Time      :2020/12/3010:44
 @Autor     :张娟娜
 @Email     :1136189505@qq.com
 @Software  :PyCharm
 """

from configs.config import HOST,logindate
import requests
from apiLib.Login import Login


class foodManage():
    def __init__(self,token,imageinfo):
        self.headers={"Authorization":token}
        self.image=imageinfo

    # 新增商品分类
    def add_foodkind(self,indata):
        payload=indata
        resp=requests.post(url=f'{HOST}/shopping/addcategory',params=payload,headers=self.headers)
        return resp.json()

    # 新增商品
    def add_food(self,indata):
        # 如果传参中含图片信息，则更新图片信息
        # 食品分类ID,店铺id
        if 'image_path' in indata:
            indata["image_path"]=self.image
        payload=indata
        resp=requests.post(url=f'{HOST}/shopping/addmyfood',params=payload,headers=self.headers)
        return resp.json()

    # 列出商品
    def list_food(self,indata):
        payload=indata
        resp=requests.get(url=f"{HOST}/shopping/v2/myFoods",params=payload,headers=self.headers)
        return resp.json()

    # 编辑商品
    def updtate_food(self,indata,**kw):
        """
        id 食品 id                列出食品的 item_id 字段

        idMenu 必填 食品分类 id   列出食品的 category_id 字段
        idShop 必填 店铺 ID       列出食品的 restaurant_id 字段
        imagePath 选填 图片名称   上传图片接口返回值 realFileName 字段
        name 必填 食品名称
        specsJson 必填 规 格 json 格 式 如 ： [{"specs":" 默 认 ","packing_fee":0,"price":20}]
        :param indata:
        :return:
        """
        indata.update(kw)
        payload=indata
        resp=requests.post(url=f'{HOST}/shopping/v2/updatemyfood',params=payload,headers=self.headers)
        return resp.json()



    def delete_food(self,id):
        """

        :param id: 为食品 id
        :return:
        """

        resp=requests.delete(url=f'{HOST}/shopping/v2/fooddel/{id}',headers=self.headers)
        return resp.json()

# if __name__ == '__main__':
    # token=Login().login(logindate,gettoken=True)
    # res=foodManage(token,111).list_food({"page":1,"limit":1})
    # print(res['data']['records'][0]['item_id'])
    # print(res['data']['records'][0]['category_id'])
    # print(res['data']['records'][0]['restaurant_id'])
    # print(res['data']['records'][0]['realFileName    # print(res2)
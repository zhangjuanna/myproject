"""  -*- coding:utf-8 -*-
 @File      :MyShop.py
 @Time      :2020/12/1411:36
 @Autor     :张娟娜
 @Email     :1136189505@qq.com
 @Software  :PyCharm
 """
from apiLib.Login import Login
import requests
from configs.config import HOST,logindate
from apiLib.Login import Login
import json

class Myshop:
    def __init__(self,token):
        self.heads={"Authorization":token}
    # 列出商铺
    def shopping_list(self,indate):
        # payload=json.loads(indate)
        payload=indate
        resp=requests.get(url=f'{HOST}/shopping/myShop',params=payload,headers=self.heads)
        return resp.json()

    def shop_list(self, inData):
        payload = inData
        url = f'{HOST}/shopping/myShop'
        resp = requests.get(url, headers=self.header, params=payload)
        return resp.json()  # 响应数据

    def file_upload(self,fileName,fileDir):
        # 组装文件对象
        user_file={'file':(fileName,open(fileDir,'rb'),'image/png')}

        resp=requests.post(f'{HOST}/file',files=user_file,headers=self.heads)
        return resp.json()['data']['realFileName']

    def shop_update(self,indate,shopid,imageinfo):
        """

        :param indate: 请求参数
        :param shopid: 修改的店铺id
        :param imageinfo: 图片信息
        :return:
        """
        indate['id']=shopid
        indate['image_path']=imageinfo
        indate["image"]=f'{HOST}/file/getImgStream?fileName={imageinfo}'
        payload=indate
        resp=requests.post(url=f'{HOST}/shopping/updatemyshop',params=payload,headers=self.heads)
        return resp.json()





if __name__ == '__main__':
    token=Login().login({"username": "sq0013", "password": "111111"},gettoken=True)
    res=Myshop(token).shopping_list({'page':1,'limit':20})
    print(res)
    # shopid=res['data']['records'][0]['_id']
    # print(shopid)
    # # 文件上传
    # imageinfo=Myshop(token).file_upload('123.png','../datas/123.png')
    # print(imageinfo)
    # # g更新店铺信息
    # res=Myshop(token).shop_update()



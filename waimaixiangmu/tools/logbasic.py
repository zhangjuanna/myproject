"""  -*- coding:utf-8 -*-
 @File      :logbasic.py
 @Time      :2020/12/1618:50
 @Autor     :张娟娜
 @Email     :1136189505@qq.com
 @Software  :PyCharm
 """
import logging
def logger():
    logging.basicConfig(format="%(asctime)s %(filename)s [line:%(nline)d] %(levelname)s-%(message)s",
                        level=logging.INFO,
                        filemode='a'
                        )
    return logging

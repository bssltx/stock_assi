# -*- coding: utf-8 -*-

'''

匹配规则
目前有高价、低价提醒
后期加入：金叉、死叉提醒等

'''

from stock import Stock
from indexes.price import PriceIndex
from fitRet import FitRet,CODE_NOT_FIT,CODE_FIT
from sendEmail import sendEmail
import random

rules = [
    ['博通集成', '603068', 130, 90],  #高价出手
    ['湖南黄金', '002155', 9, 7.0],
    ['科技ETF', '515000', 1.7, 1.2],
    ['欧菲光', '002456', 20, 15],
    ['100红利', '515180', 1.2, 0.93],
    ['贝瑞基因', '000710',53, 36.3],
    ['半导体', '512480', 2.5, 1.6],
    ['金发科技', '600143', 12, 8],
    ['药明康德', '603259', 120, 100],
    ['格力电器', '000651', 70, 49],
    ['5GETF', '515050', 1.5, 1.0],
    ['西安旅游', '000610', 9.9, 7.5],
    ['沃特股份', '002886', 37.23, 30],
    ['民生银行', '600016', 6.38, 5.6],
    ['建投能源', '000600', 5.3, 4.0],
    ['长电科技', '600584', 35, 23],
    # ['大华股份'],
    # ['京东方'],
]


for name,code,high,low in rules:
    stock = Stock(name, code)
    priceIndex = PriceIndex(stock)
    fitRet = priceIndex.higher_or_lower(high,low)
    if(fitRet.code==CODE_FIT):
        sendEmail(fitRet.msg, fitRet.msg)








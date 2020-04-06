# -*- coding: utf-8 -*-

'''

股票分析

'''

import matplotlib.pyplot as plt
from stock import Stock
import math

stocks = [
    ['博通集成', '603068'],  #高价出手
    ['湖南黄金', '002155'],
    ['科技ETF', '515000'],
    ['欧菲光', '002456'],
    ['100红利', '515180'],
    ['贝瑞基因', '000710'],
    ['半导体', '512480'],
    ['金发科技', '600143'],
    ['药明康德', '603259'],
    ['格力电器', '000651'],
    ['5GETF', '515050'],
    ['西安旅游', '000610'],
    ['沃特股份', '002886'],
    ['民生银行', '600016'],
    ['建投能源', '000600'],
    ['长电科技', '600584'],
]

stockList = []
for name,code in stocks:
    stock = Stock(name, code)
    stock.get_hist_data()
    stockList.append(stock)

plt.figure(figsize=(12,8))
cols = 3
rows = math.ceil(1.0*len(stockList) / cols)
for i in range(len(stockList)):
    plt.subplot(rows, cols, i+1)
    plt.plot(stockList[i].df_hist_data.close)

plt.show()


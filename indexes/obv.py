# -*- coding: utf-8 -*-


import sys
sys.path.append('..')
from stock import Stock
from fitRet import FitRet,CODE_FIT,CODE_NOT_FIT
import talib



class ObvIndex:
	def __init__(self, stock: Stock):
		self.stock = stock
		self.df_index_data = talib.OBV(stock.df_hist_data.close, stock.df_hist_data.volume)






'''

#当股价上升而OBV线下降，表示买盘无力，股价可能会回跌。
#股价下降时而OBV线上升，表示买盘旺盛，逢低接手强股，股价可能会止跌回升。


import os, sys
import tushare as ts
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import talib

if len(sys.argv) ==2:
	code = sys.argv[1]
else:
	print('usage: python talib_obv.py stockcode ')
	sys.exit(1)
if len(code) !=6:
	print('stock code length: 6')
	sys.exit(2)
	
df = ts.get_k_data(code)
df = df[df['date'] > '2020-01-01']
print(df)
if len(df) <10:
	print(" len(df) <10 ")
	sys.exit(2)

# 量价指标: OBV (On-Balance Volume，净额成交量或叫能量潮指标）

obv = talib.OBV(df.close, df.volume)

df.index = pd.to_datetime(df.date)
# 画股票收盘价图

fig,axes = plt.subplots(2,1)
df[['close']].plot(ax=axes[0], grid=True, title=code)
# 画 OBV 曲线图
obv.plot(ax=axes[1], grid=True)
plt.show()

#运行：python .\obv.py 600380

'''

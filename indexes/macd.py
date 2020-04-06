# -*- coding: utf-8 -*-


import sys

sys.path.append('..')
from stock import Stock
from fitRet import FitRet, CODE_FIT, CODE_NOT_FIT
import talib


class MacdIndex:
	def __init__(self, stock: Stock, fastperiod=12, slowperiod=26, signalperiod=9):
		self.stock = stock
		self.df_index_data = talib.MACD(stock.df_hist_data.close, fastperiod=fastperiod, slowperiod=slowperiod, signalperiod=signalperiod)

	def golden_crossing(self):
		return FitRet(CODE_NOT_FIT, '%s，未发现金叉' % (self.stock.name))

	def dead_crossing(self):
		return FitRet(CODE_NOT_FIT, '%s，未发现死叉' % (self.stock.name))



'''

import tushare as ts
import talib
#规则，macd值是正的还是负的无所谓，macd_diff必须是正的，macd_diff_diff最好是正的

def data_w(code):
	df = ts.get_k_data(code, start='2018-01-08', ktype='w')
	df["MACD_macd"],df["MACD_macdsignal"],df["MACD_macdhist"] = talib.MACD(df.close, fastperiod=12, slowperiod=26, signalperiod=9)
	#df["MACDEXT_macd"],df["MACDEXT_macdsignal"],df["MACDEXT_macdhist"] = talib.MACDEXT(df.close, fastperiod=12, fastmatype=0, slowperiod=26, slowmatype=0, signalperiod=9, signalmatype=0)
	#df["MACDFIX_macd"],df["MACDFIX_macdsignal"],df["MACDFIX_macdhist"] = talib.MACDFIX(df.close, signalperiod=9)

	df.dropna(inplace=True)
	return df
	
def data_d(code):

	df = ts.get_k_data(code, start='2018-01-08', ktype='D')
	df["MACD_macd"],df["MACD_macdsignal"],df["MACD_macdhist"] = talib.MACD(df.close, fastperiod=12, slowperiod=26, signalperiod=9)
	#df["MACDEXT_macd"],df["MACDEXT_macdsignal"],df["MACDEXT_macdhist"] = talib.MACDEXT(df.close, fastperiod=12, fastmatype=0, slowperiod=26, slowmatype=0, signalperiod=9, signalmatype=0)
	#df["MACDFIX_macd"],df["MACDFIX_macdsignal"],df["MACDFIX_macdhist"] = talib.MACDFIX(df.close, signalperiod=9)

	df.dropna(inplace=True)
	return df
	
def diff_(l):
	diff = [0]
	for i in range(1, len(l)):
		diff.append(l[i] - l[i-1])
	
	return diff

	
def macd_diff_1_2(df):
	
	df['macd_diff'] = diff_(df['MACD_macd'].tolist())
	df['macd_diff_diff'] = diff_(df['macd_diff'].tolist())
	return df
	

if __name__ == "__main__":

	code = '002597'
	df_w = data_w(code)
	df_w_ = macd_diff_1_2(df_w)
	print('周线macd')
	print(df_w_[['date', 'close', 'MACD_macd','macd_diff', 'macd_diff_diff']].tail(10))
	
	df_d = data_d(code)
	df_d_ = macd_diff_1_2(df_d)
	print('日线macd')
	print(df_d_[['date', 'close', 'MACD_macd','macd_diff', 'macd_diff_diff']].tail(50))
	
'''


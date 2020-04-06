# -*-coding:utf-8 -*-

import tushare as ts

class Stock:
    def __init__(self, name, code):
        self.name = name
        self.code = code
        self.df_realtime_data = None
        self.get_realtime_data()
        self.realtime_price = float(self.df_realtime_data.loc[0, 'price'])
        self.df_hist_data = None

    def get_realtime_data(self):
        self.df_realtime_data = ts.get_realtime_quotes(self.code)
        name = self.df_realtime_data.loc[0,'name']
        if(name!=self.name):
            raise Exception('stock name not match code!')

    def get_hist_data(self):
        self.df_hist_data = ts.get_hist_data(self.code)






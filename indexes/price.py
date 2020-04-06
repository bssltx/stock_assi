# -*- coding: utf-8 -*-

'''

价格规则

'''

import sys
sys.path.append('..')
from stock import Stock
from fitRet import FitRet,CODE_FIT,CODE_NOT_FIT


class PriceIndex:
    def __init__(self, stock: Stock):
        self.stock = stock

    def higher_or_lower(self, highPrice, lowPrice):
        if (self.stock.realtime_price > highPrice):
            return FitRet(CODE_FIT, '%s,高价提醒,当前价格：%.2f，高于：%.2f' % (self.stock.name, self.stock.realtime_price, highPrice))
        if (self.stock.realtime_price < lowPrice):
            return FitRet(CODE_FIT, '%s,低价提醒,当前价格：%.2f，低于：%.2f' % (self.stock.name, self.stock.realtime_price, lowPrice))
        else:
            return FitRet(CODE_NOT_FIT, '%s,当前价格无需关注：%.2f，高阈值：%.2f，低阈值：%.2f' % (self.stock.name, self.stock.realtime_price, highPrice,lowPrice))


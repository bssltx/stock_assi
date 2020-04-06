# -*- coding: utf-8 -*-

'''
规则匹配返回信息
'''

CODE_FIT = 1
CODE_NOT_FIT = 0

class FitRet():
    def __init__(self, code, msg):
        self.code = code
        self.msg = msg

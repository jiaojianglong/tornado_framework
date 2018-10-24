#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/10/24 0024 21:56
# @Author  : jiaojianglong

from tornado import gen
from tornado.concurrent import run_on_executor
from concurrent.futures import ThreadPoolExecutor
def async_decoration(func):
    @gen.coroutine
    def wrapper(self):
        try:
            res = yield func(self)
            self.write(res)
        except Exception as e:
            self.write(str(e))
    return wrapper

executor = ThreadPoolExecutor(200)
def threadpool_decoration(func):
    @gen.coroutine
    def wrapper(self):
        try:
            self.executor = executor
            res = yield run(self,func)
            self.write(res)
        except Exception as e:
            self.write(str(e))
    return wrapper

@run_on_executor
def run(self,func):
    return func(self)
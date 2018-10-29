#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/10/24 0024 22:14
# @Author  : jiaojianglong

from handlers.base_handler.decoration import threadpool_decoration
from tornado.web import RequestHandler
import time
from multiprocessing import Manager
manager = Manager()
A = manager.dict({"dta":"我是旧数据"})



class ThreadPoolHandler(RequestHandler):
    @threadpool_decoration
    def get(self):
        print("我在线程里面睡")
        global A
        A['dta'] = "我是新刷的数据"
        time.sleep(3)
        print("线程里面睡完了")
        return {"data":"thread pool sleep"}

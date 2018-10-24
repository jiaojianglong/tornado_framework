#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/10/24 0024 22:00
# @Author  : jiaojianglong

from handlers.base_handler.decoration import async_decoration
from tornado.web import RequestHandler
from tornado import gen

class AsyncHandler(RequestHandler):

    @async_decoration
    @gen.coroutine
    def get(self):
        print("进入携程")
        yield gen.sleep(3)
        print("睡完了")
        return {"data":"async"}

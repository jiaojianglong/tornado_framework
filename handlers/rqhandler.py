#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/25
# @Author  : JiaoJianglong


from tornado.web import RequestHandler
from handlers.base_handler.decoration import rq_function

from handlers.threadpoolhandler import A



class RQHandler(RequestHandler):
    @rq_function
    def get(self, *args, **kwargs):
        print("我在别的地方执行")
        print(A)
        print("在别的地方睡好了")
        return {"data": "haha"}


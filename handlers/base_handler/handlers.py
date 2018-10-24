#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/10/24 0024 20:54
# @Author  : jiaojianglong

from tornado.web import RequestHandler
from tornado import gen
from concurrent.futures import ThreadPoolExecutor
from tornado.concurrent import run_on_executor
import time
import json
class Basehandler(RequestHandler):
    pass



class AsyncHandler(Basehandler):

    @gen.coroutine
    def get(self):
        try:
            ret = yield self.sleep()
            # return JSON so we get the correct type of the return value
            self.write({'response': ret})
        except Exception as e:
            self.write({'error': str(e)})

    @gen.coroutine
    def sleep(self):
        print("hahah")
        yield gen.sleep(3)
        print("lala")
        data = {"data": "睡了三秒，哈哈哈哈哈"}
        return json.dumps(data)


class ThreadPoolBase(Basehandler):
    executor = ThreadPoolExecutor(200)
    TYPE = 'threadpool'

    @gen.coroutine
    def get(self):
        try:
            data = yield self.run(self.sleep)
            self.write({'response': data})
        except Exception as e:
            print(e)
            self.write({'error': str(e)+"aa"})

    @run_on_executor
    def run(self,func,):
        return self.sleep()


    def sleep(self):
        time.sleep(3)
        data = {"data": "睡了三秒，哈哈哈哈哈"}
        return data

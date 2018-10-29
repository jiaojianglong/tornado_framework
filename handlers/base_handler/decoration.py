#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/10/24 0024 21:56
# @Author  : jiaojianglong

from tornado import gen
from tornado.concurrent import run_on_executor
from concurrent.futures import ThreadPoolExecutor
from rq import Queue
import time
from redis import Redis,ConnectionPool
redis_conn = ConnectionPool(host="127.0.0.1", port=6379, db=1,)
redis_conn = Redis(connection_pool=redis_conn)
q = Queue(connection=redis_conn)



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



def rq_function(func):
    def wrapper(self):
        try:
            job = q.enqueue(func,self)
            print("收到请求，交给工人处理")
            while not job.result:
                time.sleep(0.01)
            self.write(job.result)
        except Exception as e:
            self.write(str(e))

    return wrapper
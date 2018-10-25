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


from rq import Queue
from redis import Redis,ConnectionPool
redis_conn = ConnectionPool(host="127.0.0.1", port=6379, db=1,)
redis_conn = Redis(connection_pool=redis_conn)
q = Queue(connection=redis_conn)


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


def jobs():
    print("我在别的地方执行")
    print("在别的地方睡好了")
    return {"data":"RQ handler"}

class RQHandler(Basehandler):

    def get(self):
        job = q.enqueue(jobs)
        print(job.result)
        print(job)
        time.sleep(2)
        print(job.result)  # => 889
        self.write("hahah")
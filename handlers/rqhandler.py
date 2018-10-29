#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/25
# @Author  : JiaoJianglong


from tornado.web import RequestHandler
from rq import Queue
import time
from redis import Redis,ConnectionPool
redis_conn = ConnectionPool(host="127.0.0.1", port=6379, db=1,)
redis_conn = Redis(connection_pool=redis_conn)
q = Queue(connection=redis_conn)

from handlers.threadpoolhandler import A


a = "lalallalala"

def jobsss():
    print("我在别的地方执行")
    print(A)
    print("在别的地方睡好了")
    return {"data":a}

class RQHandler(RequestHandler):

    def get(self, *args, **kwargs):
        job = q.enqueue(jobsss)
        print("收到请求，交给工人处理")
        while not job.result:
            time.sleep(0.01)
        self.write(job.result)
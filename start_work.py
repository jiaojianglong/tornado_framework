#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/10/25 0025 20:19
# @Author  : jiaojianglong

from rq.worker import Worker
from rq.queue import Queue
from rq import Connection
from redis import ConnectionPool,Redis
redis_conn = ConnectionPool(host="127.0.0.1", port=6379, db=1,)
redis_conn = Redis(connection_pool=redis_conn)
from handlers.base_handler.handlers import q
if __name__ == "__main__":
    with Connection(redis_conn):
        Worker(q).work()

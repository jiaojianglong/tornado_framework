#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/9/10 22:11
# @Author  : jiaojianglong

from handlers.indexhandler import IndexHandler
# from handlers.base_handler.handlers import ThreadPoolBase
# from handlers.base_handler.handlers import AsyncHandler
from handlers.asynchandler import AsyncHandler
from handlers.threadpoolhandler import ThreadPoolHandler
from handlers.base_handler.handlers import RQHandler
handler = [
    (r"/index", IndexHandler),
    (r"/threadpool", ThreadPoolHandler),
    (r"/async", AsyncHandler),
    (r"/rqhandler", RQHandler),

]

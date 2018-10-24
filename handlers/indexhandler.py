
import time
from tornado.web import RequestHandler

class IndexHandler(RequestHandler):#只能一个一个的处理接口
    def get(self, *args, **kwargs):
        time.sleep(3)
        data = {"data":"睡了三秒，哈哈哈哈哈"}
        self.write(data)

from tornado.web import RequestHandler
from logconfig.package_timeRotateLog import TimeRotateLog
logger = TimeRotateLog().time_rotate_log()

class IndexHandler(RequestHandler):
    def get(self, *arge, **kwargs):
        self.write("hubiao is a good man !")
        logger.info("/IndexHandler请求成功……")

class HubiaoHandler(RequestHandler):
    def initialize(self,word1,word2):
        self.word1 = word1
        self.word2 = word2

    def get(self, *args, **kwargs):
        logger.info("\n请求参数Word1:{0}\n请求参数Word2:{1}".format(self.word1,self.word2))
        result = self.write("hubiao is a nice man !")
        logger.info("/HubiaoHandler请求成功……")
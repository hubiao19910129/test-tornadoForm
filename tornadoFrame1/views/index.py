from tornado.web import RequestHandler
from logconfig.package_timeRotateLog import RotateLog
logger = RotateLog().time_rotate_log()

class IndexHandler(RequestHandler):
    def get(self, *arge, **kwargs):
        #反向解析self.reverse_url("name")
        url = self.reverse_url("Zhuyin")
        self.write("<a href = '%s'>去另一个界面</a>"%(url))
        logger.info("/IndexHandler请求成功……")
        logger.info("点击反向解析到url:{}".format(url))

class HubiaoHandler(RequestHandler):
    def initialize(self,word1,word2):
        self.word1 = word1
        self.word2 = word2

    def get(self, *args, **kwargs):
        logger.info("\n请求参数Word1:{0}\n请求参数Word2:{1}".format(self.word1,self.word2))
        result = self.write("hubiao is a nice man !")
        logger.info("/HubiaoHandler请求成功……")

#反向解析
class ZhuyinHandler(RequestHandler):
    def initialize(self, word3, word4):
        self.word3 = word3
        self.word4 = word4

    def get(self, *args, **kwargs):
        logger.info("\n请求参数Word1:{0}\n请求参数Word2:{1}".format(self.word3, self.word4))
        result = self.write("Zhuyin is a {} girl !".format(self.word4))
        logger.info("/ZhuyinHandler请求成功……")

#提取uri的特定部分
class LiuyifeiHandler(RequestHandler):
    def get(self,h1,h2,h3,*args,**kwargs):
        result = self.write("<a href = #>Liuyifei is a good girl</a>")
        logger.info("提取结果: h1={0},h2={1},h3={2}".format(h1,h2,h3))
        logger.info("{}请求成功".format("LiuyifeiHandler"))

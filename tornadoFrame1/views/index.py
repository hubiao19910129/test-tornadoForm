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


#浏览器传参192.168.137.1:8000/zhangmanyu？a=1&b=2&c=3
class ZhangmanyuHandler(RequestHandler):
    def get(self,*args,**kwargs):
        # self.get_query_argument(name="name",default=ArgDefaltMarker,strip=True)
        #name如果出现多个参数，name返回最后一个值
        #如果我们设置了未传的参数，返回默认default值
        #strip表示是否过滤空格
        a = self.get_query_argument(name="a", default=100, strip=True)
        b = self.get_query_argument(name="b", default=100, strip=True)
        c = self.get_query_argument(name="c", default=100, strip=True)
        #get_query_arguments可以取多个相同name的值，返回的是一个列表
        d = self.get_query_arguments(name="a",strip=True)
        print(a,b,c,d)
        self.write("Zhangmanyu is a good girl")

#post传参
import os
import config
class AgentHandler(RequestHandler):
    def get(self,*args,**kwargs):
        file = os.path.join(config.settings["templates_path"], "postfile.html")
        self.render(file)
    def post(self,*args,**kwargs):
        name = self.get_body_argument("username")
        #get_argument应用于get、post请求都可以
        passWd = self.get_argument("passwd")
        hobbyList = self.get_body_arguments("hobby")
        print(name,passWd,hobbyList)
        self.write("This is a fan day!")
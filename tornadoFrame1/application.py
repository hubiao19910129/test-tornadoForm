import tornado.web
#调用视图
from views import index
#调用配置
import config

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/",index.IndexHandler),

            #路由传参
            (r"/hubiao",index.HubiaoHandler,{"word1":"good","word2":"nice"}),

            #反向解析tornado.web.url--name
            tornado.web.url(r"/fanxiangjiexi",index.ZhuyinHandler,{"word3":"cool","word4":"beautiful"},name="Zhuyin"),

            #提取uri的特定部分
            # (r"/Liuyifei/(\w+)/(\w+)/(\w*)",index.LiuyifeiHandler)
            (r"/Liuyifei/(?P<h1>\w+)/(?P<h3>\w+)/(?P<h2>\w*)",index.LiuyifeiHandler)

        ]


        super(Application,self).__init__(handlers,**config.settings)

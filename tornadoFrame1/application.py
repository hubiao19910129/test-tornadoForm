import tornado.web
#调用视图
from views import index
#调用配置
import config

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/",index.IndexHandler),
            (r"/hubiao",index.HubiaoHandler,{"word1":"good","word2":"nice"}),

        ]


        super(Application,self).__init__(handlers,**config.settings)

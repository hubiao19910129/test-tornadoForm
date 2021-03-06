from tornado.web import RequestHandler
from logconfig.package_timeRotateLog import RotateLog
logger = RotateLog().viewIndex()

class IndexHandler(RequestHandler):
    def get(self, *arge, **kwargs):
        #反向解析self.reverse_url("name")
        url = self.reverse_url("Zhuyin")
        logger.info("/IndexHandler请求成功……")
        self.write("<a href = '%s'>去另一个界面win10</a>"%(url))
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
        logger.info(a,b,c,d)
        self.write("Zhangmanyu is a good girl")

#post传参
import os
import config
class AgentHandler(RequestHandler):
    def get(self,*args,**kwargs):
        file = os.path.join(config.settings["templates_path"],"postfile.html")
        self.render(file)
    def post(self,*args,**kwargs):
        name = self.get_body_argument("username")
        #get_argument应用于get、post请求都可以
        passWd = self.get_argument("passwd")
        hobbyList = self.get_body_arguments("hobby")
        logger.info(name,passWd,hobbyList)
        self.write("This is a fan day!")

#request对象：http://192.168.137.1:8000/zhude?a=1&b=2
class ZhudeHandler(RequestHandler):
    def get(self,*args,**kwargs):
        #请求方法
        logger.info("method:{}".format(self.request.method))
        logger.info("host:{}".format(self.request.host))
        logger.info("uri:{}".format(self.request.uri))
        logger.info("path:{}".format(self.request.path))
        #请求参数
        logger.info("query:{}".format(self.request.query))
        logger.info("version:{}".format(self.request.version))
        logger.info("headers:\n{}".format(self.request.headers))
        logger.info("body:\n{}".format(self.request.body))
        #客户端IP
        logger.info("remote_ip:\n{}".format(self.request.remote_ip))
        #上传文件,files结构需要关注
        logger.info("files:\n{}".format(self.request.files))

        self.write("zhude is a good man")

#文件上传
class LinqingxiaHandler(RequestHandler):
    def get(self, *args, **kwargs):
        file = os.path.join(config.settings["templates_path"], "upfiles.html")
        self.render(file)
    def post(self,*args,**kwargs):
        try:
            filesDict = self.request.files
            logger.info(filesDict)
            for keyName in filesDict:
                fileArr = filesDict[keyName]
                for fileObj in fileArr:
                    #存储路径
                    if fileObj.content_type == 'text/plain':
                        filePath = os.path.join(config.BASE_DIRS, "upfile/file/" + fileObj.filename)
                    elif fileObj.content_type == 'image/jpeg':
                        filePath = os.path.join(config.BASE_DIRS, "upfile/img/" + fileObj.filename)
                    else:
                        logger.info("上传文件的类型不存在")
                    with open(filePath,"wb") as f:
                        f.write(fileObj.body)
        except Exception as e:
            logger.exception(e)
        finally:
            self.write("ok")

#接口调用顺序
class InvokeHandler(RequestHandler):
    # 默认请求头
    def set_default_headers(self):
        logger.info("set_default_headers")
    #请求前初始化
    def initialize(self):
        logger.info("initialize")
    #请求前预处理
    def prepare(self):
        logger.info("prepare")

    def get(self,*args,**kwargs):
        logger.info("get")
        self.send_error(500)
        self.write("hahahahaha")
    #返回错误信息
    def write_error(self, status_code, **kwargs):
        logger.info("write_error")
        self.write("服务器内部错误")
    #在该方法中进行资源清理释放，或者是日志处理
    def on_finish(self):
        logger.info("on_finish")
    '''成功请求顺序，没有报错，不调write_error
    set_default_headers
    initialize
    prepare
    get
    on_finish
    '''
    '''服务器内部错误时的顺序
    set_default_headers
    initialize
    prepare
    get
    set_default_headers
    write_error
    on_finish
    '''
class HomeHandler(RequestHandler):

    def get(self,*args,**kwargs):
        try:
            file = os.path.join(config.settings["templates_path"],"home.html")
            tmp = 100
            self.render(file,num = tmp)
        except Exception as e:
            logger.exception(e)
        finally:
            self.write("home is ok")
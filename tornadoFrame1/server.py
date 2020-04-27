import tornado.ioloop
import tornado.httpserver
import config
from application import Application
import socket
from logconfig.package_timeRotateLog import RotateLog


class Server(object):
    def __init__(self):
        # 获取主机名
        self.hostName = socket.gethostname()
        #获取（[原始主机名]，[域名列表]，[IP地址列表]）
        self.hostInfo = socket.gethostbyname_ex(self.hostName)
        #获取主机IP地址列表
        self.hostIp = self.hostInfo[-1]
        #引用日志模块
        self.logger1 = RotateLog().rotate_log()

    def application_start(self):
        try:
            app = Application()
            httpServer = tornado.httpserver.HTTPServer(app)
            port = config.options["port"]
            httpServer.bind(port)
            self.logger1.info("服务IP地址为{}".format(self.hostIp))
            self.logger1.info("服务绑定端口为{}".format(port))
            httpServer.start(1)
            self.logger1.info("服务启动成功……")
            tornado.ioloop.IOLoop.current().start()
        except Exception as e:
            self.logger1.exception(e)


if __name__ == "__main__":
    Server().application_start()









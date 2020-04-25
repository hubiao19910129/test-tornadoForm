import logging.config
import os

class RotateLog(object):
    def __init__(self):
        self.base_path = os.path.dirname(__file__)

    def rotate_log(self):
        configFile = os.path.join(self.base_path,"log_rotate_conf.ini")
        logging.config.fileConfig(configFile)
        logger = logging.getLogger("example03")
        return logger


# for i in range(1000):
#     logger.debug("这是调式日志--%d"%i)
#     logger.info("这是提示信息--%d"%i)
#     logger.warning("这是警告信息--%d"%i)
#     logger.error("这是错误信息--%d"%i)
#     logger.critical("这是严重BUG--%d"%i)
if __name__ == "__main__":
    logger1 = RotateLog().rotate_log()
    logger1.error("我是log循环处理")

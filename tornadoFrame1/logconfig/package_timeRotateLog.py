import logging.config
import os

class RotateLog(object):
    def __init__(self):
        self.base_path = os.path.dirname(__file__)


    def time_rotate_log(self):
        configFile = os.path.join(self.base_path, "log_time_rotate_conf.ini")
        logging.config.fileConfig(configFile)
        logger = logging.getLogger("time_rotate")
        return logger

    def rotate_log(self):
        configFile = os.path.join(self.base_path,"log_rotate_conf.ini")
        logging.config.fileConfig(configFile)
        logger = logging.getLogger("rotate")
        return logger

    def viewIndex(self):
        configFile = os.path.join(self.base_path,"log_time_rotate_conf.ini")
        logging.config.fileConfig(configFile)
        logger = logging.getLogger("viewIndex")
        return logger

    def MySql(self):
        configFile = os.path.join(self.base_path,"log_time_rotate_conf.ini")
        logging.config.fileConfig(configFile)
        logger = logging.getLogger("MySql")
        return logger

    def Oracle(self):
        configFile = os.path.join(self.base_path,"log_time_rotate_conf.ini")
        logging.config.fileConfig(configFile)
        logger = logging.getLogger("Oracle")
        return logger

if __name__ == "__main__":
    # logger = RotateLog().time_rotate_log()
    # logger.error("我是log时间循环处理")
    # logger1 = RotateLog().rotate_log()
    # logger1.error("我是log循环处理")
    logger2 = RotateLog().viewIndex()
    logger2.error("我是view日志")




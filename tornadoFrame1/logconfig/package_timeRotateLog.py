import logging.config
import os

class TimeRotateLog(object):
    def __init__(self):
        self.base_path = os.path.dirname(__file__)


    def time_rotate_log(self):
        configFile = os.path.join(self.base_path, "log_time_rotate_conf.ini")
        logging.config.fileConfig(configFile)
        logger = logging.getLogger("time_rotate")
        return logger

if __name__ == "__main__":
    logger = TimeRotateLog().time_rotate_log()
    logger.error("我是log时间循环处理")



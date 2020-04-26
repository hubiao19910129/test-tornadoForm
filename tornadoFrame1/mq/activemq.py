# -*- coding: utf-8 -*-
import stomp
import time
import json
from logconfig.package_timeRotateLog import RotateLog
import config
from mq.mq_data_template import *

class MqLibrary():
    def __init__(self):
        self.value_msg = eval("msg")
        self.msg = json.dumps(self.value_msg)

        self.value_topic = eval("topic")
        self.topic  = json.dumps(self.value_topic)

        self.IP = config.mq["IP"]
        self.port = config.mq["port"]

        self.address = self.IP + ":" + str(self.port)
        self.queue_name =config.mq["queue_name"]
        self.topic_name = config.mq["topic_name"]
        self.listener_name = config.mq["listener_name"]
        self.logger = RotateLog().time_rotate_log()

    def on_error(self, headers, message):
        #编辑日志信息
        self.logger.exception("获取队列消息异常：{}".format(message))

    # stomp协议，自带on_message函数，消费mq队列消息后，能获取到队列中的message值
    def on_message(self, headers, message):
        self.logger.info("接收消息头为：{}".format(headers))
        self.logger.info("接收消息体为：{}".format(message))


    # 推送到队列queue
    def send_to_queue(self):
        try:
            conn = stomp.Connection10([(self.IP, self.port)], auto_content_length=False)
            # conn.start()
            conn.connect()

            self.logger.info("发送消息地址为:{:}".format(self.address))
            self.logger.info("发送消息队列为:{:}".format(self.queue_name))

            conn.send(self.queue_name, self.msg)
            self.logger.info("推送消息体为:\n{:}".format(self.msg))
        except Exception as e:
            self.logger.exception(e)
        finally:
            conn.disconnect()

    ##从队列接收消息
    def receive_from_queue(self):
        try:
            conn = stomp.Connection10([(self.IP, self.port)])

            self.logger.info("接收消息地址为:{:}".format(self.address))
            conn.set_listener(self.listener_name, ActiveMq)
            # conn.start()
            conn.connect()
            conn.subscribe(self.queue_name)
            self.logger.info("接收消息队列为:{:}".format(self.queue_name))

            time.sleep(1)  # secs

        except Exception as e:
            self.logger.exception(e)
        finally:
            conn.disconnect()

    # 推送到主题
    def send_to_topic(self):
        try:
            conn = stomp.Connection10([(self.IP, self.port)])
            self.logger.info("订阅主题地址为:{:}".format(self.address))

            # conn.start()
            conn.connect()
            conn.send(self.topic_name, self.topic)
            self.logger.info("订阅主题队列为:{:}".format(self.queue_name))
            self.logger.info("订阅主题内容为:{:}".format(self.topic))
        except Exception as e:
            self.logger.exception(e)
        finally:
            conn.disconnect()

    ##从主题接收消息
    def receive_from_topic(self):
        try:
            conn = stomp.Connection10([(self.IP, self.port1)])
            self.logger.info("接收主题地址为:{:}".format(self.address))
            self.logger.info("接收主题队列为:{:}".format(self.queue_name))
            conn.set_listener(self.listener_name, ActiveMq)
            # conn.start()
            conn.connect()
            conn.subscribe(self.topic_name)
            # while 1:
            #     self.send_to_topic("Android/50263545/220282199101292936")
            #     time.sleep(3)  # secs
        except Exception as e:
            self.logger.exception(e)
        finally:
            conn.disconnect()

if __name__ == '__main__':
    ActiveMq = MqLibrary()
    ActiveMq.send_to_queue()
    # ActiveMq.receive_from_queue()
    # ActiveMq.send_to_topic()
    # ActiveMq.receive_from_topic()
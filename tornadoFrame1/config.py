##### 192.168.1.5
import os
BASE_DIRS = os.path.dirname(__file__)

##### 参数部分
options = {
    "port":8000,
    }

##### 配置
settings = {
    "static_path":os.path.join(BASE_DIRS,"static"),
    "templates_path":os.path.join(BASE_DIRS,"templates"),
    "debug" : False,
    }

##### MQ
mq = {"IP":"172.20.6.22",
      "port":61616,
      #"IP"="172.20.6.22","10.150.123.247"
      #"port"=61616,61613,
      "queue_name":"msg-dispatcher.base.hello",
      "topic_name":"/topic/SampleTopic",
      "listener_name":"MqLibrary",
      }


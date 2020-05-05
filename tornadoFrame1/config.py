##### 192.168.1.5
import os
BASE_DIRS = os.path.dirname(__file__)

##### http.server绑定端口
## 端口号范围8000~60000/65535最合适
options = {
    "port":8001,
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

##### MySql
MySql = {"host":"172.20.5.69",
         "user":"test",
         "passWd":"111111",
         "dbName":"app_release",
         }

##### Oracle
Oracle = {"host":"172.20.6.22:1521",
         "user":"agent_user2",
         "passWd":"123456",
         "dbName":"mpos",
         }

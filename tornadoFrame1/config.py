#192.168.1.5
import os
BASE_DIRS = os.path.dirname(__file__)

#参数部分
options = {
    "port":8000
}

#配置
settings = {
    "static_path":os.path.join(BASE_DIRS,"static"),
    "templates_path":os.path.join(BASE_DIRS,"templates"),
    "debug" : False,

}


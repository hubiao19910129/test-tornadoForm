# -*- coding: UTF-8 -*-
import  pymysql
import config
from logconfig.package_timeRotateLog import RotateLog

class SunckMySql(object):
    def __init__(self):
        self.host = config.MySql["host"]
        self.user = config.MySql["user"]
        self.passWd = config.MySql["passWd"]
        self.dbName = config.MySql["dbName"]
        self.logger = RotateLog().MySql()

    def connect(self):
        try:
            self.db = pymysql.connect(self.host,self.user,self.passWd,self.dbName)
            self.cursor = self.db.cursor()
            self.logger.info("{}@{}数据库连接成功……".format(self.host, self.user))

        except Exception as e:
            self.logger.error("{}@{}数据库连接失败".format(self.host,self.user))
            self.logger.exception(e)


    def close(self):
        try:
            self.cursor.close()
            self.db.close()
            self.logger.info("{}@{}数据库连接已关闭……".format(self.host, self.user))
        except Exception as e:
            self.logger.error("{}@{}数据库未关闭".format(self.host, self.user),e)

    #元组
    def get_one(self,sql):
        res = None
        try:
            self.connect()
            self.cursor.execute(sql)
            self.logger.info(sql)
            res = self.cursor.fetchone()
            self.close()
            self.logger.info("调用{}查询成功，查询结果为:{}".format("get_one",res))
        except Exception as e:
            self.logger.error("调用{}查询失败……".format("get_one"),e)
        return res

    #元组
    def get_all(self,sql):
        res = None
        try:
            self.connect()
            self.cursor.execute(sql)
            self.logger.info(sql)
            res = self.cursor.fetchall()
            self.close()
            self.logger.info("调用{}查询成功，查询结果为:{}".format("get_all", res))
        except Exception as e:
            self.logger.error("调用{}查询失败……".format("get_all"),e)
        return res

    #列表[{json1},{json2},{json3}]
    def get_all_obj(self,sql,tableName,*args):
        try:
            resList = []
            fieldsList = []
            if (len(args) > 0):
                for item in args:
                    fieldsList.append(item)
            else:
                fieldsSql = "select COLUMN_NAME from information_schema.COLUMNS where table_name = '%s' and table_schema = '%s'"%(tableName,self.dbName)
                fields = self.get_all(fieldsSql)
                for item in fields:
                    fieldsList.append(item[0])

            #执行查询数据sql
            res = self.get_all(sql)
            for item in res:
                obj = {}
                count = 0
                for x in item:
                    obj[fieldsList[count]] = x
                    count += 1
                resList.append(obj)
            self.logger.info("调用{}查询成功，查询结果为:{}".format("get_all_obj", resList))
            return resList
        except Exception as e:
            self.logger.error("调用{}出错……".format("get_all_obj"),e)

    def insert(self,sql):
        return self.__edit(sql)

    def update(self,sql):
        return self.__edit(sql)

    def delete(self,sql):
        return self.__edit(sql)

    def __edit(self,sql):
        count = 0
        try:
            self.connect()
            count = self.cursor.execute(sql)
            self.db.commit()
            self.close()
        except:
            print("事物提交失败")
            self.db.rollback()
        return count

if __name__ == "__main__":
    MyDb = SunckMySql()

    sql = "select *  from gl_app_ios_release_info where commit_id='75a4059c4d9dc03c8929684b2f5a4d4a2bab29e8'"
    result = MyDb.get_all(sql)
    print(result)

    # sql1 = "select *  from gl_app_ios_release_info where commit_id='75a4059c4d9dc03c8929684b2f5a4d4a2bab29e8'"
    # result1 = MyDb.get_all_obj(sql1,"gl_app_ios_release_info")
    # print(result1)
    #
    sql2 = "select * from gl_app_ios_release_info"
    result2 = MyDb.get_all_obj(sql2,"gl_app_ios_release_info")
    print(result2)

    sql3 = "select publish_env,author from gl_app_ios_release_info"
    result3 = MyDb.get_all_obj(sql3, "gl_app_ios_release_info","publish_env","author")
    print(result3)

    # sql = 'insert into test(id,name) values(%s,%s)'
    # # 新增单条
    # MyDb.insert(sql, ('1', 'tom'))
    # # 新增多条数据
    # MyDb.insert(sql, [('1', 'tom'), ('2', 'bob')])
    # # 批量新增
    # values = []
    # for i in range(10):
    #     values.append((i, "name" + str(i)))
    # MyDb.insert(sql, values)








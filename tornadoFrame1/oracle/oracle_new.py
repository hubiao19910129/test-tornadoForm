# -*- coding: UTF-8 -*-
import cx_Oracle
import config

class OracleNew(object):
    def __init__(self):
        # db = "agent_user2/123456@172.20.6.22:1521/mpos"
        self.host = config.Oracle["host"]
        self.user = config.Oracle["user"]
        self.passWd = config.Oracle["passWd"]
        self.dbName = config.Oracle["dbName"]
        self.database = self.user + '/' + self.passWd + '@' + self.host +'/' + self.dbName

    def connect(self):
        self.db = cx_Oracle.connect(self.database)
        self.cursor = self.db.cursor()

    def close(self):
        self.cursor.close()
        self.db.close()

    # 元组()
    def get_one(self, sql):
        res = None
        try:
            self.connect()
            self.cursor.execute(sql)
            res = self.cursor.fetchone()
            self.close()
        except Exception as e:
            print("查询失败", e)
        return res

    # 列表[(),(),()……]
    def get_all(self, sql):
        res = None
        try:
            self.connect()
            self.cursor.execute(sql)
            res = self.cursor.fetchall()
            self.close()
        except Exception as e:
            print(e, "查询失败")
        return res

    # 列表[{json1},{json2},{json3}……]
    def get_all_obj(self, sql, tableName, *args):
        resList = []
        fieldsList = []
        if (len(args) > 0):
            for item in args:
                fieldsList.append(item)
        else:
            fieldsSql = "select t.column_name from user_tab_columns t where t.table_name = '%s' "% (str.upper(tableName)
            )
            # 查所有列可能出现列顺序颠倒
            fields = self.get_all(fieldsSql)
            for item in fields:
                fieldsList.append(item[0])

        # 执行查询数据sql
        res = self.get_all(sql)
        for item in res:
            obj = {}
            count = 0
            for x in item:
                obj[fieldsList[count]] = x
                count += 1
            resList.append(obj)
        return resList

    def insert(self, sql):
        return self.__edit(sql)

    def update(self, sql):
        return self.__edit(sql)

    def delete(self, sql):
        return self.__edit(sql)

    def __edit(self, sql):
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
    MyDb = OracleNew()


    # sql1 = "select column_name from USER_tab_columns where table_name = 'T_PROFIT_AMOUNT' "
    # result1 = MyDb.get_all(sql1)
    # print(result1)

    #查所有列可能出现列顺序颠倒
    # sql2 = "select * from t_profit where user_id = 50263545"
    # result2 = MyDb.get_all_obj(sql2,"t_profit")
    # print(result2)

    #推荐使用（差所有列可能出现列顺序颠倒）
    # sql3 = "select user_id,amount from t_profit where user_id = 50263545"
    # result3 = MyDb.get_all_obj(sql3, "t_profit","user_id","amount")
    # print(result3)




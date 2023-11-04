import traceback

import pymysql

from new_module.factory.filePipeline import settings


class FromMysql:
    def __init__(self, host="", user="", password="", db=""):

        # callback setting
        self.my_set = settings.MysqlSettings()

        if db == "ncbi" or db == "root":
            # user connect
            self.ncbiConnect = pymysql.connect(host=self.my_set.HOST, user=self.my_set.USER,
                                               password=self.my_set.PASSWORD,
                                               db=self.my_set.NCBI_DATABASE)
            self.ncbiCursor = self.ncbiConnect.cursor()

            # root connect
            self.rootConnect = pymysql.connect(host=self.my_set.HOST, user=self.my_set.ROOT,
                                               password=self.my_set.ROOT_PASSWORD, db=self.my_set.ROOT_DATABASE)
            self.rootCursor = self.rootConnect.cursor()

        if host or user or password or db:
            if db:
                # db connect

                self.dbConnect = pymysql.connect(host=self.my_set.HOST, user=self.my_set.ROOT,
                                                 password=self.my_set.ROOT_PASSWORD, db=db)
                self.dbCursor = self.dbConnect.cursor()

    def getInfoFromMysql(self, cursor, connect, _sql="show tables;"):
        _info = None
        try:
            numRow = cursor.execute(_sql)
            _info = cursor.fetchall()
            connect.commit()

            sql.info(f"影响行数:{numRow},执行语句:{_sql}")
            sql.info(_info)

            return _info
        except Exception as e:
            print(e)
            print(traceback.format_exc())
            print(_sql, '执行失败')
            ex.exception(traceback.format_exc())
            ex.exception(_sql, '执行失败')
            connect.rollback()
            return None

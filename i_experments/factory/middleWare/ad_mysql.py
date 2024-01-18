from .interfaceLog import *
from ..filePipeline import toMysql
from ..filePipeline import fromMysql


class AD_Mysql:

    def __init__(self):
        self.ad_dataBase = "ad_data"
        logger.debug("AD_mysql connected~")
        self._sql = "show tables;"
        self.to_mysql = toMysql.ToMysql(db=self.ad_dataBase)
        self.from_mysql = fromMysql.FromMysql(db="ad_data")
        self.ad_dic = self.dictAdDatas()

    def ad_insert_info(self, item, papers, counts, url, z_p, AD, NC, MCI):
        """

        :param item: 项目名
        :param papers: paers名称
        :param counts: 文章数量
        :param url: 文章地址
        :param z_p: z值 p值
        :param AD: AD患者的数量
        :param NC: 非AD患者的数量
        :param MCI: 是否是轻度认知障碍
        :return: None
        """
        tables = "ad_datas"

        ad_insert_info_ad_table_sql = f"INSERT INTO {tables} (`item`, `papers`, `counts`, `url`, `z_p`, `AD`, `NC`,`MCI`)" \
                                      f" VALUES ('{item}', '{papers}', '{counts}', '{url}', '{z_p}', '{AD}', '{NC}', '{MCI}')"

        sql.info(f"{ad_insert_info_ad_table_sql}")
        self.to_mysql.commitSql(cursor="db", _sql=ad_insert_info_ad_table_sql)
        # self.ad_cursor.dbConnectClose()

    def closeDb(self):
        """
        close connect dbConnect
        :return:
        """
        self.to_mysql.dbConnectClose()

    def dictAdDatas(self, tables="ad_datas"):
        """
        将mysql中的adData编辑为字典
        :return: dic：adData的字典
        """
        ad_dic = {}

        _sql = f"select * from {tables}"
        ad_data_info = self.from_mysql.getInfoFromMysql(cursor=self.from_mysql.dbCursor,
                                                        connect=self.from_mysql.dbConnect, _sql=_sql)

        ad_head = ["id", 'item', 'papers', 'counts', 'url', 'z_p', 'AD', 'NC', 'MCI']
        # print(type(ad_data_info))
        for ad_record in ad_data_info:
            for record_index in range(len(ad_record)):
                if record_index == 0:
                    ad_dic[ad_record[1]] = {}

                ad_dic[ad_record[1]][ad_head[record_index]] = ad_record[record_index]

        return ad_dic

    def verifyRecords(self, item, counts):
        """
        核对传入的item与counts是否与数据库中的items一致，如果不同或没有则返回false
        :param item:
        :param counts:
        :return: true or false
        """
        try:
            if self.ad_dic[item]["counts"] == int(counts):
                return True
            else:
                return False
        except Exception as e:
            print(e)
            return False

    def delete_exist_record(self, item, tables="ad_datas"):
        """
        删除已经修改过的记录
        :param item: 需要删除的item
        :param tables: 表
        :return:
        """
        try:
            _sql = f"delete from {tables} where item='{item}'"
            num_row = self.to_mysql.commitSql(cursor=self.to_mysql.dbCursor, connnect=self.to_mysql.dbConnect,
                                              _sql=_sql)
            sql.info(f"影响行数{num_row},执行sql：{_sql}")
        except Exception as e:
            print(e)
            sql.info(f"执行失败，sql：{_sql}")

    def update_ad_papers(self, item_name, item="item", table="ad_datas", col="papers", content="T"):
        """
        为ad——papers修改而创建的方法
        :param item_name: item名字如AD vs CTRL: albumin ratio (CSF)
        :param item: 默认为item
        :param db: db值的是
        :param col: 需要修改的列 默认是papers
        :param content: 修改的值
        :return: None
        测试过了
        """

        try:
            _sql = f"UPDATE `{table}` SET `{col}`='{content}' WHERE (`{item}`='{item_name}')"
            num_row = self.to_mysql.commitSql(cursor=self.to_mysql.dbCursor, connnect=self.to_mysql.dbConnect,
                                              _sql=_sql)
            sql.info(f"执行结果{num_row},执行sql：{_sql}")
        except Exception as e:
            print(e)
            sql.info(f"执行失败，sql：{_sql}")

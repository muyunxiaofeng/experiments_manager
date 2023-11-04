# -*- encoding: utf-8 -*-
"""
PyCharm toMysql
2022年11月03日
by Orochi
该文件目的
第一层

第二层

执行层

"""
import traceback

import pymysql

from . import settings

from ..middleWare.interfaceLog import *


class ToMysql:
    def __init__(self, host="", user="", password="", db=""):
        # callback setting
        self.my_set = settings.MysqlSettings()

        if host and user and password and db:
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

    def closeDb(self):
        self.ncbiConnect.close()
        self.rootConnect.close()

    def dbConnectClose(self):
        self.dbConnect.close()

    def commitSql(self, connnect=None, cursor="ncbi", _sql="show tables;"):
        rowNum = 0
        try:
            print(_sql)
            if type(cursor) is str:
                if cursor == 'ncbi':
                    rowNum = self.ncbiCursor.execute(_sql)
                    self.ncbiConnect.commit()
                elif cursor == 'root':
                    rowNum = self.rootCursor.execute(_sql)
                    self.rootConnect.commit()
                elif cursor == 'db':
                    rowNum = self.dbCursor.execute(_sql)
                    self.dbConnect.commit()
            else:
                # 需要再外面创建与数据库的连接和cursor
                rowNum = cursor.execute(_sql)
                connnect.commit()
        except Exception as e:
            print(e)
            print(traceback.format_exc())
            print(_sql, '执行失败')
            ex.exception(traceback.format_exc())
            ex.exception(_sql, '执行失败')

            if type(cursor) is str:
                if cursor == 'ncbi':
                    self.ncbiConnect.rollback()
                elif cursor == 'root':
                    self.rootConnect.rollback()
            else:
                connnect.rollback()

            return False
        else:
            sql.info(f"{_sql} 事件完成，影响行数{rowNum}")

        return True
        # return f"{_sql} 事件完成，影响行数{rowNum}"


"""
mysql database SQL:

create database NcbiDatabase character set utf8;
use NcbiDatabase
CREATE TABLE if not exists `papers` (
  `id` int(15) unsigned NOT NULL AUTO_INCREMENT,
  `pubmedId` int(15) NOT NULL,
  `paperTitle_url` varchar(200) NOT NULL,
  `paper_title` varchar(200) NOT NULL,
  `full_authors` varchar(250) NOT NULL,
  `short_authors` varchar(250),
  `doi` varchar(50) NOT NULL,
  `journal` varchar(50) NOT NULL,
  `pubmed` varchar(250) NOT NULL,
  `full_snippet` varchar(250) NOT NULL,
  `short_snippet` varchar(250),
  `save_date` DATETIME,
  `paperInfoDatabase` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE if not exists `paperInfo_01` (
  `id` int(15) unsigned NOT NULL AUTO_INCREMENT,
  `pubmedId` int(15) NOT NULL,
  `save_date` DATETIME,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



create database NcbiDatabase character set utf8;
use NcbiDatabase
CREATE TABLE if not exists `papers` (
  `id` int(15) unsigned NOT NULL AUTO_INCREMENT,
  `pubmedId` int(15),
  `paperTitle_url` varchar(200),
  `paper_title` varchar(200),
  `full_authors` varchar(250),
  `short_authors` varchar(250),
  `doi` varchar(50),
  `journal` varchar(50),
  `origin_url` varchar(255),
  `pubmed` varchar(250),
  `full_snippet` varchar(250),
  `short_snippet` varchar(250),
  `save_date` DATETIME,
  `paperInfoDatabase` varchar(50),
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



ALTER TABLE `papers`
MODIFY COLUMN `pubmedId`  int NULL AFTER `id`,
MODIFY COLUMN `paperTitle_url`  varchar(200) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL AFTER `pubmedId`,
MODIFY COLUMN `paper_title`  varchar(200) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL AFTER `paperTitle_url`,
MODIFY COLUMN `full_authors`  varchar(250) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL AFTER `paper_title`,
MODIFY COLUMN `doi`  varchar(50) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL AFTER `short_authors`,
MODIFY COLUMN `journal`  varchar(50) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL AFTER `doi`,
MODIFY COLUMN `pubmed`  varchar(250) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL AFTER `journal`,
MODIFY COLUMN `full_snippet`  varchar(250) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL AFTER `pubmed`,
MODIFY COLUMN `paperInfoDatabase`  varchar(50) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL AFTER `save_date`,
ADD COLUMN `origin_url`  varchar(255) NULL AFTER `journal`;

"""

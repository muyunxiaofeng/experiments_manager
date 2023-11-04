# -*- encoding: utf-8 -*-
"""
PyCharm NCBI_MW
2022年11月15日
by Orochi
该文件目的
第一层

第二层

执行层

"""
from .interfaceLog import *
from ..filePipeline import toMysql


class NCBI_MW:
    def __init__(self):
        logger.debug("start NCBI MW~~")
        self._sql = "show tables;"
        self.cursor = toMysql.ToMysql()
        # return

    def insertTo_Papers_Table(self, pubmedId, paperTitle_url, paper_title, full_authors, short_authors, doi,
                              journal, origin_url, pubmed, full_snippet, short_snippet, save_date, paperInfoDatabase):
        table = "papers"
        self._sql = f"INSERT INTO `{table}` (`pubmedId`, `paperTitle_url`, `paper_title`, `full_authors`," \
                    f" `short_authors`, `doi`, `journal`, `origin_url`, `pubmed`, `full_snippet`, `short_snippet`," \
                    f" `save_date`, `paperInfoDatabase`) " \
                    f"VALUES ('{pubmedId}', '{paperTitle_url}', '{paper_title}', '{full_authors}', '{short_authors}'," \
                    f" '{doi}', '{journal}', '{origin_url}', '{pubmed}', '{full_snippet}', '{short_snippet}'," \
                    f" '{save_date}', '{paperInfoDatabase}')"
        sql.info(self._sql)
        self.cursor.commitSql(_sql=self._sql)

        """
        INSERT INTO `papers` (`id`, `pubmedId`, `paperTitle_url`, `paper_title`, `full_authors`, `short_authors`, `doi`,
         `journal`, `pubmed`, `full_snippet`, `short_snippet`, `save_date`, `paperInfoDatabase`) 
         VALUES ('1', '123', '123', '13', '123', '123', '132', '132', '123', '213', '123', '2022-11-15 23:31:20', '123')
        
        
        INSERT INTO `papers` (`pubmedId`, `paperTitle_url`, `paper_title`, `full_authors`, `short_authors`, `doi`,
         `journal`, `pubmed`, `full_snippet`, `short_snippet`, `save_date`, `paperInfoDatabase`) 
         VALUES ('12', '123', '123', '13', '123', '123', '1', '12', '22', '11', '2022-11-30 19:56:05', '11')
        
        
        INSERT INTO `papers` (`pubmedId`, `paperTitle_url`, `paper_title`, `full_authors`, `short_authors`, `doi`,
         `journal`, `origin_url`, `pubmed`, `full_snippet`, `short_snippet`, `save_date`, `paperInfoDatabase`)
          VALUES ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '--', '2022-11-09 20:37:31', '0')
        
        print("select name,password from user where name=\"" + username + "\"")
        print("select name,password from user where name='" + username + "'")
        print("select name,password from user where name='%s'" % (username))
        print("select name,password from user where name='{}'".format(username))
        print(f"select name,password from user where name='{username}'")
        
        
        """

    def closeConnect(self):
        self.cursor.closeDb()
        # return

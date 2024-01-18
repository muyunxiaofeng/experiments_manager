# -*- encoding: utf-8 -*-
"""
PyCharm runToMysql
2022年11月03日
by Orochi
该文件目的
第一层

第二层

执行层

"""
from new_module.factory.filePipeline import toMysql

if __name__ == '__main__':
    m = toMysql.ToMysql()
    print(m.commitSql())
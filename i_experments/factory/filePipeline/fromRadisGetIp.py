# -*- encoding: utf-8 -*-
"""
PyCharm fromRadisGetIp
2022年10月29日
by Orochi
该文件目的
第一层

第二层

执行层

"""

import redis

from . import settings


class FromRadisGetIp:

    def __init__(self, db=0):
        self.s = settings.RadisSettings()
        if db == 0:
            self.r = redis.Redis(host=self.s.HOST, port=self.s.PORT, password=self.s.PASSWORD, db=self.s.DB,
                                 decode_responses=True)
        else:
            self.r = redis.Redis(host=self.s.HOST, port=self.s.PORT, password=self.s.PASSWORD, db=db,
                                 decode_responses=True)

    def getIp_fromRadis(self, zset="verifyIp"):
        return self.r.zrange(zset, 0, -1, withscores=True)

    def getTopIp_fromRadis(self, zset="verifyIp"):
        return self.r.zrangebyscore(zset, 100, 1000)

    def getMidIp_fromRadis(self, zset="verifyIp"):
        return self.r.zrangebyscore(zset, 50, 1000)

    def getFormatIp_fromRadis(self, zset="verifyIp"):
        ipScoreList = self.getIp_fromRadis(zset)
        ipList = []
        for ipScore in ipScoreList:
            _ip_port = ipScore[0].split(":")
            _ip = _ip_port[0]
            _port = _ip_port[-1]
            _score = ipScore[1]
            # save_scores_list = ['IP', '端口', "积分"]
            ipList.append({'IP': _ip, '端口': _port, "积分": _score})
        # print("fromRadisGetIp.py  \t ", ipList)
        # pprint.pprint(ipList)
        for ip in ipList:
            logger.info(f"{ip}")

        return ipList

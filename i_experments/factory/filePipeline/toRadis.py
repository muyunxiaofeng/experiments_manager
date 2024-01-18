# -*- encoding: utf-8 -*-
"""
PyCharm toRadis
2022年10月29日
by Orochi
该文件目的
第一层

第二层

执行层

"""
import redis

from . import settings


class ToRadis:
    total = 0

    def __init__(self, db=0):

        # # os.system(r"cd /d D:\OneDrive\201.python\redis-64.3.0.503")
        # os.system(r"start D:\OneDrive\201.python\redis-64.3.0.503\redis-server.exe redis.windows.conf")
        # time.sleep(2)
        # os.system(r"start D:\OneDrive\201.python\redis-64.3.0.503\redis-cli.exe")

        self.s = settings.RadisSettings()
        if db == 0:
            self.r = redis.Redis(host=self.s.HOST, port=self.s.PORT, password=self.s.PASSWORD, db=self.s.DB,
                                 decode_responses=True)
        else:
            self.r = redis.Redis(host=self.s.HOST, port=self.s.PORT, password=self.s.PASSWORD, db=db,
                                 decode_responses=True)

    def addIp(self, ipList: list, key_words: list, spot=":", zset=None):
        for ipInfo in ipList:
            ip = []
            for key_word in key_words[:2:]:
                ip.append(ipInfo.get(key_word))

            ip = spot.join(ip)
            self.total += 1
            # print("toRadis: ", ip, "\t",
            #        time.strftime("%Y年%m月%d日 %H.%M.%S", time.localtime()), "\t ip数量：", self.total)
            logger.info(f"{self.total}->{ip}")

            # 初始化
            if zset is None:
                self.r.zadd(self.s.ZSET_NAME, {f"{ip}": ipInfo.get(key_words[-1])})
            else:
                self.r.zadd(zset, {f"{ip}": ipInfo.get(key_words[-1])})

                # self.r.zadd("proxy_radis", {f"{ip}": self.s.SCORE})
        # self.r.zadd("proxy_radis", {"b": 50})
        # self.r.save()

    def ipAdd(self, iplist):
        for ip in iplist:
            self.r.zadd(self.s.ZSET_NAME, {f"{ip}": "100"})

    def flushDb(self):

        return self.r.flushdb()

    def deleteKey(self, key):

        return self.r.delete(key)

    def saveRadis(self):
        return self.r.save()

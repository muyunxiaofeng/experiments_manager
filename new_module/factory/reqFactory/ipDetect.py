# -*- encoding: utf-8 -*-
"""
PyCharm ipDetect
2022年10月29日
by Orochi
该文件目的
第一层

第二层

执行层

"""
import traceback
from ..filePipeline import toTxt, toCSV, toRadis, fromRadisGetIp
from . import ipSpider, requestTool, settings


class IpDetect:

    def __init__(self):
        self.IpDic = {}
        self.save_keys_list = ['IP', '端口']
        self.save_scores_list = ['IP', '端口', "积分"]
        self.mList = None
        self.ip_spider = ipSpider.IpSpider()
        self.req = requestTool.RequestTool(None)
        self.ipSettings = settings.IpSpiderSettings()
        self.dataBaseIp = fromRadisGetIp.FromRadisGetIp(db=self.ipSettings.VERIFY_IP_DB)

    def ipDetector(self, ipList=None, get98Ip=True):
        """
        在ipSpider中存储ip信息
        :return:
        """
        index = 0
        try:

            # 组装self.mList
            # _dic = {"1": 1}
            self.processMList(get98Ip, index, ipList)

            # save_scores_list = ['IP', '端口', "积分"]
            # detect ip
            self.select_ip()

            # SAVE
            self.save()

        except Exception as e:
            ex.exception(e)
            ex.exception(traceback.format_exc())
            # print(e)
            # print(traceback.format_exc())
            if self.ipSettings.DEBUGGER:
                exit()

    def processMList(self, get98Ip, index, ipList):
        """
        控制如何汇总self.mList（放置所有ip的）
        :param get98Ip: bool 是否进行ip98的获取
        :param index: 是否对数据库的ip进行核实
        :param ipList:
        :return:
        """
        if get98Ip is False:
            self.mList = ipList + self.dataBaseIp.getFormatIp_fromRadis(zset=self.ipSettings.VERIFY_IP_ZSET)
        # return 模式
        # _dic = self.ip_spider.get_98ip()

        # yield 模式
        else:
            for _dic in self.ip_spider.get_98ip():
                # 获取mList 【｛｝｛｝｛ipinfo｝】
                self.save_keys_list = _dic.get("save_keys_list")
                self.save_scores_list = _dic.get("save_scores_list")

                if ipList is not None:
                    self.mList = _dic.get("mList") + ipList \
                                 + self.dataBaseIp.getFormatIp_fromRadis(zset=self.ipSettings.VERIFY_IP_ZSET)

                elif index == 0:
                    self.mList = _dic.get("mList") \
                                 + self.dataBaseIp.getFormatIp_fromRadis(zset=self.ipSettings.VERIFY_IP_ZSET)
                else:
                    if index > 0:
                        index += 999
                    self.mList = _dic.get("mList")
                index += 1
                logger.warning(f"第{index}次核对ip")
                # print("ipDetect.py \t index \t ", index, "^" * 20)

    def select_ip(self):
        infoList = []
        stats_code = 0
        n = 0
        good_ip = 0
        bad_ip = 0
        for ipInfo in self.mList:
            isNewIp = "new ip"

            _ip = ipInfo.get("IP") + ":" + ipInfo.get('端口')

            # 解决已经存在了ip的问题
            _score, isNewIp = self.ipIsExist(_ip, infoList, ipInfo, isNewIp, n)

            _score = int(_score)
            try:
                stats_code = self.req.testIp(_ip)
                # print("ipDetect.py stats_code", stats_code)
                # print(type(stats_code))
                _score = self.forScore(_score, stats_code)
                if stats_code == 200:
                    good_ip += 1
            except Exception as e:
                stats_code = 999
                bad_ip += 1
                # print(e)
                _score -= 10
                if _score < -1000:
                    _score = -999
                # print(traceback.format_exc())
                continue
            finally:
                # print("ipDetect.py  \t ", time.strftime("%Y年%m月%d日 %H.%M.%S", time.localtime()),
                #       f"{_ip}:{_score} \t -->{stats_code} \t by {isNewIp}")
                logger.info(f"{_ip}:{_score}->{stats_code} is {isNewIp}")
                ipInfo["积分"] = f"{_score}"
                infoList.append(ipInfo)
        self.mList = infoList
        # print("ipDetect.py \t ", self.mList, "\t", "总共:", len(self.mList), "个")
        summary.info(f"共{len(self.mList)}个ip: good ip {good_ip} 个 \t bad ip {bad_ip} 个")

    @staticmethod
    def forScore(_score, stats_code):
        if stats_code < 201:
            if _score < 0:
                _score = 0
            _score += 1
            if _score > 999:
                _score = 999
        else:
            _score -= 1
        return _score

    def ipIsExist(self, _ip, infoList, ipInfo, isNewIp, n):
        """
        判断ip是否存在，存在的话获取旧的积分，否则使用现存的积分
        :param _ip:
        :param infoList:
        :param ipInfo:
        :param isNewIp:
        :param n:
        :return:
        """
        if self.IpDic.get(_ip) is None:
            self.IpDic.update({_ip: n})
            n += 1
            _score = ipInfo.get("积分")

        else:
            isNewIp = "old ip"
            IpDicNum = self.IpDic.get(_ip)
            old_ipInfo = infoList[IpDicNum]
            old_score = old_ipInfo.get("积分")

            new_score = ipInfo.get("积分")
            # 谁小要谁
            if int(old_score) > int(new_score):
                _score = new_score
            else:
                _score = old_score
        return _score, isNewIp

    def save(self):
        if self.ipSettings.SAVE_DATA:

            if self.ipSettings.SAVE_TXT:
                ttt = toTxt.ToTXT()
                ttt.quickSave_followedByScoreList(li=self.mList, followList=self.save_scores_list)
                ttt.quickSave_followedByList(li=self.mList, followList=self.save_keys_list)

            if self.ipSettings.SAVE_CSV:
                t_csv = toCSV.ToCSV()
                t_csv.pandasSave(self.mList)

            if self.ipSettings.SAVE_RADIS:
                t_radis = toRadis.ToRadis(db=1)
                t_radis.addIp(self.mList, self.save_scores_list, zset=self.ipSettings.VERIFY_IP_ZSET)

    def independentlyDetectIp(self):

        # 获取db0的ipList
        db0_to = toRadis.ToRadis(db=self.ipSettings.PROXY_RADIS_DB)
        db0_from = fromRadisGetIp.FromRadisGetIp(db=self.ipSettings.PROXY_RADIS_DB)

        # 获取没有过滤过的IpList
        proxy_radis_ipList = db0_from.getFormatIp_fromRadis(zset=self.ipSettings.PROXY_RADIS_ZSET)
        # print(inspect.stack())
        # print(proxy_radis_ipList)

        # 清空PROXY_RADIS_ZSET
        db0_to.deleteKey(self.ipSettings.PROXY_RADIS_ZSET)

        # 打印出来ipList
        # print(inspect.stack(), "\n", proxy_radis_ipList)
        # pprint.pprint(proxy_radis_ipList)

        # 进行筛选
        self.ipDetector(ipList=proxy_radis_ipList, get98Ip=False)

        return db0_to.saveRadis()

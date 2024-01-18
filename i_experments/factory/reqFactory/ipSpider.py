# -*- encoding: utf-8 -*-
"""
PyCharm ipSpider
2022年10月27日
by Orochi
该文件目的
第一层

第二层

执行层

"""
from multiprocessing import Manager
from ..reqFactory import requestTool as req_tool
from ..filePipeline import toTxt, toCSV, toRadis
from . import settings
import traceback


class IpSpider:

    def __init__(self):
        self.mDic = Manager().dict()
        self.mList = Manager().list()
        self.ipList = []
        self.ipInfo = []
        self.ipSettings = settings.IpSpiderSettings()
        self.exceptionNum = 0

    def get_98ip(self):
        """
        收集98ip的ip，并存储，不建议直接接连接池
        :return:
        """
        save_keys_list = ['IP', '端口']
        save_scores_list = ['IP', '端口', "积分"]

        # for num in range(1, 2):
        for num in range(1, 21):
            try:
                """
                网页访问部分
                """
                tbody, thead = self.getIps(num)

                """
                获取的ip信息进行 df格式的变化【｛｝，｛｝，｛｝】
                """
                self.formatIpInfo(tbody, thead)

                """
                存储ip信息
                """
                save_keys_list, save_scores_list = self.saveData(save_keys_list, save_scores_list)

                # yield 模式
                # yield {"save_keys_list": save_keys_list, "save_scores_list": save_scores_list, "mList": self.mList}

                if self.ipSettings.DEBUGGER:
                    exit()

                print("requestTool.py", '#' * 50)
                print("requestTool.py", '#' * 50)




            # 报错继续
            except Exception as e:
                # print("self.exceptionNum:", self.exceptionNum)
                logger.error(f"self.exceptionNum: {self.exceptionNum}")
                self.exceptionNum += 1

                # 应对断网时候
                if self.exceptionNum > self.ipSettings.MAX_EXCEPTION:
                    exit()
                print(e)
                print(traceback.format_exc())
                if self.ipSettings.DEBUGGER:
                    exit()
                continue

        # return 模式
        return [{"save_keys_list": save_keys_list, "save_scores_list": save_scores_list, "mList": self.mList}]

    def formatIpInfo(self, tbody, thead):
        _dic = {}
        for i, info in enumerate(tbody):
            if i % len(thead) == 0 and i != 0:
                # print("DIC", dic)
                self.mList.append(_dic)
                # print("mlist", mList)
                _dic = {}
            _dic[f"{thead[i % len(thead)]}".strip()] = info.strip()
            # 自定义积分部分
            _dic["积分"] = "100"

    @staticmethod
    def getIps(num):
        # https://www.89ip.cn/index_1.html
        homeUrl = f'https://www.89ip.cn/index_{num}.html'
        # 获取页面中信息
        # homeDic = tool.saveHtmlWithDate(homeUrl, ctrl=0)
        print("ipSpider.py \t homeUrl \t ", homeUrl)
        req = req_tool.RequestTool(homeUrl)
        homeDic = req.Dic
        # 获取ip的信息
        thead = homeDic.get("tree").xpath('//thead/tr/th/text()')
        tbody = homeDic.get("tree").xpath('//tbody/tr/td/text()')
        # print(thead)
        # print(tbody)
        return tbody, thead

    def saveData(self, save_keys_list=None, save_scores_list=None):
        # txt格式只存储的元素
        if save_keys_list is None:
            save_keys_list = ['IP', '端口']
        if save_scores_list is None:
            save_scores_list = ['IP', '端口', "积分"]
        # total_list = ['IP', '端口', '位置', '运营商', '收录时间']
        # 存起来本页
        # tool.save_data(mList, f"./ip_verify/ip{tool.getFormatDateNum()}{num}", save_keys_list=save_keys_list,
        #                separator=":")
        print("requestTool.py", self.mList)
        if self.ipSettings.SAVE_DATA:

            if self.ipSettings.SAVE_TXT:
                ttt = toTxt.ToTXT()
                ttt.quickSave_followedByScoreList(li=self.mList, followList=save_scores_list)
                ttt.quickSave_followedByList(li=self.mList, followList=save_keys_list)

            if self.ipSettings.SAVE_CSV:
                t_csv = toCSV.ToCSV()
                t_csv.pandasSave(self.mList)

            if self.ipSettings.SAVE_RADIS:
                t_radis = toRadis.ToRadis()
                t_radis.addIp(self.mList, save_scores_list)
                t_radis.saveRadis()
        return save_keys_list, save_scores_list

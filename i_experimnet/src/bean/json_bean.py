# -*- coding:utf-8 -*-
"""
README.md	项目名
PyCharm	集成开发环境
json_bean	文件名
frozensword	用户名（指登录电脑的那个用户名）
2023/11/9	当前系统的年月日
19:40	当前系统的时分秒
2023	当前年份
11	当前月份（形式：07）
11月	当前月份（形式：7月）
十一月	当前月份（形式：七月）
09	当天
19	当前小时
40	当前分钟
37	当前秒钟
"""


class Json_Bean:
    def __init__(self, _json=None):
        if _json is not None:
            self.load_json_bean(_json)

    def json_bean(self):
        """
        将bean转化为以个json，方便后续操作
        :return:
        """
        return json.dumps(self.__dict__)

    def load_json_bean(self, _json):
        """
        传入一个json，根据json转化成
        :param _json:
        :return:
        """

        try:
            # 将json转化为一个字典，此时可能会误传
            bean_dic = json.loads(_json)

            for _k in bean_dic:
                self.__setattr__(_k, bean_dic[_k])
        except json.JSONDecodeError:
            traceback.format_exc()

    def input_para(self, var_name, var_value):
        self.__setattr__(var_name, var_value)
        return self.__dict__

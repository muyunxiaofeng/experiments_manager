# _*_ coding:utf_8 _*_
"""
README.md	项目名
PyCharm	集成开发环境
bin_config	文件名
frozensword	用户名（指登录电脑的那个用户名）
2024/1/18	当前系统的年月日
22:37	当前系统的时分秒
2024	当前年份
01	当前月份（形式：07）
1月	当前月份（形式：7月）
一月	当前月份（形式：七月）
18	当天
22	当前小时
37	当前分钟
29	当前秒钟
"""


class items_config:
    items_files = "./files/items.xlsx"
    items_name = "items"


class de_info:
    items_base = ["date", "user", "platform"]

    de_beads_base = ["Beads_LOT", "Beads", "Beads_Conc.", "Beads_Unit", "Beads_Dilution", "Beads_Mfg.", "Beads_volume"]
    de_CA_base = ["CA_LOT", "CA", "CA_Conc.", "CA_Unit", "CA_Weight", "CA_Dilution", "CA_Mfg.", "CA_volume"]
    de_coating_base = ["before_Active_washing", "before_washing_buffer", "before_washing_times",
                       "before_washing_protocol"
                       "Active_formula", "Active_time",
                       "coating_formula", "coating_time"]
    de_blocking_base = ["before_blocking_washing", "before_washing_buffer", "blocking_formula", "blocking_time",
                        "after_Active_washing", "after_washing_buffer", "after_washing_times", "after_washing_protocol",
                        "storage_buffer"]
    de_Ag_base = ["Ag_LOT", "Ag", "Ag_Conc.", "Ag_Unit", "Ag_Dilution", "Ag_Mfg.", "Ag_volume", "Ag_protocol"]
    de_DA_base = ["DA_LOT", "DA", "DA_Conc.", "DA_Unit", "DA_Dilution", "DA_Mfg.", "DA_volume", "DA_protocol"]
    de_sbg_base = ["SBG_LOT", "SBG", "SBG_Conc.", "SBG_Unit", "SBG_Dilution", "SBG_Mfg.", "SBG_volume", "SBG_protocol"]
    de_base = ["Resuspension", "Resuspension_volume", "machine_LOT", "automatic.", "auto_washing"]
    de_calculator = ["positive_beads", "total_beads", "AEB", "positive_ratio", "input_beads", "recycle"]
    de_all = items_base + de_beads_base + de_CA_base + de_coating_base + de_blocking_base
    de_all += de_Ag_base + de_DA_base + de_sbg_base + de_base

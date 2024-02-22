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
from datetime import datetime


class items_config:
    platforms_files = "./files/platforms.xlsx"
    col_platforms = "platforms"
    items_files = "./files/items.xlsx"
    items_name = "items"
    col_items = "items"
    col_columns = "columns"
    col_version = "version"
    all_platform = "all"


class de_info:
    items_base = ["date", "user", "platform", "items", "version"]

    de_beads_base = ["Beads_LOT", "Beads", "Beads_Conc.", "Beads_Unit", "Beads_Dilution", "Beads_Mfg.", "Beads_volume"]
    de_CA_base = ["CA_LOT", "CA", "CA_Conc.", "CA_Unit", "CA_Weight", "CA_Dilution", "CA_Mfg.", "CA_volume"]
    de_coating_base = ["before_Active_washing", "before_washing_buffer", "before_washing_times",
                       "before_washing_protocol"
                       "Active_formula", "Active_time", "Active_temperature"
                                                        "coating_formula", "coating_time", "coating_temperature"]
    de_blocking_base = ["before_blocking_washing", "before_washing_buffer", "blocking_formula", "blocking_time",
                        "blocking_temperature", "after_Active_washing", "after_washing_buffer", "after_washing_times",
                        "after_washing_protocol", "storage_buffer"]
    de_Ag_base = ["Ag_LOT", "Ag", "Ag_Conc.", "Ag_Unit", "Ag_Dilution", "Ag_Mfg.", "Ag_volume", "Ag_protocol"]
    de_DA_base = ["DA_LOT", "DA", "DA_Conc.", "DA_Unit", "DA_Dilution", "DA_Mfg.", "DA_volume", "DA_protocol"]
    de_sbg_base = ["SBG_LOT", "SBG", "SBG_Conc.", "SBG_Unit", "SBG_Dilution", "SBG_Mfg.", "SBG_volume", "SBG_protocol"]
    de_base = ["Resuspension", "Resuspension_volume", "machine_LOT", "automatic.", "auto_washing", "file_path"]
    de_calculator = ["positive_beads", "total_beads", "AEB", "positive_ratio", "input_beads", "recycle"]
    de_error_base = ["effective_pictures", "AEB_STD", "AEB_CV%", "extract_version"]
    de_all = items_base + de_calculator + de_beads_base + de_CA_base + de_coating_base + de_blocking_base
    de_all += de_Ag_base + de_DA_base + de_sbg_base + de_base


class platform_info:
    platform_list = ["Digital_Elisa"]
    digital_elisa_items = [""]


from i_experments.src.de_data import De_data


class organize_data_config:
    now = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    organize_data_files_prefix = "./files/organize_data_files"
    organize_data_files_suffix = ".xlsx"
    backup_format_files = f"{now}"
    volumes_path = "/Volumes"
    platform_func = {
        "all": "De_data",
        "Digital_Elisa": De_data,
        "qRT_PCR": "De_data",
    }

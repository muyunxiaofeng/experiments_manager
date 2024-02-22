# -*- coding:utf-8 -*-
"""
README.md	项目名
PyCharm	集成开发环境
achive_files_opening	文件名
frozensword	用户名（指登录电脑的那个用户名）
2024/1/29	当前系统的年月日
07:16	当前系统的时分秒
2024	当前年份
01	当前月份（形式：07）
1月	当前月份（形式：7月）
一月	当前月份（形式：七月）
29	当天
07	当前小时
16	当前分钟
58	当前秒钟
"""
import string
import zipfile
import rarfile


class compressed_files_opening:
    def __init__(self):
        self.passwords = None
        self.passwords_file = None
        self.passwords_dir = None
        # 密码输出地址
        self.pwd_output_file = r"./compressed_files_opening.txt"

    def generate_passwords(self):
        pass

    def get_passwords(self):
        # 将字典中的所有密码读入内存
        with open(self.passwords_file, 'r') as f:
            passwords = f.readlines()

        # 去除每个密码后面的换行符
        self.passwords = [pwd.strip() for pwd in passwords]

    def uncompressed_zip(self, file_name):
        # 逐个尝试密码，直到找到正确的密码或者尝试完所有密码
        for password in self.passwords:
            try:
                with zipfile.ZipFile(file_name, 'r') as zip_file:
                    # 设置密码后解压缩文件
                    zip_file.extractall(pwd=password.encode('utf-8'))
                print('密码为：', password)
                break
            except Exception as e:
                continue

    def uncompress_rarfile(self, file_name):
        # 逐个尝试密码，直到找到正确的密码或者尝试完所有密码
        for password in self.passwords:
            try:
                with rarfile.RarFile(file_name) as rar_file:
                    # 设置密码后解压缩文件
                    rar_file.extractall(pwd=password.encode('utf-8'))
                print('密码为：', password)
                break
            except Exception as e:
                continue

    from String import string
    def pwd_output(self, file_name, pwd):
        string.ascii_letters
        pass

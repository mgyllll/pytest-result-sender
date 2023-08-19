#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2023/8/19 16:04
# @Author : Luo Yong(MGYL)
# @File : plugin.py
# @Software: PyCharm
from datetime import datetime


def pytest_configure():
    # 配置加载完毕之后执行，测试用例执行之前执行

    print(f"{datetime.now()} pytest执行！")

#!/usr/bin/env python
# encoding: utf-8
"""
@author: Shawn
@contact: 121857051@qq.com
@file: utc2local.py
@time: 12/3/2018 2:09 PM
"""

import datetime
import pytz


def utc_str_2_local_str(utc_time_str, utc_format='%Y-%m-%dT%H:%M:%SZ'):
    local_format = "%Y-%m-%d %H:%M"
    local_tz = pytz.timezone('Asia/Chongqing')
    utc_dt = datetime.datetime.strptime(utc_time_str, utc_format)
    local_dt = utc_dt.replace(tzinfo=pytz.utc).astimezone(local_tz)
    time_str = local_dt.strftime(local_format)
    return time_str


if __name__ == '__main__':
    print(utc_str_2_local_str("2018-12-03T16:19:52Z"))

#!/usr/bin/env python
# encoding: utf-8
"""
@author: Shawn
@contact: 121857051@qq.com
@file: alliance_info.py
@time: 11/30/2018 3:21 PM
"""
import request_factory


def alliance_info(alliance_id):
    r = request_factory.request_factory(alliance_id, "alliance_info")
    return r.get()


if __name__ == "__main__":
    print(alliance_info(403524217))

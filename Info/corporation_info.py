#!/usr/bin/env python
# encoding: utf-8
"""
@author: Shawn
@contact: 121857051@qq.com
@file: corporation_info.py
@time: 11/30/2018 3:21 PM
"""
from Base import request_factory


def corporation_info(corporation_id):
    r = request_factory.request_factory("corporation_info", corporation_id)
    return r.get()


if __name__ == "__main__":
    print(corporation_info(98021437))

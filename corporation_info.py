#!/usr/bin/env python
# encoding: utf-8
"""
@author: Shawn
@contact: 121857051@qq.com
@file: corporation_info.py
@time: 11/30/2018 3:21 PM
"""
import request_factory


def corporation_info(corporation_id):
    r = request_factory.request_factory(corporation_id, "corporation_info")
    return r.get()


if __name__ == "__main__":
    print(corporation_info(98021437))

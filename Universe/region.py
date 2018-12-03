#!/usr/bin/env python
# encoding: utf-8
"""
@author: Shawn
@contact: 121857051@qq.com
@file: region.py
@time: 12/3/2018 4:15 PM
"""
from Base import request_factory


def get_regions():
    r = request_factory.request_factory("universe_regions")
    return r.get()


def get_region(region_id):
    r = request_factory.request_factory("universe_region", region_id)
    return r.get()


if __name__ == "__main__":
    get = get_regions()
    print(len(get))
    for i in range(len(get)):
        if i % 10 == 0:
            print(get_region(get[i])["name"])

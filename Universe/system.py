#!/usr/bin/env python
# encoding: utf-8
"""
@author: Shawn
@contact: 121857051@qq.com
@file: system.py
@time: 12/3/2018 3:57 PM
"""
from Base import request_factory


def get_systems():
    r = request_factory.request_factory("universe_systems")
    return r.get()


def get_system(system_id):
    r = request_factory.request_factory("universe_system", system_id)
    return r.get()


if __name__ == "__main__":
    get = get_systems()
    print(len(get))
    for i in range(len(get)):
        if i % 300 == 0:
            print(get_system(get[i])["name"])


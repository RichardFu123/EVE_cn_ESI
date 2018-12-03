#!/usr/bin/env python
# encoding: utf-8
"""
@author: Shawn
@contact: 121857051@qq.com
@file: constellation.py
@time: 12/3/2018 4:11 PM
"""
from Base import request_factory


def get_constellations():
    r = request_factory.request_factory("universe_constellations")
    return r.get()


def get_constellation(constellation_id):
    r = request_factory.request_factory("universe_constellation", constellation_id)
    return r.get()


if __name__ == "__main__":
    get = get_constellations()
    print(len(get))
    for i in range(len(get)):
        if i % 50 == 0:
            print(get_constellation(get[i])["name"])

#!/usr/bin/env python
# encoding: utf-8
"""
@author: Shawn
@contact: 121857051@qq.com
@file: character_info.py
@time: 11/30/2018 3:21 PM
"""
from Base import request_factory


def character_id(name):
    r = request_factory.request_factory("character_id", name)
    return r.get()["character"][0]


def character_info(character_id):
    r = request_factory.request_factory("character_info", character_id)
    return r.get()


if __name__ == "__main__":
    print(character_id("军用馒头"))
    print(character_info(character_id("军用馒头")))

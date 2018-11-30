#!/usr/bin/env python
# encoding: utf-8
"""
@author: Shawn
@contact: 121857051@qq.com
@file: request_factory.py
@time: 11/30/2018 3:21 PM
"""
import request_base
import ESI_base


main_address = ESI_base.latest_address


def request_factory(key_str, request_type):
    request = None
    if request_type == "character_id":
        address = main_address + ESI_base.character_id(key_str)
        request = request_base.RequestBase(address, request_type)
    elif request_type == "character_info":
        address = main_address + ESI_base.character_info(key_str)
        request = request_base.RequestBase(address, request_type)
    elif request_type == "corporation_info":
        address = main_address + ESI_base.corporation_info(key_str)
        request = request_base.RequestBase(address, request_type)
    elif request_type == "alliance_info":
        address = main_address + ESI_base.alliance_info(key_str)
        request = request_base.RequestBase(address, request_type)
    else:
        print("request_factory: wrong type")
    return request

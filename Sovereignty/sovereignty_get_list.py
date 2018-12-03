#!/usr/bin/env python
# encoding: utf-8
"""
@author: Shawn
@contact: 121857051@qq.com
@file: sovereignty_get_list.py
@time: 12/3/2018 11:21 AM
"""
from enum import Enum, unique
from Base import request_factory


def campaigns_list():
    r = request_factory.request_factory("sovereignty_campaigns")
    return r.get()


def map_list():
    r = request_factory.request_factory("sovereignty_map")
    return r.get()


def structures_list():
    r = request_factory.request_factory("sovereignty_structures")
    return r.get()


@unique
class CampaignsEventType(Enum):
    tcu_defense = "TCU攻防"
    ihub_defense = "IHUB攻防"
    station_defense = "空间站攻防"
    station_freeport = "空间站自由港"


if __name__ == "__main__":
    from Convert import utc2local
    for i in CampaignsEventType:
        print(i.value)
    for campaign in campaigns_list():
        print(campaign)
        print(utc2local.utc_str_2_local_str(campaign['start_time']))
    print(len(map_list()))
    print(len(structures_list()))

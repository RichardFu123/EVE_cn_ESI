#!/usr/bin/env python
# encoding: utf-8
"""
@author: Shawn
@contact: 121857051@qq.com
@file: show_campaigns.py
@time: 12/3/2018 4:47 PM
"""

from Universe import region, constellation, system
from Sovereignty import sovereignty_get_list
from Convert import utc2local
from Player_info import alliance_info


def try_print(st):
    try:
        print(st)
    except:
        print()
        pass


def show_campaigns(campaign):
    print("="*10)
    print("战斗编号: ", end='')
    try_print(campaign["campaign_id"])
    print("防守方: ", end='')
    try_print(alliance_info.alliance_info(campaign["defender_id"])["name"])
    print("星域: ", end='')
    try_print(region.get_region(constellation.get_constellation(campaign['constellation_id'])['region_id'])["name"])
    print("星座: ", end='')
    try_print(constellation.get_constellation(campaign["constellation_id"])['name'])
    print("星系: ", end='')
    try_print(system.get_system(campaign["solar_system_id"])["name"])
    print("开始时间: ", end='')
    try_print(utc2local.utc_str_2_local_str(campaign['start_time']))
    print("作战目标: ", end='')
    try_print(sovereignty_get_list.CampaignsEventType[campaign['event_type']].value)
    print("目前进度: ", end='')
    try_print(f"进攻方{campaign['attackers_score']*100}% VS 防守方{campaign['defender_score']*100}%")
    print("="*10+"\n")


if __name__ == "__main__":
    campaigns_list = sovereignty_get_list.campaigns_list()
    for campaign in campaigns_list:
        show_campaigns(campaign)

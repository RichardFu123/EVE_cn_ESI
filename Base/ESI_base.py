#!/usr/bin/env python
# encoding: utf-8
"""
@author: Shawn
@contact: 121857051@qq.com
@file: ESI_base.py
@time: 11/30/2018 3:21 PM
"""
base_address = "https://esi.evepc.163.com/"
latest_address = base_address + "latest/"
dev_address = base_address + "dev/"
legacy_address = base_address + "legacy/"


def character_id(name):
    return f"search/?categories=character&datasource=serenity&language=zh&search={name}&strict=true"


def character_info(character_id):
    return f"characters/{character_id}/?datasource=serenity"


def corporation_info(corporation_id):
    return f"corporations/{corporation_id}/?datasource=serenity"


def alliance_info(alliance_id):
    return f"alliances/{alliance_id}/?datasource=serenity"


def sovereignty_campaigns():
    return "sovereignty/campaigns/?datasource=serenity"


def sovereignty_map():
    return "sovereignty/map/?datasource=serenity"


def sovereignty_structures():
    return "sovereignty/structures/?datasource=serenity"


def universe_systems():
    return "universe/systems/?datasource=serenity"


def universe_system(system_id):
    return f"universe/systems/{system_id}/?datasource=serenity&language=zh"


def universe_constellations():
    return "universe/constellations/?datasource=serenity"


def universe_constellation(constellation_id):
    return f"universe/constellations/{constellation_id}/?datasource=serenity&language=zh"


def universe_regions():
    return "universe/regions/?datasource=serenity"


def universe_region(region_id):
    return f"universe/regions/{region_id}/?datasource=serenity&language=zh"

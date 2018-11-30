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

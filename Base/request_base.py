#!/usr/bin/env python
# encoding: utf-8
"""
@author: Shawn
@contact: 121857051@qq.com
@file: request_base.py
@time: 11/30/2018 3:21 PM
"""
import requests


class RequestBase:
    https_address = ''
    tag = ''

    def __init__(self, https, tag):
        self.https_address = https
        self.tag = tag

    def get(self):
        try:
            result = request(self.https_address)
            return result
        except Exception:
            print(f"can not get {self.tag}.")
            print(Exception.args)


def request(address):
    r = requests.get(address, timeout=60)
    if r.status_code != 200:
        print("request error")
        raise Exception("request error")
    result = eval(r.text)  # 可能导致安全问题
    r.close()
    return result

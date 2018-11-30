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


def request(address):
    r = requests.get(address)
    if r.status_code != 200:
        print("request error")
        raise Exception
    result = eval(r.text)
    r.close()
    return result

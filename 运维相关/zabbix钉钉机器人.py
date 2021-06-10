#!/usr/bin/env python
# -*- coding:utf-8 -*-


import os
import sys
import json
import requests


# 这里填写创建的自定义机器人地址
# api_url = 'https://oapi.dingtalk.com/robot/send?access_token=673eeb8d38f99af9bb44b512449df06b349d5056cbc251e236ea8be0cfad0f78'
api_url = 'https://oapi.dingtalk.com/robot/send?access_token=decaf2ee0bcaf31f539acb0d812d10ae9b948528a0ad1611c78b646b6b76dd3f'
headers = {'Content-Type':'application/json;charset=utf-8'}

def message():
    json_text={
        "msgtype":"text",
        "text":{
            "content":text2
        },
   }
    print (requests.post(api_url,json.dumps(json_text),headers=headers).content)


if __name__ == '__main__':


#text的值为运行脚本带的参数


    text2 = sys.argv[1]
    message()
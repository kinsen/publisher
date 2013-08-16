#!/usr/bin/env python
#*_* coding=utf8 *_*

export_path = '/home/kong/project/publisher/data'
server_path = 'publisher'
server_data_path = 'publisher/data'


Applications = {
    "default": {
        "server_ip": "solidai.net",
        "server_name": "solidai",
        "server_passwd": '1234567890)(*&^%$#@!',
        "path": "/home/kong/project",
        "projects": ['solidai_bill', 'solidai_dash', 'solidai_invest',
                     'solidai_notice', 'solidai_ucenter', 'solidai_web',
                     'solidai_api_sdk', 'solidai_items', 'solidai_sdk',
                     'solidai_cms', 'solidai_ucenter_web', 'solidai_unionpay']
    },

    "cdit": {
        "server_ip": "",
        "server_name": "",
        "server_passwd": '',
        "path": "/home/kong/project/cdit",
        "projects": ['cdit_ucenter', 'cdit_host', 'cdit_bill',
                     'cdit_notice', 'cdit_cms', 'cdit_web',
                     'cdit_api_sdk', 'cdit_dash', 'cdit_unionpay',
                     '../zoro_sdk']
    }
}

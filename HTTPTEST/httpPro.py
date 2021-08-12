# coding=utf-8
import json  # 引入json标准库，美化json输出
import time

import requests  # pip安装requests第三方库，然后引入

headers = {'Content-Type': 'text/plain', 'File-Name': "scanner-config.json"}
# url = 'http://172.16.109.181:8080/scanner/configure.file'
url = 'http://192.168.199.167:8080/scanner/configure.file'
for i in range(0, 10):
    for j in range(0, 25):
        s = json.dumps({
            "DecodeMode": 1,
            "DecodeType": 1,
            "ExposureTime": 5000,
            "FlashLight1": 0,
            "FlashLight2": 0,
            "FlashLight3": 0,
            "FlashLight4": 0,
            "GainCoefficient": 35,
            "PositionLight1": False,
            "PositionLight2": False,
            "ScannerID": "SmoreScanner",
            "TriggeStart": {
                "DelayMs": 0,
                "Enable": False,
                "TriggeIo": 0,
                "TriggeModel": 0
            },
            "TriggerIntervalms": 500}
        )
        print(j)
        r = requests.post(url, headers=headers, data=s)
        print('===========PostConfigure==========')
        print(r.json())
        print('===========PostConfigure==========')
        time.sleep(0.1)
    s = json.dumps({
        "FlashLight1": 0}
    )
    r = requests.post(url, headers=headers, data=s)

# r = requests.post(url,headers = headers, data = s)


# conn = http.client.HTTPConnection('172.16.101.237',8080)
# for i in range(2):
# conn.request("GET", "/scanner/configure.file", '', {})
# r1 = conn.getresponse()
# print(r1.status, r1.reason, r1.info())
# print(r1.read())

# print('===========getConfigure==========')
# time.sleep(0.2)

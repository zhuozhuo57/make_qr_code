import json
import time

import requests  # pip安装requests第三方库，然后引入

headers = {'Content-Type': 'text/plain', 'File-Name': "scanner-config.json"}
# url = 'http://172.16.109.181:8080/scanner/configure.file'
url = 'http://192.168.199.60:8080/scanner/configure.file'
for i in range(0, 100):
    if (i % 2 == 0):
        s = json.dumps({
            "ExposureTime": 20000,
            "FlashLight1": 0,
            "FlashLight2": 1,
            "FlashLight3": 0,
            "FlashLight4": 0,
            "GainCoefficient": 80,
            "KeyConfig": {
                "TrigKeyEnable": True,
                "TuneKeyEnable": True}
        }
        )
        r = requests.post(url, headers=headers, data=s)
        print('===========PostConfigure==========')
        print(r.json())
        print(i)
        print('===========PostConfigure==========')
        time.sleep(1)
    else:
        s = json.dumps({
            "FlashLight1": 0,
            "FlashLight2": 0,
            "FlashLight3": 0,
            "FlashLight4": 0,
            "PositionLight1": True,
            "PositionLight2": True,
        }
        )
        r = requests.post(url, headers=headers, data=s)
        print('===========PostConfigure==========')
        print(r.json())
        print(i)
        ##time.sleep(1)
        print('===========PostConfigure==========')

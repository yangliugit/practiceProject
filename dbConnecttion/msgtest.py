# -*- coding: utf-8 -*-

import requests
import json


# headers = {'Content-Type': 'application/x-www-form-urlencoded'}
# data = {
#     "mob": "15651685093",
#     "msg": "【品值APP】您的验证码为898989,回复TD退订",
#     "pswd": "gloomysw@axon"
# }
#
# url = "http://v.js165.com/message/sendMessage"
#
# result = requests.post(url, data=data)
#
# print result.text, result.status_code

data = {
    "user": "19444444444",
    "password": "1",
    "vCode": "yyhh"
}

headers = {'content-type': 'application/json'}

url1 = "http://10.10.141.79:8080/icompaign/loginByName.view"

url2 = "http://10.10.141.79:8080/icompaign/getVerifyCode"

requests.get(url2)
result = requests.post(url1, data=json.dumps(data), headers=headers)


print result.status_code

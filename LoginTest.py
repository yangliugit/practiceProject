# coding=utf-8

import requests


url = 'http://10.10.141.79:8080/icompaign/loginByPhone.view'
headers = {"Accept": "application/json, text/javascript, */*; q=0.01",
           "Accept-Encoding": "gzip, deflate",
           "Accept-Language": 'zh-CN,zh;q=0.8',
           "Content-Type": "application/json;charset=UTF-8",
           "Connection": "keep-alive",
           "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36"}
s = requests.session()
r = s.get(url, headers=headers, verify=False)
print s.cookies

data = {"phone": "18626330613", "code": "111111", "vCode": "vpef"}
r1 = s.post(url, data=data, headers=headers)
print r1.status_code



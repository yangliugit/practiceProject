# -*- coding: utf-8 -*-

import requests
import time
# # 先打开登录首页，获取部分cookie
# url = "http://10.10.141.79:8080/icompaign/index.view"
# # get方法其它加个ser-Agent就可以了
# headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0"}
#
# s = requests.session()
# r = s.get(url, headers=headers, verify=False)
# print s.cookies
url = 'http://zbz.legaldaily.com.cn/works/index.php/home/works/addVote'
data = {'w_id': 224}

for i in range(1000):
    # time.sleep(1)
    respone = requests.post(url, data)
    print respone.status_code
print 'done'


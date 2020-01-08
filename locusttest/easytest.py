# coding=utf-8
from locust import HttpLocust, TaskSet, task
import json
import requests

# http://localhost:8089


class WebsiteTasks(TaskSet):

    params = {
        "udcid": 1559716305062900,
        "serviceChannel": "pzcash_wzf",
        "phone": "18800000111",
        "idcard": "500384198104010018",
        "name": "重庆男",
        "idcardFrontImg": "http://res.pinzhi.xin//useridcard/20171123/BodyPart_145b77a9-4465-43e4-9b19-9adf715610c42.png",
        "idcardBackImg": "http://res.pinzhi.xin//useridcard/20171123/BodyPart_3be0db04-95f0-417e-af60-2941fdb8671c.png",
        "NCIC": 1,
        "fivePlusTwo": {
            "idcardType": "身份证",
            "nationality": "中国",
            "nation": "汉",
            "gender": "男",
            "companyName": "Axon",
            "occupation": "软件工程师",
            "maritalStatus": "未婚",
            "familyMonthIncome": "40000",
            "monthIncome": "40000",
            "taxStatus": "纳税大户",
            "idcardValidateDate": "2016.06.12-2036.06.12",
            "relativesName": "沃钱包",
            "relativesShip": "erzi",
            "relativesPhone": "18800000111",
            "province": "江苏省",
            "city": "无锡市",
            "address": "宁双路19号云密城D栋10楼",
            "yearIncome": 3000000,
            "degree": "博士sss"
        }
    }
    headers = {'content-type': 'application/json'}

    startPhone = 10100000002

    def one_start(self):
        queryParams = {"mobilephone": self.startPhone,
                       "serviceChannel": "pzcash_wzf"}
        response = requests.post('http://10.10.141.58:8080/iudc/QueryUid', data=json.dumps(queryParams), headers=self.headers)
        self.params["udcid"] = response.json()["data"]["uid"]
        self.params["phone"] = self.startPhone
        self.startPhone += 1

    @task(1)
    def setData(self):
        self.client.post("/WZFData", data=json.dumps(self.params), headers=self.headers)


class WebsiteUser(HttpLocust):
    task_set = WebsiteTasks
    host = "http://10.10.141.51:18880/smartIcreditrisk/credit"
    min_wait = 1000
    max_wait = 5000



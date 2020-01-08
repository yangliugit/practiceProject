# -*-coding:utf-8 -*-
from locust import HttpLocust, TaskSet, task
import json
from Common import get_cycle_data_from_db


class UserBehavior(TaskSet):

    def on_start(self):
        pass

    # @seq_task(1) 表示执行顺序 python3版本中有
    def get_uid_phone(self):
        # 获取task中入参phone和uid
        phone = get_cycle_data_from_db('locust_data.wzf_phone', 'phone')
        headers = {"content-type": "application/json"}
        queryParams = {"mobilephone": phone,
                       "serviceChannel": "pzcash_wzf"}
        queryuid_url = 'http://10.10.141.58:8080/iudc/QueryUid'
        res = self.client.post(queryuid_url, data=json.dumps(queryParams), headers=headers)
        print res
        print res.json()
        uid = res.json()["data"]["uid"]
        return [phone, uid]

    @task(1)  # @task(1) 表示装饰该方法为一个压测任务， 1 表示一个Locust实例被挑选执行的权重，数值越大执行频率越高；
    def wzf_data_res(self):
        # 调用wzf_data接口，进行压测
        uid_phone_list = self.get_uid_phone()

        if len(uid_phone_list) == 2:

            params_set_idcard = {
                "udcid": uid_phone_list[1],
                "serviceChannel": "pzcash_wzf",
                "idcard": "700384198104010018",
                "name": "DBF",
                "phone": uid_phone_list[0],
                "idcardFrontImg": "http://res.pinzhi.xin//useridcard/20171123/BodyPart_145b77a9-4465-43e4-9b19-9adf715610c42.png",
                "idcardBackImg": "http://res.pinzhi.xin//useridcard/20171123/BodyPart_3be0db04-95f0-417e-af60-2941fdb8671c.png",
                "NCIC": 1
            }
            headers = {"content-type": "application/json"}
            wzf_uri = "/smartIcreditrisk/credit/WZFData"
            wzf_res = self.client.post(wzf_uri, data=json.dumps(params_set_idcard), headers=headers)

            # 添加检查点
            assert wzf_res.status_code == 200


class WebsitUser(HttpLocust):
    # 指定host
    host = "http://10.10.141.51:18880"
    # 指向一个定义了的用户类
    task_set = UserBehavior
    min_wait = 3000  # 用户执行任务之间等待时间的下界，单位：毫秒
    max_wait = 6000  # 用户执行任务之间等待时间的上界，单位：毫秒
    # 执行方式1： locust -f locustfile.py --no_web -c 1 -n 1
    # 执行方式2： locust -f --locustfile -H 指定host，在WebsitUser类中没有指定host的情况下

    # locust共存版本可以通过修改 Script中启动文件名为 locust2和locust3 ， 当locust2 -f --filename 启动报错 Fatal error in launcher: Unable to create process using '"' 的时候，采用以下方法进行解决:
    # 如果locust同时存在一台机器的多个python版本中，且修改了python.exe文件的名称。 那么第一种解决办法：还原python.exe
    # 第二种解决办法：用十六进制文件编辑器，修改locust的启动文件中python.exe为之前更改的python。。。.exe


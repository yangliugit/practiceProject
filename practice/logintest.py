from locust import HttpLocust, TaskSet, task
from random import randint

header = {'Content-type': 'application/json;charset=UTF-8'}

class LoginBehavior(TaskSet):

    def phone(self):
        with open('E:\phone.txt','r') as f:
            phones = f.readlines()
        i = randint(0, 50000)
        return phones[i]

    @task(1)
    def market(self):
        self.client.post("/icompaign/loginByPhone.view", json={"phone":self.phone(),"code":"111111"}, headers=header)


class WebsiteUser(HttpLocust):
    task_set = LoginBehavior
    min_wait = 3000
    max_wait = 6000
    host = "http://10.10.141.79:8080"
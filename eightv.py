import requests

params = {
    'login_username': 'liuyang',
    'login_password': 'qwe@1234'
}


url = "http://10.10.188.224:8080/seeyon/main.do?method=login"

reps = requests.post(url, params)
print(reps.text)

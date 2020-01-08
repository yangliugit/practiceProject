import requests


url = "http://172.10.20.204:5000/customerLmtQry"
url1 = "http://172.10.20.204:5000/loanTrial"
request_data = {
    "name": "liuyang",
    "age": 12
}
response = requests.post(url, data=request_data)
print(response.status_code)
print(response.text)

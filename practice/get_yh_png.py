import requests

url = "https://mp.weixin.qq.com/s/Bd4G5OFgO_6DdNkOO5dfCQ"
res = requests.get(url)
print(res.status_code)
print(res.text)
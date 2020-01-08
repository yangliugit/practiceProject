import requests, json


def get_phone_id():
    startPhone = 91100000003
    headers = {'content-type': 'application/json'}
    queryParams = {"mobilephone": startPhone,
                   "serviceChannel": "pzcash_wzf"}
    response = requests.post('http://10.10.141.58:8080/iudc/QueryUid', data=json.dumps(queryParams),
                             headers=headers)

    print(response.json())
    print(response.json()["data"]["uid"])
    # print(response.json()["data"]["mobilephone"])
    # print(startPhone)
    # print(json.dumps(headers))
    startPhone += 1


if __name__ == '__main__':
        get_phone_id()

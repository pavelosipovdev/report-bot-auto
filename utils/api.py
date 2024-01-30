import requests
import os
# from config_reader import config


def get_aim():
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    TOKEN = "\'" + os.getenv('OAUTH_TOKEN') + "\'"
    data = '{"yandexPassportOauthToken": %s}' % TOKEN
    # data = '{"yandexPassportOauthToken": "y0_AgAAAAAS0NXPAATuwQAAAAD3srwL_uAEamMASp6bTeJK4m2SkhXi2jE"}'

    response_iam_token = requests.post('https://iam.api.cloud.yandex.net/iam/v1/tokens', headers=headers, data=data)
    datas = response_iam_token.json()
    return datas["iamToken"]


def get_strings_vin():
    key = str(get_aim())
    headers_json = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + key,
    }

    with open('body_vin.json') as f:
        data_json = f.read().replace('\n', '').replace('\r', '').encode()

    response_output = requests.post('https://vision.api.cloud.yandex.net/vision/v1/batchAnalyze', headers=headers_json,
                                    data=data_json)
    data = response_output.json()
    alldata = data["results"][0]["results"][0]["textDetection"]["pages"][0]["entities"]
    return alldata


def get_strings_japan():
    key = str(get_aim())
    headers_json = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + key,
    }

    with open('body_japan.json') as f:
        data_json = f.read().replace('\n', '').replace('\r', '').encode()

    response_output = requests.post('https://vision.api.cloud.yandex.net/vision/v1/batchAnalyze', headers=headers_json,
                                    data=data_json)
    data = response_output.json()
    # print(data)
    # alldata = data["results"][0]["results"][0]["textDetection"]["pages"][0]["blocks"][1]["lines"][0]["words"][0]["text"]
    alldata = data["results"][0]["results"][0]["textDetection"]["pages"][0]["blocks"]
    return alldata

# python 3.8
import time
import hmac
import hashlib
import base64
import urllib.parse
import requests

timestamp = str(round(time.time() * 1000))
secret = 'SECf30d1841b7caf1ce6a7ba149f1f793c4c7d0d102c6528eba600babddef91f7fb'
secret_enc = secret.encode('utf-8')
string_to_sign = '{}\n{}'.format(timestamp, secret)
string_to_sign_enc = string_to_sign.encode('utf-8')
hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))
print(timestamp)
print(sign)

url = "https://oapi.dingtalk.com/robot/send"
data = {
    "msgtype": "text",
    "text": {
        "content": "API平台接口自动化执行完成。\n"
                   "测试概述:\n"
                   "运行总数:" + "195" +
                   "\n通过数量:" + "195" +
                   "\n失败数量:" + "0" +
                   "\n构建地址:\n" + "http://172.24.115.171:9000" +
                   "\n报告地址：\n" + "http://172.24.115.171:9000/API自动化测试/693/allure" +
                   "\n用户名：\n" +
                   "tianyancha   Tyc123456"
    },
    "at": {
        "atMobiles": [
            ""
        ],
        "isAtAll": "false"
    }
}

r = requests.post(url=url,
                  params={
                      "access_token": "8fe5e8257671025ebe28ea90fc7994e4df5b4ba55c4a5d31e84879faba91220a",
                      "timestamp": timestamp,
                      "sign": sign
                  },
                  json=data
                  )
print(r.json())

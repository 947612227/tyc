import requests


def send_alarm():
    feishu_req = requests.post(
        # url='http://alarm.tyc.local/alarm/api',  # 大群报警
        # url = 'http://alarm.test.tyc.io/alarm/api',
        url='http://10.2.128.184:10031/alarm/api',  # 小范围报警（王杨/刘淼的小群）
        json={
            "apiId": '1001',
            "text":
                    "\n【参数】\n" + "\n【其他数据】:测试内容",

            "level": "L2"
        },
        headers={
            "Content-Type": "application/json"
        })
    print(feishu_req.json())

send_alarm()
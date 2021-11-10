import requests


def feishu_retry_alert(api_id,msg_text):#调用曌哥写好的接口

    feishu_req = requests.post(
        url='http://alarm.tyc.local/alarm/api',  # 大群报警
        # url = 'http://alarm.test.tyc.io/alarm/api'
        # url='http://10.2.128.184:10031/alarm/api',  # 小范围报警（王杨/刘淼的小群）,测试群组
        json={
            "apiId": api_id,
            "text":
                msg_text,

            "level": "L3"
        },
        headers={
            "Content-Type": "application/json"
        })
    print(feishu_req.json())

if __name__ == '__main__':
    feishu_retry_alert(api_id=748, msg_text='text')
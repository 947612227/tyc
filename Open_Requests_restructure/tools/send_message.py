#!/usr/bin/env python
# coding: utf-8
import requests
import json

def get_token(app_id = "cli_a18033b79138d013",app_secret = "o4DPhGOUrzmNkCyTlm1sEee26sDkQ2qX"):
    """获取应用token，需要用app_id和app_secret，主要是上传图片需要用到token"""
    url = r"https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal/"
    headers = {"Content-Type": "text/plain"}
    Body = {
    "app_id":app_id,
    "app_secret":app_secret
    }
    r = requests.post(url, headers=headers, json=Body)
    return json.loads(r.text)['tenant_access_token']

def get_chat_id():
    url = r'https://open.feishu.cn/open-apis/chat/v4/list'
    headers = {'Authorization': "Bearer " + get_token(),"Content-Type": "application/json; charset=utf-8"}
    r = requests.post(url, headers=headers)
    return r.json()['data']['groups'][0]['chat_id']

def upload_image(image_path):
    """上传图片"""
    with open(image_path, 'rb') as f:
        image = f.read()
    resp = requests.post(
        url='https://open.feishu.cn/open-apis/image/v4/put/',
        headers={'Authorization': "Bearer "+get_token()},
        files={
            "image": image
        },
        data={
            "image_type": "message"
        },
        stream=True)
    resp.raise_for_status()
    content = resp.json()
    if content.get("code") == 0:
        return content['data']['image_key']
    else:
        return Exception("Call Api Error, errorCode is %s" % content["code"])

def send_text(Text,bot):
    """发送普通消息"""
    url = f"https://open.feishu.cn/open-apis/bot/v2/hook/{bot}"
    headers = {"Content-Type": "text/plain"}
    data = {
        "msg_type": "text",
        "content": {
            "text": Text
        }
    } 
    r = requests.post(url, headers=headers, json=data)
    return r.text

def send_img(path,bot):
    """发送图片消息"""
    url = f"https://open.feishu.cn/open-apis/bot/v2/hook/{bot}"
    headers = {"Content-Type": "text/plain"}
    data = {
        "msg_type":"image",
        "content":{
            "image_key": upload_image(path)
        }
    }  
    r = requests.post(url, headers=headers, json=data)
    return r.text

def send_markdown(text,img_path,bot):
    """发送富文本消息"""
    url = f"https://open.feishu.cn/open-apis/bot/v2/hook/{bot}"


    img = upload_image(img_path)
    chat_id = get_chat_id()

    headers = {"Content-Type": "text/plain"}
    data = {
    "chat_id":chat_id,
    "msg_type": "interactive",
    "card":{
      "elements":[
         {
            "tag":"img",
            "title":{
               "tag":"plain_text",
               "content":text
            },
            "img_key":img,
            "mode": "fit_horizontal",
            "alt":{
               "tag":"plain_text",
               "content":"Hover图片后的tips提示，不需要可以传空"
            }
         }
      ]
   }
}
    r = requests.post(url, headers=headers, json=data)
    return r.text

def send_card(Text,bot):
    """发送卡片消息"""
    url = f"https://open.feishu.cn/open-apis/bot/v2/hook/{bot}"
    headers = {"Content-Type": "text/plain"}
    data = {
    "msg_type": "interactive",
    "card": Text
    } 
    r = requests.post(url, headers=headers, json=data)
    return r.text

def send_file(file_path,bot):
    """发送文件，目前没有找到方法，推荐用七牛代替"""

if __name__ == '__main__':
    # 飞书消息发送说明
    # 测试消息群(消息机器人的id):
    bot = '6fbd7c64-f0ee-4397-8ff1-e1470529b991'

    # 1.发送普通文本消息
    text = '测试多行\n文本'
    send_text(text,bot)

    # 2.发送图文消息,markdown资料
    img_path = 'index.png'
    text = '测试多行\n文本'
    send_markdown(text,img_path,bot)



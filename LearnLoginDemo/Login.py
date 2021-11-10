# -*- coding: utf-8 -*-
# @Time : 2021/6/24 9:33 上午
# @Author : snnnnnn

# 使用flask库里面的Flask
import json
from flask import Flask, request, jsonify

from File import read_all_data, reg_write_csv

app = Flask(__name__)


@app.route('/app/register', methods=['POST'])  # 定义接口路径及请求方式
def register():  # 注册接口函数，里面编写具体逻辑

    if not request.get_data(as_text=True):
        return '请传入必要参数'
    data = json.loads(request.get_data(as_text=True))  # 接受json格式的数据
    #     定义参数
    username = data['username']
    password = data['password']

    # print(f'您输入的用户名为:{username},您输入的密码为: {password}')
    # 编写具体逻辑
    if not username:
        return {'name': username, 'message': '用户名不能为空', 'code': 2000}

    elif not password:
        return {'name': username, 'message': '密码不能为空', 'code': 2000}

    try:
        user_data = read_all_data()  # 先读取已有的用户数据
        # 如果用户存在提示用户已注册
        if username in user_data:
            data = {'name': username, 'message': '该用户已经注册，请尝试登录', 'code': 200}
            # 返回响应数据
            return jsonify(data)

    except Exception as error:
        print(f'发生异常,原因是{error}')
        data = {'name': username, 'message': f'注册发生异常,原因是：{error}', 'code': 2000}
        return jsonify(data)

    try:
        # 尝试把注册信息，储存到csv文件。
        # 如果储存成功，则返回“注册成功”的响应
        # 如果失败，则返回“注册发生异常”
        reg_write_csv(username=username, password=password)
        # 如果成功写入，那么说明注册成功
        # 组装一个注册成功的报文
        data = {'name': username, 'message': '注册成功', 'code': 200}
        # 返回响应数据
        return jsonify(data)

    except Exception as e:
        print(f'发生异常,原因是{e}')
        data = {'name': username, 'message': f'注册发生异常,原因是：{e}', 'code': 2000}
        return jsonify(data)

    # 登录接口


@app.route('/app/login', methods=["POST"])
def app_login():
    if not request.get_data(as_text=True):
        return '请传入必要参数'
    login_data = json.loads(request.get_data(as_text=True))
    # 输入用户名密码
    username = login_data['username']
    password = login_data['password']

    # 编写具体逻辑
    if not username:

        return {'name': username, 'message': '用户名不能为空', 'code': 2000}

    elif not password:
        return {'name': username, 'message': '密码不能为空', 'code': 2000}
    # 读取库里所有数据
    user_data = read_all_data()

    # if输入的用户名在库里可以查到，就去取用户的密码，取到之后去判断输入的密码和取到的密码是否一致
    if username in user_data:
        # 就去取用户的密码
        filedata = user_data[username]

        print(filedata)
        if filedata == password:

            y_res = {'name': username, 'message': '登陆成功', 'code': 200}

            return jsonify(y_res)
        else:
            n_res = {'name': username, 'message': '用户名密码错误', 'code': 2000}
            return jsonify(n_res)
    else:
        res = {'name': username, 'message': '输入的用户名不存在，请先注册', 'code': 2000}

    return jsonify(res)


app.run(port=8080, debug=True)

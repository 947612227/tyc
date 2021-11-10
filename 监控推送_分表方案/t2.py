# -*- coding: UTF-8 -*-

"""
    @Description：
    @author：by ChenZhang
    @create：2021/7/17 11:48 下午

"""
import os

import requests


class Resume:
    def __init__(self):
        self.url = "http://npo.test.tianyancha.com/user-security/resume/upload.json"
        # self.headers = {
        #     "Content-Type": "multipart/form-data; boundary=----WebKitFormBoundaryD20W1MB8faHomsof"
        # }

        self.headers = {

            "boundary":"----WebKitFormBoundaryD20W1MB8faHomsof"
        }

    def upload_resume(self):
        proxies = {'http': 'http://localhost:8888', 'https': 'http://localhost:8888'}
        # file_d = os.path.join("/无数据/aa.csv")


        files = {
            'badgeFile': "/Users/chen/jindidata/Apitest/tools/npo/无数据/aa.csv"
        }
        file = {'badgeFile':'./单独维度.py'}

        # files1 = {'badgeFile': open('./无数据/新建.rtf', 'rb')}
        # param = {
        #     "badgeFile": files
        # }

        res = requests.post(self.url, files=file, headers=self.headers)
        print(res.text)


if __name__ == "__main__":
    rs = Resume()
    rs.upload_resume()

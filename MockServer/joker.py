# -*- coding: UTF-8 -*-

"""
    @Description：起服务命令mitmweb -s addons.py
    @author：by ChenZhang
    @create：2021/7/30 5:53 下午

"""
import json

import mitmproxy.http
from mitmproxy import ctx, http


class Joker:
    def request(self, flow: mitmproxy.http.HTTPFlow):
        if flow.request.host != "www.baidu.com" or not flow.request.path.startswith("/s"):
            return

        if "wd" not in flow.request.query.keys():
            ctx.log.warn("can not get search word from %s" % flow.request.pretty_url)
            return

        ctx.log.info("catch search word: %s" % flow.request.query.get("wd"))
        flow.request.query.set_all("wd", ["360搜索"])

    def response(self, flow):
        # 拦截指定的url
        if flow.request.url.startswith("http://cstdh5.test.s.tianyancha.cn/fd-gongshang/company/pro/baseinfo.json"):
            # 返回数据json，绝对路径
            with open('fake.json', 'rb') as f:
                res = json.load(f)
            # 设置返回数据
            flow.response.set_text(json.dumps(res))
            # log中打印
            ctx.log.info('modify words-template response')

    def http_connect(self, flow: mitmproxy.http.HTTPFlow):
        if flow.request.host == "www.google.com":
            flow.response = http.HTTPResponse.make(404)

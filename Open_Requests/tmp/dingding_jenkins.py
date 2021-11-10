# -*- coding: utf-8
import base64
import csv
import hashlib
import hmac
import time
import urllib.parse
import jenkins
import requests

# ----------------环境切换-----------------
# 线上接口监控钉钉群
# secret = 'SEC58bf275e975cd461f41ab050d90237b76942c03fa4c690712fc375102f9cd2b9'
# access_token = "2bb936f1f9c4dc3674f0b8a33d9fb26d4c7a4740217a900cb3528adc561f670b"
# 工作管家钉钉群
secret = 'SECf30d1841b7caf1ce6a7ba149f1f793c4c7d0d102c6528eba600babddef91f7fb'
access_token = "8fe5e8257671025ebe28ea90fc7994e4df5b4ba55c4a5d31e84879faba91220a"
# open钉钉群
# secret = 'SEC7e204a2f8819f553d69a5ba4791da0346155fa165ea16a27f62d862c0695fbbd'
# access_token = "2a843c0083719d5138de2ab74ff792af70242610bb8bcb8cdb394c10579bd4f5"

# 服务器环境
log = "/home/work/liumiao/tmp/log/tyc-requests/log.txt"
prometheus = "/home/work/.jenkins/workspace/API自动化测试/html_report/export/prometheusData.txt"
suites = "/home/work/.jenkins/workspace/API自动化测试/html_report/data/suites.csv"
# 本地环境
# log = "/Users/tyc/PycharmProjects/Open_Requests/log/log.txt"  # 本地log文件
# prometheus = "/Users/tyc/PycharmProjects/Open_Requests/report/html_report/export/prometheusData.txt"
# suites = "/Users/tyc/PycharmProjects/Open_Requests/report/html_report/data/suites.csv"

# ---------------明文登录--------------------
# 明文登录方式获取Jenkins最后的构建号，并拼接allure报告
# jenkins_url = "http://172.24.115.171:9000/"
# server = jenkins.Jenkins(jenkins_url, username='tianyancha', password='Tyc123456')
# job_last_number = server.get_info("job/API自动化测试")['lastBuild']['number']
# report_url = jenkins_url + "job/API自动化测试/" + str(job_last_number) + "/allure"

# ----------------Jenkins API登录--------------------
# JenkinsAPI获取最后的构建号，并拼接allure报告
jenkins_url = "http://172.24.115.171:9000/"
username = "tianyancha"
token = "11b370d0f954fe47b618a5e54a4cbc62b6"  # 从个人中心 - 设置页获取token
jenkins_login = "http://%s:%s@172.24.115.171:9000" % (username, token)
server = jenkins.Jenkins(jenkins_login)
job_last_number = server.get_info("job/API自动化测试")['lastBuild']['number']
report_url = jenkins_url + "job/API%E8%87%AA%E5%8A%A8%E5%8C%96%E6%B5%8B%E8%AF%95/" + str(job_last_number) + "/allure"

# ----------------解决中文乱码--------------------
# 中文乱码解码
# link = urllib.parse.quote(report_url, safe=":/=?#")
# link_url = urllib.parse.unquote(link)
# print(link_url)

# ----------------获取监控数据--------------------
# 打开txt文件，获取case不同状态的数量
d = {}
f = open(prometheus, "r")
for lines in f:
    launch_name = lines.strip('\n').split(' ')[0]
    num = lines.strip('\n').split(' ')[1]
    d.update({launch_name: num})
f.close()
launch_retries_run = d.get('launch_retries_run')  # 运行总数
launch_status_passed = d.get('launch_status_passed')  # 通过数量
launch_status_failed = d.get('launch_status_failed')  # 不通过数量
launch_status_broken = d.get('launch_status_broken')  # 损坏数量

# 打开csv文件，获取不同状态的接口名称
failed = ""
broken = ""
with open(suites, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for k in reader:
        if k['Status'] == 'failed':
            failed += "⚫️" + k['Name']
            failed += "\n"
        elif k['Status'] == 'broken':
            broken += "⚪️" + k['Name'] + " - 接口地址或入参错误"
            broken += "\n"

# 打开log文件，获取失败的接口名称及返回信息
content = ''
with open(log, 'r', encoding='utf-8') as f:
    for data in f.readlines():
        con = data.strip('\n').split('INFO: ')[1]
        content += "⚫️" + con
        content += "\n"

# ----------------获取钉钉信息--------------------
timestamp = str(round(time.time() * 1000))
secret = secret
secret_enc = secret.encode('utf-8')
string_to_sign = '{}\n{}'.format(timestamp, secret)
string_to_sign_enc = string_to_sign.encode('utf-8')
hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))
# print("时间戳为：%s" % timestamp)
# print("加密为：%s" % sign)

# ----------------自定义发送内容--------------------
url = "https://oapi.dingtalk.com/robot/send"
data = {
    "msgtype": "text",
    "text": {
        "content": "Api开放平台接口自动化执行完成"
                   "\n👮侦察兵巡检结果:"
                   "\n📚总计：" + launch_retries_run +
                   "\n✅成功：" + launch_status_passed +
                   "\n💥损坏：" + launch_status_broken +
                   "\n🚫损坏接口：\n" + broken +
                   "❌失败：" + launch_status_failed +
                   "\n📝失败接口：\n" + content +
                   "-------------------------------------------------------"
                   "\n🌐构建地址：\n" + jenkins_url +
                   "\n📊报告地址：\n" + report_url
    },
    "at": {
        "atMobiles": [
            ""
        ],
        "isAtAll": "false"
    }
}

# ----------------发送--------------------
r = requests.post(url=url,
                  params={
                      "access_token": access_token,
                      "timestamp": timestamp,
                      "sign": sign
                  },
                  json=data
                  )
print(r.json())

'''
钉钉构建命令：
旧构建命令：
pytest -v -s --reruns 3 --reruns-delay 5 --alluredir=/home/work/.jenkins/workspace/API自动化测试/result --clean-alluredir testcase/test_online_api.py

新构建命令：
pytest -v -s --reruns 3 --reruns-delay 5 --alluredir=/home/work/.jenkins/workspace/API自动化测试/report/allure_report --clean-alluredir testcase/test_online_api.py
allure generate /home/work/.jenkins/workspace/API自动化测试/report/allure_report/ -o /home/work/.jenkins/workspace/API自动化测试/report/html_report --clean
ding=$(grep launch_status_failed /home/work/.jenkins/workspace/API自动化测试/html_report/export/prometheusData.txt | awk '{print$2}')
if [ $ding -eq 0 ]; then #如果统计数字等于0那就打印成功
    echo 'success';
elif [ $ding -ne 0 ]; then #不等于0证明有错误，那就发钉钉
    python3 /home/work/liumiao/tmp/tyc-requests/tmp/dingding_jenkins.py; #执行发钉钉脚本
    set -e
    exit 1
fi

Jenkins API方式登录：
username = "tianyancha"
token = "11b370d0f954fe47b618a5e54a4cbc62b6"
jenkins_url = "http://%s:%s@172.24.115.171:9000" % (username, token)
server = jenkins.Jenkins(jenkins_url)
last_number = server.get_info("job/API自动化测试")['lastBuild']['number']
print(last_number)
'''

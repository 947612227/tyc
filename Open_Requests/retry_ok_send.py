import jenkins
import requests

# 服务器环境
log = "./log/log.txt"
prometheus = "./html_report/export/prometheusData.txt"
suites = "./html_report/data/suites.csv"
# 本地环境
# log = "/Users/tyc/PycharmProjects/Open_Requests/log/log.txt"  # 本地log文件
# prometheus = "/Users/tyc/PycharmProjects/Open_Requests/report/html_report/export/prometheusData.txt"
# suites = "/Users/tyc/PycharmProjects/Open_Requests/report/html_report/data/suites.csv"

# ----------------Jenkins API登录--------------------
# JenkinsAPI获取最后的构建号，并拼接allure报告
jenkins_url = "http://172.24.115.171:9000/"
username = "tianyancha"
token = "11b370d0f954fe47b618a5e54a4cbc62b6"  # 从个人中心 - 设置页获取token
jenkins_login = "http://%s:%s@172.24.115.171:9000" % (username, token)
server = jenkins.Jenkins(jenkins_login)
job_last_number = server.get_info("job/API自动化测试")['lastBuild']['number']
report_url = jenkins_url + "job/API%E8%87%AA%E5%8A%A8%E5%8C%96%E6%B5%8B%E8%AF%95/" + str(job_last_number) + "/allure"

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

# 打开log文件，获取失败的接口名称及返回信息
content = ''
with open(log, 'r', encoding='utf-8') as f:
    for data in f.readlines():
        con = data.strip('\n').split('INFO: ')[1]
        if con not in content:
            content += "⚫️" + con
            content += "\n"

# ----------------自定义发送内容--------------------
url = 'https://open.feishu.cn/open-apis/bot/v2/hook/3a8329b3-273d-4d65-8aea-1a00b65cde25'
data = "温馨提示：您的自动化脚本执行成功啦。" \
       "\n👮侦察兵巡检结果如下:" \
       "\n📚总计：" + launch_retries_run + \
       "\n✅成功：" + launch_status_passed

print(data)
r = requests.post(url=url, json={"msg_type": "text", "content": {"text": data}})
print(r.json())

import requests
import logging
from logging import handlers

"""
    脚本功能：
    case_list：给定一组测试数据
    url_list：遍历读取接口地址
    for循环：测试每个接口的不同数据。
    断言状态码等于0或者300000，不等于则判定为不合格的接口，打印相关信息。
"""


def log_output(content, level='info'):
    # 实例化记录器，设置记录日志级别为 INFO
    logger = logging.getLogger()
    logger.setLevel(level=logging.INFO)

    # 实例化格式化器
    formatter = logging.Formatter(
        '%(name)s - %(asctime)s - %(levelname)s: %(message)s'
    )

    # 实例化处理器，用于输出到控制台
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    # 实例化处理器，用于输出到文件
    file_path = "/Users/tyc/PycharmProjects/TYC-requests/tmp/api_interface/test_case/log.txt"
    file_handler = logging.FileHandler(file_path)
    file_handler.setFormatter(formatter)

    # 实例化分割器，用于分割日志文件
    time_file_handler = handlers.TimedRotatingFileHandler(
        filename=file_path,
        # when='M',
        # interval=10,
        # backupCount=50
    )
    time_file_handler.setFormatter(formatter)
    logger.addHandler(time_file_handler)

    # 需要输出的日志内容
    if level == "info":
        logger.info(content)
    elif level == "warning":
        logger.warning(content)
    elif level == "error":
        logger.error(content)
    logger.handlers.clear()


# host = 'http://10.2.16.79:20064'
host = 'http://10.39.222.35:20064'
# host = 'http://newopen.api.tianyancha.com'
case_list = [
    '北京百度网讯科技有限公司',  # 普通公司
    # '桑珠孜区仁和诊所',  # 个体工商户
    # '大润发控股有限公司',  # 香港企业
    # '吴川市塘尾街道文化服务中心',  # 事业单位
    # '北京大成律师事务所',  # 律师事务所
    # '北京市海淀区曙光地区社会组织联合会',  # 社会团体
    # '彰化商业银行股份有限公司',  # 台湾企业
    # '四川省民生慈善基金会',  # 基金会
    # '龙源电力集团股份有限公司',  # 港股
    # '龙源电力集团股份有限公司',  # 上市A股
    # '广东聚石化学股份有限公司',  # 科创受理
    # '深圳市腾讯计算机系统有限公司',  # 项目品牌
    # '百度投资并购部',  # 投资机构
    # '昆山歌斐鸿坤股权投资中心（有限合伙）',  # 投资机构-有限合伙
    # '凯银投资管理有限公司',  # 私募基金
    # '全维度测试有限责任公司',
    # '福州市鼓楼区煲一世餐饮店',
    # '沧州市地产开发服务中心',
    # '12130900402711446J',
    # '22822',
    # '122.232323',
    # 'ceshiapi',
    # '~!@#$%^&',
    # '    ',
    # '😸😜',
    # '123qwe阿萨德！@#👌',
    # '5555555555555555dddddddddddddddddd啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊'
]

url_list = []
with open('/Users/tyc/PycharmProjects/TYC-requests/tmp/api_interface/test_case/api.yaml', 'r') as f:
    path = f.readlines()
    for url in path:
        url = url.strip('\n')
        url_list.append(url)
url_count = 0
for url_path in url_list:
    url_count += 1
    case_count = 0
    for case in case_list:
        case_count += 1
        url = host + url_path + '?' + 'keyword=' + case
        try:
            res = requests.get(url=url)
            if 'error_code' in res.json():
                if res.json()['error_code'] == 0 or res.json()['error_code'] == 300000:
                    print(f'第{url_count}个接口-第{case_count}个case-通过')
                else:
                    log_output(
                        f'第{url_count}个接口-第{case_count}个case-失败: \n🔴地址：{url_path} \n🔴参数：{case} \n🔴返回内容：{res.json()}\n')
            elif 'state' in res.json():
                if res.json()['state'] == 'ok' or res.json()['message'] == '无数据':
                    print(f'第{url_count}个接口-第{case_count}个case-通过')
                else:
                    log_output(
                        f'第{url_count}个接口-第{case_count}个case-失败: \n🔴地址：{url_path} \n🔴参数：{case} \n🔴返回内容：{res.json()}\n')
            else:
                log_output(
                    f'第{url_count}个接口-第{case_count}个case-失败: \n🔴地址：{url_path} \n🔴参数：{case} \n🔴返回内容：{res.json()}\n')
        except Exception as e:
            # log_output(f'第{url_count}个接口-第{case_count}个case-失败: \n🔴地址：{url_path} \n🔴参数：{case} \n🔴返回内容：{e}\n')
            log_output(f'🔴地址：{url_path} \n 内容：{res}')

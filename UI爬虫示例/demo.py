from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

from selenium.webdriver.support.wait import WebDriverWait

'''
ancestor：先辈
attribute：当前节点的所有属性
child：所有子元素
descendant：所有子代
following：当前标签后的所有节点
namespace：当前节点的所有命名空间节点
parent：父节点
preceding：当前节点前的所有节点
preceding-sibling：所有同级节点（找哥哥）
following-sibling:所有同级节点（找弟弟）
'''


def base_find_element(dev, xpath, timeout=15, pool=0.5):  # 能够自动的轮询查找一个元素,默认15秒/每0.5秒查找一次元素
    return WebDriverWait(dev, timeout=timeout, poll_frequency=pool).until(lambda element: element.find_element_by_xpath(xpath))
# ================
chrome_options = Options()
# chrome_options.add_argument('--headless')

chrome_options.add_argument('--user-data-dir=/Users/yang/Library/Application\ Support/Google/Chrome/Default') #加载前面获取的 个人资料路径
dev = webdriver.Chrome(chrome_options=chrome_options)  #启动Chrome驱动，这里为Linux系统，Windows 和 Mac OS 根据实际路径填写
# dev.implicitly_wait(3)

gid = '22822'
url = f'http://cstd.test63.tianyancha.com/com/{gid}'


# print(url)
dev.get(url)


# key = '间接'
sleep(5)
print('死等刷新')
keys = ["法定代表人","董监高","核心团队","管理团队变更","直接股东","疑似实际控制人","受益所有人","直接","间接","控股","参股","股比未知","股东变更","股权出质","股权质押","融资事件","投资事件","分支机构","总公司","工商变更","工商年报","企业公示","清算信息","破产重组","简易注销"]
res_dic = {}


for key in keys:
    xpath = f"//*[text()='{key}']/child::*"
    # el = dev.find_element_by_xpath(xpath)
    try:
        el = dev.find_element_by_xpath(xpath)
        res = el.text
    except :
        res = '无数据'

    if res == '无数据':
        try:
            xpath = f"//*[text()='{key}']/following-sibling::*"
            el = dev.find_element_by_xpath(xpath)
            res = el.text
        except:
            res = '无数据'

    print(f'{key}:{res}')
    res_dic[key] = res


print(res_dic)


dev.quit()

# 思路:
    # 1.按照列表把所有数量获取一遍
    # 2.储存一份文件-B_R_data


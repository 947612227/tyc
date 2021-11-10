from selenium import webdriver
from selenium.webdriver.chrome.options import Options


from selenium.webdriver.chrome.options import Options
# chrome_options = Options()
# chrome_options.add_argument('--headless')
# dev = webdriver.Chrome(chrome_options=chrome_options)
#
# url = 'https://open.tianyancha.com/open/795'
# dev.get(url)
#
# # 请求示例xpath
# xpath = '//*[text()="请求示例："]/following-sibling::a'
# el = dev.find_element_by_xpath(xpath)
# demo_url = el.get_attribute('href')
#
# # 对url进行去除域名处理
#
#
# demo_url=demo_url.replace('http://open.api.tianyancha.com', '', 1)
#
# print(demo_url)
# =======================
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument('--headless')
dev = webdriver.Chrome(chrome_options=chrome_options)

for i in range(1,1400):
    try:
        # url = f'http://open.test63.tianyancha.com/open/{i}'
        url = f'http://open.tianyancha.com/open/{i}'
        dev.get(url)

        # 请求示例xpath
        xpath = '//*[text()="请求示例："]/following-sibling::a'
        el = dev.find_element_by_xpath(xpath)
        demo_url = el.get_attribute('href')

        # 批量减除域名
        demo_url = demo_url.replace('http://open.api.tianyancha.com', '', 1)

        with open('线上接口示例20210715.csv', 'a') as f:
            f.write(f'{i},{demo_url}\n')
    except BaseException:
        print(f'爬虫遇到异常:{url}')





from selenium.webdriver.chrome.options import Options
from time import sleep
from loguru import logger
import pytest
from selenium import webdriver

#监控NPO导流页面


home_url = 'https://npo.tianyancha.com/'


class Test_NPO():

    # def setup_class(self):
    #     self.dev = webdriver.Chrome()

    def teardown_method(self):
        self.dev.quit()

    def setup_method(self):
        options = Options()
        # options.binary_location = '/usr/bin/google-chrome'
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        # # 在options添加这个参数就可以了
        options.add_argument('--no-sandbox')
        #
        self.dev = webdriver.Chrome(chrome_options=options)

        
        sleep(2)

    def test_PC(self):

        self.dev.get(home_url)
        self.dev.save_screenshot('index.png')  # 捕获(截屏)保存

        xp = "//div[text()='免费申请数据']"
        self.dev.find_element_by_xpath(xp).click()
        sleep(2)

        self.dev.save_screenshot('index.png')  # 捕获(截屏)保存
        xp = "//input[@id='npoFormUser']"

        self.dev.find_element_by_xpath(xp).send_keys('test_name')
        sleep(2)

        self.dev.save_screenshot('index.png')  # 捕获(截屏)保存
        xp = "//input[@id='npoFormCorp']"
        self.dev.find_element_by_xpath(xp).send_keys('TianYanCha')
        sleep(2)

        self.dev.save_screenshot('index.png')  # 捕获(截屏)保存
        xp = "//input[@id='npoFormEmailPrefix']"
        self.dev.find_element_by_xpath(xp).send_keys('wangyangttt')
        sleep(2)
        self.dev.save_screenshot('index.png')  # 捕获(截屏)保存
        xp = "//input[@id='npoFormEmailSuffix']"
        self.dev.find_element_by_xpath(xp).send_keys('tianyancha.com')
        sleep(2)
        self.dev.save_screenshot('index.png')  # 捕获(截屏)保存
        xp = "//input[@id='npoFormEmailSuffix']"
        self.dev.find_element_by_xpath(xp).send_keys('tianyancha.com')
        sleep(2)
        self.dev.save_screenshot('index.png')  # 捕获(截屏)保存

        xp = "//input[@id='npoFormUser']"
        self.dev.find_element_by_xpath(xp).click()
        #获取验证码
        xp = "//*[@id='btnCaptcha']"
        self.dev.find_element_by_xpath(xp).click()
        sleep(2)
        self.dev.save_screenshot('index.png')  # 捕获(截屏)保存
        xp = "//input[@id='npoFormCaptcha']"
        self.dev.find_element_by_xpath(xp).click()

    # def test_Mobile(self):
    #     self.dev.get(home_url)
    #     sleep(5)
    #     xp = "//span[text()='免费申请数据']"
    #     self.dev.find_element_by_xpath(xp).click()
    #     sleep(2)
    #     xp = "//input[@id='npoFormUser']"
    #     self.dev.find_element_by_xpath(xp).send_keys('test_name')
    #     sleep(2)
    #     xp = "//input[@id='npoFormCorp']"
    #     self.dev.find_element_by_xpath(xp).send_keys('TianYanCha')
    #     sleep(2)
    #     xp = "//input[@id='npoFormEmailPrefix']"
    #     self.dev.find_element_by_xpath(xp).send_keys('wangyangttt')
    #     sleep(2)
    #     xp = "//input[@id='npoFormEmailSuffix']"
    #     self.dev.find_element_by_xpath(xp).send_keys('tianyancha.com')
    #     sleep(2)
    #     xp = "//input[@id='npoFormEmailSuffix']"
    #     self.dev.find_element_by_xpath(xp).send_keys('tianyancha.com')
    #     sleep(2)
    #     xp = "//*[@id='btnCaptcha']"
    #     self.dev.find_element_by_xpath(xp).click()
    #     sleep(2)
    #     xp = "//input[@id='npoFormCaptcha']"
    #     self.dev.find_element_by_xpath(xp).click()

if __name__ == '__main__':
    pytest.main(['-s'])
# pytest -s test_homepage.py --reruns 3 --reruns-delay 5 --alluredir raw
# cd /home/work/wangyang/标准项目监控/tests
# source activate py39
# pytest -s --alluredir raw test_homepage.py
# pytest -s --alluredir ./raw
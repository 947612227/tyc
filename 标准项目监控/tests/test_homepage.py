# 访问首页
# 访问四个分页
# 检查title
from selenium.webdriver.chrome.options import Options
from time import sleep
from loguru import logger
import pytest
from selenium import webdriver

home_url = 'https://www.std-sys.com/home'
#标准专题
xp_bzzt = '//div[text()="标准专题"]/following-sibling::*[text()="查看详情"]'
xp_bzzt_info = '//div[text()="标准专题"]/following-sibling::div/div'
xp_bzzt_info_exp = '针对用户需求， 定制行业、领域或产品相关的标准专题及明细表, 提供基于标准专题的标准文献专题服务'
bzzt_title_exp = '标准专题'
# bzzt_title_exp = '标准专u'
case_data = [[xp_bzzt,xp_bzzt_info,xp_bzzt_info_exp,bzzt_title_exp]]

#标准查询
xp_bzcx = '//div[text()="标准查询"]/following-sibling::*[text()="查看详情"]'
xp_bzcx_info = '//div[text()="标准查询"]/following-sibling::div/div'
xp_bzcx_info_exp = '全球最大标准数据库: 167个国家、 1498个组织、 6437797条标准'
bzcx_title_exp = '标准查询'
case_data.append([xp_bzcx,xp_bzcx_info,xp_bzcx_info_exp,bzcx_title_exp])

#监督检查
xp_jdjc = '//div[text()="监督检查"]/following-sibling::*[text()="查看详情"]'
xp_jdjc_info = '//div[text()="标准查询"]/following-sibling::div/div'
xp_jdjc_info_exp = '全球最大标准数据库: 167个国家、 1498个组织、 6437797条标准'
jdjc_title_exp = '企标监督检查平台 | 登录'
case_data.append([xp_jdjc,xp_jdjc_info,xp_jdjc_info_exp,jdjc_title_exp])

# 标准编写
xp_bzbx = '//div[text()="标准编写"]/following-sibling::*[text()="查看详情"]'
bzbx_url = 'https://bzbx.std-sys.com/'
xp_bzbx_info = '//div[text()="标准编写"]/following-sibling::div/div'
xp_bzbx_info_exp = '用人工智能辅助您编写企业标准,'
bzbx_title_exp = '标准化服务智慧平台'
case_data_bzbx = [[xp_bzbx, xp_bzbx_info, xp_bzbx_info_exp, bzbx_title_exp]]



class Test_A():

    # def setup_class(self):
    #     self.dev = webdriver.Chrome()

    def teardown_method(self):
        self.dev.quit()

    def setup_method(self):
        options = Options()
        options.binary_location = '/usr/bin/google-chrome'
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        # 在options添加这个参数就可以了
        options.add_argument('--no-sandbox')

        self.dev = webdriver.Chrome(chrome_options=options)

        # self.dev = webdriver.Chrome()
        self.dev.get(home_url)
        sleep(2)

        r = '智标信达 &nbsp;(北京) &nbsp;信息科技有限公司' in self.dev.page_source
        assert r

        r = '地址: &nbsp;北京市海淀区知春路6号锦秋国际大厦B座5层' in self.dev.page_source
        assert r


    @pytest.mark.parametrize('item_xp,info_xp,info_exp,title_exp', case_data,ids=['标准专题','标准查询','监督检查'])
    def test_item(self,item_xp,info_xp,info_exp,title_exp):
        # print(f'进入一轮')
        self.dev.get(home_url)
        handles = self.dev.window_handles
        self.dev.switch_to.window(handles[-1])

        text = self.dev.find_element_by_xpath(info_xp).text
        # print(text)
        assert info_exp in text

        sleep(1)
        self.dev.find_element_by_xpath(item_xp).click()
        sleep(2)

        handles = self.dev.window_handles
        self.dev.switch_to.window(handles[-1])

        assert title_exp == self.dev.title

        self.dev.close()
        sleep(2)


    @pytest.mark.parametrize('item_xp,info_xp,info_exp,title_exp', case_data_bzbx,ids=['标准编写'])
    def test_bzbx(self,item_xp,info_xp,info_exp,title_exp):
        # print(f'进入一轮')
        self.dev.get(home_url)

        text = self.dev.find_element_by_xpath(info_xp).text
        # print(text)
        assert info_exp in text

        sleep(1)
        self.dev.get(bzbx_url)
        sleep(2)

        assert title_exp == self.dev.title

        self.dev.close()
        sleep(2)


if __name__ == '__main__':
    pytest.main(['-s'])
# pytest -s test_homepage.py --reruns 3 --reruns-delay 5 --alluredir raw
# cd /home/work/wangyang/标准项目监控/tests
# source activate py39
# pytest -s --alluredir raw test_homepage.py
# pytest -s --alluredir ./raw
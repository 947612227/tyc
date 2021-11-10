from Open_Requests.page.online_api import OnlineApi
import allure
import json
import pytest

# 维护日期:   20210804
# 下次维护日期:20210904


assert_content = 0


@allure.feature('人员相关')
@allure.suite('人员相关')
@allure.sub_suite('高优接口')
class TestRenYuanXiangGuan:
    def setup_method(self):
        self.r = OnlineApi()

    @allure.title('1057人员所有历史角色')
    @allure.link('http://open.api.tianyancha.com/services/open/hi/roles?name=北京百度网讯科技有限公司&humanName=李彦宏')
    def test_id_1057(self):
        case = self.r.id_1057('1057人员所有历史角色')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=1057, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('1057人员所有历史角色 -- ' + case['reason'])

    @allure.title('449人员所有角色')
    @allure.link(
        'http://open.api.tianyancha.com/services/v4/open/roles?hid=1984012283&name=北京百度网讯科技有限公司&humanName=李彦宏&cid=22822')
    def test_id_449(self):
        case = self.r.id_449('449人员所有角色')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=449, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('449人员所有角色 -- ' + case['reason'])


@allure.feature('增值服务')
@allure.suite('增值服务')
@allure.sub_suite('12个接口')
class TestZengZhiFuWu:
    def setup_method(self):
        self.r = OnlineApi()

    @allure.title('943新闻舆情')
    @allure.link(
        'http://open.api.tianyancha.com/services/open/ps/news/2.0?'
        'name=北京百度网讯科技有限公司&pageSize=20&startTime=20191020&id=22822&endTime=20191022&pageNum=1&tags=债务抵押,经营业务')
    def test_id_943(self):
        case = self.r.id_943('943新闻舆情')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=943, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('943新闻舆情 -- ' + case['reason'])

    @allure.title('630天眼地图')
    @allure.link('http://open.api.tianyancha.com/services/v4/open/proximity?'
                 'regStatus=在业&distance=10&latitude=40.05685561073758&longtitude=116.30775539540981&pageSize=10&pageNum=1')
    def test_id_630(self):
        case = self.r.id_630('630天眼地图')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=630, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('630天眼地图 -- ' + case['reason'])

    @allure.title('632企业无水印logo')
    @allure.link('http://open.api.tianyancha.com/services/v4/open/logo?keyword=北京百度网讯科技有限公司')
    def test_id_632(self):
        case = self.r.id_632('632企业无水印logo')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=632, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('632企业无水印logo -- ' + case['reason'])

    @allure.title('755企业简介')
    @allure.link('http://open.api.tianyancha.com/services/v4/open/profile?keyword=北京百度网讯科技有限公司')
    def test_id_755(self):
        case = self.r.id_755('755企业简介')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=755, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('755企业简介 -- ' + case['reason'])


@allure.suite('搜索')
@allure.sub_suite('2个接口')
class TestSouSuo:
    def setup_method(self):
        self.r = OnlineApi()

    @allure.title('816搜索')
    @allure.link('http://open.api.tianyancha.com/services/open/search/2.0?word=北京百度网讯科技有限公司')
    def test_id_816(self):
        case = self.r.id_816('816搜索')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=816, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('816搜索 -- ' + case['reason'])

    @allure.title('353搜索')
    @allure.link('http://open.api.tianyancha.com/services/v4/open/searchV2?word=北京百度网讯科技有限公司')
    def test_id_353(self):
        case = self.r.id_353('353搜索')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=353, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('353搜索 -- ' + case['reason'])


@allure.feature('工商信息')
@allure.suite('工商信息')
@allure.sub_suite('高优接口')
class TestGongShangXinXi:
    def setup_method(self):
        self.r = OnlineApi()

    data = [
        ('id', 11684584),
        ('name', '中航重机股份有限公司'),
        ('keyword', '中航重机股份有限公司')
    ]

    @allure.title('817企业基本信息：{key}入参')
    @allure.link('http://open.api.tianyancha.com/services/open/ic/baseinfo/2.0?keyword=中航重机股份有限公司')
    @pytest.mark.parametrize('key, value', data)
    def test_id_817(self, key, value):
        case = self.r.id_817(key, value, '817企业基本信息')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            # 这里需要增加逻辑,异常情况下有可能没有traceId
            self.r.feishu_alert(api_id=817, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output(
            '817-企业基本信息：%s=%s & ' % (key, value) + case['reason'])

    @allure.title('1045工商快照')
    @allure.link('http://open.api.tianyancha.com/services/open/ic/snapshot?keyword=北京百度网讯科技有限公司')
    def test_id_1045(self):
        case = self.r.id_1045('1045工商快照')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=1045, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('1045工商快照 -- ' + case['reason'])

    @allure.title('459特殊企业基本信息')
    @allure.link('http://open.api.tianyancha.com/services/v4/open/xgbaseinfoV2?keyword=百度（香港）有限公司')
    def test_id_459(self):
        case = self.r.id_459('459特殊企业基本信息')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=459, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('459特殊企业基本信息 -- ' + case['reason'])

    @allure.title('818企业基本信息（含企业联系方式）')
    @allure.link('http://open.api.tianyancha.com/services/open/ic/baseinfoV2/2.0?keyword=中航重机股份有限公司')
    def test_id_818(self):
        case = self.r.id_818('818企业基本信息（含企业联系方式）')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=818, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('818企业基本信息（含企业联系方式） -- ' + case['reason'])

    @allure.title('819企业基本信息（含主要人员）')
    @allure.link('http://open.api.tianyancha.com/services/open/ic/baseinfoV3/2.0?keyword=中航重机股份有限公司')
    def test_id_819(self):
        case = self.r.id_819('819企业基本信息（含主要人员）')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=819, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('819企业基本信息（含主要人员） -- ' + case['reason'])

    @allure.title('820主要人员')
    @allure.link('http://open.api.tianyancha.com/services/open/ic/staff/2.0?pageSize=20&keyword=北京百度网讯科技有限公司&pageNum=1')
    def test_id_820(self):
        case = self.r.id_820('820主要人员')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=820, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('820主要人员 -- ' + case['reason'])

    @allure.title('821企业股东')
    @allure.link(
        'http://open.api.tianyancha.com/services/open/ic/holder/2.0?pageSize=20&keyword=北京百度网讯科技有限公司&pageNum=1')
    def test_id_821(self):
        case = self.r.id_821('821企业股东')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=821, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('821企业股东 -- ' + case['reason'])

    @allure.title('822变更记录')
    @allure.link(
        'http://open.api.tianyancha.com/services/open/ic/changeinfo/2.0?pageSize=20&keyword=北京百度网讯科技有限公司&pageNum=1')
    def test_id_822(self):
        case = self.r.id_822('822变更记录')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=822, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('822变更记录 -- ' + case['reason'])

    @allure.title('823对外投资')
    @allure.link(
        'http://open.api.tianyancha.com/services/open/ic/inverst/2.0?pageSize=20&keyword=北京百度网讯科技有限公司&pageNum=1')
    def test_id_823(self):
        case = self.r.id_823('823对外投资')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=823, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('823对外投资 -- ' + case['reason'])

    @allure.title('824分支机构')
    @allure.link(
        'http://open.api.tianyancha.com/services/open/ic/branch/2.0?pageSize=20&keyword=北京百度网讯科技有限公司&pageNum=1')
    def test_id_824(self):
        case = self.r.id_824('824分支机构')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=824, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('824分支机构 -- ' + case['reason'])

    @allure.title('825企业年报')
    @allure.link('http://open.api.tianyancha.com/services/open/ic/annualreport/2.0?keyword=北京百度网讯科技有限公司')
    def test_id_825(self):
        case = self.r.id_825('825企业年报')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=825, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('825企业年报 -- ' + case['reason'])

    @allure.title('364获取企业基本信息（含企业联系方式）')
    @allure.link(
        'http://open.api.tianyancha.com/services/v4/open/baseinfoV2?keyword=199557844&id=199557844&name=平安银行股份有限公司')
    def test_id_364(self):
        case = self.r.id_364('364获取企业基本信息（含企业联系方式）')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=364, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('364获取企业基本信息（含企业联系方式） -- ' + case['reason'])

    @allure.title('365获取企业基本信息（含主要人员）')
    @allure.link(
        'http://open.api.tianyancha.com/services/v4/open/baseinfoV3?keyword=199557844&id=199557844&name=平安银行股份有限公司')
    def test_id_365(self):
        case = self.r.id_365('365获取企业基本信息（含主要人员）')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=365, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('365获取企业基本信息（含主要人员） -- ' + case['reason'])

    @allure.title('735招商银行获取下拉框')
    @allure.link('http://open.api.tianyancha.com/services/v4/open/suggestByRegion?city=北京&word=百度&base=bj')
    def test_id_735(self):
        case = self.r.id_735('735招商银行获取下拉框')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=735, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('735招商银行获取下拉框 -- ' + case['reason'])


@allure.feature('企业发展')
@allure.suite('企业发展')
@allure.sub_suite('高优接口')
class TestQiYeFaZhan:
    def setup_method(self):
        self.r = OnlineApi()

    @allure.title('829投资事件')
    @allure.link(
        'http://open.api.tianyancha.com/services/open/cd/findTzanli/2.0?pageSize=20&keyword=北京百度网讯科技有限公司&pageNum=1')
    def test_id_829(self):
        case = self.r.id_829('829投资事件')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=829, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('829投资事件 -- ' + case['reason'])


@allure.feature('知识产权')
@allure.suite('知识产权')
@allure.sub_suite('高优接口')
class TestShangBiaoXinXi:
    def setup_method(self):
        self.r = OnlineApi()

    @allure.title('833作品著作权')
    @allure.link(
        'http://open.api.tianyancha.com/services/open/ipr/copyRegWorks/2.0?pageSize=20&keyword=北京百度网讯科技有限公司&pageNum=1')
    def test_id_833(self):
        case = self.r.id_833('833作品著作权')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=833, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('833作品著作权 -- ' + case['reason'])


@allure.feature('经营风险')
@allure.suite('经营风险')
@allure.sub_suite('高优接口')
class TestJingYingFengXian:
    def setup_method(self):
        self.r = OnlineApi()

    @allure.title('848经营异常')
    @allure.link(
        'http://open.api.tianyancha.com/services/open/mr/abnormal/2.0?pageSize=20&keyword=重庆罗森便利店有限公司宝桐路店&pageNum=1')
    def test_id_848(self):
        case = self.r.id_848('848经营异常')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=848, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('848经营异常 -- ' + case['reason'])


@allure.feature('经营信息')
@allure.suite('经营信息')
@allure.sub_suite('29个接口')
class TestJingYingXinXi:
    def setup_method(self):
        self.r = OnlineApi()

    @allure.title('887企业招投标信息')
    @allure.link(
        'http://open.api.tianyancha.com/services/open/m/bids/2.0?publishEndTime=2020-01-01&pageSize=20&keyword=北京百度网讯科技有限公司&pageNum=1&publishStartTime=2010-01-01')
    def test_id_887(self):
        case = self.r.id_887('887企业招投标信息')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=887, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('887企业招投标信息 -- ' + case['reason'])


# ==============================
# 以下是有缓存的接口,需要后期优化

@allure.feature('司法风险')
@allure.suite('司法风险')
@allure.sub_suite('高优+缓存')
class TestSiFaFengXian:
    def setup_method(self):
        self.r = OnlineApi()

    @allure.title('839被执行人')
    @allure.link(
        'http://open.api.tianyancha.com/services/open/jr/zhixinginfo/2.0?pageSize=20&keyword=河北展发房地产开发有限公司&pageNum=1')
    def test_id_839(self):
        case = self.r.id_839('839被执行人')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=839, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('839被执行人 -- ' + case['reason'])


@allure.feature('司法风险')
@allure.suite('司法风险')
@allure.sub_suite('高优+缓存')
class TestSiFaFengXian:
    def setup_method(self):
        self.r = OnlineApi()

    @allure.title('842法律诉讼')
    @allure.link(
        'http://open.api.tianyancha.com/services/open/jr/lawSuit/2.0?pageSize=20&keyword=北京百度网讯科技有限公司&pageNum=1')
    def test_id_842(self):
        case = self.r.id_842('842法律诉讼')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=842, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('842法律诉讼 -- ' + case['reason'])

    @allure.title('843失信人')
    @allure.link('http://open.api.tianyancha.com/services/open/jr/dishonest/2.0?keyword=恩施鑫地源农业开发有限公司&pageNum=1')
    def test_id_843(self):
        case = self.r.id_843('843失信人')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=843, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('843失信人 -- ' + case['reason'])


@allure.feature('经营风险')
@allure.suite('经营风险')
@allure.sub_suite('28个接口')
class TestJingYingFengXian:
    def setup_method(self):
        self.r = OnlineApi()

    @allure.title('846严重违法')
    @allure.link(
        'http://open.api.tianyancha.com/services/open/mr/illegalinfo/2.0?pageSize=20&keyword=四川展佳空调工程有限公司深圳分公司&pageNum=1')
    def test_id_846(self):
        case = self.r.id_846('846严重违法')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=846, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('846严重违法 -- ' + case['reason'])

if __name__ == '__main__':
    pytest.main(['s','v'])
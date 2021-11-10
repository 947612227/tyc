from Open_Requests.page.online_api import OnlineApi
import allure
import json
import pytest

assert_content = 0


@allure.feature('工商信息')
@allure.suite('工商信息')
@allure.sub_suite('21个接口')
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
            #这里需要增加逻辑,异常情况下有可能没有traceId
            self.r.feishu_alert(api_id=817, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output(
            '817-企业基本信息：%s=%s & ' % (key, value) + case['reason'])

    @allure.title('1120司法拍卖')
    @allure.link(
        'http://open.api.tianyancha.com/services/open/mr/judicialSale/3.0?pageSize=20&keyword=重庆联付通网络结算科技有限责任公司&pageNum=1')
    def test_id_1120(self):
        case = self.r.id_1120('1120司法拍卖')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=1120, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('1120司法拍卖 -- ' + case['reason'])

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

    @allure.title('459特殊企业基本信息')
    @allure.link('http://open.api.tianyancha.com/services/v4/open/xgbaseinfoV2?keyword=百度（香港）有限公司')
    def test_id_459(self):
        case = self.r.id_459('459特殊企业基本信息')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=459, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('459特殊企业基本信息 -- ' + case['reason'])

    @allure.title('1042企业三要素验证')
    @allure.link(
        'http://open.api.tianyancha.com/services/open/ic/verify?code=91110000802100433B&name=北京百度网讯科技有限公司&legalPersonName=梁志祥')
    def test_id_1042(self):
        case = self.r.id_1042('1042企业三要素验证')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=1042, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('1042企业三要素验证 -- ' + case['reason'])

    @allure.title('1045工商快照')
    @allure.link('http://open.api.tianyancha.com/services/open/ic/snapshot?keyword=北京百度网讯科技有限公司')
    def test_id_1045(self):
        case = self.r.id_1045('1045工商快照')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=1045, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('1045工商快照 -- ' + case['reason'])

    @allure.title('1047企业类型')
    @allure.link('http://open.api.tianyancha.com/services/open/ic/companyType?keyword=北京百度网讯科技有限公司')
    def test_id_1047(self):
        case = self.r.id_1047('1047企业类型')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=1047, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('1047企业类型 -- ' + case['reason'])

    @allure.title('1046企业联系方式')
    @allure.link('http://open.api.tianyancha.com/services/open/ic/contact?keyword=北京百度网讯科技有限公司')
    def test_id_1046(self):
        case = self.r.id_1046('1046企业联系方式')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=1046, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('1046企业联系方式 -- ' + case['reason'])

    @allure.title('820主要人员')
    @allure.link('http://open.api.tianyancha.com/services/open/ic/staff/2.0?pageSize=20&keyword=北京百度网讯科技有限公司&pageNum=1')
    def test_id_820(self):
        case = self.r.id_820('820主要人员')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=820, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('820主要人员 -- ' + case['reason'])

    @allure.title('1050历史主要人员')
    @allure.link('http://open.api.tianyancha.com/services/open/hi/members?keyword=北京百度网讯科技有限公司')
    def test_id_1050(self):
        case = self.r.id_1050('1050历史主要人员')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=1050, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('1050历史主要人员 -- ' + case['reason'])

    @allure.title('821企业股东')
    @allure.link(
        'http://open.api.tianyancha.com/services/open/ic/holder/2.0?pageSize=20&keyword=北京百度网讯科技有限公司&pageNum=1')
    def test_id_821(self):
        case = self.r.id_821('821企业股东')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=821, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('821企业股东 -- ' + case['reason'])

    @allure.title('877历史股东信息')
    @allure.link(
        'http://open.api.tianyancha.com/services/open/hi/holder/2.0?pageSize=20&keyword=北京百度网讯科技有限公司&pageNum=1')
    def test_id_877(self):
        case = self.r.id_877('877历史股东信息')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=877, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('877历史股东信息 -- ' + case['reason'])

    @allure.title('997公司公示股东出资')
    @allure.link(
        'http://open.api.tianyancha.com/services/open/ic/holderList/2.0?pageSize=20&keyword=北京金堤科技有限公司&pageNum=1')
    def test_id_997(self):
        case = self.r.id_997('997公司公示股东出资')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=997, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('997公司公示股东出资 -- ' + case['reason'])

    @allure.title('998公司公示股权变更')
    @allure.link(
        'http://open.api.tianyancha.com/services/open/ic/holderChange/2.0?pageSize=20&keyword=北京金堤科技有限公司&pageNum=1')
    def test_id_998(self):
        case = self.r.id_998('998公司公示股权变更')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=998, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('998公司公示股权变更 -- ' + case['reason'])

    @allure.title('823对外投资')
    @allure.link(
        'http://open.api.tianyancha.com/services/open/ic/inverst/2.0?pageSize=20&keyword=北京百度网讯科技有限公司&pageNum=1')
    def test_id_823(self):
        case = self.r.id_823('823对外投资')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=823, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('823对外投资 -- ' + case['reason'])

    @allure.title('876历史对外投资')
    @allure.link(
        'http://open.api.tianyancha.com/services/open/hi/invest/2.0?pageSize=20&keyword=北京百度网讯科技有限公司&pageNum=1')
    def test_id_876(self):
        case = self.r.id_876('876历史对外投资')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=876, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('876历史对外投资 -- ' + case['reason'])

    @allure.title('824分支机构')
    @allure.link(
        'http://open.api.tianyancha.com/services/open/ic/branch/2.0?pageSize=20&keyword=北京百度网讯科技有限公司&pageNum=1')
    def test_id_824(self):
        case = self.r.id_824('824分支机构')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=824, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('824分支机构 -- ' + case['reason'])

    @allure.title('963总公司')
    @allure.link('http://open.api.tianyancha.com/services/open/ic/parentCompany/2.0?keyword=北京百度网讯科技有限公司南京分公司')
    def test_id_963(self):
        case = self.r.id_963('963总公司')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=963, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('963总公司 -- ' + case['reason'])

    @allure.title('825企业年报')
    @allure.link('http://open.api.tianyancha.com/services/open/ic/annualreport/2.0?keyword=北京百度网讯科技有限公司')
    def test_id_825(self):
        case = self.r.id_825('825企业年报')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=825, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('825企业年报 -- ' + case['reason'])

    @allure.title('822变更记录')
    @allure.link(
        'http://open.api.tianyancha.com/services/open/ic/changeinfo/2.0?pageSize=20&keyword=北京百度网讯科技有限公司&pageNum=1')
    def test_id_822(self):
        case = self.r.id_822('822变更记录')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=822, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('822变更记录 -- ' + case['reason'])

    @allure.title('878历史工商信息')
    @allure.link('http://open.api.tianyancha.com/services/open/hi/ic/2.0?keyword=北京百度网讯科技有限公司')
    def test_id_878(self):
        case = self.r.id_878('878历史工商信息')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=878, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('878历史工商信息 -- ' + case['reason'])


@allure.feature('司法风险')
@allure.suite('司法风险')
@allure.sub_suite('22个接口')
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

    @allure.title('1073法律诉讼详情')
    @allure.link('http://open.api.tianyancha.com/services/open/jr/lawSuit/detail?uuid=929dd3cc1cb511e6b554008cfae40dc0')
    def test_id_1073(self):
        case = self.r.id_1073('1073法律诉讼详情')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=1073, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('1073法律诉讼详情 -' + case['reason'])

    @allure.title('874历史法律诉讼')
    @allure.link(
        'http://open.api.tianyancha.com/services/open/hi/lawsuit/2.0?pageSize=20&keyword=北京百度网讯科技有限公司&pageNum=1')
    def test_id_874(self):
        case = self.r.id_874('874历史法律诉讼')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=874, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('874历史法律诉讼 -- ' + case['reason'])

    @allure.title('840开庭公告')
    @allure.link(
        'http://open.api.tianyancha.com/services/open/jr/ktannouncement/2.0?pageSize=10&keyword=北京百度网讯科技有限公司&pageNum=1')
    def test_id_840(self):
        case = self.r.id_840('840开庭公告')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=840, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('840开庭公告 -- ' + case['reason'])

    @allure.title('875历史开庭公告')
    @allure.link(
        'http://open.api.tianyancha.com/services/open/hi/announcement/2.0?pageSize=20&keyword=北京百度网讯科技有限公司&pageNum=1')
    def test_id_875(self):
        case = self.r.id_875('875历史开庭公告')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=875, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('875历史开庭公告 -- ' + case['reason'])

    @allure.title('841法院公告')
    @allure.link(
        'http://open.api.tianyancha.com/services/open/jr/courtAnnouncement/2.0?pageSize=20&keyword=北京百度网讯科技有限公司&pageNum=1')
    def test_id_841(self):
        case = self.r.id_841('841法院公告')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=841, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('841法院公告 -- ' + case['reason'])

    @allure.title('873历史法院公告')
    @allure.link('http://open.api.tianyancha.com/services/open/hi/court/2.0?pageSize=20&keyword=北京百度网讯科技有限公司&pageNum=1')
    def test_id_873(self):
        case = self.r.id_873('873历史法院公告')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=873, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('873历史法院公告 -- ' + case['reason'])

    @allure.title('962送达公告')
    @allure.link(
        'http://open.api.tianyancha.com/services/open/jr/sendAnnouncement/2.0?pageSize=20&keyword=深圳市诚信祥融资担保有限公司&pageNum=1')
    def test_id_962(self):
        case = self.r.id_962('962送达公告')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=962, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('962送达公告 -- ' + case['reason'])

    @allure.title('961立案信息')
    @allure.link(
        'http://open.api.tianyancha.com/services/open/jr/courtRegister/2.0?pageSize=20&keyword=南京银城物业服务有限公司&pageNum=1')
    def test_id_961(self):
        case = self.r.id_961('961立案信息')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=961, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('961立案信息 -- ' + case['reason'])

    @allure.title('756司法协助')
    @allure.link('http://open.api.tianyancha.com/services/v4/open/judicial?pageSize=20&keyword=978740860&pageNum=1')
    def test_id_756(self):
        case = self.r.id_756('756司法协助')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=756, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('756司法协助 -- ' + case['reason'])

    @allure.title('757司法协助详情')
    @allure.link('http://open.api.tianyancha.com/services/v4/open/getJudicialDetail?assistanceId=281114985578')
    def test_id_757(self):
        case = self.r.id_757('757司法协助详情')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=757, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('757司法协助详情 -- ' + case['reason'])

    @allure.title('1015历史司法协助')
    @allure.link(
        'http://open.api.tianyancha.com/services/open/hi/judicial/2.0?pageSize=20&keyword=南昌亨得利股份有限公司&pageNum=1')
    def test_id_1015(self):
        case = self.r.id_1015('1015历史司法协助')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=1015, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('1015历史司法协助 -- ' + case['reason'])

    @allure.title('1016历史司法协助详情')
    @allure.link(
        'http://open.api.tianyancha.com/services/open/hi/judicial/detail/2.0?businessId=4e4m4cv7fb12c6dff13033138l2544c8')
    def test_id_1016(self):
        case = self.r.id_1016('1016历史司法协助详情')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=1016, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('1016历史司法协助详情 -- ' + case['reason'])

    @allure.title('1036破产重整')
    @allure.link(
        'http://open.api.tianyancha.com/services/open/jr/bankruptcy/2.0?pageSize=20&keyword=长沙新世界国际大饭店有限公司&pageNum=1')
    def test_id_1036(self):
        case = self.r.id_1036('1036破产重整')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=1036, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('1036破产重整 -- ' + case['reason'])

    @allure.title('1037破产重整详情')
    @allure.link(
        'http://open.api.tianyancha.com/services/open/jr/bankruptcy/detail/2.0?gid=365223910&uuid=4905eef8fc704bcfbb82b6f0294d6fc5')
    def test_id_1037(self):
        case = self.r.id_1037('1037破产重整详情')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=1037, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('1037破产重整详情 -- ' + case['reason'])

    @allure.title('839被执行人')
    @allure.link(
        'http://open.api.tianyancha.com/services/open/jr/zhixinginfo/2.0?pageSize=20&keyword=河北展发房地产开发有限公司&pageNum=1')
    def test_id_839(self):
        case = self.r.id_839('839被执行人')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=839, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('839被执行人 -- ' + case['reason'])

    @allure.title('871历史被执行人')
    @allure.link(
        'http://open.api.tianyancha.com/services/open/hi/zhixing/2.0?pageSize=20&keyword=北京百度网讯科技有限公司&pageNum=1')
    def test_id_871(self):
        case = self.r.id_871('871历史被执行人')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=871, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('871历史被执行人 -- ' + case['reason'])

    @allure.title('843失信人')
    @allure.link('http://open.api.tianyancha.com/services/open/jr/dishonest/2.0?keyword=恩施鑫地源农业开发有限公司&pageNum=1')
    def test_id_843(self):
        case = self.r.id_843('843失信人')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=843, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('843失信人 -- ' + case['reason'])

    @allure.title('872历史失信人')
    @allure.link(
        'http://open.api.tianyancha.com/services/open/hi/dishonest/2.0?pageSize=20&keyword=天津市红宝石商务宾馆有限公司&pageNum=1')
    def test_id_872(self):
        case = self.r.id_872('872历史失信人')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=872, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('872历史失信人 -- ' + case['reason'])

    @allure.title('1014限制消费令')
    @allure.link(
        'http://open.api.tianyancha.com/services/open/jr/consumptionRestriction/2.0?pageSize=20&keyword=乐视控股（北京）有限公司&pageNum=1')
    def test_id_1014(self):
        case = self.r.id_1014('1014限制消费令')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=1014, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('1014限制消费令 -- ' + case['reason'])

    @allure.title('1013终本案件')
    @allure.link(
        'http://open.api.tianyancha.com/services/open/jr/endCase/2.0?pageSize=20&keyword=成都市武侯区桂溪房地产开发公司&pageNum=1')
    def test_id_1013(self):
        case = self.r.id_1013('1013终本案件')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=1013, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('1013终本案件 -- ' + case['reason'])

    @allure.title('1041司法解析')
    @allure.link(
        'http://open.api.tianyancha.com/services/open/jr/judicialCase/2.0?pageSize=10&keyword=北京百度网讯科技有限公司&pageNum=1')
    def test_id_1041(self):
        case = self.r.id_1041('1041司法解析')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=1041, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('1041司法解析 -- ' + case['reason'])


@allure.feature('经营信息')
@allure.suite('经营信息')
@allure.sub_suite('29个接口')
class TestJingYingXinXi:
    def setup_method(self):
        self.r = OnlineApi()

    @allure.title('888行政许可-工商局')
    @allure.link(
        'http://open.api.tianyancha.com/services/open/m/getLicense/2.0?pageSize=20&keyword=深圳市中亚医药有限公司&pageNum=1')
    def test_id_888(self):
        case = self.r.id_888('888行政许可-工商局')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=888, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('888行政许可-工商局 -- ' + case['reason'])

    @allure.title('867历史行政许可-工商局')
    @allure.link(
        'http://open.api.tianyancha.com/services/open/hi/license/2.0?pageSize=20&keyword=锦州市中远旅行社有限责任公司&pageNum=1')
    def test_id_867(self):
        case = self.r.id_867('867历史行政许可-工商局')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=867, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('867历史行政许可-工商局 -- ' + case['reason'])

    @allure.title('889行政许可-其他来源')
    @allure.link(
        'http://open.api.tianyancha.com/services/open/m/getLicenseCreditchina/2.0?pageSize=20&keyword=上海绪斌贸易有限公司&pageNum=1')
    def test_id_889(self):
        case = self.r.id_889('889行政许可-其他来源')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=889, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('889行政许可-其他来源 -- ' + case['reason'])

    @allure.title('869历史行政许可-其他来源')
    @allure.link(
        'http://open.api.tianyancha.com/services/open/hi/license/creditChina/2.0?pageSize=20&keyword=北京百度网讯科技有限公司&pageNum=1')
    def test_id_869(self):
        case = self.r.id_869('869历史行政许可-其他来源')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=869, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('869历史行政许可-其他来源 -- ' + case['reason'])

    @allure.title('883抽查检查')
    @allure.link(
        'http://open.api.tianyancha.com/services/open/m/checkInfo/2.0?pageSize=20&keyword=北京百度网讯科技有限公司&pageNum=1')
    def test_id_883(self):
        case = self.r.id_883('883抽查检查')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=883, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('883抽查检查 -- ' + case['reason'])

    @allure.title('1024双随机抽查')
    @allure.link(
        'http://open.api.tianyancha.com/services/open/m/doubleRandomCheck/2.0?pageSize=20&keyword=武汉世纪楚泽商贸有限公司&pageNum=1')
    def test_id_1024(self):
        case = self.r.id_1024('1024双随机抽查')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=1024, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('1024双随机抽查 -- ' + case['reason'])

    @allure.title('1025双随机抽查详情')
    @allure.link(
        'http://open.api.tianyancha.com/services/open/m/doubleRandomCheckDetail/2.0?businessId=4me4c1m72f122bd2d7f23e1eal2f46f7&pageSize=20&pageNum=1')
    def test_id_1025(self):
        case = self.r.id_1025('1025双随机抽查详情')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=1025, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('1025双随机抽查详情 -- ' + case['reason'])

    @allure.title('884税务评级')
    @allure.link(
        'http://open.api.tianyancha.com/services/open/m/taxCredit/2.0?pageSize=20&keyword=北京百度网讯科技有限公司&pageNum=1')
    def test_id_884(self):
        case = self.r.id_884('884税务评级')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=884, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('884税务评级 -- ' + case['reason'])

    @allure.title('881进出口信用')
    @allure.link('http://open.api.tianyancha.com/services/open/m/importAndExport/2.0?keyword=珠海市优隆贸易有限公司')
    def test_id_881(self):
        case = self.r.id_881('881进出口信用')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=881, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('881进出口信用 -- ' + case['reason'])

    @allure.title('948电信许可')
    @allure.link(
        'http://open.api.tianyancha.com/services/open/m/teleCommunicationLicense/2.0?pageSize=20&keyword=北京百度网讯科技有限公司&pageNum=1')
    def test_id_948(self):
        case = self.r.id_948('948电信许可')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=948, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('948电信许可 -- ' + case['reason'])

    @allure.title('880资质证书')
    @allure.link(
        'http://open.api.tianyancha.com/services/open/m/certificate/2.0?name=北京百度网讯科技有限公司&certificateName=中国质量认证中心_CCC证书&pageSize=20&id=22822&pageNum=1')
    def test_id_880(self):
        case = self.r.id_880('880资质证书')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=880, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('880资质证书 -- ' + case['reason'])

    @allure.title('1029公告研报')
    @allure.link(
        'http://open.api.tianyancha.com/services/open/m/announcementReport/2.0?pageSize=20&keyword=平安银行股份有限公司&pageNum=1')
    def test_id_1029(self):
        case = self.r.id_1029('1029公告研报')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=1029, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('1029公告研报 -- ' + case['reason'])

    @allure.title('1049企业信用评级')
    @allure.link(
        'http://open.api.tianyancha.com/services/open/m/creditRating/2.0?pageSize=20&keyword=光大证券股份有限公司&pageNum=1')
    def test_id_1049(self):
        case = self.r.id_1049('1049企业信用评级')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=1049, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('1049企业信用评级 -- ' + case['reason'])

    @allure.title('1048一般纳税人')
    @allure.link(
        'http://open.api.tianyancha.com/services/open/m/taxpayer/2.0?pageSize=20&keyword=北京一点网聚科技有限公司&pageNum=1')
    def test_id_1048(self):
        case = self.r.id_1048('1048一般纳税人')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=1048, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('1048一般纳税人 -- ' + case['reason'])

    @allure.title('886债券信息')
    @allure.link('http://open.api.tianyancha.com/services/open/m/bond/2.0?pageSize=20&keyword=嘉兴银行股份有限公司&pageNum=1')
    def test_id_886(self):
        case = self.r.id_886('886债券信息')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=886, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('886债券信息 -- ' + case['reason'])

    @allure.title('882产品信息')
    @allure.link(
        'http://open.api.tianyancha.com/services/open/m/appbkInfo/2.0?pageSize=20&keyword=北京百度网讯科技有限公司&pageNum=1')
    def test_id_882(self):
        case = self.r.id_882('882产品信息')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=882, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('882产品信息 -- ' + case['reason'])

    @allure.title('885购地信息')
    @allure.link(
        'http://open.api.tianyancha.com/services/open/m/purchaseLand/2.0?pageSize=20&keyword=金地（集团）股份有限公司&pageNum=1')
    def test_id_885(self):
        case = self.r.id_885('885购地信息')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=885, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('885购地信息 -- ' + case['reason'])

    @allure.title('946供应商')
    @allure.link(
        'http://open.api.tianyancha.com/services/open/m/supply/2.0?year=2018&pageSize=20&keyword=北京百度网讯科技有限公司&pageNum=1')
    def test_id_946(self):
        case = self.r.id_946('946供应商')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=946, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('946供应商 -- ' + case['reason'])

    @allure.title('947客户')
    @allure.link(
        'http://open.api.tianyancha.com/services/open/m/customer/2.0?year=2018&pageSize=20&keyword=北京百度网讯科技有限公司&pageNum=1')
    def test_id_947(self):
        case = self.r.id_947('947客户')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=947, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('947客户 -- ' + case['reason'])

    @allure.title('879企业招聘')
    @allure.link(
        'http://open.api.tianyancha.com/services/open/m/employments/2.0?pageSize=20&keyword=北京百度网讯科技有限公司&pageNum=1')
    def test_id_879(self):
        case = self.r.id_879('879企业招聘')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=879, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('879企业招聘 -- ' + case['reason'])

    @allure.title('953企业招聘-百聘')
    @allure.link(
        'http://open.api.tianyancha.com/services/open/m/bp/employments/2.0?pageSize=20&keyword=北京百度网讯科技有限公司&pageNum=1')
    def test_id_953(self):
        case = self.r.id_953('953企业招聘-百聘')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=953, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('953企业招聘-百聘 -- ' + case['reason'])

    @allure.title('1026企业微博')
    @allure.link('http://open.api.tianyancha.com/services/open/m/weibo/2.0?pageSize=20&keyword=北京百度网讯科技有限公司&pageNum=1')
    def test_id_1026(self):
        case = self.r.id_1026('1026企业微博')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=1026, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('1026企业微博 -- ' + case['reason'])

    @allure.title('834企业微信公众号')
    @allure.link('http://open.api.tianyancha.com/services/open/ipr/publicWeChat/2.0?keyword=北京百度网讯科技有限公司&pageNum=1')
    def test_id_834(self):
        case = self.r.id_834('834企业微信公众号')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=834, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('834企业微信公众号 -- ' + case['reason'])

    @allure.title('887企业招投标信息')
    @allure.link(
        'http://open.api.tianyancha.com/services/open/m/bids/2.0?publishEndTime=2020-01-01&pageSize=20&keyword=北京百度网讯科技有限公司&pageNum=1&publishStartTime=2010-01-01')
    def test_id_887(self):
        case = self.r.id_887('887企业招投标信息')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=887, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('887企业招投标信息 -- ' + case['reason'])

    @allure.title('1063招投标信息垂搜')
    @allure.link(
        'http://open.api.tianyancha.com/services/open/m/bids/search?publishEndTime=2020-01-01&searchType=1,2&pageSize=2&keyword=百度&publishStartTime=2010-01-01&pageNum=1')
    def test_id_1063(self):
        case = self.r.id_1063('1063招投标信息垂搜')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=1063, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('1063招投标信息垂搜 -- ' + case['reason'])

    @allure.title('949地块公示')
    @allure.link(
        'http://open.api.tianyancha.com/services/open/m/landPublicity/2.0?pageSize=20&keyword=天津大丰兴业科技有限公司&pageNum=1')
    def test_id_949(self):
        case = self.r.id_949('949地块公示')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=949, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('949地块公示 -- ' + case['reason'])

    @allure.title('950地块公示详情')
    @allure.link('http://open.api.tianyancha.com/services/open/m/landPublicity/detail/2.0?id=74')
    def test_id_950(self):
        case = self.r.id_950('950地块公示详情')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=950, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('950地块公示详情 -- ' + case['reason'])

    @allure.title('951土地转让')
    @allure.link(
        'http://open.api.tianyancha.com/services/open/m/landTransfer/2.0?pageSize=20&keyword=邵阳市东风房地产开发有限责任公司&pageNum=1')
    def test_id_951(self):
        case = self.r.id_951('951土地转让')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=951, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('951土地转让 -- ' + case['reason'])

    @allure.title('952土地转让详情')
    @allure.link('http://open.api.tianyancha.com/services/open/m/landTransfer/detail/2.0?id=179495')
    def test_id_952(self):
        case = self.r.id_952('952土地转让详情')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=952, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('952土地转让详情 -- ' + case['reason'])


@allure.feature('经营风险')
@allure.suite('经营风险')
@allure.sub_suite('28个接口')
class TestJingYingFengXian:
    def setup_method(self):
        self.r = OnlineApi()

    @allure.title('847行政处罚-工商局')
    @allure.link(
        'http://open.api.tianyancha.com/services/open/mr/punishmentInfo/2.0?pageSize=20&keyword=北京百度网讯科技有限公司&pageNum=1')
    def test_id_847(self):
        case = self.r.id_847('847行政处罚-工商局')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=847, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('847行政处罚-工商局 -- ' + case['reason'])

    @allure.title('870历史行政处罚-工商局')
    @allure.link(
        'http://open.api.tianyancha.com/services/open/hi/punishment/2.0?pageSize=20&keyword=北京百度网讯科技有限公司&pageNum=1')
    def test_id_870(self):
        case = self.r.id_870('870历史行政处罚-工商局')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=870, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('870历史行政处罚-工商局 -- ' + case['reason'])

    @allure.title('852行政处罚-其他来源')
    @allure.link(
        'http://open.api.tianyancha.com/services/open/mr/creditChina/2.0?pageSize=20&keyword=江苏省连云港汽车运输有限公司&pageNum=1')
    def test_id_852(self):
        case = self.r.id_852('852行政处罚-其他来源')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=852, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('852行政处罚-其他来源 -- ' + case['reason'])

    @allure.title('865历史行政处罚-其他来源')
    @allure.link(
        'http://open.api.tianyancha.com/services/open/hi/punishment/creditChina/2.0?pageSize=20&keyword=北京百度网讯科技有限公司&pageNum=1')
    def test_id_865(self):
        case = self.r.id_865('865历史行政处罚-其他来源')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=865, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('865历史行政处罚-其他来源 -- ' + case['reason'])

    @allure.title('851欠税公告')
    @allure.link('http://open.api.tianyancha.com/services/open/mr/ownTax/2.0?pageSize=20&keyword=青浦白鹤建新石材经营部&pageNum=1')
    def test_id_851(self):
        case = self.r.id_851('851欠税公告')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=851, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('851欠税公告 -- ' + case['reason'])

    @allure.title('957税收违法')
    @allure.link(
        'http://open.api.tianyancha.com/services/open/mr/taxContravention/2.0?pageSize=20&keyword=宁波保税区航晨塑化有限公司&pageNum=1')
    def test_id_957(self):
        case = self.r.id_957('957税收违法')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=957, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('957税收违法 -- ' + case['reason'])

    @allure.title('958税收违法详情')
    @allure.link('http://open.api.tianyancha.com/services/open/mr/taxContravention/detail/2.0?id=13')
    def test_id_958(self):
        case = self.r.id_958('958税收违法详情')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=958, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('958税收违法详情 -- ' + case['reason'])

    @allure.title('848经营异常')
    @allure.link(
        'http://open.api.tianyancha.com/services/open/mr/abnormal/2.0?pageSize=20&keyword=重庆罗森便利店有限公司宝桐路店&pageNum=1')
    def test_id_848(self):
        case = self.r.id_848('848经营异常')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=848, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('848经营异常 -- ' + case['reason'])

    @allure.title('996历史经营异常')
    @allure.link(
        'http://open.api.tianyancha.com/services/open/hi/abnormal/2.0?pageSize=20&keyword=湖南瑞源生物医药科技有限公司&pageNum=1')
    def test_id_996(self):
        case = self.r.id_996('996历史经营异常')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=996, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('996历史经营异常 -- ' + case['reason'])

    @allure.title('846严重违法')
    @allure.link(
        'http://open.api.tianyancha.com/services/open/mr/illegalinfo/2.0?pageSize=20&keyword=四川展佳空调工程有限公司深圳分公司&pageNum=1')
    def test_id_846(self):
        case = self.r.id_846('846严重违法')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=846, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('846严重违法 -- ' + case['reason'])

    @allure.title('849清算信息')
    @allure.link('http://open.api.tianyancha.com/services/open/mr/liquidating/2.0?keyword=上海臣堃电子商务有限公司')
    def test_id_849(self):
        case = self.r.id_849('849清算信息')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=849, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('849清算信息 -- ' + case['reason'])

    @allure.title('960简易注销')
    @allure.link('http://open.api.tianyancha.com/services/open/mr/briefCancel/2.0?keyword=上海著远网络信息技术有限公司')
    def test_id_960(self):
        case = self.r.id_960('960简易注销')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=960, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('960简易注销 -- ' + case['reason'])

    @allure.title('1023询价评估')
    @allure.link(
        'http://open.api.tianyancha.com/services/open/mr/inquiryEvaluation/2.0?pageSize=20&keyword=武汉金湖科技有限公司&pageNum=1')
    def test_id_1023(self):
        case = self.r.id_1023('1023询价评估')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=1023, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('1023询价评估 -- ' + case['reason'])

    @allure.title('850司法拍卖')
    @allure.link(
        'http://open.api.tianyancha.com/services/open/mr/judicialSale/2.0?pageSize=10&keyword=常州市武进区银通农村小额贷款股份有限公司&pageNum=1')
    def test_id_850(self):
        case = self.r.id_850('850司法拍卖')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=850, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('850司法拍卖 -- ' + case['reason'])

    @allure.title('796公示催告')
    @allure.link(
        'http://open.api.tianyancha.com/services/v4/open/publicNotice?pageSize=1&keyword=广州立达尔生物科技股份有限公司&pageNum=1')
    def test_id_796(self):
        case = self.r.id_796('796公示催告')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=796, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('796公示催告 -- ' + case['reason'])

    @allure.title('844动产抵押')
    @allure.link(
        'http://open.api.tianyancha.com/services/open/mr/mortgageInfo/2.0?pageSize=20&keyword=讷河市丰盛现代农业农机专业合作社&pageNum=1')
    def test_id_844(self):
        case = self.r.id_844('844动产抵押')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=844, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('844动产抵押 -- ' + case['reason'])

    @allure.title('866历史动产抵押')
    @allure.link(
        'http://open.api.tianyancha.com/services/open/hi/mortgageInfo/2.0?pageSize=20&keyword=嫩江县朝阳种植专业合作社&pageNum=1')
    def test_id_866(self):
        case = self.r.id_866('866历史动产抵押')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=866, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('866历史动产抵押 -- ' + case['reason'])

    @allure.title('955土地抵押')
    @allure.link(
        'http://open.api.tianyancha.com/services/open/mr/landMortgage/2.0?pageSize=20&keyword=邵阳市东风房地产开发有限责任公司&pageNum=1')
    def test_id_955(self):
        case = self.r.id_955('955土地抵押')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=955, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('955土地抵押 -- ' + case['reason'])

    @allure.title('956土地抵押详情')
    @allure.link('http://open.api.tianyancha.com/services/open/mr/landMortgage/detail/2.0?id=57277')
    def test_id_956(self):
        case = self.r.id_956('956土地抵押详情')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=956, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('956土地抵押详情 -- ' + case['reason'])

    @allure.title('795知识产权出质')
    @allure.link(
        'http://open.api.tianyancha.com/services/v4/open/getPledgeReg?pageSize=1&keyword=广州立达尔生物科技股份有限公司&pageNum=1')
    def test_id_795(self):
        case = self.r.id_795('795知识产权出质')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=795, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('795知识产权出质 -- ' + case['reason'])

    @allure.title('845股权出质')
    @allure.link(
        'http://open.api.tianyancha.com/services/open/mr/equityInfo/2.0?pageSize=20&keyword=内蒙古大草原生态产业投资有限公司&pageNum=1')
    def test_id_845(self):
        case = self.r.id_845('845股权出质')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=845, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('845股权出质 -- ' + case['reason'])

    @allure.title('868历史股权出质')
    @allure.link(
        'http://open.api.tianyancha.com/services/open/hi/equityInfo/2.0?pageSize=20&keyword=北京百度网讯科技有限公司&pageNum=1')
    def test_id_868(self):
        case = self.r.id_868('868历史股权出质')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=868, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('868历史股权出质 -- ' + case['reason'])

    @allure.title('1021质押明细')
    @allure.link(
        'http://open.api.tianyancha.com/services/open/mr/stockPledge/detailList/2.0?pageSize=20&keyword=厦门安妮股份有限公司&pageNum=1')
    def test_id_1021(self):
        case = self.r.id_1021('1021质押明细')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=1021, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('1021质押明细 -- ' + case['reason'])

    @allure.title('1022质押明细详情')
    @allure.link(
        'http://open.api.tianyancha.com/services/open/mr/stockPledge/detail/2.0?businessId=49o1ecbae1bb82282dbe7a1aflbf1f36&id=7996092')
    def test_id_1022(self):
        case = self.r.id_1022('1022质押明细详情')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=1022, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('1022质押明细详情 -- ' + case['reason'])

    @allure.title('1019重要股东质押')
    @allure.link(
        'http://open.api.tianyancha.com/services/open/mr/stockPledge/shareholder/2.0?pageSize=20&keyword=通源石油科技集团股份有限公司&pageNum=1')
    def test_id_1019(self):
        case = self.r.id_1019('1019重要股东质押')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=1019, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('1019重要股东质押 -- ' + case['reason'])

    @allure.title('1020重要股东质押详情')
    @allure.link(
        'http://open.api.tianyancha.com/services/open/mr/stockPledge/shareholder/detail/2.0?businessId=1o118ef2424dfb670e699b1b0l671c24&id=7996092')
    def test_id_1020(self):
        case = self.r.id_1020('1020重要股东质押详情')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=1020, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('1020重要股东质押详情 -- ' + case['reason'])

    @allure.title('1018质押比例')
    @allure.link(
        'http://open.api.tianyancha.com/services/open/mr/stockPledge/ratio/2.0?date=2019-07-26&keyword=厦门安妮股份有限公司')
    def test_id_1018(self):
        case = self.r.id_1018('1018质押比例')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=1018, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('1018质押比例 -- ' + case['reason'])

    @allure.title('1017质押走势')
    @allure.link('http://open.api.tianyancha.com/services/open/mr/stockPledge/trend/2.0?keyword=平安银行股份有限公司')
    def test_id_1017(self):
        case = self.r.id_1017('1017质押走势')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=1017, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('1017质押走势 -- ' + case['reason'])


@allure.feature('知识产权')
@allure.suite('知识产权')
@allure.sub_suite('10个接口')
class TestShangBiaoXinXi:
    def setup_method(self):
        self.r = OnlineApi()

    @allure.title('838企业商标信息')
    @allure.link(
        'http://open.api.tianyancha.com/services/open/ipr/tm/2.0?'
        'appDateBegin=2010-01-01&pageSize=20&tmClass=29&appDateEnd=2020-01-01&keyword=北京百度网讯科技有限公司&pageNum=1&status=1')
    def test_id_838(self):
        case = self.r.id_838('838企业商标信息')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=838, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('838企业商标信息 -- ' + case['reason'])

    @allure.title('1027历史企业商标信息')
    @allure.link('http://open.api.tianyancha.com/services/open/hi/tm/2.0?pageSize=20&keyword=全维度测试有限责任公司&pageNum=1')
    def test_id_1027(self):
        case = self.r.id_1027('1027历史企业商标信息')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=1027, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('1027历史企业商标信息 -- ' + case['reason'])

    @allure.title('1061商标信息垂搜')
    @allure.link(
        'http://open.api.tianyancha.com/services/open/ipr/tm/search?'
        'searchType=1,2&appDateBegin=2010-01-01&pageSize=20&tmClass=1&appDateEnd=2020-01-01&keyword=百度&pageNum=1&status=1')
    def test_id_1061(self):
        case = self.r.id_1061('1061商标信息垂搜')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=1061, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('1061商标信息垂搜 -- ' + case['reason'])

    @allure.title('1051商标信息详情')
    @allure.link('http://open.api.tianyancha.com/services/open/ipr/tm/detail/2.0?regNo=35834580&intCls=38-通讯服务')
    def test_id_1051(self):
        case = self.r.id_1051('1051商标信息详情')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=1051, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('1051商标信息详情 -- ' + case['reason'])

    @allure.title('837企业专利信息')
    @allure.link(
        'http://open.api.tianyancha.com/services/open/ipr/patents/2.0?'
        'pubDateBegin=2010-01-01&appDateBegin=2010-01-01&pageSize=20&pubDateEnd=2020-01-01&appDateEnd=2020-01-01&'
        'keyword=北京百度网讯科技有限公司&pageNum=1&patentType=1')
    def test_id_837(self):
        case = self.r.id_837('837企业专利信息')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=837, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('837企业专利信息 -- ' + case['reason'])

    @allure.title('1062专利信息垂搜')
    @allure.link(
        'http://open.api.tianyancha.com/services/open/ipr/patents/search?'
        'searchType=1,2,3&pubDateBegin=2010-01-01&appDateBegin=2010-01-01&pageSize=20&pubDateEnd=2020-01-01&'
        'appDateEnd=2020-01-01&keyword=百度&pageNum=1&patentType=1')
    def test_id_1062(self):
        case = self.r.id_1062('1062专利信息垂搜')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=1062, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('1062专利信息垂搜 -- ' + case['reason'])

    @allure.title('836软件著作权')
    @allure.link(
        'http://open.api.tianyancha.com/services/open/ipr/copyReg/2.0?pageSize=20&keyword=北京百度网讯科技有限公司&pageNum=1')
    def test_id_836(self):
        case = self.r.id_836('836软件著作权')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=836, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('836软件著作权 -- ' + case['reason'])

    @allure.title('833作品著作权')
    @allure.link(
        'http://open.api.tianyancha.com/services/open/ipr/copyRegWorks/2.0?pageSize=20&keyword=北京百度网讯科技有限公司&pageNum=1')
    def test_id_833(self):
        case = self.r.id_833('833作品著作权')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=833, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('833作品著作权 -- ' + case['reason'])

    @allure.title('1038网站备案')
    @allure.link('http://open.api.tianyancha.com/services/open/ipr/icp/3.0?pageSize=20&keyword=北京百度网讯科技有限公司&pageNum=1')
    def test_id_1038(self):
        case = self.r.id_1038('1038网站备案')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=1038, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('1038网站备案 -- ' + case['reason'])

    @allure.title('995历史网站备案')
    @allure.link('http://open.api.tianyancha.com/services/open/hi/icp/2.0?pageSize=20&keyword=北京百度网讯科技有限公司&pageNum=1')
    def test_id_995(self):
        case = self.r.id_995('995历史网站备案')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=995, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('995历史网站备案 -- ' + case['reason'])


@allure.feature('人员相关')
@allure.suite('人员相关')
@allure.sub_suite('6个接口')
class TestRenYuanXiangGuan:
    def setup_method(self):
        self.r = OnlineApi()

    @allure.title('449人员所有角色')
    @allure.link(
        'http://open.api.tianyancha.com/services/v4/open/roles?hid=1984012283&name=北京百度网讯科技有限公司&humanName=李彦宏&cid=22822')
    def test_id_449(self):
        case = self.r.id_449('449人员所有角色')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=449, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('449人员所有角色 -- ' + case['reason'])

    @allure.title('1057人员所有历史角色')
    @allure.link('http://open.api.tianyancha.com/services/open/hi/roles?name=北京百度网讯科技有限公司&humanName=李彦宏')
    def test_id_1057(self):
        case = self.r.id_1057('1057人员所有历史角色')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=1057, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('1057人员所有历史角色 -- ' + case['reason'])

    @allure.title('450人员所有公司')
    @allure.link(
        'http://open.api.tianyancha.com/services/v4/open/allCompanys?name=北京百度网讯科技有限公司&humanName=李彦宏')
    def test_id_450(self):
        case = self.r.id_450('450人员所有公司')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=450, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('450人员所有公司 -- ' + case['reason'])

    @allure.title('451人员所有合作伙伴')
    @allure.link(
        'http://open.api.tianyancha.com/services/v4/open/partners?hid=1984012283&name=北京百度网讯科技有限公司&humanName=李彦宏&cid=22822')
    def test_id_451(self):
        case = self.r.id_451('451人员所有合作伙伴')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=451, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('451人员所有合作伙伴 -- ' + case['reason'])

    @allure.title('448企业人员简介')
    @allure.link(
        'http://open.api.tianyancha.com/services/v4/open/description?hid=1984012283&name=北京百度网讯科技有限公司&humanName=李彦宏&cid=22822')
    def test_id_448(self):
        case = self.r.id_448('448企业人员简介')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=448, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('448企业人员简介 -- ' + case['reason'])

    @allure.title('1033人员控股企业')
    @allure.link('http://open.api.tianyancha.com/services/open/human/companyholding/2.0?'
                 'hid=1984012283&name=北京百度网讯科技有限公司&pageSize=20&pageNum=1&humanName=李彦宏&cid=22822')
    def test_id_1033(self):
        case = self.r.id_1033('1033人员控股企业')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=1033, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('1033人员控股企业 -- ' + case['reason'])


@allure.feature('关系发现')
@allure.suite('关系发现')
@allure.sub_suite('7个接口')
class TestGuanXiFaXian:
    def setup_method(self):
        self.r = OnlineApi()

    @allure.title('783企业图谱')
    @allure.link('http://open.api.tianyancha.com/services/v4/open/oneKey/c?keyword=中航重机股份有限公司')
    def test_id_783(self):
        case = self.r.id_783('783企业图谱')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=783, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('783企业图谱 -- ' + case['reason'])

    @allure.title('453股权结构图')
    @allure.link('http://open.api.tianyancha.com/services/v4/open/equityRatio?keyword=北京百度网讯科技有限公司')
    def test_id_453(self):
        case = self.r.id_453('453股权结构图')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=453, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('453股权结构图 -- ' + case['reason'])

    @allure.title('455股权穿透图')
    @allure.link('http://open.api.tianyancha.com/services/v3/open/investtree?flag=2&dir=down&keyword=北京百度网讯科技有限公司')
    def test_id_455(self):
        case = self.r.id_455('455股权穿透图')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=455, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('455股权穿透图 -- ' + case['reason'])

    @allure.title('945最终受益人')
    @allure.link(
        'http://open.api.tianyancha.com/services/open/ic/humanholding/2.0?pageSize=20&keyword=北京百度网讯科技有限公司&pageNum=1')
    def test_id_945(self):
        case = self.r.id_945('945最终受益人')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=945, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('945最终受益人 -- ' + case['reason'])

    @allure.title('747实际控制权')
    @allure.link(
        'http://open.api.tianyancha.com/services/v4/open/companyholding?pageSize=1&keyword=北京百度网讯科技有限公司&pageNum=1')
    def test_id_747(self):
        case = self.r.id_747('747实际控制权')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=747, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('747实际控制权 -- ' + case['reason'])

    @allure.title('1028疑似实际控制人')
    @allure.link('http://open.api.tianyancha.com/services/open/ic/actualControl/2.0?keyword=北京百度网讯科技有限公司')
    def test_id_1028(self):
        case = self.r.id_1028('1028疑似实际控制人')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=1028, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('1028疑似实际控制人 -- ' + case['reason'])

    @allure.title('1044最短路径发现')
    @allure.link(
        'http://open.api.tianyancha.com/services/open/rela/shortPath?'
        'types=ALL&depth=3&idTo=3043827609&nameTo=北京百度智行科技有限公司&idFrom=22822&nameFrom=北京百度网讯科技有限公司')
    def test_id_1044(self):
        case = self.r.id_1044('1044最短路径发现')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=1044, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('1044最短路径发现 -- ' + case['reason'])


@allure.feature('增值服务')
@allure.suite('增值服务')
@allure.sub_suite('12个接口')
class TestZengZhiFuWu:
    def setup_method(self):
        self.r = OnlineApi()

    @allure.title('1058企业天眼风险')
    @allure.link('http://open.api.tianyancha.com/services/open/risk/riskInfo/2.0?keyword=北京百度网讯科技有限公司')
    def test_id_1058(self):
        case = self.r.id_1058('1058企业天眼风险')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=1058, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('1058企业天眼风险 -- ' + case['reason'])

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

    @allure.title('427人员天眼风险')
    @allure.link(
        'http://open.api.tianyancha.com/services/v4/open/humanRiskInfo?hid=2020172991&name=北京百度网讯科技有限公司&humanName=梁志祥&cid=22822')
    def test_id_427(self):
        case = self.r.id_427('427人员天眼风险')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=427, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('427人员天眼风险 -- ' + case['reason'])

    @allure.title('426天眼风险详情')
    @allure.link('http://open.api.tianyancha.com/services/v4/open/riskDetail?pageSize=5&id=104176702&type=8&pageNum=1')
    def test_id_426(self):
        case = self.r.id_426('426天眼风险详情')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=426, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('426天眼风险详情 -- ' + case['reason'])

    @allure.title('632企业无水印logo')
    @allure.link('http://open.api.tianyancha.com/services/v4/open/logo?keyword=北京百度网讯科技有限公司')
    def test_id_632(self):
        case = self.r.id_632('632企业无水印logo')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=632, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('632企业无水印logo -- ' + case['reason'])

    @allure.title('633验证企业')
    @allure.link('http://open.api.tianyancha.com/services/v4/open/match?name=北京百度网讯科技有限公司&keyword=91110000802100433B')
    def test_id_633(self):
        case = self.r.id_633('633验证企业')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=633, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('633验证企业 -- ' + case['reason'])

    @allure.title('778企业经纬度')
    @allure.link('http://open.api.tianyancha.com/services/v4/open/position?keyword=北京正方向汽车租赁有限公司')
    def test_id_778(self):
        case = self.r.id_778('778企业经纬度')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=778, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('778企业经纬度 -- ' + case['reason'])

    @allure.title('458企业曾用名')
    @allure.link('http://open.api.tianyancha.com/services/v4/open/historyNames?keyword=贵州荷泰集团酒业有限公司')
    def test_id_458(self):
        case = self.r.id_458('458企业曾用名')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=458, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('458企业曾用名 -- ' + case['reason'])

    @allure.title('457纳税人识别号')
    @allure.link('http://open.api.tianyancha.com/services/v4/open/taxesCode?keyword=北京百度网讯科技有限公司')
    def test_id_457(self):
        case = self.r.id_457('457纳税人识别号')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=457, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('457纳税人识别号 -- ' + case['reason'])

    @allure.title('776按行业/区域查询公司')
    @allure.link(
        'http://open.api.tianyancha.com/services/v4/open/searchV3?categoryGuobiao=759&areaCode=110108&word=百度&pageNum=1')
    def test_id_776(self):
        case = self.r.id_776('776按行业/区域查询公司')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=776, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('776按行业/区域查询公司 -- ' + case['reason'])

    @allure.title('755企业简介')
    @allure.link('http://open.api.tianyancha.com/services/v4/open/profile?keyword=北京百度网讯科技有限公司')
    def test_id_755(self):
        case = self.r.id_755('755企业简介')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=755, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('755企业简介 -- ' + case['reason'])


@allure.feature('报告服务')
@allure.suite('报告服务')
@allure.sub_suite('2个接口')
class TestBaoGaoFuWu:
    def setup_method(self):
        self.r = OnlineApi()

    @allure.title('1034企业信用报告（基础版）')
    @allure.link(
        'http://open.api.tianyancha.com/services/open/report/company/base?name=北京天眼查科技有限公司&id=3069334211&uuid=929dd1191cb511e6b554008cfae40dc0')
    def test_id_1034(self):
        case = self.r.id_1034('1034企业信用报告（基础版）')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=1034, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('1034企业信用报告（基础版） -- ' + case['reason'])

    @allure.title('1035企业信用报告（专业版）')
    @allure.link(
        'http://open.api.tianyancha.com/services/open/report/company/pro?name=北京天眼查科技有限公司&id=3069334211&uuid=929dd1191cb511e6b554008cfae40dc1')
    def test_id_1035(self):
        case = self.r.id_1035('1035企业信用报告（专业版）')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=1035, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('1035企业信用报告（专业版） -- ' + case['reason'])


@allure.feature('集团族群')
@allure.suite('集团族群')
@allure.sub_suite('7个接口')
class TestJiTuanZuQun:
    def setup_method(self):
        self.r = OnlineApi()

    @allure.title('1105所属集团查询')
    @allure.link('http://open.api.tianyancha.com/services/open/group/base?keyword=北京百度网讯科技有限公司')
    def test_id_1105(self):
        case = self.r.id_1105('1105所属集团查询')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=1105, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('1105所属集团查询 -- ' + case['reason'])

    @allure.title('1106集团详情信息')
    @allure.link(
        'http://open.api.tianyancha.com/services/open/group/base/details?uuid=21711e8f83a24df483a949313ad66299')
    def test_id_1106(self):
        case = self.r.id_1106('1106集团详情信息')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=1106, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('1106集团详情信息 -- ' + case['reason'])

    @allure.title('1107集团成员')
    @allure.link(
        'http://open.api.tianyancha.com/services/open/group/member?uuid=21711e8f83a24df483a949313ad66299&type=1&pageNum=1&pageSize=20')
    def test_id_1107(self):
        case = self.r.id_1107('1107集团成员')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=1107, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('1107集团成员 -- ' + case['reason'])

    @allure.title('1108集团对外投资')
    @allure.link(
        'http://open.api.tianyancha.com/services/open/group/investors?uuid=21711e8f83a24df483a949313ad66299&pageNum=1&pageSize=20')
    def test_id_1108(self):
        case = self.r.id_1108('1108集团对外投资')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=1108, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('1108集团对外投资 -- ' + case['reason'])

    @allure.title('1109集团内参与投资该企业的成员列表')
    @allure.link(
        'http://open.api.tianyancha.com/services/open/group/investorMember?uuid=21711e8f83a24df483a949313ad66299&id=3410303988&pageNum=1&pageSize=20')
    def test_id_1109(self):
        case = self.r.id_1109('1109集团内参与投资该企业的成员列表')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=1109, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output(
            '1109集团内参与投资该企业的成员列表 -- ' + case['reason'])

    @allure.title('1110集团投资方')
    @allure.link(
        'http://open.api.tianyancha.com/services/open/group/shareholders?uuid=21711e8f83a24df483a949313ad66299&pageNum=1&pageSize=20')
    def test_id_1110(self):
        case = self.r.id_1110('1110集团投资方')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=1110, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('1110集团投资方 -- ' + case['reason'])

    @allure.title('1111集团内被该投资方投资的成员列表')
    @allure.link(
        'http://open.api.tianyancha.com/services/open/group/shareholdersMember?uuid=21711e8f83a24df483a949313ad66299&id=22822&pageNum=1&pageSize=20')
    def test_id_1111(self):
        case = self.r.id_1111('1111集团内被该投资方投资的成员列表')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=1111, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output(
            '1111集团内被该投资方投资的成员列表 -- ' + case['reason'])


@allure.feature('组合接口')
@allure.suite('组合接口')
@allure.sub_suite('5个接口')
class TestZuHeJieKou:
    def setup_method(self):
        self.r = OnlineApi()

    @allure.title('1001工商信息')
    @allure.link('http://open.api.tianyancha.com/services/open/cb/ic/2.0?keyword=北京百度网讯科技有限公司')
    def test_id_1001(self):
        case = self.r.id_1001('1001工商信息')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=1001, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('1001工商信息 -- ' + case['reason'])

    @allure.title('1002司法风险')
    @allure.link('http://open.api.tianyancha.com/services/open/cb/judicial/2.0?keyword=北京百度网讯科技有限公司')
    def test_id_1002(self):
        case = self.r.id_1002('1002司法风险')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=1002, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('1002司法风险 -- ' + case['reason'])

    @allure.title('1003知识产权')
    @allure.link('http://open.api.tianyancha.com/services/open/cb/ipr/2.0?keyword=北京百度网讯科技有限公司')
    def test_id_1003(self):
        case = self.r.id_1003('1003知识产权')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=1003, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('1003知识产权 -- ' + case['reason'])

    @allure.title('1004企业发展')
    @allure.link('http://open.api.tianyancha.com/services/open/cb/development/2.0?keyword=北京百度网讯科技有限公司')
    def test_id_1004(self):
        case = self.r.id_1004('1004企业发展')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=1004, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('1004企业发展 -- ' + case['reason'])

    @allure.title('1005历史信息')
    @allure.link('http://open.api.tianyancha.com/services/open/cb/history/2.0?keyword=北京百度网讯科技有限公司')
    def test_id_1005(self):
        case = self.r.id_1005('1005历史信息')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if 'error_code' in case:
            if case['error_code'] != assert_content:
                self.r.feishu_alert(api_id=1005, text=str(case), traceId=case['debugInfo']['traceId'])
            assert case['error_code'] == assert_content, self.r.log_output('1005历史信息 -- ' + case['reason'])
        else:
            self.r.log_output('1005-历史信息，返回内容不正确：' + str(case))


@allure.feature('企业发展')
@allure.suite('企业发展')
@allure.sub_suite('10个接口')
class TestQiYeFaZhan:
    def setup_method(self):
        self.r = OnlineApi()

    @allure.title('799投资动态')
    @allure.link('http://open.api.tianyancha.com/services/v4/open/investEvent?name=百度资本&pageSize=20&pageNum=1')
    def test_id_799(self):
        case = self.r.id_799('799投资动态')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=799, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('799投资动态 -- ' + case['reason'])

    @allure.title('826融资历史')
    @allure.link(
        'http://open.api.tianyancha.com/services/open/cd/findHistoryRongzi/2.0?pageSize=20&keyword=北京百度网讯科技有限公司&pageNum=1')
    def test_id_826(self):
        case = self.r.id_826('826融资历史')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=826, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('826融资历史 -- ' + case['reason'])

    @allure.title('827核心团队')
    @allure.link(
        'http://open.api.tianyancha.com/services/open/cd/findTeamMember/2.0?pageSize=20&keyword=北京百度网讯科技有限公司&pageNum=1')
    def test_id_827(self):
        case = self.r.id_827('827核心团队')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=827, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('827核心团队 -- ' + case['reason'])

    @allure.title('828企业业务')
    @allure.link(
        'http://open.api.tianyancha.com/services/open/cd/getProductInfo/2.0?pageSize=20&keyword=北京百度网讯科技有限公司&pageNum=1')
    def test_id_828(self):
        case = self.r.id_828('828企业业务')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=828, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('828企业业务 -- ' + case['reason'])

    @allure.title('829投资事件')
    @allure.link(
        'http://open.api.tianyancha.com/services/open/cd/findTzanli/2.0?pageSize=20&keyword=北京百度网讯科技有限公司&pageNum=1')
    def test_id_829(self):
        case = self.r.id_829('829投资事件')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=829, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('829投资事件 -- ' + case['reason'])

    @allure.title('830竞品信息')
    @allure.link(
        'http://open.api.tianyancha.com/services/open/cd/findJingpin/2.0?pageSize=20&keyword=北京百度网讯科技有限公司&pageNum=1')
    def test_id_830(self):
        case = self.r.id_830('830竞品信息')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=830, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('830竞品信息 -- ' + case['reason'])

    @allure.title('831获取标签')
    @allure.link('http://open.api.tianyancha.com/services/open/cd/tags/2.0?id=b6bc016381')
    def test_id_831(self):
        case = self.r.id_831('831获取标签')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=831, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('831获取标签 -- ' + case['reason'])

    @allure.title('832搜索项目品牌/投资机构')
    @allure.link('http://open.api.tianyancha.com/services/open/cd/searchBrandAndAgency/2.0?word=百度')
    def test_id_832(self):
        case = self.r.id_832('832搜索项目品牌/投资机构')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=832, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('832搜索项目品牌/投资机构 -- ' + case['reason'])

    @allure.title('944投资机构')
    @allure.link(
        'http://open.api.tianyancha.com/services/open/cd/investOrg/2.0?pageSize=20&keyword=北京百度网讯科技有限公司&pageNum=1')
    def test_id_944(self):
        case = self.r.id_944('944投资机构')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=944, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('944投资机构 -- ' + case['reason'])

    @allure.title('954私募基金')
    @allure.link(
        'http://open.api.tianyancha.com/services/open/cd/privateFund/2.0?pageSize=20&keyword=9143010532070930XC&pageNum=1')
    def test_id_954(self):
        case = self.r.id_954('954私募基金')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=954, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('954私募基金 -- ' + case['reason'])


@allure.feature('上市信息')
@allure.suite('上市信息')
@allure.sub_suite('24个接口')
class TestShangShiXinXi:
    def setup_method(self):
        self.r = OnlineApi()

    @allure.title('1075上市公司')
    @allure.link(
        'http://open.api.tianyancha.com/services/open/stock/list?keyword=深圳市振业（集团）股份有限公司&pageNum=1&pageSize=10')
    def test_id_1075(self):
        case = self.r.id_1075('1075上市公司')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=1075, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('1075上市公司 -- ' + case['reason'])

    @allure.title('798上市公司财务简析')
    @allure.link('http://open.api.tianyancha.com/services/v4/open/financialAnalysis?keyword=平安银行股份有限公司')
    def test_id_798(self):
        case = self.r.id_798('798上市公司财务简析')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=798, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('798上市公司财务简析 -- ' + case['reason'])

    @allure.title('853股票行情')
    @allure.link('http://open.api.tianyancha.com/services/open/stock/volatility/2.0?keyword=199557844')
    def test_id_853(self):
        case = self.r.id_853('853股票行情')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=853, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('853股票行情 -- ' + case['reason'])

    @allure.title('854上市公司企业简介')
    @allure.link('http://open.api.tianyancha.com/services/open/stock/companyInfo/2.0?keyword=深圳市振业（集团）股份有限公司')
    def test_id_854(self):
        case = self.r.id_854('854上市公司企业简介')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=854, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('854上市公司企业简介 -- ' + case['reason'])

    @allure.title('855高管信息')
    @allure.link(
        'http://open.api.tianyancha.com/services/open/stock/seniorExecutive/2.0?pageSize=10&keyword=深圳市振业（集团）股份有限公司&pageNum=1')
    def test_id_855(self):
        case = self.r.id_855('855高管信息')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=855, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('855高管信息 -- ' + case['reason'])

    @allure.title('856参股控股')
    @allure.link(
        'http://open.api.tianyancha.com/services/open/stock/holdingCompany/2.0?pageSize=10&keyword=深圳市振业（集团）股份有限公司&pageNum=1')
    def test_id_856(self):
        case = self.r.id_856('856参股控股')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=856, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('856参股控股 -- ' + case['reason'])

    @allure.title('857上市公告')
    @allure.link(
        'http://open.api.tianyancha.com/services/open/stock/announcement/2.0?pageSize=10&keyword=深圳市振业（集团）股份有限公司&pageNum=1')
    def test_id_857(self):
        case = self.r.id_857('857上市公告')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=857, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('857上市公告 -- ' + case['reason'])

    @allure.title('859十大股东（十大流通股东）')
    @allure.link(
        'http://open.api.tianyancha.com/services/open/stock/shareholder/2.0?time=2020-03-31&keyword=485568977&type=1')
    def test_id_859(self):
        case = self.r.id_859('859十大股东（十大流通股东）')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=859, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('859十大股东（十大流通股东） -- ' + case['reason'])

    @allure.title('860发行相关')
    @allure.link('http://open.api.tianyancha.com/services/open/stock/issueRelated/2.0?keyword=深圳市振业（集团）股份有限公司')
    def test_id_860(self):
        case = self.r.id_860('860发行相关')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=860, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('860发行相关 -- ' + case['reason'])

    @allure.title('861股本结构')
    @allure.link(
        'http://open.api.tianyancha.com/services/open/stock/shareStructure/2.0?time=2019-06-30&keyword=深圳市振业（集团）股份有限公司')
    def test_id_861(self):
        case = self.r.id_861('861股本结构')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=861, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('861股本结构 -- ' + case['reason'])

    @allure.title('862股本变动')
    @allure.link(
        'http://open.api.tianyancha.com/services/open/stock/equityChange/2.0?pageSize=10&keyword=深圳市振业（集团）股份有限公司&pageNum=1')
    def test_id_862(self):
        case = self.r.id_862('862股本变动')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=862, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('862股本变动 -- ' + case['reason'])

    @allure.title('863分红情况')
    @allure.link(
        'http://open.api.tianyancha.com/services/open/stock/bonusInfo/2.0?pageSize=10&keyword=深圳市振业（集团）股份有限公司&pageNum=1')
    def test_id_863(self):
        case = self.r.id_863('863分红情况')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=863, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('863分红情况 -- ' + case['reason'])

    @allure.title('864配股情况')
    @allure.link(
        'http://open.api.tianyancha.com/services/open/stock/allotmen/2.0?pageSize=10&keyword=深圳市振业（集团）股份有限公司&pageNum=1')
    def test_id_864(self):
        case = self.r.id_864('864配股情况')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=864, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('864配股情况 -- ' + case['reason'])

    @allure.title('964证券信息')
    @allure.link('http://open.api.tianyancha.com/services/open/stock/security/2.0?keyword=广发证券股份有限公司')
    def test_id_964(self):
        case = self.r.id_964('964证券信息')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=964, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('964证券信息 -- ' + case['reason'])

    @allure.title('965重要人员')
    @allure.link('http://open.api.tianyancha.com/services/open/stock/corpBasicInfo/2.0?keyword=广发证券股份有限公司')
    def test_id_965(self):
        case = self.r.id_965('965重要人员')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=965, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('965重要人员 -- ' + case['reason'])

    @allure.title('966联系信息')
    @allure.link('http://open.api.tianyancha.com/services/open/stock/corpContactInfo/2.0?keyword=广发证券股份有限公司')
    def test_id_966(self):
        case = self.r.id_966('966联系信息')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=966, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('966联系信息 -- ' + case['reason'])

    @allure.title('967主要指标-年度')
    @allure.link('http://open.api.tianyancha.com/services/open/stock/mainIndex/2.0?keyword=厦门安妮股份有限公司')
    def test_id_967(self):
        case = self.r.id_967('967主要指标-年度')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=967, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('967主要指标年度 -- ' + case['reason'])

    @allure.title('968主要指标-季度')
    @allure.link(
        'http://open.api.tianyancha.com/services/open/stock/quarMainIndex/2.0?year=2019&keyword=山西兰花科技创业股份有限公司')
    def test_id_968(self):
        case = self.r.id_968('968主要指标-季度')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=968, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('968主要指标-季度 -- ' + case['reason'])

    @allure.title('969对外担保')
    @allure.link(
        'http://open.api.tianyancha.com/services/open/stock/guarantees/2.0?pageSize=20&keyword=厦门安妮股份有限公司&pageNum=1')
    def test_id_969(self):
        case = self.r.id_969('969对外担保')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=969, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('969对外担保 -- ' + case['reason'])

    @allure.title('970违规处理')
    @allure.link(
        'http://open.api.tianyancha.com/services/open/stock/illegal/2.0?pageSize=20&keyword=厦门安妮股份有限公司&pageNum=1')
    def test_id_970(self):
        case = self.r.id_970('970违规处理')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=970, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('970违规处理 -- ' + case['reason'])

    @allure.title('971利润表')
    @allure.link('http://open.api.tianyancha.com/services/open/stock/profit/2.0?year=2018&keyword=厦门安妮股份有限公司')
    def test_id_971(self):
        case = self.r.id_971('971利润表')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=971, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('971利润表 -- ' + case['reason'])

    @allure.title('972资产负债表')
    @allure.link('http://open.api.tianyancha.com/services/open/stock/balanceSheet/2.0?year=2018&keyword=厦门安妮股份有限公司')
    def test_id_972(self):
        case = self.r.id_972('972资产负债表')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=972, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('972资产负债表 -- ' + case['reason'])

    @allure.title('973现金流量表')
    @allure.link('http://open.api.tianyancha.com/services/open/stock/cashFlow/2.0?year=2018&keyword=厦门安妮股份有限公司')
    def test_id_973(self):
        case = self.r.id_973('973现金流量表')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=973, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('973现金流量表 -- ' + case['reason'])

    @allure.title('999招股书')
    @allure.link('http://open.api.tianyancha.com/services/open/stock/prospectus/2.0?keyword=广发证券股份有限公司')
    def test_id_999(self):
        case = self.r.id_999('999招股书')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=999, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('999招股书 -- ' + case['reason'])


@allure.feature('投资机构')
@allure.suite('投资机构')
@allure.sub_suite('10个接口')
class TestTouZiJiGou:
    def setup_method(self):
        self.r = OnlineApi()

    @allure.title('978工商追踪')
    @allure.link('http://open.api.tianyancha.com/services/open/oi/businessEvent/2.0?name=百度投资并购部&pageSize=20&pageNum=1')
    def test_id_978(self):
        case = self.r.id_978('978工商追踪')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=978, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('978工商追踪 -- ' + case['reason'])

    @allure.title('979相关新闻')
    @allure.link('http://open.api.tianyancha.com/services/open/oi/news/2.0?name=百度投资并购部&pageSize=20&pageNum=1')
    def test_id_979(self):
        case = self.r.id_979('979相关新闻')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=979, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('979相关新闻 -- ' + case['reason'])

    @allure.title('980机构成员')
    @allure.link('http://open.api.tianyancha.com/services/open/oi/team/2.0?name=百度投资并购部&pageSize=20&pageNum=1')
    def test_id_980(self):
        case = self.r.id_980('980机构成员')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=980, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('980机构成员 -- ' + case['reason'])

    @allure.title('981公开投资事件')
    @allure.link('http://open.api.tianyancha.com/services/open/oi/publicInvest/2.0?name=百度投资并购部&pageSize=20&pageNum=1')
    def test_id_981(self):
        case = self.r.id_981('981公开投资事件')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=981, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('981公开投资事件 -- ' + case['reason'])

    @allure.title('982未公开投资')
    @allure.link('http://open.api.tianyancha.com/services/open/oi/secretInvest/2.0?name=百度投资并购部&pageSize=20&pageNum=1')
    def test_id_982(self):
        case = self.r.id_982('982未公开投资')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=982, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('982未公开投资 -- ' + case['reason'])

    @allure.title('983管理基金')
    @allure.link('http://open.api.tianyancha.com/services/open/oi/funds/2.0?name=百度投资并购部&pageSize=20&pageNum=1')
    def test_id_983(self):
        case = self.r.id_983('983管理基金')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=983, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('983管理基金 -- ' + case['reason'])

    @allure.title('984对外投资基金')
    @allure.link('http://open.api.tianyancha.com/services/open/oi/extFunds/2.0?name=百度投资并购部&pageSize=20&pageNum=1')
    def test_id_984(self):
        case = self.r.id_984('984对外投资基金')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=984, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('984对外投资基金 -- ' + case['reason'])

    @allure.title('985基金管理人')
    @allure.link('http://open.api.tianyancha.com/services/open/oi/fundManager/2.0?name=红杉资本中国&pageSize=20&pageNum=1')
    def test_id_985(self):
        case = self.r.id_985('985基金管理人')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=985, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('985基金管理人 -- ' + case['reason'])

    @allure.title('986投资动态')
    @allure.link('http://open.api.tianyancha.com/services/open/oi/investEvent/2.0?name=百度投资并购部&pageSize=20&pageNum=1')
    def test_id_986(self):
        case = self.r.id_986('986投资动态')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=986, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('986投资动态 -- ' + case['reason'])

    @allure.title('987统计分析')
    @allure.link('http://open.api.tianyancha.com/services/open/oi/stats/2.0?year=2019&name=百度投资并购部')
    def test_id_987(self):
        case = self.r.id_987('987统计分析')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=987, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('987统计分析 -- ' + case['reason'])


@allure.feature('私募基金')
@allure.suite('私募基金')
@allure.sub_suite('7个接口')
class TestSiMuJiJin:
    def setup_method(self):
        self.r = OnlineApi()

    @allure.title('988机构信息')
    @allure.link('http://open.api.tianyancha.com/services/open/pf/orgInfo/2.0?keyword=新疆中科援疆创新创业私募基金管理有限公司')
    def test_id_988(self):
        case = self.r.id_988('988机构信息')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=988, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('988机构信息 -- ' + case['reason'])

    @allure.title('989会员信息')
    @allure.link('http://open.api.tianyancha.com/services/open/pf/member/2.0?keyword=新疆中科援疆创新创业私募基金管理有限公司')
    def test_id_989(self):
        case = self.r.id_989('989会员信息')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=989, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('989会员信息 -- ' + case['reason'])

    @allure.title('990法律意见书信息')
    @allure.link('http://open.api.tianyancha.com/services/open/pf/legalOpinion/2.0?keyword=新疆中科援疆创新创业私募基金管理有限公司')
    def test_id_990(self):
        case = self.r.id_990('990法律意见书信息')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=990, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('990法律意见书信息 -- ' + case['reason'])

    @allure.title('991高管信息')
    @allure.link('http://open.api.tianyancha.com/services/open/pf/boss/2.0?keyword=新疆中科援疆创新创业私募基金管理有限公司')
    def test_id_991(self):
        case = self.r.id_991('991高管信息')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=991, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('991高管信息 -- ' + case['reason'])

    @allure.title('992高管情况')
    @allure.link('http://open.api.tianyancha.com/services/open/pf/staff/2.0?keyword=新疆中科援疆创新创业私募基金管理有限公司')
    def test_id_992(self):
        case = self.r.id_992('992高管情况')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=992, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('992高管情况 -- ' + case['reason'])

    @allure.title('993产品信息')
    @allure.link('http://open.api.tianyancha.com/services/open/pf/product/2.0?keyword=厦门壹舟星辰投资管理有限公司')
    def test_id_993(self):
        case = self.r.id_993('993产品信息')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=993, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('993产品信息 -- ' + case['reason'])

    @allure.title('994诚信信息')
    @allure.link('http://open.api.tianyancha.com/services/open/pf/integrity/2.0?keyword=新疆中科援疆创新创业私募基金管理有限公司')
    def test_id_994(self):
        case = self.r.id_994('994诚信信息')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=994, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('994诚信信息 -- ' + case['reason'])


@allure.feature('建筑资质')
@allure.suite('建筑资质')
@allure.sub_suite('7个接口')
class TestJianZhuZiZhi:
    def setup_method(self):
        self.r = OnlineApi()

    @allure.title('1030建筑资质-不良行为')
    @allure.link(
        'http://open.api.tianyancha.com/services/open/bq/badConduct/2.0?pageSize=20&keyword=郑州久鼎路桥工程有限公司&pageNum=1')
    def test_id_1030(self):
        case = self.r.id_1030('1030建筑资质-不良行为')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=1030, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('1030建筑资质-不良行为 -- ' + case['reason'])

    @allure.title('1007建筑资质-资质资格')
    @allure.link(
        'http://open.api.tianyancha.com/services/open/bq/qualification/2.0?pageSize=20&keyword=全维度测试有限责任公司&pageNum=1')
    def test_id_1007(self):
        case = self.r.id_1007('1007建筑资质-资质资格')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=1007, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('1007建筑资质-资质资格 -- ' + case['reason'])

    @allure.title('1008建筑资质-资质资格详情')
    @allure.link(
        'http://open.api.tianyancha.com/services/open/bq/qualification/detail/2.0?businessId=5d5a553befe14117624e96cc-D123456789')
    def test_id_1008(self):
        case = self.r.id_1008('1008建筑资质-资质资格详情')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=1008, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('1008建筑资质-资质资格详情 -- ' + case['reason'])

    @allure.title('1009建筑资质-注册人员')
    @allure.link(
        'http://open.api.tianyancha.com/services/open/bq/regHuman/2.0?pageSize=20&keyword=全维度测试有限责任公司&pageNum=1')
    def test_id_1009(self):
        case = self.r.id_1009('1009建筑资质-注册人员')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=1009, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('1009建筑资质-注册人员 -- ' + case['reason'])

    @allure.title('1010建筑资质-注册人员详情')
    @allure.link(
        'http://open.api.tianyancha.com/services/open/bq/regHuman/detail/2.0?businessId=5d5a4e48efe14117624e96c8')
    def test_id_1010(self):
        case = self.r.id_1010('1010建筑资质-注册人员详情')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=1010, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('1010建筑资质-注册人员详情 -- ' + case['reason'])

    @allure.title('1011建筑资质-工程项目')
    @allure.link(
        'http://open.api.tianyancha.com/services/open/bq/project/2.0?pageSize=20&keyword=全维度测试有限责任公司&pageNum=1')
    def test_id_1011(self):
        case = self.r.id_1011('1011建筑资质-工程项目')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=1011, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('1011建筑资质-工程项目 -- ' + case['reason'])

    @allure.title('1012建筑资质-工程项目详情')
    @allure.link(
        'http://open.api.tianyancha.com/services/open/bq/project/detail/2.0?businessId=5d5a4fe7efe14117624e96ca')
    def test_id_1012(self):
        case = self.r.id_1012('1012建筑资质-工程项目详情')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=1012, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('1012建筑资质-工程项目详情 -- ' + case['reason'])


@allure.feature('搜索')
@allure.suite('搜索')
@allure.sub_suite('1个接口')
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


@allure.feature('人员风险')
@allure.suite('人员风险')
@allure.sub_suite('9个接口')
class TestRenYuanFengXian:
    def setup_method(self):
        self.r = OnlineApi()

    @allure.title('1076失信被执行人（人员）')
    @allure.link(
        'http://open.api.tianyancha.com/services/v4/open/human/dishonest?hid=2187083120&name=北京百乐文化传媒有限公司&humanName=贾跃亭&cid=34630712&pageSize=20&pageNum=1')
    def test_id_1076(self):
        case = self.r.id_1076('1076失信被执行人（人员）')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=1076, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('1076失信被执行人（人员） -- ' + case['reason'])

    @allure.title('1077被执行人（人员）')
    @allure.link(
        'http://open.api.tianyancha.com/services/v4/open/human/zhixinginfo?hid=2187083120&name=北京百乐文化传媒有限公司&humanName=贾跃亭&cid=34630712&pageSize=20&pageNum=1')
    def test_id_1077(self):
        case = self.r.id_1077('1077被执行人（人员）')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=1077, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('1077被执行人（人员） -- ' + case['reason'])

    @allure.title('1078限制消费令（人员）')
    @allure.link(
        'http://open.api.tianyancha.com/services/v4/open/human/consumptionRestriction?hid=2187083120&name=北京百乐文化传媒有限公司&humanName=贾跃亭&cid=34630712&pageSize=20&pageNum=1')
    def test_id_1078(self):
        case = self.r.id_1078('1078限制消费令（人员）')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=1078, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('1078限制消费令（人员） -- ' + case['reason'])

    @allure.title('1079司法协助（人员）')
    @allure.link(
        'http://open.api.tianyancha.com/services/v4/open/human/judicialAssistance?hid=2187083120&name=北京百乐文化传媒有限公司&humanName=贾跃亭&cid=34630712&pageSize=20&pageNum=1')
    def test_id_1079(self):
        case = self.r.id_1079('1079司法协助（人员）')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=1079, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('1079司法协助（人员） -- ' + case['reason'])

    @allure.title('1080司法协助（人员）详情')
    @allure.link(
        'http://open.api.tianyancha.com/services/v4/open/human/judicialAssistanceDetail?assistanceId=c37116808216')
    def test_id_1080(self):
        case = self.r.id_1080('1080司法协助（人员）详情')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=1080, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('1080司法协助（人员）详情 -- ' + case['reason'])

    @allure.title('1081终本案件（人员）')
    @allure.link(
        'http://open.api.tianyancha.com/services/v4/open/human/endCase?hid=2187083120&name=北京百乐文化传媒有限公司&humanName=贾跃亭&cid=34630712&pageSize=20&pageNum=1')
    def test_id_1081(self):
        case = self.r.id_1081('1081终本案件（人员）')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=1081, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('1081终本案件（人员） -- ' + case['reason'])

    @allure.title('1101历史失信被执行人（人员）')
    @allure.link(
        'http://open.api.tianyancha.com/services/open/hi/human/dishonest?hid=2187083120&name=北京百乐文化传媒有限公司&humanName=贾跃亭&cid=34630712&pageSize=20&pageNum=1')
    def test_id_1101(self):
        case = self.r.id_1101('1101历史失信被执行人（人员）')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=1101, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('1101历史失信被执行人（人员） -- ' + case['reason'])

    @allure.title('1102历史失信被执行人（人员）')
    @allure.link(
        'http://open.api.tianyancha.com/services/open/hi/human/zhixinginfo?hid=2187083120&name=北京百乐文化传媒有限公司&humanName=贾跃亭&cid=34630712&pageSize=20&pageNum=1')
    def test_id_1102(self):
        case = self.r.id_1102('1102历史失信被执行人（人员）')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=1102, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('1102历史失信被执行人（人员） -- ' + case['reason'])

    @allure.title('1103历史限制消费令（人员）')
    @allure.link(
        'http://open.api.tianyancha.com/services/open/hi/human/consumptionRestriction?hid=2187083120&name=北京百乐文化传媒有限公司&humanName=贾跃亭&cid=34630712&pageSize=20&pageNum=1')
    def test_id_1103(self):
        case = self.r.id_1103('1103历史限制消费令（人员）')
        allure.attach(json.dumps(case, indent=2, ensure_ascii=False), 'JSON响应内容', allure.attachment_type.JSON)
        if case['error_code'] != assert_content:
            self.r.feishu_alert(api_id=1103, text=str(case), traceId=case['debugInfo']['traceId'])
        assert case['error_code'] == assert_content, self.r.log_output('1103历史限制消费令（人员） -- ' + case['reason'])

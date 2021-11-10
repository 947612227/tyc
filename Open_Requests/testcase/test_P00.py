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



if __name__ == '__main__':
    pytest.main(['s','v'])
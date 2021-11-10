from Open_Requests.page.baseapi import BaseApi


class OnlineApi(BaseApi):
    # 日志存放地址
    # _file_path = "/Users/tyc/PycharmProjects/TYC-requests/log/log.txt"
    # _file_path = "/home/work/liumiao/tmp/log/tyc-requests/log.txt"
    _file_path = "./log/log.txt"

    # 预发、线上环境 - 18810143184，充值调用token
    _host = "http://open.api.tianyancha.com/services"
    # _host = "http://10.39.222.35:20064/services"
    _header = {"Authorization": "36ded9cc-6080-4570-9f14-badd0828bf88"}

    # 阿里云数据源--测试环境
    # _host = 'http://10.39.222.108:20064/services'
    # _header = {"Authorization": '05ec08ec-b7c3-487c-a150-cb8ce6c02626'}

    # 工商信息
    def id_817(self, key, value, name):
        self._api_name = name
        self._url = "/open/ic/baseinfo/2.0"
        self._params = {
            key: value,
            # "id": 11684584,
            # "name": "中航重机股份有限公司",
            # "keyword": "中航重机股份有限公司",
            'debug': 'true'
        }
        return self.api_send()

    def id_1120(self, name):
        self._api_name = name
        self._url = "/open/mr/judicialSale/3.0"
        self._params = {
            "id": 2417221770,
            "name": "中国东方资产管理股份有限公司",
            "keyword": "中国东方资产管理股份有限公司",
            "pageNum": 1,
            "pageSize": 20,
            'debug': 'true'
        }
        return self.api_send()

    def id_818(self, name):
        self._api_name = name
        self._url = "/open/ic/baseinfoV2/2.0"
        self._params = {
            "id": 11684584,
            "name": "中航重机股份有限公司",
            "keyword": "中航重机股份有限公司",
            'debug': 'true'
        }
        return self.api_send()

    def id_819(self, name):
        self._api_name = name
        self._url = "/open/ic/baseinfoV3/2.0"
        self._params = {
            "id": 11684584,
            "name": "中航重机股份有限公司",
            "keyword": "中航重机股份有限公司",
            'debug': 'true'
        }
        return self.api_send()

    def id_459(self, name):
        self._api_name = name
        self._url = "/v4/open/xgbaseinfoV2"
        self._params = {
            "id": 11364828,
            "name": "百度（香港）有限公司",
            "keyword": "百度（香港）有限公司",
            'debug': 'true'
        }
        return self.api_send()

    def id_1042(self, name):
        self._api_name = name
        self._url = "/open/ic/verify"
        self._params = {
            "name": "北京百度网讯科技有限公司",
            "code": "91110000802100433B",
            "legalPersonName": "梁志祥",
            'debug': 'true'
        }
        return self.api_send()

    def id_1045(self, name):
        self._api_name = name
        self._url = "/open/ic/snapshot"
        self._params = {
            "id": 22822,
            "name": "北京百度网讯科技有限公司",
            "keyword": "北京百度网讯科技有限公司",
            'debug': 'true'
        }
        return self.api_send()

    def id_1047(self, name):
        self._api_name = name
        self._url = "/open/ic/companyType"
        self._params = {
            "id": 22822,
            "name": "北京百度网讯科技有限公司",
            "keyword": "北京百度网讯科技有限公司",
            'debug': 'true'
        }
        return self.api_send()

    def id_1046(self, name):
        self._api_name = name
        self._url = "/open/ic/contact"
        self._params = {
            "id": 22822,
            "name": "北京百度网讯科技有限公司",
            "keyword": "北京百度网讯科技有限公司",
            'debug': 'true'
        }
        return self.api_send()

    def id_820(self, name):
        self._api_name = name
        self._url = "/open/ic/staff/2.0"
        self._params = {
            "id": 22822,
            "name": "北京百度网讯科技有限公司",
            "keyword": "北京百度网讯科技有限公司",
            "pageNum": 1,
            "pageSize": 20,
            'debug': 'true'
        }
        return self.api_send()

    def id_1050(self, name):
        self._api_name = name
        self._url = "/open/hi/members"
        self._params = {
            "id": 22822,
            "name": "北京百度网讯科技有限公司",
            "keyword": "北京百度网讯科技有限公司",
            'debug': 'true'
        }
        return self.api_send()

    def id_821(self, name):
        self._api_name = name
        self._url = "/open/ic/holder/2.0"
        self._params = {
            "id": 22822,
            "name": "北京百度网讯科技有限公司",
            "keyword": "北京百度网讯科技有限公司",
            "pageNum": 1,
            "pageSize": 20,
            'debug': 'true'
        }
        return self.api_send()

    def id_877(self, name):
        self._api_name = name
        self._url = "/open/hi/holder/2.0"
        self._params = {
            "id": 22822,
            "name": "北京百度网讯科技有限公司",
            "keyword": "北京百度网讯科技有限公司",
            "pageNum": 1,
            "pageSize": 20,
            'debug': 'true'
        }
        return self.api_send()

    def id_997(self, name):
        self._api_name = name
        self._url = "/open/ic/holderList/2.0"
        self._params = {
            "id": 2318455639,
            "name": "北京金堤科技有限公司",
            "keyword": "北京金堤科技有限公司",
            "pageNum": 1,
            "pageSize": 20,
            'debug': 'true'
        }
        return self.api_send()

    def id_998(self, name):
        self._api_name = name
        self._url = "/open/ic/holderChange/2.0"
        self._params = {
            "id": 2318455639,
            "name": "北京金堤科技有限公司",
            "keyword": "北京金堤科技有限公司",
            "pageNum": 1,
            "pageSize": 20,
            'debug': 'true'
        }
        return self.api_send()

    def id_823(self, name):
        self._api_name = name
        self._url = "/open/ic/inverst/2.0"
        self._params = {
            "id": 22822,
            "name": "北京百度网讯科技有限公司",
            "keyword": "北京百度网讯科技有限公司",
            "pageNum": 1,
            "pageSize": 20,
            'debug': 'true'
        }
        return self.api_send()

    def id_876(self, name):
        self._api_name = name
        self._url = "/open/hi/invest/2.0"
        self._params = {
            "id": 22822,
            "name": "北京百度网讯科技有限公司",
            "keyword": "北京百度网讯科技有限公司",
            "pageNum": 1,
            "pageSize": 20,
            'debug': 'true'
        }
        return self.api_send()

    def id_824(self, name):
        self._api_name = name
        self._url = "/open/ic/branch/2.0"
        self._params = {
            "id": 22822,
            "name": "北京百度网讯科技有限公司",
            "keyword": "北京百度网讯科技有限公司",
            "pageNum": 1,
            "pageSize": 20,
            'debug': 'true'
        }
        return self.api_send()

    def id_963(self, name):
        self._api_name = name
        self._url = "/open/ic/parentCompany/2.0"
        self._params = {
            "id": 139573097,
            "name": "北京百度网讯科技有限公司南京分公司",
            "keyword": "北京百度网讯科技有限公司南京分公司",
            'debug': 'true'
        }
        return self.api_send()

    def id_825(self, name):
        self._api_name = name
        self._url = "/open/ic/annualreport/2.0"
        self._params = {
            "id": 22822,
            "name": "北京百度网讯科技有限公司",
            "keyword": "北京百度网讯科技有限公司",
            'debug': 'true'
        }
        return self.api_send()

    def id_822(self, name):
        self._api_name = name
        self._url = "/open/ic/changeinfo/2.0"
        self._params = {
            "id": 22822,
            "name": "北京百度网讯科技有限公司",
            "keyword": "北京百度网讯科技有限公司",
            "pageNum": 1,
            "pageSize": 20,
            'debug': 'true'
        }
        return self.api_send()

    def id_878(self, name):
        self._api_name = name
        self._url = "/open/hi/ic/2.0"
        self._params = {
            "id": 22822,
            "name": "北京百度网讯科技有限公司",
            "keyword": "北京百度网讯科技有限公司",
            'debug': 'true'
        }
        return self.api_send()

    def id_364(self, name):
        self._api_name = name
        self._url = "/v4/open/baseinfoV2"
        self._params = {
            "id": 199557844,
            "name": "平安银行股份有限公司",
            "keyword": "平安银行股份有限公司",
            'debug': 'true'
        }
        return self.api_send()

    def id_365(self, name):
        self._api_name = name
        self._url = "/v4/open/baseinfoV3"
        self._params = {
            "id": 199557844,
            "name": "平安银行股份有限公司",
            "keyword": "平安银行股份有限公司",
            'debug': 'true'
        }
        return self.api_send()

    def id_735(self, name):
        self._api_name = name
        self._url = "/v4/open/suggestByRegion"
        self._params = {
            "city": '北京',
            "word": "百度",
            "base": "bj",
            'debug': 'true'
        }
        return self.api_send()

    # 司法风险
    def id_842(self, name):
        self._api_name = name
        self._url = "/open/jr/lawSuit/2.0"
        self._params = {
            "id": 22822,
            "name": "北京百度网讯科技有限公司",
            "keyword": "北京百度网讯科技有限公司",
            "pageNum": 1,
            "pageSize": 20,
            'debug': 'true'
        }
        return self.api_send()

    def id_1073(self, name):
        self._api_name = name
        self._url = "/open/jr/lawSuit/detail"
        self._params = {
            "uuid": "929dd3cc1cb511e6b554008cfae40dc0",
            'debug': 'true'
        }
        return self.api_send()

    def id_874(self, name):
        self._api_name = name
        self._url = "/open/hi/lawsuit/2.0"
        self._params = {
            "id": 22822,
            "name": "北京百度网讯科技有限公司",
            "keyword": "北京百度网讯科技有限公司",
            "pageNum": 1,
            "pageSize": 20,
            'debug': 'true'
        }
        return self.api_send()

    def id_840(self, name):
        self._api_name = name
        self._url = "/open/jr/ktannouncement/2.0"
        self._params = {
            "id": 22822,
            "name": "北京百度网讯科技有限公司",
            "keyword": "北京百度网讯科技有限公司",
            "pageNum": 1,
            "pageSize": 20,
            'debug': 'true'
        }
        return self.api_send()

    def id_875(self, name):
        self._api_name = name
        self._url = "/open/hi/announcement/2.0"
        self._params = {
            "id": 22822,
            "name": "北京百度网讯科技有限公司",
            "keyword": "北京百度网讯科技有限公司",
            "pageNum": 1,
            "pageSize": 20,
            'debug': 'true'
        }
        return self.api_send()

    def id_841(self, name):
        self._api_name = name
        self._url = "/open/jr/courtAnnouncement/2.0"
        self._params = {
            "id": 22822,
            "name": "北京百度网讯科技有限公司",
            "keyword": "北京百度网讯科技有限公司",
            "pageNum": 1,
            "pageSize": 20,
            'debug': 'true'
        }
        return self.api_send()

    def id_873(self, name):
        self._api_name = name
        self._url = "/open/hi/court/2.0"
        self._params = {
            "id": 22822,
            "name": "北京百度网讯科技有限公司",
            "keyword": "北京百度网讯科技有限公司",
            "pageNum": 1,
            "pageSize": 20,
            'debug': 'true'
        }
        return self.api_send()

    def id_962(self, name):
        self._api_name = name
        self._url = "/open/jr/sendAnnouncement/2.0"
        self._params = {
            "id": 1556051522,
            "name": "深圳市诚信祥融资担保有限公司",
            "keyword": "深圳市诚信祥融资担保有限公司",
            "pageNum": 1,
            "pageSize": 20,
            'debug': 'true'
        }
        return self.api_send()

    def id_961(self, name):
        self._api_name = name
        self._url = "/open/jr/courtRegister/2.0"
        self._params = {
            "id": 804277172,
            "name": "南京银城物业服务有限公司",
            "keyword": "南京银城物业服务有限公司",
            "pageNum": 1,
            "pageSize": 20,
            'debug': 'true'
        }
        return self.api_send()

    def id_756(self, name):
        self._api_name = name
        self._url = "/v4/open/judicial"
        self._params = {
            "id": 978740860,
            "name": "上海东浩环保装备有限公司",
            "keyword": "上海东浩环保装备有限公司",
            "pageNum": 1,
            "pageSize": 20,
            'debug': 'true'
        }
        return self.api_send()

    def id_757(self, name):
        self._api_name = name
        self._url = "/v4/open/getJudicialDetail"
        self._params = {
            "assistanceId": 281114985578,
            'debug': 'true'
        }
        return self.api_send()

    def id_1015(self, name):
        self._api_name = name
        self._url = "/open/hi/judicial/2.0"
        self._params = {
            "id": 837081876,
            "name": "南昌亨得利股份有限公司",
            "keyword": "南昌亨得利股份有限公司",
            'debug': 'true'
        }
        return self.api_send()

    def id_1016(self, name):
        self._api_name = name
        self._url = "/open/hi/judicial/detail/2.0"
        self._params = {
            "businessId": "4e4m4cv7fb12c6dff13033138l2544c8",
            'debug': 'true'
        }
        return self.api_send()

    def id_1036(self, name):
        self._api_name = name
        self._url = "/open/jr/bankruptcy/2.0"
        self._params = {
            "id": 365223910,
            "name": "长沙新世界国际大饭店有限公司",
            "keyword": "长沙新世界国际大饭店有限公司",
            "pageNum": 1,
            "pageSize": 20,
            'debug': 'true'
        }
        return self.api_send()

    def id_1037(self, name):
        self._api_name = name
        self._url = "/open/jr/bankruptcy/detail/2.0"
        self._params = {
            "gid": 365223910,
            "uuid": "4905eef8fc704bcfbb82b6f0294d6fc5",
            'debug': 'true'
        }
        return self.api_send()

    def id_839(self, name):
        self._api_name = name
        self._url = "/open/jr/zhixinginfo/2.0"
        self._params = {
            "id": 506749873,
            "name": "河北展发房地产开发有限公司",
            "keyword": "河北展发房地产开发有限公司",
            "pageNum": 1,
            "pageSize": 20,
            'debug': 'true'
        }
        return self.api_send()

    def id_871(self, name):
        self._api_name = name
        self._url = "/open/hi/zhixing/2.0"
        self._params = {
            "id": 22822,
            "name": "北京百度网讯科技有限公司",
            "keyword": "北京百度网讯科技有限公司",
            "pageNum": 1,
            "pageSize": 20,
            'debug': 'true'
        }
        return self.api_send()

    def id_843(self, name):
        self._api_name = name
        self._url = "/open/jr/dishonest/2.0"
        self._params = {
            "id": 2327152269,
            "name": "恩施鑫地源农业开发有限公司",
            "keyword": "恩施鑫地源农业开发有限公司",
            "pageNum": 1,
            "pageSize": 20,
            'debug': 'true'
        }
        return self.api_send()

    def id_872(self, name):
        self._api_name = name
        self._url = "/open/hi/dishonest/2.0"
        self._params = {
            "id": 2861521122,
            "name": "天津市红宝石商务宾馆有限公司",
            "keyword": "天津市红宝石商务宾馆有限公司",
            "pageNum": 1,
            "pageSize": 20,
            'debug': 'true'
        }
        return self.api_send()

    def id_1014(self, name):
        self._api_name = name
        self._url = "/open/jr/consumptionRestriction/2.0"
        self._params = {
            "id": 13983271,
            "name": "乐视控股（北京）有限公司",
            "keyword": "乐视控股（北京）有限公司",
            "pageNum": 1,
            "pageSize": 20,
            'debug': 'true'
        }
        return self.api_send()

    def id_1013(self, name):
        self._api_name = name
        self._url = "/open/jr/endCase/2.0"
        self._params = {
            "id": 795669467,
            "name": "成都市武侯区桂溪房地产开发公司",
            "keyword": "成都市武侯区桂溪房地产开发公司",
            "pageNum": 1,
            "pageSize": 20,
            'debug': 'true'
        }
        return self.api_send()

    def id_1041(self, name):
        self._api_name = name
        self._url = "/open/jr/judicialCase/2.0"
        self._params = {
            "id": 22822,
            "name": "北京百度网讯科技有限公司",
            "keyword": "北京百度网讯科技有限公司",
            "pageNum": 1,
            "pageSize": 20,
            'debug': 'true'
        }
        return self.api_send()

    # 经营信息
    def id_888(self, name):
        self._api_name = name
        self._url = "/open/m/getLicense/2.0"
        self._params = {
            "id": 2319089069,
            "name": "深圳市中亚医药有限公司",
            "keyword": "深圳市中亚医药有限公司",
            "pageNum": 1,
            "pageSize": 20,
            'debug': 'true'
        }
        return self.api_send()

    def id_867(self, name):
        self._api_name = name
        self._url = "/open/hi/license/2.0"
        self._params = {
            "id": 2319562440,
            "name": "锦州市中远旅行社有限责任公司",
            "keyword": "锦州市中远旅行社有限责任公司",
            "pageNum": 1,
            "pageSize": 20,
            'debug': 'true'
        }
        return self.api_send()

    def id_889(self, name):
        self._api_name = name
        self._url = "/open/m/getLicenseCreditchina/2.0"
        self._params = {
            "id": 2329413540,
            "name": "上海绪斌贸易有限公司",
            "keyword": "上海绪斌贸易有限公司",
            "pageNum": 1,
            "pageSize": 20,
            'debug': 'true'
        }
        return self.api_send()

    def id_869(self, name):
        self._api_name = name
        self._url = "/open/hi/license/creditChina/2.0"
        self._params = {
            "id": 22822,
            "name": "北京百度网讯科技有限公司",
            "keyword": "北京百度网讯科技有限公司",
            "pageNum": 1,
            "pageSize": 20,
            'debug': 'true'
        }
        return self.api_send()

    def id_883(self, name):
        self._api_name = name
        self._url = "/open/m/checkInfo/2.0"
        self._params = {
            "id": 22822,
            "name": "北京百度网讯科技有限公司",
            "keyword": "北京百度网讯科技有限公司",
            "pageNum": 1,
            "pageSize": 20,
            'debug': 'true'
        }
        return self.api_send()

    def id_1024(self, name):
        self._api_name = name
        self._url = "/open/m/doubleRandomCheck/2.0"
        self._params = {
            "id": 700002100,
            "name": "武汉世纪楚泽商贸有限公司",
            "keyword": "武汉世纪楚泽商贸有限公司",
            "pageNum": 1,
            "pageSize": 20,
            'debug': 'true'
        }
        return self.api_send()

    def id_1025(self, name):
        self._api_name = name
        self._url = "/open/m/doubleRandomCheckDetail/2.0"
        self._params = {
            "businessId": "4me4c1m72f122bd2d7f23e1eal2f46f7",
            "pageNum": 1,
            "pageSize": 20,
            'debug': 'true'
        }
        return self.api_send()

    def id_884(self, name):
        self._api_name = name
        self._url = "/open/m/taxCredit/2.0"
        self._params = {
            "id": 22822,
            "name": "北京百度网讯科技有限公司",
            "keyword": "北京百度网讯科技有限公司",
            "pageNum": 1,
            "pageSize": 20,
            'debug': 'true'
        }
        return self.api_send()

    def id_881(self, name):
        self._api_name = name
        self._url = "/open/m/importAndExport/2.0"
        self._params = {
            "id": 2352946528,
            "name": "珠海市优隆贸易有限公司",
            "keyword": "珠海市优隆贸易有限公司",
            'debug': 'true'
        }
        return self.api_send()

    def id_948(self, name):
        self._api_name = name
        self._url = "/open/m/teleCommunicationLicense/2.0"
        self._params = {
            "id": 22822,
            "name": "北京百度网讯科技有限公司",
            "keyword": "北京百度网讯科技有限公司",
            "pageNum": 1,
            "pageSize": 20,
            'debug': 'true'
        }
        return self.api_send()

    def id_880(self, name):
        self._api_name = name
        self._url = "/open/m/certificate/2.0"
        self._params = {
            "id": 22822,
            "name": "北京百度网讯科技有限公司",
            "keyword": "北京百度网讯科技有限公司",
            "certificateName": "中国质量认证中心_CCC证书",
            "pageNum": 1,
            "pageSize": 20,
            'debug': 'true'
        }
        return self.api_send()

    def id_1029(self, name):
        self._api_name = name
        self._url = "/open/m/announcementReport/2.0"
        self._params = {
            "id": 199557844,
            "name": "平安银行股份有限公司",
            "keyword": "平安银行股份有限公司",
            "pageNum": 1,
            "pageSize": 20,
            'debug': 'true'
        }
        return self.api_send()

    def id_1049(self, name):
        self._api_name = name
        self._url = "/open/m/creditRating/2.0"
        self._params = {
            "id": 212307280,
            "name": "光大证券股份有限公司",
            "keyword": "光大证券股份有限公司",
            "pageNum": 1,
            "pageSize": 20,
            'debug': 'true'
        }
        return self.api_send()

    def id_1048(self, name):
        self._api_name = name
        self._url = "/open/m/taxpayer/2.0"
        self._params = {
            "id": 43743335,
            "name": "北京一点网聚科技有限公司",
            "keyword": "北京一点网聚科技有限公司",
            "pageNum": 1,
            "pageSize": 20,
            'debug': 'true'
        }
        return self.api_send()

    def id_886(self, name):
        self._api_name = name
        self._url = "/open/m/bond/2.0"
        self._params = {
            "id": 78931523,
            "name": "嘉兴银行股份有限公司",
            "keyword": "嘉兴银行股份有限公司",
            "pageNum": 1,
            "pageSize": 20,
            'debug': 'true'
        }
        return self.api_send()

    def id_882(self, name):
        self._api_name = name
        self._url = "/open/m/appbkInfo/2.0"
        self._params = {
            "id": 22822,
            "name": "北京百度网讯科技有限公司",
            "keyword": "北京百度网讯科技有限公司",
            "pageNum": 1,
            "pageSize": 20,
            'debug': 'true'
        }
        return self.api_send()

    def id_885(self, name):
        self._api_name = name
        self._url = "/open/m/purchaseLand/2.0"
        self._params = {
            "name": "恒大集团有限公司",
            'debug': 'true'
        }
        return self.api_send()

    def id_946(self, name):
        self._api_name = name
        self._url = "/open/m/supply/2.0"
        self._params = {
            "id": 22822,
            "name": "北京百度网讯科技有限公司",
            "keyword": "北京百度网讯科技有限公司",
            "year": 2018,
            "pageNum": 1,
            "pageSize": 20,
            'debug': 'true'
        }
        return self.api_send()

    def id_947(self, name):
        self._api_name = name
        self._url = "/open/m/customer/2.0"
        self._params = {
            "id": 22822,
            "name": "北京百度网讯科技有限公司",
            "keyword": "北京百度网讯科技有限公司",
            "year": 2018,
            "pageNum": 1,
            "pageSize": 20,
            'debug': 'true'
        }
        return self.api_send()

    def id_879(self, name):
        self._api_name = name
        self._url = "/open/m/employments/2.0"
        self._params = {
            "id": 22822,
            "name": "北京百度网讯科技有限公司",
            "keyword": "北京百度网讯科技有限公司",
            "pageNum": 1,
            "pageSize": 20,
            'debug': 'true'
        }
        return self.api_send()

    def id_953(self, name):
        self._api_name = name
        self._url = "/open/m/bp/employments/2.0"
        self._params = {
            "id": 22822,
            "name": "北京百度网讯科技有限公司",
            "keyword": "北京百度网讯科技有限公司",
            "pageNum": 1,
            "pageSize": 20,
            'debug': 'true'
        }
        return self.api_send()

    def id_1026(self, name):
        self._api_name = name
        self._url = "/open/m/weibo/2.0"
        self._params = {
            "id": 22822,
            "name": "北京百度网讯科技有限公司",
            "keyword": "北京百度网讯科技有限公司",
            "pageNum": 1,
            "pageSize": 20,
            'debug': 'true'
        }
        return self.api_send()

    def id_834(self, name):
        self._api_name = name
        self._url = "/open/ipr/publicWeChat/2.0"
        self._params = {
            "id": 22822,
            "name": "北京百度网讯科技有限公司",
            'debug': 'true'
        }
        return self.api_send()

    def id_887(self, name):
        self._api_name = name
        self._url = "/open/m/bids/2.0"
        self._params = {
            "id": 22822,
            "name": "北京百度网讯科技有限公司",
            "keyword": "北京百度网讯科技有限公司",
            "pageNum": 1,
            "pageSize": 20,
            "publishStartTime": "2010-01-01",
            "publishEndTime": "2020-01-01",
            'debug': 'true'
        }
        return self.api_send()

    def id_1063(self, name):
        self._api_name = name
        self._url = "/open/m/bids/search"
        self._params = {
            "keyword": "百度",
            "searchType": "1,2",
            "publishStartTime": "2010-01-01",
            "publishEndTime": "2020-01-01",
            'debug': 'true'
        }
        return self.api_send()

    def id_949(self, name):
        self._api_name = name
        self._url = "/open/m/landPublicity/2.0"
        self._params = {
            "id": 3022576126,
            "name": "天津大丰兴业科技有限公司",
            "keyword": "天津大丰兴业科技有限公司",
            "pageNum": 1,
            "pageSize": 20,
            'debug': 'true'
        }
        return self.api_send()

    def id_950(self, name):
        self._api_name = name
        self._url = "/open/m/landPublicity/detail/2.0"
        self._params = {
            "id": 74,
            'debug': 'true'
        }
        return self.api_send()

    def id_951(self, name):
        self._api_name = name
        self._url = "/open/m/landTransfer/2.0"
        self._params = {
            "id": 403856439,
            "name": "邵阳市东风房地产开发有限责任公司",
            "keyword": "邵阳市东风房地产开发有限责任公司",
            "pageNum": 1,
            "pageSize": 20,
            'debug': 'true'
        }
        return self.api_send()

    def id_952(self, name):
        self._api_name = name
        self._url = "/open/m/landTransfer/detail/2.0"
        self._params = {
            "id": 179495,
            'debug': 'true'
        }
        return self.api_send()

    # 经营风险
    def id_847(self, name):
        self._api_name = name
        self._url = "/open/mr/punishmentInfo/2.0"
        self._params = {
            "id": 22822,
            "name": "北京百度网讯科技有限公司",
            "keyword": "北京百度网讯科技有限公司",
            "pageNum": 1,
            "pageSize": 20,
            'debug': 'true'
        }
        return self.api_send()

    def id_870(self, name):
        self._api_name = name
        self._url = "/open/hi/punishment/2.0"
        self._params = {
            "id": 22822,
            "name": "北京百度网讯科技有限公司",
            "keyword": "北京百度网讯科技有限公司",
            "pageNum": 1,
            "pageSize": 20,
            'debug': 'true'
        }
        return self.api_send()

    def id_852(self, name):
        self._api_name = name
        self._url = "/open/mr/creditChina/2.0"
        self._params = {
            "id": 2324446183,
            "name": "江苏省连云港汽车运输有限公司",
            "keyword": "江苏省连云港汽车运输有限公司",
            "pageNum": 1,
            "pageSize": 20,
            'debug': 'true'
        }
        return self.api_send()

    def id_865(self, name):
        self._api_name = name
        self._url = "/open/hi/punishment/creditChina/2.0"
        self._params = {
            "id": 22822,
            "name": "北京百度网讯科技有限公司",
            "keyword": "北京百度网讯科技有限公司",
            "pageNum": 1,
            "pageSize": 20,
            'debug': 'true'
        }
        return self.api_send()

    def id_851(self, name):
        self._api_name = name
        self._url = "/open/mr/ownTax/2.0"
        self._params = {
            "id": 3067496862,
            "name": "青浦白鹤建新石材经营部",
            "keyword": "青浦白鹤建新石材经营部",
            "pageNum": 1,
            "pageSize": 20,
            'debug': 'true'
        }
        return self.api_send()

    def id_957(self, name):
        self._api_name = name
        self._url = "/open/mr/taxContravention/2.0"
        self._params = {
            "id": 136622514,
            "name": "宁波保税区航晨塑化有限公司",
            "keyword": "宁波保税区航晨塑化有限公司",
            "pageNum": 1,
            "pageSize": 20,
            'debug': 'true'
        }
        return self.api_send()

    def id_958(self, name):
        self._api_name = name
        self._url = "/open/mr/taxContravention/detail/2.0"
        self._params = {
            "id": 1152,
            'debug': 'true'
        }
        return self.api_send()

    def id_848(self, name):
        self._api_name = name
        self._url = "/open/mr/abnormal/2.0"
        self._params = {
            "id": 3472845776,
            "name": "重庆罗森便利店有限公司宝桐路店",
            "keyword": "重庆罗森便利店有限公司宝桐路店",
            "pageNum": 1,
            "pageSize": 20,
            'debug': 'true'
        }
        return self.api_send()

    def id_996(self, name):
        self._api_name = name
        self._url = "/open/hi/abnormal/2.0"
        self._params = {
            "id": 1073117874,
            "name": "湖南瑞源生物医药科技有限公司",
            "keyword": "湖南瑞源生物医药科技有限公司",
            "pageNum": 1,
            "pageSize": 20,
            'debug': 'true'
        }
        return self.api_send()

    def id_846(self, name):
        self._api_name = name
        self._url = "/open/mr/illegalinfo/2.0"
        self._params = {
            "id": 2328347771,
            "name": "四川展佳空调工程有限公司深圳分公司",
            "keyword": "四川展佳空调工程有限公司深圳分公司",
            "pageNum": 1,
            "pageSize": 20,
            'debug': 'true'
        }
        return self.api_send()

    def id_849(self, name):
        self._api_name = name
        self._url = "/open/mr/liquidating/2.0"
        self._params = {
            "id": 2411972547,
            "name": "上海臣堃电子商务有限公司",
            "keyword": "上海臣堃电子商务有限公司",
            'debug': 'true'
        }
        return self.api_send()

    def id_960(self, name):
        self._api_name = name
        self._url = "/open/mr/briefCancel/2.0"
        self._params = {
            "id": 1657833888,
            "name": "上海著远网络信息技术有限公司",
            "keyword": "上海著远网络信息技术有限公司",
            'debug': 'true'
        }
        return self.api_send()

    def id_1023(self, name):
        self._api_name = name
        self._url = "/open/mr/inquiryEvaluation/2.0"
        self._params = {
            "id": 700101451,
            "name": "武汉金湖科技有限公司",
            "keyword": "武汉金湖科技有限公司",
            "pageNum": 1,
            "pageSize": 20,
            'debug': 'true'
        }
        return self.api_send()

    def id_850(self, name):
        self._api_name = name
        self._url = "/open/mr/judicialSale/2.0"
        self._params = {
            "id": 2349508353,
            "name": "常州市武进区银通农村小额贷款股份有限公司",
            "keyword": "常州市武进区银通农村小额贷款股份有限公司",
            "pageNum": 1,
            "pageSize": 20,
            'debug': 'true'
        }
        return self.api_send()

    def id_796(self, name):
        self._api_name = name
        self._url = "/v4/open/publicNotice"
        self._params = {
            "id": 373555849,
            "name": "广州立达尔生物科技股份有限公司",
            "keyword": "广州立达尔生物科技股份有限公司",
            "pageNum": 1,
            "pageSize": 20,
            'debug': 'true'
        }
        return self.api_send()

    def id_844(self, name):
        self._api_name = name
        self._url = "/open/mr/mortgageInfo/2.0"
        self._params = {
            "id": 2337686417,
            "name": "讷河市丰盛现代农业农机专业合作社",
            "keyword": "讷河市丰盛现代农业农机专业合作社",
            "pageNum": 1,
            "pageSize": 20,
            'debug': 'true'
        }
        return self.api_send()

    def id_866(self, name):
        self._api_name = name
        self._url = "/open/hi/mortgageInfo/2.0"
        self._params = {
            "id": 2345174046,
            "name": "嫩江县朝阳种植专业合作社",
            "keyword": "嫩江县朝阳种植专业合作社",
            "pageNum": 1,
            "pageSize": 20,
            'debug': 'true'
        }
        return self.api_send()

    def id_955(self, name):
        self._api_name = name
        self._url = "/open/mr/landMortgage/2.0"
        self._params = {
            "id": 403856439,
            "name": "邵阳市东风房地产开发有限责任公司",
            "keyword": "邵阳市东风房地产开发有限责任公司",
            "pageNum": 1,
            "pageSize": 20,
            'debug': 'true'
        }
        return self.api_send()

    def id_956(self, name):
        self._api_name = name
        self._url = "/open/mr/landMortgage/detail/2.0"
        self._params = {
            "id": 57277,
            'debug': 'true'
        }
        return self.api_send()

    def id_795(self, name):
        self._api_name = name
        self._url = "/v4/open/getPledgeReg"
        self._params = {
            "id": 373555849,
            "name": "广州立达尔生物科技股份有限公司",
            "keyword": "广州立达尔生物科技股份有限公司",
            "pageNum": 1,
            "pageSize": 20,
            'debug': 'true'
        }
        return self.api_send()

    def id_845(self, name):
        self._api_name = name
        self._url = "/open/mr/equityInfo/2.0"
        self._params = {
            "id": 236499922,
            "name": "内蒙古大草原生态产业投资有限公司",
            "keyword": "内蒙古大草原生态产业投资有限公司",
            "pageNum": 1,
            "pageSize": 20,
            'debug': 'true'
        }
        return self.api_send()

    def id_868(self, name):
        self._api_name = name
        self._url = "/open/hi/equityInfo/2.0"
        self._params = {
            "id": 22822,
            "name": "北京百度网讯科技有限公司",
            "keyword": "北京百度网讯科技有限公司",
            "pageNum": 1,
            "pageSize": 20,
            'debug': 'true'
        }
        return self.api_send()

    def id_1021(self, name):
        self._api_name = name
        self._url = "/open/mr/stockPledge/detailList/2.0"
        self._params = {
            "id": 7996092,
            "name": "厦门安妮股份有限公司",
            "keyword": "厦门安妮股份有限公司",
            "pageNum": 1,
            "pageSize": 20,
            'debug': 'true'
        }
        return self.api_send()

    def id_1022(self, name):
        self._api_name = name
        self._url = "/open/mr/stockPledge/detail/2.0"
        self._params = {
            "id": 7996092,
            "businessId": "49o1ecbae1bb82282dbe7a1aflbf1f36",
            'debug': 'true'
        }
        return self.api_send()

    def id_1019(self, name):
        self._api_name = name
        self._url = "/open/mr/stockPledge/shareholder/2.0"
        self._params = {
            "id": 3329072553,
            "name": "通源石油科技集团股份有限公司",
            "keyword": "通源石油科技集团股份有限公司",
            "pageNum": 1,
            "pageSize": 20,
            'debug': 'true'
        }
        return self.api_send()

    def id_1020(self, name):
        self._api_name = name
        self._url = "/open/mr/stockPledge/shareholder/detail/2.0"
        self._params = {
            "businessId": "1o118ef2424dfb670e699b1b0l671c24",
            "id": 7996092,
            'debug': 'true'
        }
        return self.api_send()

    def id_1018(self, name):
        self._api_name = name
        self._url = "/open/mr/stockPledge/ratio/2.0"
        self._params = {
            "id": 7996092,
            "name": "厦门安妮股份有限公司",
            "keyword": "厦门安妮股份有限公司",
            "date": "2019-07-26",
            'debug': 'true'
        }
        return self.api_send()

    def id_1017(self, name):
        self._api_name = name
        self._url = "/open/mr/stockPledge/trend/2.0"
        self._params = {
            "id": 199557844,
            "name": "平安银行股份有限公司",
            "keyword": "平安银行股份有限公司",
            'debug': 'true'
        }
        return self.api_send()

    # 知识产权
    def id_838(self, name):
        self._api_name = name
        self._url = "/open/ipr/tm/2.0"
        self._params = {
            "id": 22822,
            "name": "北京百度网讯科技有限公司",
            "keyword": "北京百度网讯科技有限公司",
            "pageNum": 1,
            "pageSize": 20,
            "tmClass": 29,
            "status": 1,
            "appDateBegin": "2010-01-01",
            "appDateEnd": "2020-01-01",
            'debug': 'true'
        }
        return self.api_send()

    def id_1027(self, name):
        self._api_name = name
        self._url = "/open/hi/tm/2.0"
        self._params = {
            "id": 3355627294,
            "name": "全维度测试有限责任公司",
            "keyword": "全维度测试有限责任公司",
            "pageNum": 1,
            "pageSize": 20,
            'debug': 'true'
        }
        return self.api_send()

    def id_1061(self, name):
        self._api_name = name
        self._url = "/open/m/bids/search"
        self._params = {
            "keyword": "百度",
            "searchType": "1,2",
            "tmClass": 1,
            "status": 1,
            "appDateBegin": "2010-01-01",
            "appDateEnd": "2020-01-01",
            "pageNum": 1,
            "pageSize": 20,
            'debug': 'true'
        }
        return self.api_send()

    def id_1051(self, name):
        self._api_name = name
        self._url = "/open/ipr/tm/detail/2.0"
        self._params = {
            "regNo": 35834580,
            "intCls": "38-通讯服务",
            'debug': 'true'
        }
        return self.api_send()

    def id_837(self, name):
        self._api_name = name
        self._url = "/open/ipr/patents/2.0"
        self._params = {
            "id": 22822,
            "name": "北京百度网讯科技有限公司",
            "keyword": "北京百度网讯科技有限公司",
            "pageNum": 1,
            "pageSize": 20,
            "patentType": 1,
            "pubDateBegin": "2010-01-01",
            "pubDateEnd": "2020-01-01",
            "appDateBegin": "2010-01-01",
            "appDateEnd": "2020-01-01",
            'debug': 'true'
        }
        return self.api_send()

    def id_1062(self, name):
        self._api_name = name
        self._url = "/open/ipr/patents/search"
        self._params = {
            "keyword": "百度",
            "searchType": "1,2,3",
            "patentType": 1,
            "pubDateBegin": "2010-01-01",
            "pubDateEnd": "2020-01-01",
            "appDateBegin": "2010-01-01",
            "appDateEnd": "2020-01-01",
            "pageNum": 1,
            "pageSize": 20,
            'debug': 'true'
        }
        return self.api_send()

    def id_836(self, name):
        self._api_name = name
        self._url = "/open/ipr/copyReg/2.0"
        self._params = {
            "id": 22822,
            "name": "北京百度网讯科技有限公司",
            "keyword": "北京百度网讯科技有限公司",
            "pageNum": 1,
            "pageSize": 20,
            'debug': 'true'
        }
        return self.api_send()

    def id_833(self, name):
        self._api_name = name
        self._url = "/open/ipr/copyRegWorks/2.0"
        self._params = {
            "id": 22822,
            "name": "北京百度网讯科技有限公司",
            "keyword": "北京百度网讯科技有限公司",
            "pageNum": 1,
            "pageSize": 20,
            'debug': 'true'
        }
        return self.api_send()

    def id_1038(self, name):
        self._api_name = name
        self._url = "/open/ipr/icp/3.0"
        self._params = {
            "id": 22822,
            "name": "北京百度网讯科技有限公司",
            "keyword": "北京百度网讯科技有限公司",
            "pageNum": 1,
            "pageSize": 20,
            'debug': 'true'
        }
        return self.api_send()

    def id_995(self, name):
        self._api_name = name
        self._url = "/open/hi/icp/2.0"
        self._params = {
            "id": 22822,
            "name": "北京百度网讯科技有限公司",
            "keyword": "北京百度网讯科技有限公司",
            "pageNum": 1,
            "pageSize": 20,
            'debug': 'true'
        }
        return self.api_send()

    # 人员相关
    def id_449(self, name):
        self._api_name = name
        self._url = "/v4/open/roles"
        self._params = {
            "name": "北京百度网讯科技有限公司",
            "humanName": "李彦宏",
            "cid": 22822,
            "hid": 1984012283,
            'debug': 'true'
        }
        return self.api_send()

    def id_1057(self, name):
        self._api_name = name
        self._url = "/open/hi/roles"
        self._params = {
            "name": "北京百度网讯科技有限公司",
            "humanName": "李彦宏",
            "cid": 22822,
            "hid": 1984012283,
            'debug': 'true'
        }
        return self.api_send()

    def id_450(self, name):
        self._api_name = name
        self._url = "/v4/open/allCompanys"
        self._params = {
            "name": "北京百度网讯科技有限公司",
            "humanName": "李彦宏",
            "cid": 22822,
            "hid": 1984012283,
            'debug': 'true'
        }
        return self.api_send()

    def id_451(self, name):
        self._api_name = name
        self._url = "/v4/open/partners"
        self._params = {
            "name": "北京百度网讯科技有限公司",
            "humanName": "李彦宏",
            "cid": 22822,
            "hid": 1984012283,
            'debug': 'true'
        }
        return self.api_send()

    def id_448(self, name):
        self._api_name = name
        self._url = "/v4/open/description"
        self._params = {
            "name": "北京百度网讯科技有限公司",
            "humanName": "李彦宏",
            "cid": 22822,
            "hid": 1984012283,
            'debug': 'true'
        }
        return self.api_send()

    def id_1033(self, name):
        self._api_name = name
        self._url = "/open/human/companyholding/2.0"
        self._params = {
            "name": "北京百度网讯科技有限公司",
            "humanName": "李彦宏",
            "cid": 22822,
            "hid": 1984012283,
            "pageNum": 1,
            "pageSize": 20,
            'debug': 'true'
        }
        return self.api_send()

    # 关系发现
    def id_783(self, name):
        self._api_name = name
        self._url = "/v4/open/oneKey/c"
        self._params = {
            "id": 11684584,
            "name": "中航重机股份有限公司",
            "keyword": "中航重机股份有限公司",
            'debug': 'true'
        }
        return self.api_send()

    def id_453(self, name):
        self._api_name = name
        self._url = "/v4/open/equityRatio"
        self._params = {
            "id": 22822,
            "name": "北京百度网讯科技有限公司",
            "keyword": "北京百度网讯科技有限公司",
            'debug': 'true'
        }
        return self.api_send()

    def id_455(self, name):
        self._api_name = name
        self._url = "/v3/open/investtree"
        self._params = {
            "id": 22822,
            "name": "北京百度网讯科技有限公司",
            "keyword": "北京百度网讯科技有限公司",
            "flag": 2,
            "dir": "down",
            'debug': 'true'
        }
        return self.api_send()

    def id_945(self, name):
        self._api_name = name
        self._url = "/open/ic/humanholding/2.0"
        self._params = {
            "id": 22822,
            "name": "北京百度网讯科技有限公司",
            "keyword": "北京百度网讯科技有限公司",
            "pageNum": 1,
            "pageSize": 20,
            'debug': 'true'
        }
        return self.api_send()

    def id_747(self, name):
        self._api_name = name
        self._url = "/v4/open/companyholding"
        self._params = {
            "id": 22822,
            "name": "北京百度网讯科技有限公司",
            "keyword": "北京百度网讯科技有限公司",
            "pageNum": 1,
            "pageSize": 20,
            'debug': 'true'
        }
        return self.api_send()

    def id_1028(self, name):
        self._api_name = name
        self._url = "/open/ic/actualControl/2.0"
        self._params = {
            "id": 22822,
            "name": "北京百度网讯科技有限公司",
            "keyword": "北京百度网讯科技有限公司",
            'debug': 'true'
        }
        return self.api_send()

    def id_1044(self, name):
        self._api_name = name
        self._url = "/open/rela/shortPath"
        self._params = {
            "nameFrom": "北京百度网讯科技有限公司",
            "idFrom": 22822,
            "nameTo": "北京百度智行科技有限公司",
            "idTo": 3043827609,
            "depth": 3,
            "types": "ALL",
            'debug': 'true'
        }
        return self.api_send()

    # 增值服务
    def id_1058(self, name):
        self._api_name = name
        self._url = "/open/risk/riskInfo/2.0"
        self._params = {
            "id": 22822,
            "name": "北京百度网讯科技有限公司",
            "keyword": "北京百度网讯科技有限公司",
            'debug': 'true'
        }
        return self.api_send()

    def id_943(self, name):
        self._api_name = name
        self._url = "/open/ps/news/2.0"
        self._params = {
            "id": 22822,
            "name": "北京百度网讯科技有限公司",
            "startTime": 20191020,
            "endTime": 20191022,
            "pageNum": 1,
            "pageSize": 20,
            "tags": "债务抵押,经营业务",
            'debug': 'true'
        }
        return self.api_send()

    def id_630(self, name):
        self._api_name = name
        self._url = "/v4/open/proximity"
        self._params = {
            "pageNum": 1,
            "pageSize": 10,
            "distance": 10,
            "longtitude": 116,
            "latitude": 40,
            "regStatus": "在业",
            'debug': 'true'
        }
        return self.api_send()

    def id_427(self, name):
        self._api_name = name
        self._url = "/v4/open/humanRiskInfo"
        self._params = {
            "name": "北京百度网讯科技有限公司",
            "humanName": "梁志祥",
            "cid": 22822,
            "hid": 2020172991,
            'debug': 'true'
        }
        return self.api_send()

    def id_426(self, name):
        self._api_name = name
        self._url = "/v4/open/riskDetail"
        self._params = {
            "id": 104176702,
            "pageSize": 5,
            "pageNum": 1,
            "type": 8,
            'debug': 'true'
        }
        return self.api_send()

    def id_632(self, name):
        self._api_name = name
        self._url = "/v4/open/logo"
        self._params = {
            "id": 22822,
            "name": "北京百度网讯科技有限公司",
            "keyword": "北京百度网讯科技有限公司",
            'debug': 'true'
        }
        return self.api_send()

    def id_633(self, name):
        self._api_name = name
        self._url = "/v4/open/match"
        self._params = {
            "name": "北京百度网讯科技有限公司",
            "keyword": "北京百度网讯科技有限公司",
            'debug': 'true'
        }
        return self.api_send()

    def id_778(self, name):
        self._api_name = name
        self._url = "/v4/open/position"
        self._params = {
            "id": 2069,
            "name": "北京正方向汽车租赁有限公司",
            "keyword": "北京正方向汽车租赁有限公司",
            'debug': 'true'
        }
        return self.api_send()

    def id_458(self, name):
        self._api_name = name
        self._url = "/v4/open/historyNames"
        self._params = {
            "id": 696122112,
            "name": "贵州荷泰集团酒业有限公司",
            "keyword": "贵州荷泰集团酒业有限公司",
            'debug': 'true'
        }
        return self.api_send()

    def id_457(self, name):
        self._api_name = name
        self._url = "/v4/open/taxesCode"
        self._params = {
            "id": 22822,
            "name": "北京百度网讯科技有限公司",
            "keyword": "北京百度网讯科技有限公司",
            'debug': 'true'
        }
        return self.api_send()

    def id_776(self, name):
        self._api_name = name
        self._url = "/v4/open/searchV3"
        self._params = {
            "word": "百度",
            "pageNum": 1,
            "categoryGuobiao": 759,
            "areaCode": 110108,
            'debug': 'true'
        }
        return self.api_send()

    def id_755(self, name):
        self._api_name = name
        self._url = "/v4/open/profile"
        self._params = {
            "id": 22822,
            # "name": "北京百度网讯科技有限公司",
            # "keyword": "北京百度网讯科技有限公司",
            'debug': 'true'
        }
        return self.api_send()

    # 集团族群
    def id_1105(self, name):
        self._api_name = name
        self._url = "/open/group/base"
        self._params = {
            "keyword": "北京百度网讯科技有限公司",
            'debug': 'true'
        }
        return self.api_send()

    def id_1106(self, name):
        self._api_name = name
        self._url = "/open/group/base/details"
        self._params = {
            "uuid": "21711e8f83a24df483a949313ad66299",
            'debug': 'true'
        }
        return self.api_send()

    def id_1107(self, name):
        self._api_name = name
        self._url = "/open/group/member"
        self._params = {
            "uuid": "21711e8f83a24df483a949313ad66299",
            "type": "1",
            "pageNum": "1",
            "pageSize": "20",
            'debug': 'true'
        }
        return self.api_send()

    def id_1108(self, name):
        self._api_name = name
        self._url = "/open/group/investors"
        self._params = {
            "uuid": "21711e8f83a24df483a949313ad66299",
            "pageNum": "1",
            "pageSize": "20",
            'debug': 'true'
        }
        return self.api_send()

    def id_1109(self, name):
        self._api_name = name
        self._url = "/open/group/investorMember"
        self._params = {
            "uuid": "21711e8f83a24df483a949313ad66299",
            "id": 3410303988,
            "pageNum": "1",
            "pageSize": "20",
            'debug': 'true'
        }
        return self.api_send()

    def id_1110(self, name):
        self._api_name = name
        self._url = "/open/group/shareholders"
        self._params = {
            "uuid": "21711e8f83a24df483a949313ad66299",
            "pageNum": "1",
            "pageSize": "20",
            'debug': 'true'
        }
        return self.api_send()

    def id_1111(self, name):
        self._api_name = name
        self._url = "/open/group/shareholdersMember"
        self._params = {
            "uuid": "21711e8f83a24df483a949313ad66299",
            "id": 22822,
            "pageNum": "1",
            "pageSize": "20",
            'debug': 'true'
        }
        return self.api_send()

    # 报告服务
    def id_1034(self, name):
        self._api_name = name
        self._url = "/open/report/company/base"
        self._params = {
            "id": 3069334211,
            "name": "北京天眼查科技有限公司",
            "uuid": "929dd1191cb511e6b554008cfae40dc0",
            'debug': 'true'
        }
        return self.api_send()

    def id_1035(self, name):
        self._api_name = name
        self._url = "/open/report/company/pro"
        self._params = {
            "id": 3069334211,
            "name": "北京天眼查科技有限公司",
            "uuid": "929dd1191cb511e6b554008cfae40dc0",
            'debug': 'true'
        }
        return self.api_send()

    # 组合接口
    def id_1001(self, name):
        self._api_name = name
        self._url = "/open/cb/ic/2.0"
        self._params = {
            "id": 3355627294,
            "name": "全维度测试有限责任公司",
            "keyword": "全维度测试有限责任公司",
            'debug': 'true'
        }
        return self.api_send()

    def id_1002(self, name):
        self._api_name = name
        self._url = "/open/cb/judicial/2.0"
        self._params = {
            "id": 22822,
            "name": "北京百度网讯科技有限公司",
            "keyword": "北京百度网讯科技有限公司",
            'debug': 'true'
        }
        return self.api_send()

    def id_1003(self, name):
        self._api_name = name
        self._url = "/open/cb/ipr/2.0"
        self._params = {
            "id": 3355627294,
            "name": "全维度测试有限责任公司",
            "keyword": "全维度测试有限责任公司",
            'debug': 'true'
        }
        return self.api_send()

    def id_1004(self, name):
        self._api_name = name
        self._url = "/open/cb/development/2.0"
        self._params = {
            "id": 22822,
            "name": "北京百度网讯科技有限公司",
            "keyword": "北京百度网讯科技有限公司",
            'debug': 'true'
        }
        return self.api_send()

    def id_1005(self, name):
        self._api_name = name
        self._url = "/open/cb/history/2.0"
        self._params = {
            "id": 22822,
            "name": "北京百度网讯科技有限公司",
            "keyword": "北京百度网讯科技有限公司",
            'debug': 'true'
        }
        return self.api_send()

    # 企业发展
    def id_799(self, name):
        self._api_name = name
        self._url = "/v4/open/investEvent"
        self._params = {
            "name": "百度资本",
            "pageNum": 1,
            "pageSize": 20,
            'debug': 'true'
        }
        return self.api_send()

    def id_826(self, name):
        self._api_name = name
        self._url = "/open/cd/findHistoryRongzi/2.0"
        self._params = {
            "id": 22822,
            "name": "北京百度网讯科技有限公司",
            "keyword": "北京百度网讯科技有限公司",
            "pageNum": 1,
            "pageSize": 20,
            'debug': 'true'
        }
        return self.api_send()

    def id_827(self, name):
        self._api_name = name
        self._url = "/open/cd/findTeamMember/2.0"
        self._params = {
            "id": 3355627294,
            "name": "全维度测试有限责任公司",
            "keyword": "全维度测试有限责任公司",
            "pageNum": 1,
            "pageSize": 20,
            'debug': 'true'
        }
        return self.api_send()

    def id_828(self, name):
        self._api_name = name
        self._url = "/open/cd/getProductInfo/2.0"
        self._params = {
            "id": 3355627294,
            "name": "全维度测试有限责任公司",
            "keyword": "全维度测试有限责任公司",
            "pageNum": 1,
            "pageSize": 20,
            'debug': 'true'
        }
        return self.api_send()

    def id_829(self, name):
        self._api_name = name
        self._url = "/open/cd/findTzanli/2.0"
        self._params = {
            "id": 3355627294,
            "name": "全维度测试有限责任公司",
            "keyword": "全维度测试有限责任公司",
            "pageNum": 1,
            "pageSize": 20,
            'debug': 'true'
        }
        return self.api_send()

    def id_830(self, name):
        self._api_name = name
        self._url = "/open/cd/findJingpin/2.0"
        self._params = {
            "id": 3355627294,
            "name": "全维度测试有限责任公司",
            "keyword": "全维度测试有限责任公司",
            "pageNum": 1,
            "pageSize": 20,
            'debug': 'true'
        }
        return self.api_send()

    def id_831(self, name):
        self._api_name = name
        self._url = "/open/cd/tags/2.0"
        self._params = {
            "id": "b6bc016381",
            'debug': 'true'
        }
        return self.api_send()

    def id_832(self, name):
        self._api_name = name
        self._url = "/open/cd/searchBrandAndAgency/2.0"
        self._params = {
            "word": "百度",
            'debug': 'true'
        }
        return self.api_send()

    def id_944(self, name):
        self._api_name = name
        self._url = "/open/cd/investOrg/2.0"
        self._params = {
            "id": 22822,
            "name": "北京百度网讯科技有限公司",
            "keyword": "北京百度网讯科技有限公司",
            "pageNum": 1,
            "pageSize": 20,
            'debug': 'true'
        }
        return self.api_send()

    def id_954(self, name):
        self._api_name = name
        self._url = "/open/cd/privateFund/2.0"
        self._params = {
            "id": 1067465196,
            "name": "湖南汇垠天星股权投资私募基金管理有限公司",
            "keyword": "9143010532070930XC",
            "pageNum": 1,
            "pageSize": 20,
            'debug': 'true'
        }
        return self.api_send()

    # 上市信息
    def id_1075(self, name):
        self._api_name = name
        self._url = "/open/stock/list"
        self._params = {
            "keyword": "深圳市振业（集团）股份有限公司",
            "pageNum": 1,
            "pageSize": 20,
            'debug': 'true'
        }
        return self.api_send()

    def id_798(self, name):
        self._api_name = name
        self._url = "/v4/open/financialAnalysis"
        self._params = {
            "id": 199557844,
            "name": "平安银行股份有限公司",
            "keyword": "平安银行股份有限公司",
            'debug': 'true'
        }
        return self.api_send()

    def id_853(self, name):
        self._api_name = name
        self._url = "/open/stock/volatility/2.0"
        self._params = {
            "id": 199557844,
            "name": "平安银行股份有限公司",
            "keyword": "平安银行股份有限公司",
            'debug': 'true'
        }
        return self.api_send()

    def id_854(self, name):
        self._api_name = name
        self._url = "/open/stock/companyInfo/2.0"
        self._params = {
            "id": 485568977,
            "name": "深圳市振业（集团）股份有限公司",
            "keyword": "深圳市振业（集团）股份有限公司",
            'debug': 'true'
        }
        return self.api_send()

    def id_855(self, name):
        self._api_name = name
        self._url = "/open/stock/seniorExecutive/2.0"
        self._params = {
            "id": 485568977,
            "name": "深圳市振业（集团）股份有限公司",
            "keyword": "深圳市振业（集团）股份有限公司",
            "pageNum": 1,
            "pageSize": 10,
            'debug': 'true'
        }
        return self.api_send()

    def id_856(self, name):
        self._api_name = name
        self._url = "/open/stock/holdingCompany/2.0"
        self._params = {
            "id": 485568977,
            "name": "深圳市振业（集团）股份有限公司",
            "keyword": "深圳市振业（集团）股份有限公司",
            "pageNum": 1,
            "pageSize": 10,
            'debug': 'true'
        }
        return self.api_send()

    def id_857(self, name):
        self._api_name = name
        self._url = "/open/stock/announcement/2.0"
        self._params = {
            "id": 485568977,
            "name": "深圳市振业（集团）股份有限公司",
            "keyword": "深圳市振业（集团）股份有限公司",
            "pageNum": 1,
            "pageSize": 10,
            'debug': 'true'
        }
        return self.api_send()

    def id_859(self, name):
        self._api_name = name
        self._url = "/open/stock/shareholder/2.0"
        self._params = {
            "id": 485568977,
            "name": "深圳市振业（集团）股份有限公司",
            "keyword": 485568977,
            "type": 1,
            "time": "2020-03-31",
            'debug': 'true'
        }
        return self.api_send()

    def id_860(self, name):
        self._api_name = name
        self._url = "/open/stock/issueRelated/2.0"
        self._params = {
            "id": 485568977,
            "name": "深圳市振业（集团）股份有限公司",
            "keyword": "深圳市振业（集团）股份有限公司",
            'debug': 'true'
        }
        return self.api_send()

    def id_861(self, name):
        self._api_name = name
        self._url = "/open/stock/shareStructure/2.0"
        self._params = {
            "id": 485568977,
            "name": "深圳市振业（集团）股份有限公司",
            "keyword": "深圳市振业（集团）股份有限公司",
            "time": "2019-06-30",
            'debug': 'true'
        }
        return self.api_send()

    def id_862(self, name):
        self._api_name = name
        self._url = "/open/stock/equityChange/2.0"
        self._params = {
            "id": 485568977,
            "name": "深圳市振业（集团）股份有限公司",
            "keyword": "深圳市振业（集团）股份有限公司",
            "pageNum": 1,
            "pageSize": 10,
            'debug': 'true'
        }
        return self.api_send()

    def id_863(self, name):
        self._api_name = name
        self._url = "/open/stock/bonusInfo/2.0"
        self._params = {
            "id": 485568977,
            "name": "深圳市振业（集团）股份有限公司",
            "keyword": "深圳市振业（集团）股份有限公司",
            "pageNum": 1,
            "pageSize": 10,
            'debug': 'true'
        }
        return self.api_send()

    def id_864(self, name):
        self._api_name = name
        self._url = "/open/stock/allotmen/2.0"
        self._params = {
            "id": 485568977,
            "name": "深圳市振业（集团）股份有限公司",
            "keyword": "深圳市振业（集团）股份有限公司",
            "pageNum": 1,
            "pageSize": 10,
            'debug': 'true'
        }
        return self.api_send()

    def id_964(self, name):
        self._api_name = name
        self._url = "/open/stock/security/2.0"
        self._params = {
            "id": 18709573,
            "name": "广发证券股份有限公司",
            "keyword": "广发证券股份有限公司",
            'debug': 'true'
        }
        return self.api_send()

    def id_965(self, name):
        self._api_name = name
        self._url = "/open/stock/corpBasicInfo/2.0"
        self._params = {
            "id": 18709573,
            "name": "广发证券股份有限公司",
            "keyword": "广发证券股份有限公司",
            'debug': 'true'
        }
        return self.api_send()

    def id_966(self, name):
        self._api_name = name
        self._url = "/open/stock/corpContactInfo/2.0"
        self._params = {
            "id": 18709573,
            "name": "广发证券股份有限公司",
            "keyword": "广发证券股份有限公司",
            'debug': 'true'
        }
        return self.api_send()

    def id_967(self, name):
        self._api_name = name
        self._url = "/open/stock/mainIndex/2.0"
        self._params = {
            "id": 7996092,
            "name": "厦门安妮股份有限公司",
            "keyword": "厦门安妮股份有限公司",
            'debug': 'true'
        }
        return self.api_send()

    def id_968(self, name):
        self._api_name = name
        self._url = "/open/stock/quarMainIndex/2.0"
        self._params = {
            "id": 90583569,
            "name": "山西兰花科技创业股份有限公司",
            "keyword": "山西兰花科技创业股份有限公司",
            'debug': 'true'
        }
        return self.api_send()

    def id_969(self, name):
        self._api_name = name
        self._url = "/open/stock/guarantees/2.0"
        self._params = {
            "id": 7996092,
            "name": "厦门安妮股份有限公司",
            "keyword": "厦门安妮股份有限公司",
            "pageNum": 1,
            "pageSize": 20,
            'debug': 'true'
        }
        return self.api_send()

    def id_970(self, name):
        self._api_name = name
        self._url = "/open/stock/illegal/2.0"
        self._params = {
            "id": 7996092,
            "name": "厦门安妮股份有限公司",
            "keyword": "厦门安妮股份有限公司",
            "pageNum": 1,
            "pageSize": 20,
            'debug': 'true'
        }
        return self.api_send()

    def id_971(self, name):
        self._api_name = name
        self._url = "/open/stock/profit/2.0"
        self._params = {
            "id": 7996092,
            "name": "厦门安妮股份有限公司",
            "keyword": "厦门安妮股份有限公司",
            'debug': 'true'
        }
        return self.api_send()

    def id_972(self, name):
        self._api_name = name
        self._url = "/open/stock/balanceSheet/2.0"
        self._params = {
            "id": 7996092,
            "name": "厦门安妮股份有限公司",
            "keyword": "厦门安妮股份有限公司",
            'debug': 'true'
        }
        return self.api_send()

    def id_973(self, name):
        self._api_name = name
        self._url = "/open/stock/cashFlow/2.0"
        self._params = {
            "id": 7996092,
            "name": "厦门安妮股份有限公司",
            "keyword": "厦门安妮股份有限公司",
            "year": 2018,
            'debug': 'true'
        }
        return self.api_send()

    def id_999(self, name):
        self._api_name = name
        self._url = "/open/stock/prospectus/2.0"
        self._params = {
            "id": 18709573,
            "name": "广发证券股份有限公司",
            "keyword": "广发证券股份有限公司",
            'debug': 'true'
        }
        return self.api_send()

    # 投资机构
    def id_978(self, name):
        self._api_name = name
        self._url = "/open/oi/businessEvent/2.0"
        self._params = {
            "name": "百度投资并购部",
            "pageNum": 1,
            "pageSize": 20,
            'debug': 'true'
        }
        return self.api_send()

    def id_979(self, name):
        self._api_name = name
        self._url = "/open/oi/news/2.0"
        self._params = {
            "name": "百度投资并购部",
            "pageNum": 1,
            "pageSize": 20,
            'debug': 'true'
        }
        return self.api_send()

    def id_980(self, name):
        self._api_name = name
        self._url = "/open/oi/team/2.0"
        self._params = {
            "name": "百度投资并购部",
            "pageNum": 1,
            "pageSize": 20,
            'debug': 'true'
        }
        return self.api_send()

    def id_981(self, name):
        self._api_name = name
        self._url = "/open/oi/publicInvest/2.0"
        self._params = {
            "name": "百度投资并购部",
            "pageNum": 1,
            "pageSize": 20,
            'debug': 'true'
        }
        return self.api_send()

    def id_982(self, name):
        self._api_name = name
        self._url = "/open/oi/secretInvest/2.0"
        self._params = {
            "name": "百度投资并购部",
            "pageNum": 1,
            "pageSize": 20,
            'debug': 'true'
        }
        return self.api_send()

    def id_983(self, name):
        self._api_name = name
        self._url = "/open/oi/funds/2.0"
        self._params = {
            "name": "百度投资并购部",
            "pageNum": 1,
            "pageSize": 20,
            'debug': 'true'
        }
        return self.api_send()

    def id_984(self, name):
        self._api_name = name
        self._url = "/open/oi/extFunds/2.0"
        self._params = {
            "name": "百度投资并购部",
            "pageNum": 1,
            "pageSize": 20,
            'debug': 'true'
        }
        return self.api_send()

    def id_985(self, name):
        self._api_name = name
        self._url = "/open/oi/fundManager/2.0"
        self._params = {
            "name": "红杉资本中国",
            "pageNum": 1,
            "pageSize": 20,
            'debug': 'true'
        }
        return self.api_send()

    def id_986(self, name):
        self._api_name = name
        self._url = "/open/oi/investEvent/2.0"
        self._params = {
            "name": "百度投资并购部",
            "pageNum": 1,
            "pageSize": 20,
            'debug': 'true'
        }
        return self.api_send()

    def id_987(self, name):
        self._api_name = name
        self._url = "/open/oi/stats/2.0"
        self._params = {
            "name": "百度投资并购部",
            "year": 2019,
            'debug': 'true'
        }
        return self.api_send()

    # 私募基金
    def id_988(self, name):
        self._api_name = name
        self._url = "/open/pf/orgInfo/2.0"
        self._params = {
            "id": 2322352210,
            "name": "新疆中科援疆创新创业私募基金管理有限公司",
            "keyword": "新疆中科援疆创新创业私募基金管理有限公司",
            'debug': 'true'
        }
        return self.api_send()

    def id_989(self, name):
        self._api_name = name
        self._url = "/open/pf/member/2.0"
        self._params = {
            "id": 2322352210,
            "name": "新疆中科援疆创新创业私募基金管理有限公司",
            "keyword": "新疆中科援疆创新创业私募基金管理有限公司",
            'debug': 'true'
        }
        return self.api_send()

    def id_990(self, name):
        self._api_name = name
        self._url = "/open/pf/legalOpinion/2.0"
        self._params = {
            "id": 2322352210,
            "name": "新疆中科援疆创新创业私募基金管理有限公司",
            "keyword": "新疆中科援疆创新创业私募基金管理有限公司",
            'debug': 'true'
        }
        return self.api_send()

    def id_991(self, name):
        self._api_name = name
        self._url = "/open/pf/boss/2.0"
        self._params = {
            "id": 2322352210,
            "name": "新疆中科援疆创新创业私募基金管理有限公司",
            "keyword": "新疆中科援疆创新创业私募基金管理有限公司",
            'debug': 'true'
        }
        return self.api_send()

    def id_992(self, name):
        self._api_name = name
        self._url = "/open/pf/staff/2.0"
        self._params = {
            "id": 2322352210,
            "name": "新疆中科援疆创新创业私募基金管理有限公司",
            "keyword": "新疆中科援疆创新创业私募基金管理有限公司",
            'debug': 'true'
        }
        return self.api_send()

    def id_993(self, name):
        self._api_name = name
        self._url = "/open/pf/product/2.0"
        self._params = {
            "id": 3176771149,
            "name": "厦门壹舟星辰投资管理有限公司",
            "keyword": "厦门壹舟星辰投资管理有限公司",
            'debug': 'true'
        }
        return self.api_send()

    def id_994(self, name):
        self._api_name = name
        self._url = "/open/pf/integrity/2.0"
        self._params = {
            "id": 2322352210,
            "name": "新疆中科援疆创新创业私募基金管理有限公司",
            "keyword": "新疆中科援疆创新创业私募基金管理有限公司",
            'debug': 'true'
        }
        return self.api_send()

    # 建筑资质
    def id_1030(self, name):
        self._api_name = name
        self._url = "/open/bq/badConduct/2.0"
        self._params = {
            "id": 491463287,
            "name": "郑州久鼎路桥工程有限公司",
            "keyword": "郑州久鼎路桥工程有限公司",
            "pageNum": 1,
            "pageSize": 20,
            'debug': 'true'
        }
        return self.api_send()

    def id_1007(self, name):
        self._api_name = name
        self._url = "/open/bq/qualification/2.0"
        self._params = {
            "id": 3355627294,
            "name": "全维度测试有限责任公司",
            "keyword": "全维度测试有限责任公司",
            "pageNum": 1,
            "pageSize": 20,
            'debug': 'true'
        }
        return self.api_send()

    def id_1008(self, name):
        self._api_name = name
        self._url = "/open/bq/qualification/detail/2.0"
        self._params = {
            "businessId": "5d5a553befe14117624e96cc-D123456789",
            'debug': 'true'
        }
        return self.api_send()

    def id_1009(self, name):
        self._api_name = name
        self._url = "/open/bq/regHuman/2.0"
        self._params = {
            "id": 3355627294,
            "name": "全维度测试有限责任公司",
            "keyword": "全维度测试有限责任公司",
            "pageNum": 1,
            "pageSize": 20,
            'debug': 'true'
        }
        return self.api_send()

    def id_1010(self, name):
        self._api_name = name
        self._url = "/open/bq/regHuman/detail/2.0"
        self._params = {
            "businessId": "5d5a4e48efe14117624e96c8",
            'debug': 'true'
        }
        return self.api_send()

    def id_1011(self, name):
        self._api_name = name
        self._url = "/open/bq/project/2.0"
        self._params = {
            "id": 3355627294,
            "name": "全维度测试有限责任公司",
            "keyword": "全维度测试有限责任公司",
            "pageNum": 1,
            "pageSize": 20,
            'debug': 'true'
        }
        return self.api_send()

    def id_1012(self, name):
        self._api_name = name
        self._url = "/open/bq/project/detail/2.0"
        self._params = {
            "businessId": "5d5a4fe7efe14117624e96ca",
            "pageNum": 1,
            "pageSize": 20,
            'debug': 'true'
        }
        return self.api_send()

    # 搜索
    def id_816(self, name):
        self._api_name = name
        self._url = "/open/search/2.0"
        self._params = {
            "word": "北京百度网讯科技有限公司",
            'debug': 'true'
        }
        return self.api_send()

    def id_353(self, name):
        self._api_name = name
        self._url = "/v4/open/searchV2"
        self._params = {
            "word": "北京百度网讯科技有限公司",
            'debug': 'true'
        }
        return self.api_send()

    # 人员风险
    def id_1076(self, name):
        self._api_name = name
        self._url = "/v4/open/human/dishonest"
        self._params = {
            "name": "北京百乐文化传媒有限公司",
            "humanName": "贾跃亭",
            "hid": 2187083120,
            "cid": 34630712,
            "pageNum": 1,
            "pageSize": 20,
            'debug': 'true'
        }
        return self.api_send()

    def id_1077(self, name):
        self._api_name = name
        self._url = "/v4/open/human/zhixinginfo"
        self._params = {
            "name": "北京百乐文化传媒有限公司",
            "humanName": "贾跃亭",
            "hid": 2187083120,
            "cid": 34630712,
            "pageNum": 1,
            "pageSize": 20,
            'debug': 'true'
        }
        return self.api_send()

    def id_1078(self, name):
        self._api_name = name
        self._url = "/v4/open/human/consumptionRestriction"
        self._params = {
            "name": "北京百乐文化传媒有限公司",
            "humanName": "贾跃亭",
            "hid": 2187083120,
            "cid": 34630712,
            "pageNum": 1,
            "pageSize": 20,
            'debug': 'true'
        }
        return self.api_send()

    def id_1079(self, name):
        self._api_name = name
        self._url = "/v4/open/human/judicialAssistance"
        self._params = {
            "name": "北京百乐文化传媒有限公司",
            "humanName": "贾跃亭",
            "hid": 2187083120,
            "cid": 34630712,
            "pageNum": 1,
            "pageSize": 20,
            'debug': 'true'
        }
        return self.api_send()

    def id_1080(self, name):
        self._api_name = name
        self._url = "/v4/open/human/judicialAssistanceDetail"
        self._params = {
            "assistanceId": "c37116808216",
            'debug': 'true'
        }
        return self.api_send()

    def id_1081(self, name):
        self._api_name = name
        self._url = "/v4/open/human/endCase"
        self._params = {
            "name": "北京百乐文化传媒有限公司",
            "humanName": "贾跃亭",
            "hid": 2187083120,
            "cid": 34630712,
            "pageNum": 1,
            "pageSize": 20,
            'debug': 'true'
        }
        return self.api_send()

    def id_1101(self, name):
        self._api_name = name
        self._url = "/open/hi/human/dishonest"
        self._params = {
            "hid": 2187083120,
            "name": "北京百乐文化传媒有限公司",
            "humanName": "贾跃亭",
            "cid": 34630712,
            "pageSize": "20",
            "pageNum": "1",
            'debug': 'true'
        }
        return self.api_send()

    def id_1102(self, name):
        self._api_name = name
        self._url = "/open/hi/human/zhixinginfo"
        self._params = {
            "hid": 2187083120,
            "name": "北京百乐文化传媒有限公司",
            "humanName": "贾跃亭",
            "cid": 34630712,
            "pageSize": "20",
            "pageNum": "1",
            'debug': 'true'
        }
        return self.api_send()

    def id_1103(self, name):
        self._api_name = name
        self._url = "/open/hi/human/consumptionRestriction"
        self._params = {
            "hid": 2187083120,
            "name": "北京百乐文化传媒有限公司",
            "humanName": "贾跃亭",
            "cid": 34630712,
            "pageSize": "20",
            "pageNum": "1",
            'debug': 'true'
        }
        return self.api_send()

# xpath = "//*[@placeholder='请输入账号']"
# dev.find_element_by_xpath(xpath).send_keys('王杨')
#
# dev.find_element_by_xpath("//*[@placeholder='请输入登录密码']").send_keys('888888')
# dev.find_element_by_xpath("//*[@placeholder='请输入图片验证码']").send_keys('888888')




# url = 'http://cstd.test63.tianyancha.com/home'


dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
dict2 = {'a': 1, 'b': 2, 'c': 5, 'e': 6}

differ = set(dict1.items()) ^ set(dict2.items())
print(differ)
# 所有差异
# 输出:{('c', 3), ('e', 6), ('c', 5), ('d', 4)}
diff = dict1.keys() & dict2

diff_vals = [(k, dict1[k], dict2[k]) for k in diff if dict1[k] != dict2[k]]
print(diff_vals)
# 相同key，不同value
# 输出:[('c', 3, 5)]
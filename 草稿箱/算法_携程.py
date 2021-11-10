

def cut(s: str):#提取所有子串
    results = []
    # x + 1 表示子字符串长度
    for x in range(len(s)):
        # i 表示偏移量
        for i in range(len(s) - x):
            results.append(s[i:i + x + 1])
    return results

def func(S):#判断①大于3个字符-false②首尾字符相等-true③其他-false
    if len(S) < 3:
        return False
    if S[0] == S[-1]:
        return True
    else:
        return False

def func2(S):#遍历所有子串,并拼装预期结果
    r_list = cut(S)

    res_f = []

    for i in r_list:  # 遍历进行判断
        if func(i):
            res_f.append(i)

    # print(res_f)
    for i in range(len(res_f)):  # 拼装结果
        t = f'{i}.    {res_f[i]}    {len(res_f[i])-2}'
        print(t)

# =====================
s = 'abccdca'
func2(s)
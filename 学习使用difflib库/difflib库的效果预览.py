#coding:utf-8

import difflib
hd = difflib.HtmlDiff()#新建一个"对比"对象

#打开文件C.TXT
loads = ''
with open('c.txt', 'r') as load:
    loads = load.readlines()
    load.close()

# 打开文件D.TXT
mems = ''
with open('d.txt', 'r') as mem:
    mems = mem.readlines()
    mem.close()

# 比对,并生成差异报告
with open('htmlout.html', 'w') as fo:
    fo.write(hd.make_file(loads,mems))
    fo.close()

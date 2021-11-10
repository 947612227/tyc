# orient ='dict'，是函数默认的，转化后的字典形式：{column(列名) : {index(行名) : value(值) )}}；
# orient ='list' ，转化后的字典形式：{column(列名) :{[ values ](值)}};
# orient ='series' ，转化后的字典形式：{column(列名) : Series (values) (值)};
# orient ='split' ，转化后的字典形式：{'index' : [index]，‘columns' :[columns]，’data‘ : [values]};
# orient ='records' ，转化后是 list形式：[{column(列名) : value(值)}......{column:value}];
# orient ='index' ，转化后的字典形式：{index(值) : {column(列名) : value(值)}};

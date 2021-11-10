from deepdiff import DeepDiff


from deepdiff import DeepDiff

t1 = {'a': 10, 'b': 20}#第一个对比的数据
t2 = {'a': 10, 'b': 22}#第二个对比的数据

ddiff = DeepDiff(t1, t2, ignore_order=True)
print(ddiff.pretty())

dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
dict2 = {'a': 1, 'b': 2, 'c': 5, 'e': 6}
ddiff = DeepDiff(dict1, dict2, ignore_order=True)
print(ddiff.pretty())
print(ddiff.to_dict())

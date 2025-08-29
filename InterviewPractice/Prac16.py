# Dictorny

dict1 = {'a': 1, 'b':2}
dict2 = {'b': 3, 'c':4}
dict3 = {'a': 5, 'd':6}

result = dict1 | dict2 | dict3

print(result['b'], result['c'])
a = frozenset({1,2})
b = frozenset({'a','b'})
c = a|b
print(c)
'''
In python, you can combine two frozen sets using the
union operator '|' and it will produce a new frozenSet.
* The order of the elements is not guarranteed in sets,
So your answer might contain the same elements but in a
different order here.
'''
a = [1,2,3]
b = a[:]
print(a is b, a == b)

/*
a[:] creates a new list object
is checks object identity -> False
== checks value -> True

*/
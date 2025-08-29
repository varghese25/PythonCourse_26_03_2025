def f(x):
    return x * 2
result = f(3)
result *= f(4)
print(result)


"""
-> f(3)   2*2*2 = 8
-> f(4) 2*2*2*2 = 16 
         -----
          x= 24


x= 24 * 2, copies two times  24 + 24 =  Output:48

"""
a = [10,11] * 2 
a[1] = (11)*2
print(a)


"""
Explanation:

Step 1: List repetition :
 a = [10, 11] * 2
-> [10, 11] * 2 means repeat the list two times.
-> So a = [10, 11, 10, 11].

Step 2: Update an element :
a[1] = (11) * 2
-> a[1] is the second element of the list (Python uses 0-based index).
-> Currently, a = [10, 11, 10, 11], so a[1] = 11.
-> (11) * 2 = 22
-> So now a = [10, 22, 10, 11].

Step 3: Print :
print(a) -> Output: [10, 22, 10, 11]
-------------------------------------------------------------------------
Inshort:
* 2 on a list repeats it.
a[1] = 11*2 replaces the second element with 22.


"""
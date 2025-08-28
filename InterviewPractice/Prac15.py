#Slice Notation

my_list =[1,2,3,4,5]
print(my_list[::2]) # list[start:stop:step]


"""
start → where to begin (default is 0, the first element).

stop → where to end (default is the end of the list).

step → how many elements to skip each time (default is 1).




Applying [::2]

start → not given → so it starts from index 0.

stop → not given → so it goes until the end of the list.

step = 2 → means "take every second element."


Step-by-step

my_list = [1, 2, 3, 4, 5]


 0   1   2   3   4
[1,  2,  3,  4,  5]


Start at index 0 → value 1

Skip 1 → index 2 → value 3

Skip 1 → index 4 → value 5


Output:
[1, 3, 5]




"""
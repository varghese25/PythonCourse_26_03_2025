# Append

myList_Append =[1,2,3,4,5]
myList_Append.append(6)
print('Append:',myList_Append)


#extend
myList_Extend =[1,2,3,4,5]
myList_Extend.extend([6,7])
print('Extend:',myList_Extend)

#insert
myList_insert = [1,2,3,4,5]
myList_insert.insert(2,10)
print('Insert:',myList_insert)

#remove
myList_remove = [1,2,3,4,5]
myList_remove.remove(3)
print('Remove:', myList_remove)

#pop
myList_pop = [1,2,3,4,5]
myList_pop.pop(0) #removes the first element (index 0) 1 removed Zero-based indexing
print('Pop:', myList_pop)

#index
myList_index = [1,2,3,4,5]
myList_index.index(4)
print('Index:',myList_index.index(4)) # Output: 3 (the index of the first occurrence of 4)

"""
1 → index 0

2 → index 1

3 → index 2

4 → index 3 ✅

5 → index 4"""

#Count
myList_Count = [1,2,3,3,4,5]
myList_Count.count(3)
print('Count:',myList_Count.count(3)) # Output: 2 (the number of occurrences of 3)

#sort
myList_Sort = [1,5,3,4,2]
myList_Sort.sort()
print('Sort:',myList_Sort) # Arrages the list in ascending order

#reverse
myList_reverse = [5,4,3,2,1]
myList_reverse.reverse()
print('Reverse:',myList_reverse) # Reverses the order of the list

#clear
myList_Clear = [1,2,3,4,5]
myList_Clear.clear()
print('Clear:',myList_Clear) # Output: an empty list []

#copy
myList_Copy = [1,2,3,4,5]
myList_Copy2 = myList_Copy.copy()
print('Original:',myList_Copy)
print('Copy:',myList_Copy2) 


#sort(reverse=True)
myList_Sort_Reverse = [1,2,3,4,5]
myList_Sort_Reverse.sort(reverse=True)
print('Sort Reverse:', myList_Sort_Reverse) # Arranges the list in descending order

# len
myList_Len = [1,2,3,4,5]
print('Length:', len(myList_Len))

#min() and max()
myList_min = [1,2,3,4,5]
print('Min:', min(myList_min)) # Output: 1
print('Max:', max(myList_min)) # Output: 5


#sum()
myList_sum = [1,2,3,4,5]
print('Sum:', sum(myList_sum)) # Output: 15 (the sum of all elements in the list)


# List Slicing
myList_Slicing = [1,2,3,4,5]
print('Slicing:', myList_Slicing[1:4]) # Output: [2, 3, 4] (elements from index 1 to 3)

"""
list[start : stop]

Start index is INCLUDED
Stop index is EXCLUDED



| Index | Value |
| ----- | ----- |
| 0     | 1     |
| 1     | 2     |
| 2     | 3     |
| 3     | 4     |
| 4     | 5     |


myList_Slicing[1:4]
Start from index 1 ✅ (value = 2)

Index 1 → 2

Index 2 → 3

Index 3 → 4 


OutPut
[2, 3, 4]
"""

#List Comprehension (Advanced but powerful)
myList_Comprehension = [1,2,3,4,5]
squared = [x**2 for x in myList_Comprehension]
print('Squared:', squared) # Output: [1, 4, 9, 16, 25] (squares of each element in the list)

"""
| x | x**2 |
| - | ---- |
| 1 | 1    |
| 2 | 4    |
| 3 | 9    |
| 4 | 16   |
| 5 | 25   |
"""
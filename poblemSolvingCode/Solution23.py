# print()
# print()
# print()


# # one-linear to reverse string in python 
# # Example: reversed_string = your_string[::-1]

# x=5
# print(f"Number:(x)")
# # f-String substitute x with its value 5.

# text = "hello"
# print(text.replace("l","p"))

# #Output : ??


# print(any[0,'',False,[]])
# #output: False

# print()
# print(23)
# print(danjo)



#=====================================#
# s = "abcdef"
# print(s[::2])

"""
Step 3: Let’s walk through the string

Start at index 0:

1️⃣ take letter at index 0 → “a”
👣 move 2 steps ahead → next index is 2

2️⃣ take letter at index 2 → “c”
👣 move 2 steps ahead → next index is 4

3️⃣ take letter at index 4 → “e”
👣 move 2 steps ahead → next index is 6 (but string ends at 5)

Stop.

✅ Collected letters: a, c, e

👉 Output: "ace"""


# s = "Developer"
# print(s[-3:])


#=====================================#


a = [1,2,3]
b = ['x','y','z']
print(list(zip(a,b)))

#zip() pairs elements from both lists based on Thier positions.

# Output:(1,'x'),(2,'y'),(3,'z')




# for x in range(1,7):
#     if x % 2 ==0:
#         continue
#  print(x)


for i in range(1,11):
        if i == 4:
            continue
        if i == 8:
            break
        print(i, end = ' ')





*x,y=1,2
print(x,y)

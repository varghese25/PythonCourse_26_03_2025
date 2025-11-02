# a, *b, c='Python'
# print(a,b,c)

# *_,='Python'# unpacks all characters into a list
# print()

# header, *body, footer = 'VarghesE'
# print(header,body,footer)


# *all_chars, = 'Python'
# print(all_chars) # unpacks all characters into a list



# response = ['OK', 200, 'Success', 'Data received']
# status, code, *message = response
# print(status, code, message)
#OK 200 ['Success', 'Data received']

# 
# Unpacking with Loops or Conditions

# records = [
#     ('Tom', 28, 'Developer'),
#     ('Sarah', 31, 'Designer'),
#     ('Raj', 26, 'Tester'),
# ]

# for name, *details in records:
#     print(name, details)


    # Output:    # Tom [28, 'Developer']
    # Sarah [31, 'Designer']



for i in range(10, 0, -3):
 print(i)
 """range(start, stop, step)
 
 
 
 start = 10

stop = 0 (exclusive) → don’t go below 0

step = -3 (decreasing)



"""
# a, *b, c='Python'
# print(a,b,c)

# *_,='Python'# unpacks all characters into a list
# print()

# header, *body, footer = 'VarghesE'
# print(header,body,footer)


*all_chars, = 'Python'
print(all_chars) # unpacks all characters into a list



response = ['OK', 200, 'Success', 'Data received']
status, code, *message = response
print(status, code, message)
#OK 200 ['Success', 'Data received']
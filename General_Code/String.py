# Day 1
#method, Function - performs a specified task

message = 'happbirthday'
name = " Varghese"
quote = '"peace"'


print(name)
print(quote)
print(name.upper()) # print is Function & upper() is a method
print(name.lower()) # dot (.upper()) invoking a method


print(message.title())
print(message +  name)


msg = message + name


#escape sequence
print("hello \n world")
print("hello \t varghese")

print(len(message)) # find length
print(message.find("h")) # index of h is Zero , .find method name
print(message.find("#")) # -1 does't have any character
print(message.count("a")) # 2
print(message.replace('a','v')) # replace v

print(message.isalpha()) # message = 'hvpp birthdvy' OutPut False because in between space
print(message.isalpha()) # message = 'hvppbirthdvy' outPut True because removed space isalpha means alphabet


print(message.isdigit()) # message is not digit
print(message *  5) # print 5 times happy birthday



'''
Multiple Assignment '''


# below  we can write single line
name = 'varghese'
age = 38
height = 177


name, age, height = "varghese", 38, 178
print(name, age, height)
print(age)


like = dislike = 100
print(like)
# print("like " + str(like))








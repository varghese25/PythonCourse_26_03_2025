pwd_correct = False

if pwd_correct: #conditional stmt
    print("Logged In")
    print("Have a Nice Day")
else:
    print("Incorrect Pwd")
    print("Try Again")

print("Bye")




# Releation Operator
# num = 20
num = int(input("enter the number: "))
if num % 10 == 0:
    print(str(num) + " is a multiple of 10")
else:
    print(str(num) + " is not a multiple of 10")


# Else If Ladder
ind_score = 360

if ind_score >= 350:
   print("India will win")
elif ind_score >=250:
    print("India might win")
elif ind_score >=150:
    print("Aus might win")
else:
    print("Aus will win")

print("Congrts")


#nested if
#check if the given num is a three digit even number
#logical operators - and or not

num = int(input("enter a num: "))

if num > 99 and num < 1000:
    if num % 2 == 0:
     print(str(num) + " is a three digit even number")
else:
    print(str(num) +  " is not a three digit even number")

'''
Truth Table
a b  a and b   a or b 
t t     t         t 
t f     f         t
f t     f         t
f f     f         f

not
t  f
f  t'''

name = "Varghese"
if name[0] == 'V' or name[0] == 'v':
 print("the name starts with v")



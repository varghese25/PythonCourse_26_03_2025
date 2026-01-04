# Day 1
#Data Type - str, int, float, boolean

otp = 25121986
print("your otp is " + str (otp))

cvv = 123
print("Your CVV number is " + str(cvv))

print(type(otp)) # is <class 'int'>
print(type(cvv)) # is <class 'int'>

number = 5485774624
number = str(number) # Type Casting , I changed number to string
print("your Mobile " + number)
print(type(number))



#Type Casting
count = "20"
print(int(count)+1) # out Put is 21. . Temporly int for count and then add 1 if i remove int it will 201.

count = "20.5"
print(float(count)+1) # Output is 21.5



count = "20.5"
print(int(float(count)+1)) # Output count+1 float = 21.5 and finally it convert to int 21







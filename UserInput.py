#Day 1
name = input("What is your name: ")
print("Hello " + name)

height = float(input("What is your height: ")) # here typCasting from str to float
print(type(height)) #<class 'str'> height is string

print("Your are " + str(height) + "cm") # error occured in height cause we used typCasting in this line we have to change to string
print("Your are " + str(height/2.54) + "inches tall" )
# cont from 56.09
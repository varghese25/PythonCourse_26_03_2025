#Day 1
name = input("What is your name: ")
print("Hello " + name)

height = float(input("What is your height: ")) # here typCasting from str to float
# print(type(height)) #<class 'str'> height is string
height_inches = "{:.2f}".format(height/2.54) # syntax {:.}for format
print("Your are " + str(height) + "cm") # error occured in height cause we used typCasting in this line we have to change to string
print("Your are " + height_inches + "inches tall" )
# cont from 56.09



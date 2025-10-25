#equivalutnt to 'r' or 'rt'

# f = open ("test.txt")

# #write in text mode
# f = open ("test.txt",'w')

# #read and write in binary mode
# f = open ("img.bmp",'r+b')



# Exception handling

# Import module sys to get the type of exception
import sys #importing sys module to access exception info
randomList =['a',0,2] # list with different entries, 
for entry in randomList:
    try:
        print("The entry is",entry)
        r = 1/int(entry)
        break
    except:
        print("Oops!",sys.exc_info()[0],"occurred.")
        print("Next entry.")
        print() # print a blank line
print("The reciprocal of",entry,"is",r) # Inside except → error, because r never gets created when an exception happens.

# Outside except (after loop) → works, because eventually r gets created in a later successful iteration.



# --- IGNORE ---#
# Directory operations
# import os
# os.mkdir("newdir") # create a directory
# os.chdir("newdir") # change current working directory
# os.rmdir("newdir") # remove a directory



print("-+++++++++++++-")

https://github.com/LegendofKARTIS


print("-+++++++++++++-")



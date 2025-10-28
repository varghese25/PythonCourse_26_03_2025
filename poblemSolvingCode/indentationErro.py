



# Missing Indentation Error I
# if True:
# print("Hello") # this line should be indented to be part of if block, So will give indentation error.


# Unexpected Indentation Error II
# print("Hello")
#    print("World") # this line has unexpected indentation, So will give indentation error.



# Incorrect, Indentation Error III

# x =10
# if x < 5:
#     print("Hello") # this belongs to if block
#     print("Hi") # This is not  belong to if block this should be indented. So it will not show outPut




# Automatic Indentation Enable in Vscode 
# Setting -> format on type Editor On Type
# Below Code Checked in vscode with above setting enabled

def do_things(x):
    if x == 1:
        print(0)
    elif x ==2:
         print(1)
    else:
        print(2)
# tree       Heigth is 6 
#       * -> 1
#      *** -> 2
#     ***** -> 3 
#    *******  -> 4
#   ********* -> 5
#  ***********  -> 6   width is 11
#       *
# height is 6
# 6 *2 = 12 - 1 = 11 width of the tree
def tree(height):
    length = height * 2 - 1 # total width of the tree (max stars in the bottom row)
    stars = 1 # start with 1 star at the top
    for i in range(1, height + 1):  # loop through tree height
        print(("*" * stars).center(length)) # print stars, centered
        stars += 2  # increase stars by 2 each row (1, 3, 5, …)

         # Print the trunk (just 1 star, centered)
    print("*".center(length))

tree(9)  # Add this line to call the function
# ref: https://www.youtube.com/shorts/SGD7k-8i0Mw
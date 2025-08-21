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
    length = height * 2 - 1
    stars = 1
    for i in range(1, height + 1):
        print(("*" * stars).center(length))
        stars += 2
    print("*".center(length))

tree(9)  # Add this line to call the function
# ref: https://www.youtube.com/shorts/SGD7k-8i0Mw
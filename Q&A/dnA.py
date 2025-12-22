a = 7
repeate = 3

for z in range(repeate):
    for i in range(a):
        for j in range(a):
            if i == j or i + j == a - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
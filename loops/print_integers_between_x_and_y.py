"""
Algorithm: print all integer numbers between x and y
Author: Novo
Course: Loop structures (Python)
"""

print("Algorithm to print all integer numbers between x and y")

# input
x = int(input("Input the x value: "))
y = int(input("Input the y value: "))

# process and output
if x == y:
    print("X and Y have the same value. Please choose different values.")
elif abs(x - y) == 1:
    print("There are no integer numbers between x and y.")
else:
    if x < y:
        while x < y - 1:
            x = x + 1
            print(x)
    else:
        while x > y + 1:
            x = x - 1
            print(x)

print("End")



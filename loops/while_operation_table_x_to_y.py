"""
Algorithm: print the operation table for x until y using while loops
Author: Novo
Course: Loop structures (Python)
"""

print("Operation table for x until y using while loops")

# input
op_signal = input("Input the operation symbol (+, -, *, /): ")
x = float(input("Input the x value: "))
y = int(input("Input the y value: "))
z = 0
k = 0

# process and output
if op_signal not in ('+', '*', '-', '/'):
    print("Input a valid operation symbol.")
elif y <= 0:
    print("y must be greater than 0.")
else:
    if op_signal == '+':
        while z < y:
            z = z + 1
            k = x + z
            print(f"{x} + {z} == {k}")
    elif op_signal == '-':
        while z < y:
            z = z + 1
            k = x - z
            print(f"{x} - {z} == {k}")
    elif op_signal == '*':
        while z < y:
            z = z + 1
            k = x * z
            print(f"{x} * {z} == {k:f}")
    elif op_signal == '/':
        while z < y:
            z = z + 1
            k = x / z
            print(f"{x} / {z} == {k:f}")

print("End")

        

    
    


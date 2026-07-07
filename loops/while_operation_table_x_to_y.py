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
    while z < y:
        z += 1
        if op_signal == '+':
            k = x + z
        elif op_signal == '-':
            k = x - z
        elif op_signal == '*':
            k = x * z
        elif op_signal == '/':
            k = x / z
        print(f"{x} {op_signal} {z} == {k:.6f}")

print("End")

        

    
    


"""
Algorithm: print the operation table for x up to y using loops
Author: Novo
Course: Loop structures (Python)
"""

print("Operation table for x up to y using loops")

# input
op_signal = input("Enter operation symbol (+, -, *, /): ").strip()
try:
    x = float(input("Enter the x value: ").strip())
except ValueError:
    print("Invalid x value. Must be a number.")
    raise SystemExit(1)
try:
    y = int(input("Enter the y value (positive integer): ").strip())
except ValueError:
    print("Invalid y value. Must be an integer.")
    raise SystemExit(1)

# process and output
if op_signal not in ('+', '-', '*', '/'):
    print("Input a valid operation symbol.")
elif y <= 0:
    print("y must be greater than 0.")
else:
    z = 0
    while z < y:
        z += 1
        if op_signal == '+':
            k = x + z
        elif op_signal == '-':
            k = x - z
        elif op_signal == '*':
            k = x * z
        else:  # '/'
            k = x / z

        # show integer x without decimal point when appropriate
        x_str = str(int(x)) if float(x).is_integer() else str(x)
        print(f"{x_str} {op_signal} {z} = {k:.6f}")

print("End")

        

    
    


"""
Algorithm to calculate +, -, * and / operations with two values
Author: Novo
Course: conditional structures (python)
"""

print("Algorithm to calculate +, -, * and / operations with two values")

# input
operation = input("Input the sign of operation: addition (+), subtraction (-), division (/), multiplication (*): ")
a = float(input("Input the first value: "))
b = float(input("Input the last value: "))
final = 0

# process and output
if operation not in ('+', '-', '*', '/'):
    print("Invalid symbol. Use +, -, * or /")
elif operation == '/' and b == 0:
    print("An error (division by zero)")
else:
    if operation == '+':
        final = a + b
    elif operation == '-':
        final = a - b
    elif operation == '*':
        final = a * b
    else:
        final = a / b
        
    print(f"The final result is {final}")
"""
Algorithm to calculate the highest and lowest value
Author: Novo
Course: conditional-structures (python)
"""
print("Algorithm to calculate the highest and lowest value")

# input
a = float(input("Input the first value: "))
b = float(input("Input the second value: "))
c = float(input("Input the third value: "))

# values
d = 0
e = 0
high = 0
low = 0

# process and output
if b == a == c:
    print(f"{a}, {b}, {c} have the same values.")
else:
    if a > b:
        d = a
    else:
        d = b

    if d == a:
        e = b
    else:
        e = a

    if c > d:
        high = c   
    else:
        high = d

    if e < c:
        low = e
    else:
        low = c

    print(f"So the highest value is {high} and the lowest is {low}")
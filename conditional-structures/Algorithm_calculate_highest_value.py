"""
Algorithm: calculate which is the highest value
Author: Novo
Course: Conditional structures (Python)
"""

print("Algorithm to calculate which is the highest value")

#input 
a = float(input("Input the first value: "))
b = float(input("Input the second value: "))

#output
if a>b:
    print(f"The highest value is {a}")
elif a==b:
    print("You input the same values, please input different values")
else:
    print(f"The highest value is {b}")

#end
print("end")
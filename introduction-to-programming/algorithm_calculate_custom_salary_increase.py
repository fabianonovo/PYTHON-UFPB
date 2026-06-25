"""
Algorithm to calculate salary increase
Author: Novo
course: conditional-structures (python)
"""
print("Algorithm to calculate salary increase")

#input
salary = float(input("Input how much your earn per month: "))
increase = float(input("Input the percentege increase 'NUMBERS - ONLY': "))

#process and output
salary = salary + (increase * salary) * 0.01
print(f"This is your new salary ${salary}")
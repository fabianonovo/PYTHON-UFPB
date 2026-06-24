"""
Algorithm to calculate tax
Author: Novo
course: conditional-structures (python)
"""

print("Algorithm to calculate tax")

#input
base = float(input("input how much you earn per month: "))
tax = 0.0

#process and output
if base > 3000:
    tax = tax + (base - 1000) * 0.30
elif 1000 < base <= 3000:
    tax = tax + (base - 1000) * 0.20
print(f"you were chargede {tax}$ in taxes")
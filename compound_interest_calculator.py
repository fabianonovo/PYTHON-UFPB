"""
Algorithm: compound interest calculator
Author: Novo
"""

print("Compound interest calculator")

# input
valor = float(input("Enter the principal amount: "))
juros = float(input("Enter the interest rate (percentage): "))
tempo = int(input("Enter the number of months: "))
z = 0

# process and output
while z < tempo:
    z += 1
    formula_Juros = (1 + juros / 100) ** z
    valor *= formula_Juros
    valorinicial = valor / formula_Juros

    print(f"These are your results after {z} month(s)")
    print(f"Total accumulated amount: {valor:.2f}")
    print(f"Total interest earned: {valor - valorinicial:.2f}")

    valor = valorinicial

print("End")

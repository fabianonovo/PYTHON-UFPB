"""
Algorithm to calculate the price charged per trip
Author: NOVO
Couse: conditional structures (PYTHON)
"""
print("Algorithm to calculate the price charged per trip")

#input
km = float(input("Input the total distance: "))
price_km = 0

#process and output
if km <= 0:
    print("Invalid value")
else:
    if km <= 200:
        price_km = 0.50 * km
    else:
        price_km = 0.45 * km
    
    print(f"You will be charged ${price_km:.2f}")

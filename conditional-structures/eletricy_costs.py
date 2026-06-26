"""
Algorithm to calculate the electricity charge for a company.
Author: Novo
Course: Conditional structures (PYTHON)
"""
print("Electricity charge calculator")

# input
KWH = float(input("Enter how many kWh you used this month: "))
instalation_type = int(input("Enter the installation type: (1) residence, (2) market, (3) factory: "))
price = 0

# process and output
if instalation_type not in (1, 2, 3):
    print("Invalid installation type.")
elif KWH <= 0:
    print("kWh must be greater than 0. Please enter a valid value.")
elif instalation_type == 1 and KWH <= 500:
    price = 0.40 * KWH
elif instalation_type == 1:
    price = 0.60 * KWH
elif instalation_type == 2 and KWH <= 1000:
    price = 0.55 * KWH
elif instalation_type == 3 and KWH <= 5000:
    price = 0.55 * KWH
else:
    price = 0.60 * KWH

if price > 0:
    print(f"You were charged ${price:.2f}")


    
        

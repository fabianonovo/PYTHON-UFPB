"""
Algorithm: calculate the electricity bill for a company
Author: Novo
Course: Conditional structures (Python)
"""

print("Electricity charge calculator")

# input
kwh = float(input("Enter how many kWh you used this month: "))
installation_type = int(input("Enter the installation type: (1) residence, (2) market, (3) factory: "))
price = 0

# process and output
if installation_type not in (1, 2, 3):
    print("Invalid installation type.")
elif kwh <= 0:
    print("kWh must be greater than 0. Please enter a valid value.")
elif installation_type == 1 and kwh <= 500:
    price = 0.40 * kwh
elif installation_type == 1:
    price = 0.60 * kwh
elif installation_type == 2 and kwh <= 1000:
    price = 0.55 * kwh
elif installation_type == 3 and kwh <= 5000:
    price = 0.55 * kwh
else:
    price = 0.60 * kwh

if price > 0:
    print(f"You were charged ${price:.2f}")


    
        

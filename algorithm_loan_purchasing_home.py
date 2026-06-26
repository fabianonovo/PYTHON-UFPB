"""
Algorithm to approve a bank loan for purchasing a house
author: fabiano novo guedes
course: conditional structures (python)
"""
print("Algorithm to approve a bank loan for purchasing a house")

house_price = float(input("Enter the house price (numbers only): "))
salary = float(input("Enter how much you earn per year: "))
years_to_pay = float(input("Enter how many years you plan to repay the house: "))
monthly_payment = 0

# process and output
if salary * 1/3 < house_price / years_to_pay:
    print("You are not eligible for that number of installments")
elif house_price <= 0 or salary <= 0 or years_to_pay <= 0:
    print("Please enter a valid value")
else:
    months = years_to_pay * 12
    monthly_payment = house_price / months
    print(f"This is the monthly amount you will be charged: ${monthly_payment:.2f}")
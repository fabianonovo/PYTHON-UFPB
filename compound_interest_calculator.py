"""
Algorithm: compound interest calculator
Author: Novo
"""

print("Compound interest calculator")

# input
principal = float(input("Enter the principal amount: "))
interest_rate = float(input("Enter the interest rate (percentage): "))
months = int(input("Enter the number of months: "))
month = 0

# process and output
while month < months:
    month += 1
    interest_factor = (1 + interest_rate / 100) ** month
    principal *= interest_factor
    initial_amount = principal / interest_factor

    print(f"These are your results after {month} month(s)")
    print(f"Total accumulated amount: {principal:.2f}")
    print(f"Total interest earned: {principal - initial_amount:.2f}")

    principal = initial_amount

print("End")

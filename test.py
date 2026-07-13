"""
Algorithm: compound interest calculator with monthly deposit
Author: Novo
"""

print("Compound interest calculator")

# input
principal = float(input("Enter the initial principal amount: "))
monthly_deposit = float(input("Enter the monthly deposit amount: "))
interest_rate = float(input("Enter the interest rate (percentage): "))
months = int(input("Enter the number of months: "))
month = 0

# process and output
while month < months:
    month += 1
    previous_balance = principal
    interest_factor = 1 + interest_rate / 100
    principal *= interest_factor
    principal += monthly_deposit

    print(f"These are your results after {month} month(s)")
    print(f"Total accumulated amount: {principal - monthly_deposit:.2f}$")
    print(
        f"Monthly interest earned: "
        f"{(principal - monthly_deposit) - previous_balance:.2f}$"
    )
    print(f"Monthly deposit amount: {monthly_deposit:.2f}$")
    print(
        "New balance after fixed deposit at the end of the month "
        f"({monthly_deposit:.2f}$): {principal:.2f}$"
    )
    print()

print("End")

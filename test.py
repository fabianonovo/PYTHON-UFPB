"""
Debt interest calculator over time
Author: Fabiano
Course: loops (Python)
"""

# input
debt = float(input("Enter the amount of your debt in '$': "))
interest_rate = float(
    input("Enter the monthly interest rate for the debt (percentage): ")
)
months = int(
    input("Enter the number of months you plan to pay the debt: ")
)
monthly_payment = float(
    input("Enter the amount you will pay monthly: ")
)

initial_debt = debt
month = 0
total_interest = 0.0
total_paid = 0.0

# process and output
while month < months and debt > 0:
    previous_debt = debt

    # apply monthly payment then interest (payment at start of period)
    debt -= monthly_payment
    interest = debt * (interest_rate / 100)
    debt += interest

    month += 1
    total_paid += monthly_payment
    total_interest += interest

    print(f"\n===== MONTH {month} =====")
    print(f"Starting debt:         {previous_debt:.2f}$")
    print(f"Monthly interest:      {interest:.2f}$")
    print(f"Debt after interest:   {previous_debt - monthly_payment + interest:.2f}$")
    print(f"Payment:              -{monthly_payment:.2f}$")
    print(f"Remaining debt:        {debt:.2f}$")

    if debt > initial_debt:
        print("WARNING: the debt is increasing.")

if debt <= 0:
    print("Congratulations! Your debt has been paid off.")
    print(f"Months used: {month}")
    print(f"Total paid: {total_paid:.2f}$")
    print(f"Total interest paid: {total_interest:.2f}$")
    print(f"Extra amount paid: {abs(debt):.2f}$")
else:
    print("The term ended and the debt was not paid off.")
    print(f"Remaining debt: {debt:.2f}$")
    print(f"Months used: {month}")
    print(f"Total paid: {total_paid:.2f}$")
    print(f"Total interest paid: {total_interest:.2f}$")
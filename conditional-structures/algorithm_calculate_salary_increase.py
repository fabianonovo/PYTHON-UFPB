"""
Algorithm to calculate the salary increase
Author: Novo
Course: Conditional-structures
"""
print("Algorithm to calculate the salary increase: ")

#input
salary = float(input("input how much you earn per month: "))
increase = 0

#process and output
if salary <= 0:
    print("please input a valid salary")
else:
    if salary >= 1250:
        increase = 0.10
    else: 
        increase = 0.15
        
    salary = salary + (salary * increase)
    print(f"Your new salary is {salary:.2f}")
    
    


"""
Algorithm to compare and show the maximum speed on the street, if speed >80kmh the driver will be fined 5$
Author: Novo
Course: Conditional Structures (python) -UFPB
"""

print("Algorithm to compare and show the maximum speed on the street")

#input
car_spd = int(input("input your car speed on the street 'kmh'- NUMBERS ONLY: "))

#processing and output
if car_spd>80:
    print(f"the max speed is 80kmh, you got {car_spd}. will be fined 5$")
elif car_spd<=0:
    print("input a valid speed")
else:
    print(f"the max speed is 80kmh, you got {car_spd}. will not be fined")

#end
print("end")






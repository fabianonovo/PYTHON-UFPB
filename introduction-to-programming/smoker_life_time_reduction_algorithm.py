#smoker_life_time_reduction_algorithm
#start
print("algorithm for calculating the reduction in a smokers lifespan")

#input
cperday = int(input("how many cigarettes you smoke every day?: "))
time_years = int(input("how many years you smoke on entire of your life?: "))

#processing/setup
cperday_lost_minutes = 10 * cperday
minutes_to_days = (60 * 24) ** -1
cperday_lost_days = minutes_to_days * cperday_lost_minutes
years_to_days = 365 * time_years
lifespan_lost_total = (cperday_lost_days * (years_to_days)) * -1

#output
print (f"you lost {lifespan_lost_total:.1f} days of lifespan")

#end
print("end")


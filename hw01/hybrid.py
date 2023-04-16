'''hybrid.py
Bode W
Homework 1 Problem Challenge

Calculate cost of a car if use for 5 years, based on cost, miles per year,
gas cost, fuel efficiency, and resale price after 5 year. 
'''
# Ask for user inputs
cost = float(input("Cost of car:"))
miles = float(input("Miles driven per year:"))
gas_cost = float(input("Cost of gas:"))
fuel_efficiency = float(input("Fuel efficiency (mpg):"))
resale_value = float(input("Estimated resale value after 5 years:"))

# calculate
gas_cost_5yr = 5 * (miles / fuel_efficiency) * gas_cost
car_cost_5yr = cost - resale_value

# Print output
print(f"""Five year gas cost: {gas_cost_5yr}
Five year car cost: {car_cost_5yr}
Five year total cost: {gas_cost_5yr + car_cost_5yr}""")

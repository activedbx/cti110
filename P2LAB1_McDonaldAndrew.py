# P2LAB1
# 10/01/2022
# CTI-110 - P2LAB1 - 8.13 LAB: Driving costs
# McDonald, Andrew
#
# Get input from input value box
# Calculates gas cost for 20, 75, and 500 miles
# print one line for each total gas cost per miles traveled with two digits after decimal
# 
# BEGIN

miles_per_gallon = float(input())
dollars_per_gallon = float(input())

miles_traveled_20 = 20 / miles_per_gallon * dollars_per_gallon
miles_traveled_75 = 75 / miles_per_gallon * dollars_per_gallon
miles_traveled_500 = 500 / miles_per_gallon * dollars_per_gallon

print(f'{miles_traveled_20:.2f} {miles_traveled_75:.2f} \
{miles_traveled_500:.2f}')

# END


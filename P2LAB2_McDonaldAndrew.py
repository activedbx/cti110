# P2LAB2
# 10/05/2022
# CTI-110 - P2LAB2 - 9.16 LAB: Simple statistics
# McDonald, Andrew

# Gets 4 numbers from input value box
# Calculates product
# Calculates average
# prints line for product and average as rounded integer
# prints line for product and average with 3 digits after decimal point

# BEGIN

num1 = float(input())
num2 = float(input())
num3 = float(input())
num4 = float(input())

product_output = num1 * num2 * num3 * num4
average_output = (num1 + num2 + num3 + num4) / 4

print(f'{product_output:.0f} {average_output:.0f}')
print(f'{product_output:.3f} {average_output:.3f}')

# END

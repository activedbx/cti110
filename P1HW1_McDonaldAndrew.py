#7.19.1: Lab: Warm up: Basic output with variables

# This will Display 'Enter Integer:', pull in input value,
# change it to interger and store in variable user_num
user_num = int(input('Enter integer:\n'))
# Note to self: initially subbed for grading with print(user_num) but realized that
# is not correct as it was only displayed for convenience.

# print variable
print('You entered:', user_num)

# print string/output and display user_num squared then cubed
print(user_num, 'squared is', user_num * user_num)
print('And', user_num, 'cubed is', user_num * user_num * user_num, '!!')

# This displays 'Enter another integer:' pull input value,
# change it to interger and store in variable user_num2
user_num2 = int(input('Enter another integer:\n'))
# Note to self: initially subbed for grading with print(user_num) but realized that
# is not correct as it was only displayed for convenience.

# print string/output and display equation with sum then product
print(user_num, '+', user_num2, 'is', user_num + user_num2)
print(user_num, '*', user_num2, 'is', user_num * user_num2)



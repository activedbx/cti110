# CTI-110-0901
# 11/08/22
# McDonald, Andrew
# P4LAB2 Output Range
# Obtain input for two numbers
# IF first number is less than second number
#     OUTPUT "Second integer can't be less than the first."
# ELSE
#     WHILE first number is greater or equal to second number
# OUTPUT increments of 5 from first num to second num
#
# Begin

first_num = int(input())
second_num = int(input())

if first_num > second_num:
    print("Second integer can't be less than the first.")
else:
    while first_num <= second_num:
        print(first_num, end=' ')
        first_num += 5
    print()
#
# END
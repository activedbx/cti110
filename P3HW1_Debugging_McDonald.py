#
# CTI-110 P3HW1 Debugging
# 10/25/2022
# McDonald, Andrew
# Debugging provided code

# PROMPT for module test scores
#    STORE scores in list
# CALCULATE grade average
# DISPLAY min, max, sum, average grade
#
# IF greater or equal to 90 then
#     DISPLAY letter grade A
# ELSE 
# IF greater or equal to 80 and less than or equal to 89.9
#     DISPLAY letter grade B
# ELSE
# IF greater or equal to 70 and less than or equal to 79.9
#     DISPLAY letter grade C
# ELSE
# IF greater or equal to 60 and less than or equal to 69.9
#     DISPLAY letter grade D
# ELSE
#     DISPLAY letter grade F
# ENDIF
#
#
# BEGIN

grades = []

print("Enter grade for Module 1:", end=' ')
mod_1 = float(input())
grades.append(mod_1)

print("Enter grade for Module 2:", end=' ')
mod_2 = float(input())
grades.append(mod_2)

print("Enter grade for Module 3:", end=' ')
mod_3 = float(input())
grades.append(mod_3)

print("Enter grade for Module 4:", end=' ')
mod_4 = float(input())
grades.append(mod_4)

print("Enter grade for Module 5:", end=' ')
mod_5 = float(input())
grades.append(mod_5)

print("Enter grade for Module 6:", end=' ')
mod_6 = float(input())
grades.append(mod_6)

avg = sum(grades) / len(grades)

print("\n------------Results------------")
print('Lowest Grade:','     ', min(grades))
print('Highest Grade:','    ', max(grades))
print('Sum of Grades:','    ', sum(grades))
print('Average:','          ', f'{avg:.2f}')
print("----------------------------------------")


if avg >= 90:
    print('Your grade is: A')
elif avg >= 80 and avg <= 89.9:
    print('Your grade is: B')
elif avg >= 70 and avg <= 79.9:
    print('Your grade is: C')
elif avg >= 60 and avg <= 69.9:
    print('Your grade is: D')
else:
    print('Your grade is: F')

#
# END



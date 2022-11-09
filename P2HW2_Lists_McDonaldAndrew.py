#
# CTI-110
# P2HW2 - List
# McDonald, Andrew
# 10/15/2022
#
# PROMPT for module test scores
#   STORE scores in list
# CALCULATE grade average
# DISPLAY min, max, sum, average grade
#

# BEGIN
#

all_grade_list = [ ]

print("Enter grade for Module 1:", end=' ')
grade_mod1 = float(input())
all_grade_list.append(grade_mod1)

print("Enter grade for Module 2:", end=' ')
grade_mod2 = float(input())
all_grade_list.append(grade_mod2)

print("Enter grade for Module 3:", end=' ')
grade_mod3 = float(input())
all_grade_list.append(grade_mod3)

print("Enter grade for Module 4:", end=' ')
grade_mod4 = float(input())
all_grade_list.append(grade_mod4)

print("Enter grade for Module 5:", end=' ')
grade_mod5 = float(input())
all_grade_list.append(grade_mod5)

print("Enter grade for Module 6:", end=' ')
grade_mod6 = float(input())
all_grade_list.append(grade_mod6)

grade_average = sum(all_grade_list) / len(all_grade_list)

print("\n------------Results------------")
print('Lowest Grade:','     ', min(all_grade_list))
print('Highest Grade:','    ', max(all_grade_list))
print('Sum of Grades:','    ', sum(all_grade_list))
print('Average:','          ', f'{grade_average:.2f}')
print("----------------------------------------")

#
# END

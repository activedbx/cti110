# CTI-110
# P3HW2 - Salary
# McDonald, Andrew
# 10/29/2022
#
# PROMPT for name, hours worked, & pay rate
#     STORE variables
#
# DISPLAY employee name
#
# IF hours worked are greater than 40
#     CALCULATE over time hours
#     CALCULATE over time, regular, & gross pay
# ELSE hours worked are less than or equal to 40
#     CALCULATE reg pay
#     SET gross pay as regular pay
#     SET ot hours and pay to 0
# ENDIF
#
# DISPLAY hours, rate, OT, OT pay,
# DISPLAY $ symbol with reg pay, gross pay.
#
#
#
#BEGIN
#

print("Enter employee's name:", end=' ')
emp_name = input()

print("Enter number of hours worked:", end=' ')
hours_worked = float(input())

print("Enter employee's pay rate:", end=' ')
pay_rate = float(input())

print("-------------------------------------")
print('Employee name:',' ',emp_name)

if hours_worked > 40:
    ot_hours = (hours_worked - 40)
    ot_pay = (ot_hours * pay_rate * 1.5)
    reg_pay = (40 * pay_rate)
    gross_pay = (reg_pay + ot_pay)
else:
    hours_worked <= 40
    reg_pay = (hours_worked * pay_rate)
    gross_pay = reg_pay
    ot_hours = 0
    ot_pay = 0

print("{:<16}{:<12}{:<12}{:<20}{:<20}{:<19}".format\
      ("\nHours Worked", "Pay Rate", "OverTime", \
       "OverTime Pay", "RegHour Pay", "Gross Pay"))

print("------------------------------------------------------\
--------------------------------------------")

print("{:<15.1f}{:<12.1f}{:<12.1f}{:<20.2f}${:<20.2f}${:<11.2f}".format\
      (hours_worked, pay_rate, ot_hours, ot_pay, reg_pay, gross_pay))
#
#
#END
#


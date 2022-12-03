#
# CTI-110
# P4HW2 - Salary Calculator
# McDonald, Andrew
# 11/14/2022
#
# SET employee count, total OT, regular, and gross pay variables starting at 0
#
# WHILE loop until done adding requested employee info or None is entered
#  PROMPT and DISPLAY text for name or None
#  STORE variables
#     IF name is None end loop
#     ELSE COMPUTE employee count as increment + 1

#  PROMPT and DISPLAY text for hours worked, & pay rate
#  STORE variables

#  SET ot hours, ot pay, reg, and gross pay variables starting at 0

#     IF hours worked are greater than 40
#         CALCULATE over time hours
#         CALCULATE over time, regular, & gross pay
#     ELSE hours worked are less than or equal to 40
#         CALCULATE reg pay
#         SET gross pay as regular pay

#  DISPLAY employee name
#  DISPLAY hours, rate, OT, OT pay,
#  DISPLAY $ symbol with reg pay, gross pay.     

# END WHILE loop if None is entered

# DISPLAY number of employee's entered, total ot, reg, and gross pay
# DISPLAY # symbol with total ot, reg, gross
#

# BEGIN Salary Calculator Program
#

emp_count = 0
total_all_ot = 0
total_reg_pay = 0
total_gross_pay = 0

while(True):

    emp_name = input("Enter employee's name or \"None\" to terminate: ")

    if emp_name == "None":
        break
    else:                        
        emp_count += 1

    hours_worked = float(input("How many hours did " + emp_name + " worked? "))
    pay_rate = float(input("What is " + emp_name + " pay rate? "))

    ot_hours = 0
    ot_pay = 0
    reg_pay = 0
    gross_pay = 0

    if hours_worked > 40:
        ot_hours = (hours_worked - 40)
        ot_pay = (ot_hours * pay_rate * 1.5)
        reg_pay = (40 * pay_rate)
        gross_pay = (reg_pay + ot_pay)
    else:
        hours_worked <= 40
        reg_pay = (hours_worked * pay_rate)
        gross_pay = reg_pay

    total_all_ot += ot_pay
    total_reg_pay += reg_pay
    total_gross_pay += gross_pay
    
    print("\nEmployee name: " + emp_name)

    print("{:<16}{:<12}{:<12}{:<20}{:<20}{:<19}".format\
      ("\nHours Worked", "Pay Rate", "OverTime", \
       "OverTime Pay", "RegHour Pay", "Gross Pay"))

    print("------------------------------------------------------\
--------------------------------------------")

    print("{:<15.1f}{:<12.1f}{:<12.1f}{:<20.2f}${:<20.2f}${:<11.2f}".format\
        (hours_worked, pay_rate, ot_hours, ot_pay, reg_pay, gross_pay))
    print()

print()
print("Total number of employees entered:" + '{:0.0f}'.format(emp_count))
print("Total amount payed for overtime: $" + '{:.2f}'.format(total_all_ot))
print("Total amount payed for regular hours: $" + '{:.2f}'.format(total_reg_pay))
print("Total amount payed in gross: $" + '{:.2f}'.format(total_gross_pay))


# End Salaray Calculator Program
#
#




# My NOTE
# original way I did print string with user input for my reference
# print("Enter employee's name or \"None\" to terminate:", end=' ')
# emp_name = input()


# still would like to replace break with condition statement
# my pseudocode is too detailed

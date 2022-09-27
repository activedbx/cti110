# P1HW2 Using IDLE to create and test code learned.
# 09/23/2022
# CTI-110- P1HW2 - Travel Expense
# McDonald, Andrew
#
# BEGIN

# Displays print string for program title.
print("\nThis program calculates and displays travel expenses")

# Ask user to enter their total budget
# Displays print string with User_Budget input value
# User input value stored in variable User_Budget
# Convert/float User_Budget to display with single decimal place
print("\nEnter Budget:", end=' ')
User_Budget = input()
User_Budget = float(User_Budget)

# Ask user to enter travel destination
# Displays print string with user Travel_Location input value
# User input value stored in variable Travel_Location
print("\nEnter your travel destination:", end=' ')
Travel_Location = input()

# Ask user for amount they will spend on gas
# Displays print string with user Gas_Expense input value
# User input value stored in variable Gas_Expense
# Convert/float Gas_Expense to display with single decimal place
print("\nHow much do you think you will spend on gas?", end=' ')
Gas_Expense = input()
Gas_Expense = float(Gas_Expense)

# Ask user for amount they will spend on accomodation
# Displays print string with user Accom_Expense input value
# User input value stored in variable Accom_Expense
# Convert/float Accom_Expense to display with single decimal place
print("\nApproximatley, how much will you need for \
accomodation/hotel?", end=' ')
Accom_Expense = input()
Accom_Expense = float(Accom_Expense)

# Ask user for amount they will spend on food
# Displays print string with user Food_Expense input value
# User input value stored in variable Food_Expense
# Convert/float Food_Expense to display with single decimal place
print("\nLast, how much do you need for food?", end=' ')
Food_Expense = input()
Food_Expense = float(Food_Expense)     

# Add Gas_Expense, Accom_Expense, and Food_Expense
# sum stored in variable Total_Expenses as float value
Total_Expenses = float(Gas_Expense) + float(Accom_Expense) + float(Food_Expense)

# Subtract variable Total_Expenses from User_Budget
# Difference is stored in variable Remaining_Balance as float value
Remaining_Balance = float(User_Budget) - float(Total_Expenses)
 
# Display Results
# print string with title for displayed results
# print string with stored user input/float variable Travel_Location
# print string with stored user input/float variable User_Budget
# print string with stored user input/float variable Gas_Expense
# print string with stored user input/float variable Accom_Expense
# print string with stored user input/float variable Food_Expense
# print string with stored float variable Remaining_Balance
print("\n------------Travel Expenses------------")
print('Location:', Travel_Location)
print('Initial Budget:', User_Budget)
print('\nFuel:', Gas_Expense)
print('Accomodation:', Accom_Expense)
print('Food:', Food_Expense)
print('\nRemaining Balance:', Remaining_Balance)

# END

# Travel Expense part 2
# 10/10/2022
# CTI-110 P2HW1 - Travel
# McDonald, Andrew
#
# Print program title
# User enters budget, destination, and how much
#   they need for gas, hotel, and food.
# Print requested info with label and user input
# Input converted to float showing decimal place
# Calculate sum of total expenses
# Calculate difference of expense out of total budget
# Convert floats to strings
# Combine $ with variables
# Align variable output
# Print travel expense results
# 
# Begin

print("\nThis program calculates and displays travel expenses")

print("\nEnter Budget:", end=' ')
User_Budget = float(input())

print("\nEnter your travel destination:", end=' ')
Travel_Location = input()

print("\nHow much do you think you will spend on gas?", end=' ')
Gas_Expense = float(input())

print("\nApproximatley, how much will you need for \
accomodation/hotel?", end=' ')
Accom_Expense = float(input())

print("\nLast, how much do you need for food?", end=' ')
Food_Expense = float(input())
 
Total_Expenses = Gas_Expense + Accom_Expense + Food_Expense
Remaining_Balance = User_Budget - Total_Expenses

print("\n------------Travel Expenses------------")
print('Location:','         ', Travel_Location)
User_Budget = str(float(User_Budget))
User_Budget = '$' + User_Budget
print('Initial Budget:','   ', User_Budget)
Gas_Expense = str(float(Gas_Expense))
Gas_Expense = '$' + Gas_Expense
print('Fuel:','             ', Gas_Expense)
Accom_Expense = str(float(Accom_Expense))
Accom_Expense = '$' + Accom_Expense
print('Accomodation:','     ', Accom_Expense)
Food_Expense = str(float(Food_Expense))
Food_Expense = '$' + Food_Expense
print('Food:','             ', Food_Expense)
print("---------------------------------------")
Remaining_Balance = str(float(Remaining_Balance))
Remaining_Balance = '$' + Remaining_Balance
print('\nRemaining Balance:','', Remaining_Balance)

#
#end



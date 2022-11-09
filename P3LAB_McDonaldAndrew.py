# CTI-110 LAB 10.19 Zybooks Leap Year
# 10/19/2022
# McDonald, Andrew
# Calculating Leap Year based on Gregorian Calender

# OBTAIN year input
# IF century year THEN
#   must be divisible by 400 to be leap
# IF evenly divisible by 4 it is leap year.
#     DISPLAY year - leap year
# ELSE is not a leap year
#     DISPLAY year - is not a leap year      
# ENDIF
# 

# BEGIN

is_leap_year = False
   
input_year = int(input())
    
if((input_year % 400 == 0) or 
    (input_year % 100 != 0) and  
    (input_year % 4 == 0)):
    print(input_year, "- leap year")

else:
    print(input_year, "- not a leap year")

# END

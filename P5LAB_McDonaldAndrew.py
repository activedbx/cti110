# CTI-110 LAB 12.23.1: Zybooks Leap Year - functions
# 11/23/2022
# McDonald, Andrew
# Calculating leap year day in February

# define call function
# IF century year THEN
#   must be divisible by 400
# IF not century year
#   must be evenly divisible by 4
# return 29 else return 28
# OBTAIN user input for year
# DISPLAY year/days in Feb result
#
#
# BEGIN
#

def days_in_feb(user_year):

    if((user_year % 400 == 0) or 
    (user_year % 100 != 0) and  
    (user_year % 4 == 0)):
        return '29'
    else:
        return '28'
        
if __name__ == '__main__':
    user_input = int(input())
    days_print = days_in_feb(user_input)
    print(f'{user_input} has {days_print} days in February.')

# END
#
#

## When I run the program with various year inputs
## individually it seems to be calculating properly
## although when I run in submit mode it is having issues.
## I was unable to figure out what I am doing wrong, or what the problem is.

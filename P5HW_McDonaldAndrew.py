# Using import random to generate addition or substraction equations
# 11/28/2022
# CTI-110 P5HW2 - Math Quiz
# McDonald, Andrew
#
# import random
# define adding and subtracting for random integers
# if answer is too low display too low
# if answer is too high display too high
# prompt user to try again
# record count of guesses
# when correct display congrats and guess count
# if option 3 is selected exit program
# if option 4 or greater display invalid selection

#
# BEGIN
#

import random

def add_random():
    num_one = random.randint(0,100)
    num_two = random.randint(0,100)
    print(f'{num_one:>4}')
    print(f'+{num_two:>3}')
    print('\nEnter answer.')      
    answer_ent = int(input())
    add_guess_count = 1

    while answer_ent != num_one + num_two:
        
        if answer_ent < num_one + num_two:
            print("Sorry, guess is too low.\n")
            add_guess_count += 1
        else:
            add_guess_count += 1
            print("Sorry, guess is too high.\n")
        answer_ent = int(input('try again: '))
        
    print("Congratulations!!!! your answer is correct..")
    print('Number of guesses:',add_guess_count,'\n')

def sub_random():
    num_one = random.randint(0,100)
    num_two = random.randint(0,100)
    print(f'{num_one:>4}')
    print(f'-{num_two:>3}')
    print('\nEnter answer.')
    answer_ent = int(input())
    sub_guess_count = 1

    while answer_ent != num_one - num_two:

        if answer_ent < num_one - num_two:
            print("Sorry, guess is too low.\n")
            sub_guess_count += 1
    
        else:
            sub_guess_count += 1
            print("Sorry, guess is too high.\n")
        answer_ent = int(input('try again: '))
        
    print("Congratulations!!!! your answer is correct..")
    print('Number of guesses:',sub_guess_count,'\n')
if __name__=="__main__":
    print("Welcome to Math Quiz\n\n")
    quit_program = False
    while not quit_program:

        print("MAIN MENU")
        print("--------------------")
        print("1. Adding Random Numbers ")
        print("2. Subtracting Random Numbers")
        print("3. Exit\n")
        menu_num = int(input("Please choose one of the menu options: "))
        if menu_num == 3:
            print("Thank you for playing...")
            print('Bye!!')
            quit_program = True
        elif menu_num == 1:
            add_random()
        elif menu_num == 2:
            sub_random()
        else:
            menu_num >= 4
            print("\nInvalid menu selection!!!!\n")
            
#
# END

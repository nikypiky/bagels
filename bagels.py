import math
import random

print('I am thinking of a 3-digit number. Try to guess what it is.')
print('Here are some clues:')
print('When I say:    That means:')
print('  Pico         One digit is correct but in the wrong position.')
print('  Fermi        One digit is correct and in the right position.')
print('  Bagels       No digit is correct.')
print('I have thought up a number.')
print(' You have 10 guesses to get it.')

computer_number = [(random.randrange(10)), (random.randrange(10)), (random.randrange(10)) ]
print(computer_number)

for i in range(1,11):
    user_number = input('Guess #' + str(i) + ': ')
    if user_number.isnumeric() == False:
        print('Please choose a number')
        continue 
    fermi = 0
    pico = 0
    
    for n in range(3):  
        if int(computer_number[n]) == int(user_number[n]):
            fermi = fermi + 1
        elif int(user_number[n] in computer_number):
            piko = piko + 1
        else:
            print('Bagel')


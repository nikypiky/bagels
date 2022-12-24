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

random_number = [str(random.randrange(10)), str(random.randrange(10)), str(random.randrange(10)) ]
#random_number = (str(random.randrange(10)) + str(random.randrange(10)) + str(random.randrange(10)))
print(random_number)

for i in range(1,11):
    user_guess = input('Guess #' + str(i) + ': ')
    if user_guess.isnumeric() == False:
        print('Please choose a number')
        i = i-1
        continue
        

    user_guess = int(user_guess)

        
#    for n in range(2):
 #       if random_number(n) == user_guess(n):
  #          print('bagel')

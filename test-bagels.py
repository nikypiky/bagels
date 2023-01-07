import math
import random

#initial instructions
print('I am thinking of a 3-digit number. Try to guess what it is.')
print('Here are some clues:')
print('When I say:    That means:')
print('  Pico         One digit is correct but in the wrong position.')
print('  Fermi        One digit is correct and in the right position.')
print('  Bagels       No digit is correct.')
print('I have thought up a number.')
print(' You have 10 guesses to get it.')
def main():
#generate computer number
    computer_number = [(random.randrange(10)), (random.randrange(10)), (random.randrange(10)) ]

    for i in range(1,11):
        print(computer_number)
#request and validate user input
        user_number = input('Guess #' + str(i) + ': ')
        if user_number.isnumeric() == False or len(user_number) != 3:
            print('Please choose a three digit number')
            continue 

        fermi = 0
        pico = 0

#compare user number to computer number
        for n in range(3):  
            try:
                if int(computer_number[n]) == int(user_number[n]):
                    fermi = fermi + 1
            except:
                if int(user_number[n]) in computer_number:
                    pico = pico + 1


#calculate number of pico and fermi + set win/loose conditions
        if pico == 0 and fermi == 0:
            print('Bagels')
        if fermi == 3:
            print('Congratulations! You have found the right number!!')
            break
        print(i)
        
        print('Fermi '* fermi + 'Pico ' * pico)

    else:
#        computer_number_str = (int.join(computer_number))
 #       print(type(computer_number_str))
        print('Sorry, you lost! The correct answer was ' + ''.join(map(str, computer_number)))
        print()

#game repeat question for incorect user response
    def game_repeat():
        additional_user_response = input('Please choose yes or no. ')
        if user_response or additional_user_response == 'yes':
            main()
        elif user_response or additional_user_response == 'no':
            print('Thank you for playing, have a nice day. ')
            print()
            exit(main)
        else:
            additional_user_response = input('Please choose yes or no. ')
            game_repeat()  
               
#game repeat question after user finishes game
    user_response= input('Do you want to play again? (yes or no) ')
    if user_response == 'yes':
        main()
    elif user_response == 'no':
        print('Thank you for playing, have a nice day. ')
        print()
        exit(main)
    else:
        game_repeat()


main()
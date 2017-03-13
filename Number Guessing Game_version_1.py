# number guessing game

import random
from time import sleep

def guess_game():
    """Main guessing logic. Creates a random integer between 1 and 100.
        The user then has to enter in integers to try and 'guess' what the random number is.
        This also keeps track of how many guesses it takes and tells the user once they win.
        """
    number = random.randint(1,101)
    Guesses = 1
    print()
    print('This is the Number Guessing Game!')
    print()
    print('A random number from 1 to 100 has been generated and you must guess what number it is.')
    # For testing purposes. This next line prints the random number that was generated.
    #print(str(number)) 
    sleep(1.5)
    guess = (input("What is your first guess?: "))
    
    while True:
        print('Hmmm. I\'m checking your number.')
        print('3...')
        sleep(1)
        print('2...')
        sleep(1)
        print('1...')
        sleep(1)
        while not guess.isdigit():
            guess = input("Input must be an integer between 1 and 100. Please re-enter: ")
        guess = int(guess)
            
        if guess > number:
            print("Wrong! Your guess is too high.")
            Guesses += 1
            guess = input('Enter a number lower than ' + str(guess) + ': ')
            
        elif guess < number:
            print("Wrong! Your guess is too low.")
            Guesses += 1
            guess = input('Enter a number higher than ' + str(guess) + ': ')

        else:
            if Guesses == 1:
                print('Yes!! ' + str(guess) + ' is the right number. It only took you 1 guess. I think you got lucky...')
            elif 2 <= Guesses < 6:
                print('Yes!! ' + str(guess) + ' is the right number. It only took you ' + str(Guesses) + ' guesses. You are pretty good at this.')
            else:
                print('Yes! ' + str(guess) + ' is the right number. It took you ' + str(Guesses) + ' guesses. I think you can do better.')
            break


# This is the 'play again' logic. Asks if the user wants to play again.
# If they type 'yes' then the guess_game function starts over.
# If the user types 'no' then the program terminates.

play_again = 'yes'
while play_again == 'yes':
    guess_game()
    play_again = input('Would you like to play again? Yes or no: ')   
    
    while True:
        play_again = play_again.lower() 
        if play_again == 'yes':
            break
        elif play_again != 'no':
            print('Sorry, that is not an acceptable answer. Please type \'yes\' or \'no\'.')
            play_again = input()
            continue
        else:
            break
print()
print('Thanks for playing :)')

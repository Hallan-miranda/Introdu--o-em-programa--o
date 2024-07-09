import random

magic_number = int(random.randint(1,100))
guess_number = int(input('Whats is your guess? '))
attempts = 1
play_again = 'yes'

while play_again == 'yes':
    while guess_number != magic_number:
        if guess_number < magic_number:
            print('Higher')
            attempts = attempts +1
            guess_number = int(input('Whats is your guess? '))
        elif guess_number > magic_number:
            print('Lower')
            attempts = attempts +1
            guess_number = int(input('Whats is your guess? '))
    print(f'You guessed it! \nYour attempts is {attempts}')
    magic_number = int(random.randint(1,100))
    attempts = 1
    play_again = str(input('Do you anto to play again YES or NO? ')).lower()
    guess_number = int(input('Whats is your guess? '))
print('Thanks for playing. Goodbye!')
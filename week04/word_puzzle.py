secred_word = 'python'

print('Welcome to the word guessing game!\n')
print('Your hint is: _ _ _ _ _ _')
guess_word = input('What is your guess? ')
guess = 1  #Set the number of attempts 
letter_equal = 0 # 
letter = '' 
repeat = True # Set if tehe game continue or no

# Start the game an stop if the player get he worg correct
while repeat == True: 
    if guess_word == secred_word:
        repeat = False
        print('Congratulations! You guessed it!')
        print(f'It took you {guess} guesses.')
    else:
        if len(secred_word) == len(guess_word):
            # Validates whether the letters in the guess word are in the secret word
            for letter_g in guess_word: 
                for letter_s in secred_word:
                    if letter_g == letter_s:
                        letter_equal = letter_equal + 1
                    else:
                        letter_equal = letter_equal
                if letter_equal > 0:
                    letter = letter + str(letter_g) + ' '
                    letter_equal = 0
                else:
                    letter = letter + '_ '
                hint_guide_word = 'Your hint is: ' + str(letter)
                # shows the player if he got any letter of the secret word right and resets the letter variable
            print(hint_guide_word)
            letter = ''
        else:
            print('Sorry, the guess must have the same number of letters as the secret word.')
        guess_word = input('What is your guess? ')
        guess = guess + 1
    

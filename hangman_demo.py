import random
HANGMAN_PICS = ['''
    +---+
        |
        |
        |
       ===''', ''' 
    +---+
    0   |
        |
        |   
       ===''', '''
    +---+
    0   |
    |   |
        |   
       ===''', '''
    +---+
    0   |
   /|   |
        |   
       ===''', '''
    +---+
    0   |
   /|\  |
        |   
       ===''', '''
    +---+
    0   |
   /|\  |
   /    |   
       === ''', '''
    +---+
    0   |
   /|\  |
   / \  |   
       ===''']

words = '''stork shark baboon ram badger beaver bull camel wolf sparrow crow 
otter pigeon goose toad zebra snake turkey whale cobra goat goat coyote cow cat 
rabbit rat chicken llama weasel swan lion fox salmon moose frog bear clam mole
ant mouse mink rhinoceros monkey sheep perch deer eagle donkey panda spider
python parrot puma salmon skunk dog owl tiger newt seal duck trout ferret turtle
hawk lizard'''.split()


def get_random_word(wordlist):
    # Returns a random string from the passed list.
    word_index = random.randint(0, len(wordlist) - 1)
    return wordlist[word_index]


def display_board(missed_letters, correct_letters, secret_word):
    print(HANGMAN_PICS[len(missed_letters)])
    print()

    print('Missed letters:', end=' ')
    for letter in missed_letters:
        print(letter, end='')
    print()

    blanks = '_' * len(secret_word)

    for i in range(len(secret_word)):
        if secret_word[i] in correct_letters:
            blanks = blanks[:i] + secret_word[i] + blanks[i+1:]

    for letter in blanks:
        print(letter, end='')
    print()


def get_guess(already_guessed):
    # Returns a letter entered by player
    while True:
        print('Enter a letter.')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Enter a letter, please.')
        elif guess in already_guessed:
            print('You have already entered this letter. Enter another one')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please, enter a LETTER')
        else:
            return guess


def play_again():
    # Returns True if player wants to start again; otherwise False
    print('Do you wanna try again? (yes or no)')
    return input().lower().startswith('y')


print('H A N G M A N')
missed_letters = ''
correct_letters = ''
secret_word = get_random_word(words)
game_is_done = False

while True:
    display_board(missed_letters, correct_letters, secret_word)

    # Lets player enter the letter.
    guess = get_guess(missed_letters + correct_letters)

    if guess in secret_word:
        correct_letters += guess

        # Checks the player's win
        found_all_letters = True
        for i in range(len(secret_word)):
            if secret_word[i] not in correct_letters:
                found_all_letters = False
                break
        if found_all_letters:
            print('YES! Secret word is "' + secret_word + '"! You guessed!')
            game_is_done = True
    else:
        missed_letters += guess

        # Checks if player lost or exceeded tries limit
        if len(missed_letters) == len(HANGMAN_PICS) - 1:
            display_board(missed_letters, correct_letters, secret_word)
            print('You have exhausted all tries!\n')
            print('Missed letters: ' + str(len(missed_letters)))
            print('And correct letters: ' + str(len(correct_letters)) +
                  '\nThe word ' + secret_word + ' was guessed.')
            game_is_done = True
    # Asks player to play again (if game is done)
    if game_is_done:
        if play_again():
            missed_letters = ''
            correct_letters = ''
            game_is_done = False
            secret_word = get_random_word(words)
        else:
            break

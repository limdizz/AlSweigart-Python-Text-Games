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
       ===''', '''
    +---+
   [0   |
   /|\  |
   / \  |   
       ===''', '''
     +---+
   [0]  |
   /|\  |
   / \  |   
       ===''']

words = {'Animals': '''stork shark baboon ram badger beaver bull camel wolf
otter pigeon goose toad zebra snake turkey whale cobra goat goat coyote cow cat 
rabbit rat chicken llama weasel swan lion fox salmon moose frog bear clam mole
ant mouse mink rhinoceros monkey sheep perch deer eagle donkey panda spider
python parrot puma salmon skunk dog owl tiger newt seal duck trout ferret turtle
hawk lizard crow sparrow'''.split(),
         'Colors': '''black orange yellow green blue violet purple white grey 
brown beige scarlet pink silver gold coral emerald turquoise'''.split(),
         'Drinks': '''wine coffee tea cognac tequila cocktail liquor
vodka champagne gin rum milk cocoa milkshake kvass cider brandy juice
bourbon whiskey beer'''.split()}


def get_random_word(word_dict):
    # Returns a random key and the string from the passed dict.
    word_key = random.choice(list(word_dict.keys()))
    word_index = random.randint(0, len(word_dict[word_key]) - 1)
    return [word_dict[word_key][word_index], word_key]


def display_board(missed_letters, correct_letters, secret_word):
    print(HANGMAN_PICS[len(missed_letters)])
    print()

    print('Missed letters:', end=' ')
    for letter in missed_letters:
        print(letter, end=' ')
    print()

    blanks = '_' * len(secret_word)

    for i in range(len(secret_word)):  # replace blanks with correctly guessed lrs
        if secret_word[i] in correct_letters:
            blanks = blanks[:i] + secret_word[i] + blanks[i + 1:]

    for letter in blanks:  # show the secret word with spaces in between each letter
        print(letter, end=' ')
    print()


def get_guess(already_guessed):
    # Returns a letter entered by player (a single letter, not something else)
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
    print('Do you wanna play again? (yes or no)')
    return input().lower().startswith('y')


print('H A N G M A N')

difficulty = 'X'
while difficulty not in 'EMH':
    print('Choose the difficulty level: E - Easy, M - Medium, H - Hard')
    difficulty = input().upper()
if difficulty == 'M':
    del HANGMAN_PICS[8]
    del HANGMAN_PICS[7]
if difficulty == 'H':
    del HANGMAN_PICS[8]
    del HANGMAN_PICS[7]
    del HANGMAN_PICS[5]
    del HANGMAN_PICS[3]

missed_letters = ''
correct_letters = ''
secret_word, secret_set = get_random_word(words)
game_is_done = False

while True:
    print('The secret word from group: ' + secret_set)
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
            print('YES! The secret word is "' + secret_word + '"! You have won!')
            game_is_done = True
    else:
        missed_letters += guess

        # Checks if player lost or exceeded tries limit
        if len(missed_letters) == len(HANGMAN_PICS) - 1:
            display_board(missed_letters, correct_letters, secret_word)
            print('You have run out of guesses!\nAfter ' +
                  str(len(missed_letters)) + ' missed guesses and ' +
                  str(len(correct_letters)) + ' correct guesses, the word was "' +
                  secret_word + '"')
            game_is_done = True
    # Asks player to play again (if game is done)
    if game_is_done:
        if play_again():
            missed_letters = ''
            correct_letters = ''
            game_is_done = False
            secret_word, secret_set = get_random_word(words)
        else:
            break

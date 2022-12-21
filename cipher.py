# Caesar Cipher
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()'
MAX_KEY_SIZE = len(SYMBOLS)


def get_mode():
    while True:
        print('Do you want to encrypt, decrypt or hack a message?')
        mode = input().lower()
        if mode in ['encrypt', 'e', 'decrypt', 'd', 'hack', 'h']:
            return mode
        else:
            print('Enter either "encrypt" or "e" or "decrypt" or "d" or "hack" or "h"')


def get_message():
    print('Enter your message: ')
    return input()


def get_key():
    while True:
        print('Enter the key (1-%s)' % MAX_KEY_SIZE)
        key = int(input())
        if 1 <= key <= MAX_KEY_SIZE:
            return key


def get_translated_message(mode, message, key):
    if mode[0] == 'd':
        key = -key
    translated = ''

    for symbol in message:
        symbol_index = SYMBOLS.find(symbol)
        if symbol_index == -1:  # Symbol is not found in SYMBOLS
            # Add this symbols without changes
            translated += symbol
        else:
            # Encrypt or decrypt
            symbol_index += key

            if symbol_index >= len(SYMBOLS):
                symbol_index -= len(SYMBOLS)
            elif symbol_index < 0:
                symbol_index += len(SYMBOLS)

            translated += SYMBOLS[symbol_index]
    return translated


mode = get_mode()
message = get_message()
if mode[0] != 'h':
    key = get_key()
print('Your translated message is: ')
if mode[0] != 'h':
    print(get_translated_message(mode, message, key))
else:
    for key in range(1, MAX_KEY_SIZE + 1):
        print(key, get_translated_message('decrypt', message, key))

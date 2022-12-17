import random
import time


def display_intro():
    print('''You are in a land inhabited by dragons.
    In front of you you see two caves.
    In one of them there is a friendly dragon
    who is ready to share his treasures with you.
    In the second — a greedy and hungry dragon that will eat you instantly.''')
    print()


def choose_cave():
    cave = ''
    while cave != '1' and cave != '2':
        print('Which cave will you enter? (press key 1 or 2)')
        cave = input()

    return cave


def check_cave(chosen_cave):
    print('You are approaching the cave...')
    time.sleep(2)
    print('Its darkness makes you tremble with fear...')
    time.sleep(2)
    print('A big dragon jumps out in front of you! He opens his mouth and...')
    print()
    time.sleep(2)

    friendly_cave = random.randint(1, 2)

    if chosen_cave == str(friendly_cave):
        print('...shares his treasures with you!')
    else:
        print('...eats you instantly!')


play_again = 'yes'
while play_again == 'yes' or play_again == 'y':
    display_intro()
    cave_number = choose_cave()
    check_cave(cave_number)

    print('Try your luck again? (yes or no)')
    play_again = input()


#!/usr/bin/python
'''
A simple 'magic game' for my neice, juliana
'''
from family_fun import name_ages, winning_combos
import random
import time

def print_board(td):
    print('{}   {}   {}'.format(td['x1'], td['x2'], td['x3']))
    print('')
    print('{}   {}   {}'.format(td['x4'], td['x5'], td['x6']))
    print('')
    print('{}   {}   {}'.format(td['x7'], td['x8'], td['x9']))

def get_new_value(td, tw, i, break_game):
    if i % 2 == 1:
        trigger = False
        guess = raw_input('What value would you like? ')
        while not trigger:
            if guess != td['x{}'.format(guess)]:
                td['x{}'.format(guess)] = 'X'
                tw['x{}'.format(guess)] = 1
                trigger = True
            else:
                guess = raw_input('Hmm... that value has already been chosen. Choose again. ')
    else:
        time.sleep(1.5)
        values_available = [j for j in td.values() if isinstance(j, int)]
        guess = random.choice(values_available)
        print('The computer selects {}.'.format(guess))
        td['x{}'.format(guess)] = 'O'
        tw['x{}'.format(guess)] = 0
    win_check = [[v for k, v in ttt_wins.items() if k in x] for x in winning_combos]

    for check in win_check:
        try:
            game_sum = sum(check)
            if game_sum==0 or game_sum==3 or len([j for j in td.values() if
                                                 isinstance(j, int)])==0:
                break_game = True
        except TypeError:
            continue
    print_board(td)
    i += 1
    return i, break_game


decision_flag = False
while not decision_flag:
    decision = raw_input('Would you like to play a game? ')
    if decision=='yes' or decision=='no':
        decision_flag = True
    else:
        decision = raw_input('Silly! You have to say \'yes\' or \'no\'! ')

if decision=='yes':
    name = raw_input('Great! What\'s your name? ')
    name_proper = name.title()
else:
    print('Too bad, maybe next time!')
    exit()

game_flag = False
while not game_flag:
    if name_ages.get(name_proper):
        game = raw_input('I bet you are {} years old! Would you like to play a game of '
                        'tic-tac-toe? '.format(name_ages[name_proper]))
    else:
        name_ages[name_proper] = int(raw_input('How old are you? '))
        game = raw_input('Would you like to play a game of tic-tac-toe? ')

    if game=='yes' or game=='no':
        game_flag = True
    else:
        game = raw_input('I\'m not the smartest -- you have to say \'yes\' or \'no\'! ')

if game=='no':
    print('Thanks for visiting; good bye! :P')
    exit()
else:
    ttt_values = {'x{}'.format(i+1): i+1 for i in xrange(9)}
    ttt_wins = {'x{}'.format(i+1): None for i in xrange(9)}
    print_board(ttt_values)
    i = 1
    break_game = False
    while not break_game:
        i, break_game = get_new_value(ttt_values, ttt_wins, i, break_game)
    if len([j for j in ttt_values.values() if isinstance(j, int)])!=0:
        print('Congratulations, {} won the game!'.format(name_proper if i % 2 == 0 else
                                                         'the computer'))
    else:
        print('Looks like this game ended in a tie. Try again!')
    exit()

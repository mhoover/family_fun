#!/usr/bin/python
'''
A simple tic-tac-toe game
'''
import time
import random

from family_fun import ttt_winning_combos

def print_ttt_board(td):
    print('{}   {}   {}'.format(td['x1'], td['x2'], td['x3']))
    print('')
    print('{}   {}   {}'.format(td['x4'], td['x5'], td['x6']))
    print('')
    print('{}   {}   {}'.format(td['x7'], td['x8'], td['x9']))


def get_new_ttt_value(td, tw, i, break_game):
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
    win_check = [[v for k, v in tw.items() if k in x] for x in ttt_winning_combos]

    for check in win_check:
        try:
            game_sum = sum(check)
            if game_sum==0 or game_sum==3 or len([j for j in td.values() if
                                                 isinstance(j, int)])==0:
                break_game = True
        except TypeError:
            continue
    print_ttt_board(td)
    i += 1
    return i, break_game

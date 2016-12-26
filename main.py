#!/usr/bin/python
'''
Main module to load interaction and game menu for play.
'''
import random
import time

from family_fun import *
from tic_tac_toe import print_ttt_board, get_new_ttt_value
from connect_four import print_cf_board, get_new_cf_value


decision_flag = False
while not decision_flag:
    print('Would you like to play a game? You can play...')
    print('1. Tic-Tac-Toe')
    print('2. Connect Four')
    decision = int(raw_input('Enter the number of the game you want to play '
                             '(enter \'0\' to quit): '))
    if decision<=2:
        decision_flag = True
    else:
        print('Silly! You have to enter a number!')
        print('1. Tic-Tac-Toe')
        print('2. Connect Four')
        decision = int(raw_input('Enter the number of the game you want to play '
                                 '(enter \'0\' to quit): '))

if decision>0:
    name = raw_input('Great! What\'s your name? ')
    name_proper = name.title()
else:
    print('Too bad, maybe next time!')
    exit()

game_flag = False
while not game_flag:
    if name_ages.get(name_proper):
        game = raw_input('I bet you are {} years old! Ready to play a game of {}? '
                         .format(name_ages[name_proper], game_choices[decision]))
    else:
        name_ages[name_proper] = int(raw_input('How old are you? '))
        game = raw_input('Ready to play a game of {}? '.format(game_choices[decision]))

    if game=='yes' or game=='no':
        game_flag = True
    else:
        game = raw_input('I\'m not the smartest -- you have to say \'yes\' or \'no\'! ')

if game=='no':
    print('Thanks for visiting; good bye! :P')
    exit()
else:
    if decision==1:
        ttt_values = {'x{}'.format(i+1): i+1 for i in xrange(9)}
        ttt_wins = {'x{}'.format(i+1): None for i in xrange(9)}
        print_ttt_board(ttt_values)
        i = 1
        break_game = False
        while not break_game:
            i, break_game = get_new_ttt_value(ttt_values, ttt_wins, i, break_game)
        if len([j for j in ttt_values.values() if isinstance(j, int)])!=0:
            print('Congratulations, {} won the game!'.format(name_proper if i % 2 == 0 else
                                                             'the computer'))
        else:
            print('Looks like this game ended in a tie. Try again!')
        exit()
    else:
        cf_values = {'x{}'.format(i+1): ' ' for i in xrange(42)}
        cf_wins = {'x{}'.format(i+1): None for i in xrange(42)}
        print_cf_board(cf_values)
        i = 1
        break_game = False
        while not break_game:
            i, break_game = get_new_cf_value(cf_values, cf_wins, i, break_game)
        if len([j for j in cf_values.values() if j==' '])!=0:
            print('Congratulations, {} won the game!'.format(name_proper if i % 2 == 0 else
                                                             'the computer'))
        else:
            print('Looks like this game ended in a tie. Try again!')
        exit()

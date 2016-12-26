#!/usr/bin/python
'''
A simple connect-four game
'''
import random
import time

from family_fun import cf_winning_combos


def print_cf_board(cfd):
    print('  1   2   3   4   5   6   7')
    print('| {} | {} | {} | {} | {} | {} | {} |'
          .format(cfd['x1'], cfd['x2'], cfd['x3'], cfd['x4'], cfd['x5'], cfd['x6'], cfd['x7']))
    print('| {} | {} | {} | {} | {} | {} | {} |'
          .format(cfd['x8'], cfd['x9'], cfd['x10'], cfd['x11'], cfd['x12'], cfd['x13'],
                  cfd['x14']))
    print('| {} | {} | {} | {} | {} | {} | {} |'
          .format(cfd['x15'], cfd['x16'], cfd['x17'], cfd['x18'], cfd['x19'], cfd['x20'],
                  cfd['x21']))
    print('| {} | {} | {} | {} | {} | {} | {} |'
          .format(cfd['x22'], cfd['x23'], cfd['x24'], cfd['x25'], cfd['x26'], cfd['x27'],
                  cfd['x28']))
    print('| {} | {} | {} | {} | {} | {} | {} |'
          .format(cfd['x29'], cfd['x30'], cfd['x31'], cfd['x32'], cfd['x33'], cfd['x34'],
                  cfd['x35']))
    print('| {} | {} | {} | {} | {} | {} | {} |'
          .format(cfd['x36'], cfd['x37'], cfd['x38'], cfd['x39'], cfd['x40'], cfd['x41'],
                  cfd['x42']))
    print('_____________________________')


def place_symbol(cd, cw, move, choice, trigger):
    while not trigger:
        if move[0]=='O':
            bad_choices = []
        for i in reversed(xrange(0, 36, 7)):
            if cd['x{}'.format(i+choice)]==' ':
                cd['x{}'.format(i+choice)] = move[0]
                cw['x{}'.format(i+choice)] = move[1]
                trigger = True
                break
            if i==0:
                if move[0]=='X':
                    choice = int(raw_input('Whoops... looks like the column is full; choose '
                                       'again (1 through 7). '))
                else:
                    bad_choices.append(choice)
                    choice_set = [x for x in xrange(1, 8) if x not in bad_choices]
                    choice = random.choice(choice_set)
                    if choice==[]:
                        trigger = True


def get_new_cf_value(cd, cw, i, break_game):
    trigger = False
    if i % 2 == 1:
        move = ('X', 1)
        choice = int(raw_input('Where do you want to play (choose 1 through 7)? '))
        place_symbol(cd, cw, move, choice, trigger)
    else:
        time.sleep(1.5)
        move = ('O', 0)
        choice = random.randint(1, 7)
        place_symbol(cd, cw, move, choice, trigger)
    win_check = [[v for k, v in cw.items() if k in x] for x in cf_winning_combos]

    for check in win_check:
        try:
            game_sum = sum(check)
            if game_sum==0 or game_sum==4 or len([j for j in cd.values() if j==' '])==0:
                break_game = True
        except TypeError:
            continue
    print_cf_board(cd)
    i += 1
    return i, break_game

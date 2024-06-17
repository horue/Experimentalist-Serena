import sys
import os
import configparser

save = configparser.ConfigParser()
save.read('save.ini')


def save_game(r):
    save['level'] = {'i':f'{r}'}
    with open('save.ini', 'w') as configfile:
        save.write(configfile)

save_game(8)
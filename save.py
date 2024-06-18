import sys
import os
import configparser

save = configparser.ConfigParser()
save.read('save.ini')

## Used to save the game ##
def save_game(r):
    save['level'] = {'i':f'{r}'}
    with open('save.ini', 'w') as configfile:
        save.write(configfile)

## Used to check stage status ##
def save_status(stage, status):
    save[f'{stage}'] = {'satatus' : f'{status}'}
    with open('save.ini', 'w') as configfile:
        save.write(configfile)

## Read save file ##
def read_save_file():
    global level
    level = (save['level']['i'])

def read_name():
    global name
    name = (save['name']['status'])

def continue_game(l, f):
    if level == l:
        f()
    else:
        print('False')

def test():
    print('Level Test')

if __name__ == '__main__':
    save_game(10)
    read_save_file()
    print(level)
    continue_game('10',test)
import sys
import os
import configparser

save = configparser.ConfigParser()
save.read('save.ini')


def save_game(r):
    save['level'] = {'i':f'{r}'}
    with open('save.ini', 'w') as configfile:
        save.write(configfile)

def save_status(stage, status):
    save[f'{stage}'] = {'satatus' : f'{status}'}
    with open('save.ini', 'w') as configfile:
        save.write(configfile)

def read_save_file():
    global level
    level = (save['level']['i'])

def test():
    if level == '3':
        print('Level 3')
    elif level == '17':
        print('Level 17')
    else:
        print('False')

if __name__ == '__main__':
    save_game(3)
    read_save_file()
    test()
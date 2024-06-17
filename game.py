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
    print(save['level']['i'])


read_save_file()
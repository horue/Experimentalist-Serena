from save import *
from type import *

def level_1():
    save_game(1)
    typewriter('Hello, I am Serena. Nice to meet you.')
    typewriter('We are here today to star a new analysis system, and you will be helping us.')
    typewriter('First of all, I would like to know your name.')
    n = input('> ')
    save_status('player', n)
    player = read_save_file('level','i')
    typewriter(f'Hello,{player}, it is a pleasure to meet you.')
    typewriter("Now, let's get started.")
    typewriter("I'll be asking you things and you must answer me with Yes or No.")
    typewriter('Do you understand?')
    answer('status1')

if __name__ == '__main__':
    level_1()
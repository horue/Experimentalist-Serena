from save import *
from type import *

def level_1():
    save_game(1)
    typewriter('Hello, I am Serena. Nice to meet you.')
    typewriter('We are here today to star a new analysis system, and you will be helping us.')
    typewriter('First of all, I would like to know your name.')
    typewriter("Now, let's get started.")
    typewriter("I'll be asking you things and you must answer me with Yes or No.")
    typewriter('Do you understand?')
    answer('status1')
    typewriter('Do you understand why we are doing this?')
    answer('status2')
    next_level(level_2)

def level_2():
    save_game(2)
    typewriter('It was a very nice start.')
    typewriter('Now that you have got how it works, I will be continuing our interview.')
    typewriter('Do you think AI could take our place? Sorry, I mean, YOUR place.')
    answer('status3')

if __name__ == '__main__':
    level_1()
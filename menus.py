import os
import sys
from bcolors import bcolors



def main_menu():
    option = input('> ')
    if option == '1':
        sys.exit
    elif option == '2':
        print(1)
        main_menu()
    elif option == '3':
        print(2)
        main_menu()
    elif option == '4':
        print(3)
        main_menu()
    else:
        print('Enter a valid command.')
        main_menu()
        
def main_scr():
    os.system('cls' if os.name == 'nt' else 'clear')
    text = f"* {bcolors.Pink}Experimentalist Serena{bcolors.ENDC} *"
    print("#" * len('* Experimentalist Serena *'))
    print(text)
    print("#" * len('* Experimentalist Serena *'))
    print('1 — Exit')
    print('2 — New game')
    print('3 — Continue')
    print('4 — Help')
    print('Made by Jorge Magno.')
    main_menu()

def warning():
    os.system('cls' if os.name == 'nt' else 'clear')
    text = f"{bcolors.Red}*   THIS GAME IS A WORK OF FICTION!  *{bcolors.ENDC}"
    print('**************************************')
    print(text)
    print('**************************************')
    notice = """
All characters, events, and locations depicted in this game are products of the creators' imagination.
Any resemblance to actual persons, living or dead, or actual events is purely coincidental.

**************************************
"""
    print(notice)
    print('Press any key to continue')
    input('> ')
    main_scr()


warning()
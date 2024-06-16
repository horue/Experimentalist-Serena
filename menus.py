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
**************************************
All characters, events, and locations depicted in this game are products of the creators' imagination.
Any resemblance to actual persons, living or dead, or actual events is purely coincidental.

This game has been developed for the purpose of entertainment and should not be construed as a factual 
representation of reality. The opinions and views expressed by the characters in the game are fictional 
and do not necessarily reflect the opinions of the developers or any other associated entity.

Please remember that the situations and actions portrayed in the game are fictional and should not be 
replicated or performed in real life. Playing is a safe and controlled act; ensure you distinguish 
between the game world and the real world.
**************************************
"""
    print(notice)
    print('Press any key to continue')
    input('> ')
    main_scr()


warning()
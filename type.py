from save import *
import time
import sys


def typewriter(text, delay=0.1):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # Move to the next line after finishing

def answer(st):
    answer_input = input('> ')
    if answer_input.lower() == 'yes':
        save_status(st, 1)
    elif answer_input.lower() == 'no':
        save_status(st, 0)
    else:
        typewriter('Sorry, but this answer do not match with our expectations.')
        answer(st)
import time
import sys
import os
import pyttsx3
from animation.colors import *


engine = pyttsx3.init()


def clear():
    if os.name == 'nt':
        os.system('cls')
    sys.stdout.flush()


def wait():
    # sys.stdout.flush()
    # engine.say("Please wait..")
    # engine.runAndWait()
    print("Please wait..", end='')
    time.sleep(2)
    clear()
    print(end='\r')
    print(end='\r')


def countdown_timer(_register, _duty: str = 'creation', countdown: int = 3):
    """Countdown for any bank process.
    It enhances users' experience.

    Parameters
    ----------
    _register : str
        A variable that holds some identifier or name related to the process being executed.
    _duty : str
        A variable that holds the task or duty related to the process being executed.
    countdown : int
        A variable that starts with a certain value
        and is decremented until it reaches 0. Represents the time remaining.
    """

    print()
    while countdown != 0:
        print(bold, brt_black_bg, brt_blue, end='')  # coloring
        print(f"processing {_register} {_duty}... {countdown}", end='')
        print(end, end='')  # coloring

        countdown -= 1
        time.sleep(1)

        # Move the cursor to the beginning of the line without adding a new line
        print(end='\r')


# Whatsapp
def wait_and_count():
    for i in range(3, 0, -1):
        # sys.stdout.flush()
        # engine.say("Processing..:")
        # engine.runAndWait()
        print(f"{italic}{brt_black_bg}{bold}{brt_blue}Processing...{i}sec", end='')
        time.sleep(1)
        print(end, end='\r')
    clear()
    print(end='\r')
    print(end='\r')


def print_slowly(text):
    for char in text:
        print(char, end='', flush=True)  # Print without newline and flush the output
        time.sleep(0.05)  # Adjust the delay (in seconds) as desired
    print()  # Print a newline at the end


def invalid():
    engine.say("Invalid phone number")
    engine.runAndWait()
    print(f'{brt_red}::Invalid Phone number.{end}   {bold}{magenta}')
    time.sleep(0.6)
    engine.say("Please try again")
    engine.runAndWait()
    print(f'{brt_red}::Please try again{end}   {bold}{magenta}')
    print()


def out():
    time.sleep(0.8)
    engine.say("invalid entry. Please try again")
    engine.runAndWait()
    print(f'{brt_red}::Invalid Entry. Please try again{end}   {bold}{magenta}')
    print()

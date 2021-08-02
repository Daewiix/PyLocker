from pyfiglet import Figlet
import pyfiglet
from termcolor import colored
import os


def start():
    print(colored(r"""
        .--------.
        / .------. \
    / /        \ \
    | |        | |
    _| |________| |_
    .' |_|        |_| '.
    '._____ ____ _____.'
    |     .'____'.     |
    '.__.'.'    '.'.__.'
    '.__  |      |  __.'
    |   '.'.____.'.'   |
    '.____'.____.'____.'
    '.________________.'
        """, "green"))

    f = Figlet(font="slant")
    print(colored(f.renderText('PyLocker'), "green"))

    print(colored(r"""
    -------------------------------------------------------------------------
                        PICK AN OPTION FROM THE LIST
    -------------------------------------------------------------------------
        """, "yellow"))

def start_loop_menu():
    while True:
        print(colored("1.", "red"), end="")
        print(colored(" Update database", "blue"))

        print(colored("2.", "red"), end="")
        print(colored(" Find Password", "blue"))

        print(colored("3.", "red"), end="")
        print(colored(" Add Password", "blue"))

        print(colored("4.", "red"), end="")
        print(colored(" Print Complete List of your passwords in a tabular form", "blue"))

        print(colored("5.", "red"), end="")
        print(colored(" Exit", "blue"))

        try:
            option  = int(input(colored(">> ", "red")))

            if option in {1, 2, 3}:
                os.system('cls' if os.name == 'nt' else 'clear')
            elif option == 5:
                print(colored("Goodbye!", "yellow"))
                exit()
        except KeyboardInterrupt:
            print(colored("\nGoodbye!", "yellow"))
            exit()
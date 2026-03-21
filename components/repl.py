
import sys
from components.secretapikeys import sensitiveFunction

# inspired by python repl
def repl(passthrough: str):
    # print info
    print("PCINT, running on Python", sys.version)
    print('Type "help", "copyright", "credits" or license" for more information.')
    while True:
        try:
            usrinput = input(">>> ") or passthrough
            if usrinput == "help": # print help
                print("exit() to exit, clear() to clear the screen")
            elif usrinput == "clear()": # clears the screen
                import os
                os.system('cls' if os.name == 'nt' else 'clear')
            elif usrinput == "exit()": #exits the repl
                print("Exiting...")
                break
            elif usrinput == "copyright": # print copyright
                print("Copyright at https://github.com/some-du6e/pleasecompilerineedthis/blob/main/LICENSE")
            elif usrinput == "credits": # print credits
                print("Copilot, Claude, Hunter alpha, Nemotron.")
            elif usrinput == "license": # print license
                print("License at https://github.com/some-du6e/pleasecompilerineedthis/blob/main/LICENSE")
            else:
                convertedPythonString = sensitiveFunction(fast=False, line=usrinput, filename="REPL")
                eval(convertedPythonString)
        except Exception as e:
            print("Error: "+str(e))
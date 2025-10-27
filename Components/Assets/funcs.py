import os, platform
def clearConsole():
    UserOS = platform.system()
    if (UserOS == "Windows"):
            os.system('cls')
    if (UserOS == "Linux"):
            os.system('clear')
            
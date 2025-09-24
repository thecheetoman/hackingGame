from Assets.Scripts.info import *
import sys, time, os

connectedServer = "home"

print("haking game")
print(ver)
while True:
    error = True
    userInput = input("\033[1m>\033[0m ")
    #install hackingTools
    if userInput.startswith("hackingTools --install"):
        error = False
        hackingToolsInstalled = True
        import Assets.Scripts.OutputLogs.hackingToolsOutput
    
    if userInput.startswith("servers --tree"):
        error = False
        if connectedServer == "home":
            print("hi")

    #Close game functionality
    if userInput.startswith("shutdown"):
        error = False
        print("Disconnecting from " + gameName)
        time.sleep(1.5)
        sys.exit()
    
    #clear output functionality
    if userInput.startswith("clear"):
        error = False
        os.system('cls')

    #Leave a blank space above this comment for ease of adding commands
    if error == True:
        print("Terminal: Command unrecognized")
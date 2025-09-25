from Assets.Scripts.info import *
import sys, time, os

connectedServer = "home"
hackingToolsInstalled = False
print("haking game")
print(ver)
while True:
    error = True
    userInput = input(connectedServer + "/> ")
    #Install hackingTools
    if userInput.startswith("hackingTools"):
        if hackingToolsInstalled == False:
            #Installation functionality
            if "--install" in userInput:
                error = False
                import Assets.Scripts.OutputLogs.hackingToolsOutput
                hackingToolsInstalled = True
                error = False
            #What to do if hackingTools is not installed
            else:
                print("Package 'hackingTools' is not installed")
                error = False
        ##Write commands that use hackingTools here
        if hackingToolsInstalled == True:
            print("guh")

    #Look for "victim" servers =D
    if userInput.startswith("servers --tree"):
        error = False
        if connectedServer == "home":
            import Assets.ServerInfo.homeServerTree

    #Close game functionality
    if userInput.startswith("shutdown"):
        error = False
        print("Disconnecting from " + gameName)
        time.sleep(1.5)
        sys.exit()
    
    #Clear terminal functionality that works on linux and windows
    if userInput.startswith("clear"):
        error = False
        if (OsType == "Windows"):
            os.system('cls')
        if (OsType == "Linux"):
            os.system('clear')

    #Leave a blank space above this comment for ease of adding commands
    if error == True:
        print("Terminal: Command unrecognized")

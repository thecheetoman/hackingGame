from Assets.Scripts.info import *
from Assets.Scripts.OutputLogs.connectToServer import connectToServer
import sys, time, os

#Servers in each part
homeAvailableServers = ["testServer01", "Elmore Packard", "freeMonE"]

connectedServer = "home"
hackingToolsInstalled = False
print(gameName)
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
            if "--connect" in userInput:
                serverToConnect = userInput.replace("hackingTools --connect ", "", 1)
                if serverToConnect in homeAvailableServers:
                    connectToServer(serverToConnect)
                    connectedServer = serverToConnect
                    error = False
                else:
                    print("Server not found")
                    error = False

    #Look for "victim" servers =D
    if userInput.startswith("nmap -a"):
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

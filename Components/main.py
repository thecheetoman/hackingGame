from Assets.Scripts.info import *
from Assets.Scripts.OutputLogs.connectToServer import connectToServer
from Assets.ServerInfo.homeServerTree import *
from Assets.funcs import *
import sys, time, os

#Servers in each part
homeAvailableServers = ["testServer01", "Gigmore electronics", "freeMonE"]

connectedServer = "home"
hackingToolsInstalled = False
print(gameName)
print(ver)
while True:
    error = True
    userInput = input(connectedServer + "/> ")
    #What to do if home client
    if (connectedServer == "home"):
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
                        print("Server \n" + serverToConnect + "\' not found")
                        error = False

        #Look for "victim" servers =D
        if userInput.startswith("nmap"):
            error = False
            if connectedServer == "home":
                homeTree()

        #Close game functionality
        if userInput.startswith("shutdown"):
            error = False
            print("Disconnecting from " + gameName)
            time.sleep(1.5)
            sys.exit()
        
        #Clear terminal functionality that works on linux and windows
        if userInput.startswith("clear"):
            error = False
            clearConsole()
    elif (connectedServer in homeAvailableServers):
        if userInput.startswith("shutdown"):
            error = False
            print("Disconnecting from " + gameName)
            time.sleep(0.5)
            sys.exit()

    #Leave a blank space above this comment for ease of adding commands
    if error == True:
        print("\'" + userInput + "\' is not recognized as a operable command.")

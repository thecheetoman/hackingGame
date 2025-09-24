from Assets.Scripts.info import *
import sys, time

connectedServer = "home"

print("haking game")
print(ver)
while True:
    error = False
    userInput = input("\033[1m>\033[0m ")

    if userInput.startswith("hackingTools --install"):
        hackingToolsInstalled = True
        import Assets.Scripts.OutputLogs.hackingToolsOutput
    

    #Close game functionality
    if userInput.startswith("shutdown"):
        error = False
        print("Disconnecting from " + gameName)
        time.sleep(1.5)
        sys.exit()
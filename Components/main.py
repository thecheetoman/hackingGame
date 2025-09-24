from Assets.Scripts.info import *
import sys, time

connectedServer = "home"

print("haking game")
print(ver)
while True:
    error = False
    userInput = input("\033[1m>\033[0m ")
    if userInput.startswith("disconnect"):
        error = False
        print("Disconnecting from " + gameName)
        time.sleep(2)

        sys.exit()
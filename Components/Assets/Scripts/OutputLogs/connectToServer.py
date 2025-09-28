import time, random
def connectToServer(serverName):
    port = random.randint(1, 10000)
    print("Target server: " + serverName)
    time.sleep(.5)
    print("hackTools: Found open port " + str(port))
    time.sleep(random.randint(1, 3))
    print("Establishing connection to " + serverName + " on port " + str(port) + "...")
    time.sleep(random.randint(1, 2))
    print("Connection established.")
    time.sleep(1)
    print("Injecting payload 'hijack.pload' ...")
    print("Terminal connection aquired")
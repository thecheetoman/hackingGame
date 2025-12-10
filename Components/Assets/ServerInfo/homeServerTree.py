

class server:
    def __init__(self, name, futurePlans, clients, moneyAccountInfo, securitylevel):
        self.name = name
        self.futurePlans = futurePlans
        self.clients = clients
        self.moneyAccountInfo = moneyAccountInfo
        self.securitylevel = securitylevel
    def Info(self):
        return f"Server: {str(self.name)} \n Future plans from management: \n {str(self.futurePlans)} \n {str(self.name)}'s clients {str(self.clients)} \n Money info {str(self.moneyAccountInfo)}"
def homeTree():
    print("home")
    print("|-> testServer01")
    print("|-> Gigmore electronics")
    print("--> freeMonE")
testServer01 = server("testServer01", "planForHeatingUpPizza.zip", 0, "none", 20)

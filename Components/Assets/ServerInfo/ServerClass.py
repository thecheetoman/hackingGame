class server:
    def __init__(self, name, money, securitylevel):
        self.name = name
        self.money = money
        self.securitylevel = securitylevel
    def __str__(self):
        return f"Money on {str(server.name)} {str(server.money)}, Security security level {str(server.securitylevel)}"

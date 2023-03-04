class Company:
    def __init__(self, companyName, managerName, address, employeeNumbers, revenu) :
        self.companyName = companyName
        self.managerName = managerName
        self.address = address
        self.employeeNumbers = employeeNumbers
        self.revenu = revenu

    def productivity(self, revenu, employeeNumbers):
        return self.revenu/self.employeeNumbers

    def __str__(self) :
        return f"company name : {self.companyName}\tmanager name : {self.managerName}\taddress : {self.address}\temployee numbers : {self.employeeNumbers}\trevenu : {self.revenu}"


xyz = Company("XYZ", "ali", "Iran, Tehran", 23, 450)
print(xyz.productivity(23,450))
print(str(xyz))
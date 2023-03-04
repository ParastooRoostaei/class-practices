class Person:
    def __init__(self, name, family):
        self.name = self.__toPascalCase(name)
        self.family = self.__toPascalCase(family)

    def _showInformation(self):
        return f"Name: {self.name}\tFamily: {self.family}"

    def __toPascalCase(self,str1):
        strList = list(str1)
        st = ord(strList[0])
        if st > 96:
            strList[0] = chr(st-32)
            
        return ''.join(strList)

class Manager(Person):
    managerCount = 0
    def __init__(self, name, family, personalId, salary):
        super().__init__(name, family)
        self.personalId = personalId
        self.__salary = salary
        Manager.managerCount+=1

    def getsalary(self):
        return self.__salary

    def setSalary(self, salary):
        self.__salary = salary

    def showManagerInfo(self):
        return f"Name: {self.name}\t   Family: {self.family}\t   PersonalId: {self.personalId}\t   Salary: {self.__salary}"

class Employee(Person):
    employeeCount = 0
    def __init__(self, name, family, personalId, degree):
        super().__init__(name, family)
        self.personalId = personalId
        self.__degree = degree
        Employee.employeeCount+=1

    def getDegree(self):
        return self.__degree

    def setDegree(self, degree):
        self.__degree = degree
    
    def showEmployeeInfo(self):
        return f"Name: {self.name}\t   Family: {self.family}\t   PersonalId: {self.personalId}\t   Degree: {self.__degree}"

class Trainee(Person):
    traineeCount = 0
    def __init__(self, name, family, timeLearn):
        super().__init__(name, family)
        self.timeLearn = 12
        Trainee.traineeCount+=1

    def showTraineeInfo(self):
        return f"Name: {self.name}\t   Family: {self.family}\t   Time learn: {self.timeLearn}"

#----------------------------------------------------
listManager = []

M1 = Manager("Ali", "ahmadi", 23, 3500)
M2 = Manager("Reza", "mohamadi", 45, 4250)
M3 = Manager("sara", "saiedi", 68, 1250)
M4 = Manager("bahar", "Bahmani", 12, 5600)

listManager.append(M1)
listManager.append(M2)
listManager.append(M3)
listManager.append(M4)

for item in listManager:
    print(item.showManagerInfo())

print("Manager count: ", Manager.managerCount)
#---------------------------------------------------
listEmployee = []

E1 = Employee("Amir", "Amiri",89 ,"A" )
E2 = Employee("Bahram", "razavi", 37,"B" )
E3 = Employee("sahar", "Amini",13 ,"D" )

listEmployee.append(E1)
listEmployee.append(E2)
listEmployee.append(E3)

for item in listEmployee:
    print(item.showEmployeeInfo())

print("Employee count: ", Employee.employeeCount)
#---------------------------------------------------
listTrainee = []

T1 = Trainee("fariba", "sharifi", 34)
T2 = Trainee("elmire", "rajabi", 64)
T3 = Trainee("farzad", "modiri", 72)
T4 = Trainee("mobina", "sarmadi", 213)

listTrainee.append(T1)
listTrainee.append(T2)
listTrainee.append(T3)
listTrainee.append(T4)

for item in listTrainee:
    print(item.showTraineeInfo())

print("Trainee count: ", Trainee.traineeCount)
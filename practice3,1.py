#--------------------------------parent class
class ProgrammingLanguageCourse:
    def __init__(self, startDate, endDate, levelCourse, teacher):
        self._startDate = startDate
        self._endDate = endDate
        self._levelCourse = levelCourse
        self._teacher = teacher
        self._dates = []
        
    def addDates(self, date):
        self._dates.append(date )
    def _showInfo(self):
        return f"Start date of class: {self._startDate}\tEnd date of class: {self._endDate}\tLevel course is: {self._levelCourse}\t Teacher name is: {self._teacher}"
#-----------------------------------child class
class Python(ProgrammingLanguageCourse):
    def __init__(self, pythonCode, pythonCost, startDate, endDate, levelCourse, teacher):
        super().__init__(startDate, endDate, levelCourse, teacher)
        self.__pythonCode = pythonCode
        self.__pythonCost = pythonCost

    def showPythonInfo(self):
        print(f"Python code is: {self.__pythonCode}")
        print(self._showInfo)
        print(f"Python cost is: {self.__pythonCost}")
        print(f"Schedule date of class is:")
        for item in self._dates:
            print(item, end = ".")

    def __str__(self):
        return f"{self.__pythonCode}\t {self.__pythonCost}\t {self._startDate}\t {self._endDate}\t {self._levelCourse}\t {self._teacher}\t {self._dates}"
#------------------------------------child class
class Php(ProgrammingLanguageCourse):
    def __init__(self, phpCode, phpcCost, startDate, endDate, levelCourse, teacher):
        super().__init__(startDate, endDate, levelCourse, teacher)
        self.__phpCode = phpCode
        self.__phpcCost = phpcCost

    def  showPhpInfo(self):
        print(f"PHP code is: {self.__phpCode}")
        print(self._showInfo)
        print(f"PHP cost is: {self.__phpcCost}")
        print(f"Schedule date of class is:")
        for item in self._dates:
            print(item, end = ".")
    
    def __str__(self):
        return f"{self.__phpCode}\t {self.__phpcCost}\t {self._startDate}\t {self._endDate}\t {self._levelCourse}\t {self._teacher}\t {self._dates}"
#-----------------------------------child class
class Java(ProgrammingLanguageCourse):
    def __init__(self, javaCode, javaCost, startDate, endDate, levelCourse, teacher):
        super().__init__(startDate, endDate, levelCourse, teacher)
        self.__javaCode = javaCode
        self.__javaCost = javaCost

    def showJavaInfo(self):
        print(f"Java code is: {self.__javaCode}")
        print(self.showInfo)
        print(f"Java cost is: {self.__javaCost}")
        print(f"Schedule date of class is:")
        for item in self._dates:
            print(item, end = ".")

    def __str__(self):
        return f"{self.__javaCode}\t {self.__javaCost}\t {self._startDate}\t {self._endDate}\t {self._levelCourse}\t {self._teacher}\t {self._dates}"


p1 = Python(12, 1200, "2022,12,18", "2023,2,3", "Basic", "Mahdavi")
p1.addDates("sunday")
p2 = Python(34, 2400, "2023,01,20", "2023,06,08", "Advanced", "Hoseini")
p2.addDates("monday")
p2.addDates("friday")

h1 = Php(42, 800, "2022,12,24", "2023,01,18", "Basic", "Rezai")
h1.addDates("saturday")
h1.addDates("thursday")
h2 = Php(11, 1200, "2023,01,20", "2023,03,01", "Adanced", "Rezai")
h2.addDates("saturday")


j1 = Java(169, 2400, "2023,02,01", "2023,08,06", "Basic", "Hoseini")
j1.addDates("tuseday")
j2 = Java(67, 2800, "2023,03,06", "2023,08,04", "Advanced", "PorReza")
j2.addDates("saturday")
j2.addDates("monday")
j2.addDates("wednesday")

courseList = []
courseList.append(p1)
courseList.append(p2)
courseList.append(h1)
courseList.append(h2)
courseList.append(j1)
courseList.append(j2)

for item in courseList:
    print(item)

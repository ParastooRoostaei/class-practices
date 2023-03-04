from abc import ABC, abstractmethod
class Participant(ABC):
    def __init__(self, name, family, personId,studyField,address):
        self.name = name
        self.family = family
        self.personId = personId
        self.studyField = studyField
        self.address = address
    
    @abstractmethod
    def scoreComputing():
        pass

    def _showInfo(self):
        return f"Name: {self.name}\t Family: {self.family}\t ID: {self.personId}\t Field of study: {self.studyField}\t Address: {self.address}"

    def __str__(self) -> str:
        return self.showInfo()

class FreeParticipant(Participant):
    def __init__(self, name, family, personId, studyField, address,interviewScore, testScore):
        super().__init__(name, family, personId, studyField, address)
        self.__interviewScore = interviewScore
        self.__testScore = testScore

    @property
    def interviewScore(self):
        return self.__interviewScore

    @interviewScore.setter
    def interviewScore(self, score):
        self.__interviewScore = score

    @property
    def testScore(self):
        return self.__testScore

    @testScore.setter
    def testScore(self, score):
        self.__testScore = score

    def scoreComputing(self):
        return (self.__interviewScore + self.__testScore)/2

    def __str__(self):
        return self._showInfo()
    
class EliteParticipant(Participant):
    def __init__(self, name, family, personId, studyField, address, avarageScore, universityRank):
        super().__init__(name, family, personId, studyField, address)
        self.__avarageScore = avarageScore
        self.__universityRank = universityRank

    @property
    def avarageScore(self):
        return self.__avarageScore

    @avarageScore.setter
    def avarageScore(self, score):
        self.__avarageScore = score

    @property
    def universityRank(self):
        return self.__universityRank

    @universityRank.setter
    def universityRank(self, rank):
        self.__universityRank = rank

    def scoreComputing(self):
        grade = 0
        universityGrade =  0
        if self.__universityRank == 1 :
            universityGrade = 100
        elif self.__universityRank == 2 :
            universityGrade = 80
        elif self.__universityRank == 3 :
            universityGrade = 60
        if self.__avarageScore < 17.5 and self.__avarageScore > 16 :
            grade = 60
        elif self.__avarageScore < 18.5 and self.__avarageScore > 17.5:
            grade = 80
        elif self.__avarageScore > 18.5 :
            grade = 100

        return (grade + universityGrade)/2

    def __str__(self):
        return self._showInfo()
    
class EmployeeParticipant(Participant):
    def __init__(self, name, family, personId, studyField, address, workingYears, performanceAvarage):
        super().__init__(name, family, personId, studyField, address)
        self.__workingYears = workingYears
        self.__performanceAvarage = performanceAvarage

    @property
    def performanceAvarage(self):
        return self.__performanceAvarage

    @performanceAvarage.setter
    def performanceAvarage(self, degree):
        self.__performanceAvarage = degree

    @property
    def workingYears(self):
        return self.__workingYears

    @workingYears.setter
    def workingYears(self, year):
        self.__workingYears = year

    def scoreComputing(self):
        if self.__workingYears < 5 :
            return self.__performanceAvarage + (self.__performanceAvarage * 0.1)
        else:
            return self.__performanceAvarage + (self.__performanceAvarage * 0.2)

    def __str__(self):
        return self._showInfo()
    #------------------------------------------------------objects
participantList = []
acceptedList = []
for item in range(1):
    name = input("Enter your name:")
    family = input("Enter your family:")
    id = input("Enter PersonId:")
    field = input("Enter field of study:")
    address = input("Enter your address:")
    interviewScore = int(input("Enter interview Score:"))
    testScore = int(input("Enter testS core:"))
    pf = FreeParticipant(name, family, id, field, address, interviewScore, testScore)
    participantList.append(pf)
    if pf.scoreComputing() >= 90 :
        print(pf.scoreComputing())
        acceptedList.append(pf)
    print("-------------------------")

for item in range(1):
    name = input("Enter your name:")
    family = input("Enter your family:")
    id = input("Enter PersonId:")
    field = input("Enter field of study:")
    address = input("Enter your address:")
    avarageScore = int(input("Enter avarage Score:"))
    universityRank = int(input("Enter testS university rank:"))
    pe = EliteParticipant(name, family, id, field, address, avarageScore, universityRank)
    participantList.append(pe)
    if pe.scoreComputing() >= 90 :
        print(pe.scoreComputing())
        acceptedList.append(pe)
    print("-------------------------")

for item in range(1):
    name = input("Enter your name:")
    family = input("Enter your family:")
    id = input("Enter PersonId:")
    field = input("Enter field of study:")
    address = input("Enter your address:")
    workingYears = int(input("Enter avarage Score:"))
    performanceAvarage = int(input("Enter testS university rank:"))
    pm = EmployeeParticipant(name, family, id, field, address, workingYears, performanceAvarage)
    participantList.append(pm)
    if pm.scoreComputing() >= 90 :
        print(pm.scoreComputing())
        acceptedList.append(pm)
    print("-------------------------")
for item in acceptedList:
    print(item)
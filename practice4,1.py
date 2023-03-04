class Student:
    schoolName = "sarmad primary school"
    def __init__(self, studentId, name, family, level) :
        self.studentId = studentId
        self.name = name
        self.family = family
        self.level = level
    
    @staticmethod
    def showCours(level):
        courseList = []
        if level == 1:
            courseList1 = ["mathematic", "language", "science"]
            courseList = courseList1
        elif level == 2:
            courseList2 = ["mathematic", "language", "science", "sport"]
            courseList =courseList2
        elif level == 3:
            courseList3 = ["mathematic", "language", "science", "sport", "geography"]
            courseList = courseList3
        elif level == 4:
            courseList4 = ["mathematic", "language", "science", "sport", "geography", "art"]
            courseList = courseList4
        elif level == 5:
            courseList5 = ["mathematic", "language", "science", "sport", "geography", "art", "history"]
            courseList = courseList5
        elif level == 6:
            courseList6 = ["mathematic", "language", "science", "sport", "geography", "art", "history"]
            courseList = courseList6
        for item in courseList:
            print(item, end = ". ")
        print("\n")
    @classmethod
    def changeScoolName(Student, name):
        Student.schoolName = name
        return Student.schoolName
    def __hash__(self):
        return hash(self.studentId) + hash(self.name) + hash(self.family) + hash(self.level)
        
    def __eq__(self, object2):
        return self.studentId == object2.studentId and self.name == object2.name and self.family == object2.family and self.level == object2.level

    def __str__(self):
        return f"Id : {self.studentId}\t Name: {self.name}\t Family: {self.family}\t Level: {self.level}"

#-------------------------------------objects
students = set()
for item in range(10):
    id = int(input("Enter student ID:"))
    name = input("Enter student name:")
    family = input("Enter student family:")
    level = int(input("Enter student level:"))
    student = Student(id, name, family, level)
    students.add(student)
    print("------------------------")

for item in students:
    print(item)
    print(hash(item))
print("**************************")
level = int(input("Enter level courses:"))
Student.showCours(level)

s1 = Student(12, "ali", "ahmadi", 3)
for item in students:
    x = False
    if item == s1 :
        print("yes")
        x = True
        break
if x == False:
    print("no")
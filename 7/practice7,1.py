#-----------------------------------libraries
from datetime import *
from khayyam import *
#-----------------------------------
name = input("Enter name: ")
family = input("Enter family: ")
date1 = input("Enter Date of Birth: for example: 1380-08-08: ").split("-")
year, month, day = [int(item) for item in date1 ]
JD = JalaliDate(year, month, day)
dateOfBirth = [year, month, day]

def personInfo(a, b, c, d):
        if d == True:
                print(f"Dear  {name}\t {family}, \n You are now eligibleto get a COVID-19 vaccination.")
        else :
                print(f"Dear  {name}\t {family}, \n You are not eligibleto get a COVID-19 vaccination.")
def check_Birth_Date(name, family, *dateOfBirth):
        person = [name, family, dateOfBirth]
        personBD = list(dateOfBirth)
        deserveVaccine = False
        if personBD[0] < 1340 :
                deserveVaccine = True
        person.append(deserveVaccine)
        personInfo(*person)

check_Birth_Date(name, family, *dateOfBirth)
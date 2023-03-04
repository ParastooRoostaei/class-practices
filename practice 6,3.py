from datetime import *
from khayyam import *
def dateInJalali():
        inputDate = input("Enter Date (For Example: 1399-06-20)").split("-") 
        year, month, day = [int(item) for item in inputDate]
        d = JalaliDate(year, month, day)
        yield d
        miladdiDate = d.todate()
        yield miladdiDate
        momentDate = date.today()
        dayDiff = momentDate - miladdiDate
        yield dayDiff


for item in dateInJalali():
        print(item)

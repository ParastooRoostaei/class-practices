import re
import os
f = open("information.txt", "r")
filePerson = f.read()
print(filePerson)
p1 = ""
person = "Name, Family, Mobile, Postal Code, city\n"
p = re.findall(r'Name:\w+,Family:\w+,Mobile:0912\d{7},Postal Code:\d{10},city:\w+',filePerson)
for item in p:
        p1 += str(item) + '\n'
person += re.sub(r'Name:(\w+),Family:(\w+),Mobile:(0912\d{7}),Postal Code:(\d{10}),city:(\w+)','\g<1>,\g<2>,\g<3>,\g<4>,\g<5>', p1)
with open ('personInfow.csv', 'a') as personI:
        personI.write(person)
f.close()
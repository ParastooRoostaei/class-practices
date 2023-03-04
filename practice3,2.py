class Address:
    def __init__(self, cityName, streetName, number):
        self.cityname = cityName
        self.streetName = streetName
        self.number = number
        self.address = {}

    def addAddressContent(self):
        self.address["Number"] = self.number
        self.address["Street"] = self.streetName
        self.address["City"] = self.cityname
        return self.address

    def showInfo(self):
        return f"Number: {self.number}\t, {self.streetName}\t, {self.cityname} "

class Person:
    def __init__(self, customerId, name, family, contactNumber, emailAddress):
        self.customerId = str(customerId)
        self.name = name
        self.family = family
        self.contactNumber = contactNumber
        self.emailAddress = emailAddress
        self.person = {}

    def addPersonContent(self):
        self.person["ID"] = self.customerId
        self.person["Name"] = self.name
        self.person["Family"] = self.family
        self.person["Mobile"] = self.contactNumber
        self.person["Email"] = self.emailAddress
        return self.person

    def showInfo(self):
        return f"Customer ID: {self.customerId}\tName: {self.name}\tFamily: {self.family}\tMobile: {self.contactNumber}\tEmail: {self.emailAddress}"

class Contact(Address,Person):
    def __init__(self, cityName, streetName, number, customerId, name, family, contactNumber, emailAddress):
        Address.__init__(self, cityName, streetName, number)
        Person.__init__(self, customerId, name, family, contactNumber, emailAddress)
        self.contact = {}

    def addContactInfo(self):
        c1 = self.addAddressContent()
        c2 = self.addPersonContent()
        for item in (c1,c2):
            self.contact.update(item)
        return self.contact

    def showInfo(self):
        Address.showInfo(self)
        Person.showInfo(self)

class PhoneBook:
    def __init__(self):
        self.phoneBook = []

    def addContact(self, input1):
        self.phoneBook.append(input1)
        return self.phoneBook

    def showPhoneBookInfo(self):
        for item in self.phoneBook:
            print(item)

    def searchCustomer(self, family):
        searchlist = []
        for item in self.phoneBook:
            if item["Family"] == family:
                searchlist.append(item)
        if searchlist == []:
            print("Unknown Customer")
        else :
            for contact in searchlist:
                print(contact)
                contact = Contact(contact["City"], contact["Street"], contact["Number"],contact["ID"], contact["Name"], contact["Family"], contact["Mobile"], contact["Email"])
                contact.showInfo()
    

c1 = Contact("Tehran", "Bahar", 32, 36, "Ali", "Mohseni", "098765", "hjfriufgu@yahoo.com")
contacts1 = c1.addContactInfo()
c2 = Contact("Mashhad", "Nofel", 16, 67, "Bahar", "Razavi","0935746586", "jduifgz@google.com")
contacts2 = c2.addContactInfo()

phoneBook = PhoneBook()
phoneBook.addContact(contacts1)
phoneBook.addContact(contacts2)
phoneBook.showPhoneBookInfo()
print("------------------------")
phoneBook.searchCustomer("Ali")
phoneBook.searchCustomer("Mohseni")

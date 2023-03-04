customerList = ["Sara Ahmadi", "Ali Rezaee", "Bahar Sadr", "Ahmad Majedpoor", "Iman Mohammadi", "Mina Bavandpoor"
, "Mohammad Alimoradi", "Majid Rafiee", "Sima Sefidiyan"]
customerSpecial = ["Vahid Abdoli", "Ali Rezaee", "Bahar Sadr", "Sima Sefidiyan"]
def monthSpecialList(list1):
        list3 = []
        for item in customerList:
                if item == list1:
                        list3.append(item)
        return list3
print(list(filter(monthSpecialList, customerSpecial)))

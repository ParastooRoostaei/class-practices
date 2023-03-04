shoppingList1 = ["milk", "cheese", "butter", "tomato", "banana", "apple"] 
shoppingList2 = ["orange", "cheese", "kiwi", "tomato","banana", "butter"]

def compareList(list1, list2):
        list3 = []
        if list1 == list2:
                list3.append(list1)
        return list3

endList = list(map(compareList, shoppingList1, shoppingList2))
for item in endList:
        if item != []:
                print(item)
#--------------------------two price list of 10 product for two store
productPriceList1 = [5000,10000,15000,6000,25000,12000,14000,10000,7000,20000]
productPriceList2 = [4000,12000,16000,5000,22000,10000,16000,11000,5000,18000]
#--------------------------
class ProductPrice :
    def __init__(self, productPriceList):
      self.productPriceList = productPriceList

    def __add__(self, obj2):
        templist = []
        for item in range(0, len(self.productPriceList)):
            sum = self.productPriceList[item]+obj2.productPriceList[item]
            templist.append(sum)
        return templist
    
    def __sub__(self, obj2):
        templist = []
        for item in range(0, len(self.productPriceList)):
            sub = self.productPriceList[item]-obj2.productPriceList[item]
            templist.append(sub)
        return templist

    def __mul__(self, number):
        tempList = []
        for item in range(0, len(self.productPriceList)):
            mul = self.productPriceList[item]*number
            tempList.append(mul)
        return tempList

    def __truediv__(self, number):
        tempList =[]
        for item in range(0, len(self.productPriceList)):
            div = self.productPriceList[item]/number
            tempList.append(div)
        return tempList

    def __lt__(self, obj2):
        tempList = []
        for item in range(0, len(self.productPriceList)):
            tempList.append(self.productPriceList[item]<obj2.productPriceList[item])
        return tempList
#------------------------------------------------------------create objects
p1 = ProductPrice(productPriceList1)
p2 = ProductPrice(productPriceList2)
print(p2.productPriceList)
sum = p1 + p2
print(sum)
print("sssssssssssssssssssssssss")
p3 = ProductPrice(sum)
div = p3.__truediv__(2)
print(div)
print("avrageeeeeeeeeeeeeeeeeeeeeee")

def mainFunc(func):
        def func1(mL):
                integerPoitiveList = []
                for i in mL:
                        if i > 0 :
                                if type(i) == int :
                                        integerPoitiveList.append(i)
                print(func(integerPoitiveList))
        return func1
@mainFunc
def factoriel(myList):
        list2 = []
        for number in myList:
                x = 1
                for i in range (1,number+1):
                        x *= i
                list2.append(x)
        return list2


l = [-2, 5, 3, 3.6]
factoriel(l)

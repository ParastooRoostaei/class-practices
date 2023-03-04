class Counter:
        def __init__(self, start, end):
                self.start = start
                self.end = end

        def __iter__(self):
                return self

        def __next__(self):
                number = self.start
                if (number > self.end) :
                        print("end")
                        raise StopIteration
                else :
                        self.start += 3
                        return number

c1 = Counter(10, 100)
for item in c1:
        print(item , end = "\t")
        
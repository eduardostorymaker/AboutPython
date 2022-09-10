import time

class FiboIter():

    def __init__(self,max = 0):
        self.max = max 

    def __iter__(self):
        self.n1 = 0
        self.n2 = 1
        self.counter = 0
        return self

    def __next__(self):
        if (not self.max or self.counter <= self.max-1) and self.max > 0:
            if self.counter == 0:
                self.counter += 1
                return self.n1
            elif self.counter == 1:
                self.counter += 1
                return self.n2
            else:
                self.counter += 1
                self.aux = self.n1 + self.n2
                self.n1, self.n2 = self.n2, self.aux
                return self.aux
        else:
            raise StopIteration

class EvenNumbers:

    def __init__(self,max=None):
        self.max = max
    
    def __iter__(self):
        self.num = 0
        self.count = 0
        return self

    def __next__(self):
        if (not self.max or self.count <= self.max-1)and self.max>0:
            result = self.num
            self.num += 2
            self.count += 1
            return result
        else:
            raise StopIteration
        


if __name__ == "__main__":
    fibonacci = FiboIter(5)

    for element in fibonacci:
             print(element)

        #time.sleep(1)
        
    # pares = EvenNumbers(0)
    # for par in pares:
    #     print(par)

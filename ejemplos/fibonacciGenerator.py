import time

def FibonacciGenerator(max = None):
    n1 = 0
    n2 = 1
    counter = 0

    while True:
        if counter <= max-1 and max > 0:
            if counter == 0:
                counter += 1
                yield n1
            elif counter == 1:
                counter += 1
                yield n2
            else:
                aux = n1 + n2
                counter += 1
                n1,n2 = n2,aux
                yield aux
        else:
            raise StopIteration

fibonacci = FibonacciGenerator(10)

for element in fibonacci:
    print(element)
    #time.sleep(1)


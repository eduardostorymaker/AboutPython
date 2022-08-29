

def es_primo(evaluar):
    for i in range(2,evaluar):
        #print(i)
        if evaluar%i == 0:
            #print("divisible")
            return False
            break
    return True

def run():
    evaluar = int(input("ingresa el numero limite para los primos: "))
    #evaluar = 5

    for i in range(1,evaluar+1):
        if es_primo(i) == True:
            print(i)
            #print(str(i)+" es primo")
        else:
            #print(str(i)+" no es primo")
            continue


if __name__ == '__main__':
    run()
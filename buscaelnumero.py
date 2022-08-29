import random


def evaluar(numero,aleatorio):
    if numero == aleatorio:
        print("acertaste!")
        return False
        Break
    elif numero>aleatorio:
        print("prueba un numero menor!")
    else:
        print("intenta un nuero mayor!")
    return True


def run():
    print("funciona")

    LIMITE = 100

    numero = int(input("ingrese el numero entre 1 y 100: "))
    aleatorio = random.randint(1,100)

    estado = True
    while estado:
        if numero == aleatorio:
            print("acertaste!")
            estado=False
        elif numero>aleatorio:
            numero = int(input("prueba un numero menor! "))
        else:
            numero = int(input("intenta un nuero mayor! "))
    return True

if __name__ == '__main__':
    run()
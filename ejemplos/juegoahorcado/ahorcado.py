import random
import os

def leer_palabras():
    palabras = []
    with open("./listapalabras.txt","r") as f:
        #for line in f:
        #    lista_palabras.append(line.strip("\n"))
        palabras = [line.strip("\n") for line in f]
    return palabras

def elegir_palabra(lista):
    elegido = random.randint(0,len(lista)-1)
    return lista[elegido]

def leer_ingreso():
    letra = input("Ingrese una letra: ")
    return letra

def verificar_letra(palabra_buscada,palabra_usuario,letra):
    palabra_buscada = list(enumerate(palabra_buscada))

    for posicion,valor in palabra_buscada:
        if valor == letra:
            palabra_usuario[posicion] = letra
    return palabra_usuario

def verificar_si_gano(palabra_buscada,palabra_usuario):
    gano = False
    if palabra_buscada == palabra_usuario:
        gano = True
    return gano

def imprimir_pantalla(palabra_usuario):
    os.system("clear")
    print("")
    print("Juego del Ahorcado!!!!")
    print("")
    for letra in palabra_usuario:
        if letra=="":
            print("__",end=" ")
        else:
            print(" "+letra,end="  ")
    print("")
    print("")

def run():
    print("Bienvenido")
    lista_palabras = leer_palabras()
    palabra_elegida = elegir_palabra(lista_palabras)
    palabra_buscada = [letra for letra in palabra_elegida]
    palabra_usuario = ["" for letra in palabra_elegida]
    
    gano = False
    while not gano:
        imprimir_pantalla(palabra_usuario)
        letra = leer_ingreso()
        palabra_usuario = verificar_letra(palabra_buscada,palabra_usuario,letra)
        gano =  verificar_si_gano(palabra_buscada,palabra_usuario)

    if gano:
        imprimir_pantalla(palabra_usuario)
        print("Felicidades!!! Gano el Juego!!!")



if __name__ == "__main__":
    run()
# Basic Python
> Let's go to learn basic Python - 2022

## Operators

### Math

| Detail | Operator  | 
| ------ | ------ |
| Addition  | + |
| Subtraction | - |
| Multiplication | * |
| Division | / |
| Modulus | % |
| Floor division | // |
| Exponentation | ** |

### Comparison

| Detail | Operator  | 
| ------ | ------ |
| Equal | == |
| Not equal | != |
| Greather than | > |
| Less than | < |
| Greather than or equal to | >= |
| Less than or equal to | <= |

### Logic

| Detail | Operator  | 
| ------ | ------ |
| and | and |
| or | or |
| not | not |


## Strings
Functions with strings:
~~~
mystring = 'test With strings'
~~~
- How to do: 'TEST WITH STRINGS'
~~~
mystring.upper()
~~~
- How to do: 'Test with strings'
~~~
mystring.capitalize()
~~~
- How to do: 'test with strings'
~~~
mystring.lower()
~~~
- How to do: 'test wath strangs'
~~~
mystring.replace('i','a')
~~~
#####
Strings are lists, then we can use as lists:
**my_string[ begin: how many : steps ]**

- How to get: 't'
~~~
mystring[0]
~~~
- How to get: 'st W'
~~~
mystring[2:6]
~~~
- How to get: 'est With string'
~~~
mystring[1:-1]
~~~
- How to get: 'test '
~~~
mystring[:5]
~~~
- How to get: 'st With strings'
~~~
mystring[2:]
~~~
- How to get: 'ts ihsrns'
~~~
mystring[::2]
~~~
- How to get: 'sgnirts htiW tset'
~~~
mystring[::-1]
~~~
- What is the lenght? 
~~~
len(mystring)
~~~
#####
~~~
mystring2 = '   this is a weird /n text     '
~~~
- How to do: 'this is a weird /n text'
~~~
mystring2.strip()
~~~
#####
We can use variables in strings:
If we want 'Numbers: 5 7 9':
~~~
"Numbers: {0} {1} {2}". format(5, 7, 9)
~~~
~~~
"Numbers: {x} {y} {z}". format(x=5, y=7, z=9)
~~~
~~~
x=5
y=7
z=9
f'Numbers: {x} {y} {z}'
~~~
#####
We also can create a string from a list:
If we want 'one, two, three':
~~~
mystring3 = ", ".join(["one","two","three"])
~~~
#####
We also can create a list from a string:
If we want ['one', 'two', 'three']:
~~~
mystring3.split(", ")
~~~



## Ranges

range(inicio,fin,pasos) el fin no es inclusivo, empieza del cero hasta el fin -1
~~~
[0,1,2,3,4]
~~~
```sh
list(Range(5))
```
```sh

list(Range(1,5)) /[1,2,3,4]
```
```sh
list(Range(1,5,2)) /[1,3]
```
```sh
list(Range(7,3,-1)) /[7,6,5,4]
```

for contador in range(0,1000):
	print(contador)

for letra in nombre:
	print(letra)

## Lists

lista = [1,2,5,7]
5 in lista /true
lista.append(9) /agrega el 9 al final
lista.pop(2) /borra el objeto de posicion 2
lista.pop() /borra el ultimo numero
lista.insert(0,9) /inserta 9 en la posicion 9
lista.index(2) /devuelve el indice del primer valor 2 -> 1 
lista[::-1] /concatena listas
lista*5 /multiplica la lista
max(lista) /devuelve el mayor valor -> 7
min(lista) /devuelve el menor valor -> 1
lista.count(5) /cuenta cuantas veces se repite el valor 5
lista.remove(7) /remueve el primer item que encuentra con ese valor
lista.reverse() /invierte el orden de la lista
----
lista.clear()
lista.sort()
lista.sort(revere =true)
----

a = [1,2,3]
b = a /en este caso asigna la misma posicion de memoria a is b true, si modificas uno, se modificara el otro, no se deben igualar listas se debe de clonar
b = list(a) /ahora son distintos objetos, tienen distintas direcciones de memoria

## Tuples

tupla = (1,2,3,4,5) /es estatico, no se puede modificar
tupla2 = "uno", "dos", "tres"
/desempaquetar valores
a,b,c = tupla2 / a="uno", b="dos", c="tres"
a,b,*c,d = [1,2,3,4,5,6,7,8,9] / a=1, b=2, c=[3, 4, 5, 6, 7, 8], d=9
tupla = (1,) / si se ingresa integer = (1), resulta un integer, la tupla debe de tener comas (tupla de un valor)


## Sets

//no tiene valores repetidos y son inmutables
miset = {1,1,1,1,1,1,1,2,3,4,5,5,5,5,5,5} /{1, 2, 3, 4, 5}
3 in miset / true
/añadir 1 elemento
miset.add(6) /{1, 2, 3, 4, 5, 6}
/eliminar un elemento existente, si no esta en la lista envia error
miset.remove(2) //{1, 3, 4, 5, 6}
/eliminar un elemento inexistente, si esta en la lista, lo borra, si no esta, devuelve el mismo set
miset.discard(2) 
/elimina un elemento aleatorio
miset.pop()
/borra todo el set
miset.clear()

/añadir multiples elementos
miset.update([1,2,3])
miset.update((1,2,3),{4,5})

/para crear un set vacio se debe de utilizar un constructor, {}, esto crea un diccionario vacio
miset = set()

uno = {1,2,3,4,5,6}
dos = {4,5,6,7,8,9}
print(uno|dos) /{1, 2, 3, 4, 5, 6, 7, 8, 9}
print(uno&dos) /{4, 5, 6}
print(uno-dos) /{1, 2, 3}
print(dos-uno) /{8, 9, 7}
print(dos^uno) /{1, 2, 3, 7, 8, 9}

//otra opcion
set1.union(set2)
set1.symmetric_difference(set2)
set1.difference(set2)
set1.intersection(set2)

/para convertir una lista en set
miset = set(lista)
/convertir tupla en set
miset = set(tupla)

## Dictionaries

diccionario = {
	'llave1': 1,
	'llave2': 2,
	'llave3': 3,
}
//agregar datos
diccionario['llave4'] = 4
//consultas
diccionario['llave1']
diccionario['llave2']
diccionario['llave3']
diccionario.get('llave1')
diccionario.get('llave5','valor no determinado')
del diccionario['llave1']
'llave1' in diccionario /false
'llave2' in diccionario /true

for llave in diccionario.keys():
	print(llave)

for valor in diccionario.values():
	print(valor)

for llave,valor in diccionario.items():
	print(llave)
	print(valor)


## Estructures

### Conditional

### Itera

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
Strings are lists, then we can use them as lists:
**my_string[ begin: how many : steps ]**
~~~
mystring = 'test With strings'
~~~
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
We also can create a string from a list.
If we want **'one, two, three'**:
~~~
mystring3 = ", ".join(["one","two","three"])
~~~
#####
We also can create a list from a string.
If we want **['one', 'two', 'three']**:
~~~
mystring3.split(", ")
~~~

- How to print all letters from string
~~~
mystring4 = "print this string"
for letter in mystring4:
	print(letter)
~~~

## Ranges

**range(begin: how many : steps)**
- How to get: **[0,1,2,3,4]**
~~~
list(Range(5))
~~~
- How to get: **[1,2,3,4]**
~~~
list(Range(1,5))
~~~
- How to get: **[1,3]**
~~~
list(Range(1,5,2))
~~~
- How to get: **[7,6,5,4]**
~~~
list(Range(7,3,-1))
~~~

- How to print numbers from 0 to 9
~~~
for counter in range(0,10):
	print(counter)
~~~


## Lists

Functions with lists:
~~~
mylist = [1,2,5,7]
~~~
- Add 9 at the end: **[1, 2, 5, 7, 9]**
~~~
mylist.append(9)
~~~
- Remove the thirth position: **[1, 2, 7, 9]**
~~~
mylist.pop(2)
~~~
- Remove the last position: **[1, 2, 7]**
~~~
mylist.pop()
~~~
- Insert 9 in the first position: **[9, 1, 2, 7]**
~~~
mylist.insert(0,9)
~~~
- Find the number 9 index : **0**
~~~
mylist.index(9)
~~~
- Invert the list: **[7, 2, 1, 9]**
~~~
mylist[::-1]
~~~
- Multiply the list five times: **[9, 1, 2, 7, 9, 1, 2, 7, 9, 1, 2, 7, 9, 1, 2, 7, 9, 1, 2, 7]**
~~~
mylist*5
~~~
- Find the max value: **9**
~~~
max(mylist)
~~~
- Find the min value: **1**
~~~
min(mylist)
~~~
- Count how many 5s there are in the list: **0**
~~~
mylist.count(5)
~~~
- Remove the number 7: **[9, 1, 2]**
~~~
mylist.remove(7)
~~~
- Revert the list: **[2, 1, 9]**
~~~
mylist.reverse()
~~~
- Sort the list: **[1, 2, 9]**
~~~
mylist.sort()
~~~
- Invert sort the list: **[9, 2, 1]**
~~~
mylist.sort(reverse=True)
~~~
- Clear the list: **[]**
~~~
mylist.clear()
~~~

## Tuples
How about tuples, they are inmutables, you can't change the values, but you can assign other tuple.
~~~
mytuple = (1,2,3,4,5)
~~~
~~~
mytuple2 = "uno", "dos", "tres"
~~~
unpackage the values: a="uno", b="dos", c="tres"
~~~
a,b,c = mytuple2  
~~~
unpackage the values: a=1, b=2, c=[3, 4, 5, 6, 7, 8], d=9
~~~
a,b,*c,d = [1,2,3,4,5,6,7,8,9]
~~~


## Sets
How about sets, they don't have repeated values.
If i assign repeated values, the result will be unrepeated values.
~~~
myset = {1,1,1,1,1,1,1,2,3,4,5,5,5,5,5,5}
~~~
~~~
{1, 2, 3, 4, 5}
~~~
- Add number 6: **{1, 2, 3, 4, 5, 6}**
~~~
myset.add(6)
~~~
- Remove number 2 (if it does't exist, the result will be an error): **{1, 3, 4, 5, 6}**
~~~
myset.remove(2)
~~~
- Discard number 2 (if it does't exist, the result will be the same set): **{1, 3, 4, 5, 6}**
~~~
myset.discard(2) 
~~~
- Remove a random element
~~~
myset.pop()
~~~
- Clear all the set: **{}**
~~~
myset.clear()
~~~

/añadir multiples elementos
myset.update([1,2,3])
myset.update((1,2,3),{4,5})

/para crear un set vacio se debe de utilizar un constructor, {}, esto crea un diccionario vacio
myset = set()

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

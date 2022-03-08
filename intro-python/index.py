
from operator import truediv


# if 5 > 3:                    # * este es el operador mayor que > 
#    print('5 es mayor a 3')
  
# if 3 > 6: 
#    print('Esto no se va a imprimir')

            # ? Variables

x = 6
y = 'chanchito feliz'
# print(x, y)

email = 'angel@angel.com'
# print(email)

miVar = 'chanchito'


            # ? Multiples variables 

a, b, c = 'lala', 'lele', 'lolo'
# print(a, b, c);

valor1 = valor2 = valor3 = 'chanchito feliz'
# print(valor1, valor2, valor3)


            # ? Concatenacion

inicio = 'Hola '
final = 'mundo'

# print(inicio + final);


            # ? Strings y numeros 


palabra = 'Hola mundo'    # String
oracion = "hola mundo comilla doble"

entero = 20          # integer
decimal = 20.2        # float
complejo = 1j         # complex

# print(palabra, oracion, entero, decimal, complejo)


            # ? Listas


lista = [3, 'hola', 3, 3, 3]      # * Esto es una lista o array 
lista2 = lista.copy()     # * Copiamos la lista en una nueva variable

lista.append(4)         # * Asi se agregan valores a la lista 
#lista.clear()           # * Elimina todos los elementos dentro de la lista

#print('lista 1:',lista,'lista 2:' , lista2)


            # ? Contando elementos y calculando el largo de una lista


#print('count:' ,lista.count(3), lista2.count(9))    # * count, cuenta el numero de veces que aparece el parametro que se le pasa.a

#print( 'len: lista = ' ,len(lista), '; lista 2 = ', len(lista2))               # * len, mide el largo del array

largoLista = len(lista)
largoLista2 = len(lista2)


#print('largoLista:', largoLista, 'largoLista2:', largoLista2)

#print(lista[0])
#print(lista[1])


           # ? Eliminando elementos de una lista

lista3 = ['hola', 'buenas', 'como', 'esta', 'qwer', 1, True]

lista3.pop();       # * Elimina el ultimo elemento de la lista

#print('Eliminado el ultimo elemento:'  ,lista3)

lista3.remove('qwer')

#print('Eliminando un elemento en especifico: qwer', lista3)

            # ? Reverse y sort 

lista4 = lista3.copy()
lista4.pop()
lista4.reverse()
# lista4.sort() # Esto no funciona porque no puede ordernar strings y enteros
# todo: Solo se pueden ordenar con sort() listas del mismo tipo. 

# print('Lista invertida:', lista4)

lista4.sort()
# print('lista invertida y ordenada', lista4)


               # ? Tuplas

# * las tuplas tienen mucho menos propiedades que las listas y usa () en lugar de [];

tupla = ('hola', 'mundo', 'que', 'hace')
# tupla.append('de bueno') Est no va a funcionar porque no posee el metodo append();
# todo: Hay que convertir la tupla en una lista: 

listaDeTupla = list(tupla)
listaDeTupla.append('de bueno')

# print('lista de tupla:', listaDeTupla)


               # ? Rangos

rango = range(6)
# print('Rango:', rango) # Esto indica que el rango va de 0 hasta 6.


               # ? Diccionarios

# Los diccionarios son como los objetos en javaScript

diccionario = {
   "nombre": "Chanchito feliz",
   "raza": "Persa",
   "edad": 5,
   "color": "rojo"
}


# print('diccionario:', diccionario)
# print('diccionario["raza"]:', diccionario["raza"])
# print('diccionario["edad"]:', diccionario["edad"])
# print('diccionario["nombre"]:', diccionario["nombre"])

# print(diccionario.get('color'))

   # * Cambiar valores de los diccionarios

diccionario['nombre'] = 'Fluffy';

# print('nuevo diccionario' ,diccionario)
# print( 'lentgh de diccionario:' ,len(diccionario))


               # ? Profundizando en diccionarios

   # * Agregar y eliminar valores a los diccionarios 

# Asi se agrega un elemento: 

diccionario['ronronea'] = True
# print(diccionario)

# copiaGatito = diccionario.copy()    # ? Asi podemos hacer una copia
copiaGatito = dict (diccionario)       # ? Otra manera de hacer copias.
# Asi se elimina un elemento: 

# diccionario.pop('ronronea')
# diccionario.popitem()
# del diccionario['ronronea'] # ! Esta opcion elimina solo el elemento deseado
diccionario.clear()           # ! Esta opcion elimina todo el contenido dentro del diccionario.

#print('copiaGatito:', copiaGatito)
#print('diccionario:', diccionario)


            # ? Diccionarios anidados y constructor dict 

# Diccionarios Anidados

fluffy = { 
   "nombre": "fluffy",
   "edad": 4,
}
mamba = { 
   "nombre": "Black mamba",
   "edad": 12,
}
gatitos = { 
   "Fluffy": fluffy,
   "Mamba": mamba,
}

print('Gatitos:', gatitos)


# Constructor Dict: 

perritos = dict (nombre = 'Chanchito feliz', edad = 8,)

print('Perritos:', perritos)


            # ? Booleanos

verdadero = True
falso = False

print('verdadero: ', verdadero, 'falso:', falso)

from curses import init_color
from unicodedata import decimal


if 5 > 3:                    # * este es el operador mayor que > 
   print('5 es mayor a 3')
  
if 3 > 6: 
   print('Esto no se va a imprimir')

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


lista = [3, 3, 3, 3, 3]      # * Esto es una lista o array 
lista2 = lista.copy()     # * Copiamos la lista en una nueva variable

lista.append(4)         # * Asi se agregan valores a la lista 
#lista.clear()           # * Elimina todos los elementos dentro de la lista

print('lista 1:',lista,'lista 2:' , lista2)


  # ? Contando elementos y calculando el largo de una lista

# print('count:' ,lista.count(3), lista2.count(9))    # * count, cuenta el numero de veces que aparece el parametro que se le pasa.a
#print( 'len: lista = ' ,len(lista), '; lista 2 = ', len(lista2))               # * len, mide el largo del array

largoLista = len(lista)
largoLista2 = len(lista2)

print('largoLista:', largoLista, 'largoLista2:', largoLista2)














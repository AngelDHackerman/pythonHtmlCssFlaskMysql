
# ? multiplicar dos números sin usar el símbolo de multiplicación

from cmath import pi


def multiplicar (multiplicador1, multiplicador2):
  contador = multiplicador1
  for i in range(multiplicador2 - 1):
    contador += multiplicador1
  print(multiplicador1, '*', multiplicador2, ':', contador)

multiplicar(5, 4)

          # Respuesta del profesor: 

a = 4
b = 8
resultado = 0

for x in range(a):
    resultado += b

print(resultado)


# ? ingresar nombre y apellido e imprimirlo al reves

def invertirNombre (nombre, apellido):
  nombreCompleto = nombre + ' ' + apellido
  cadenaInvertida = ''
  for letra in nombreCompleto:
    cadenaInvertida = letra + cadenaInvertida
  print(cadenaInvertida)

invertirNombre('angel', 'hernandez')

# Respuesta del profesor: 

nombre = 'Nicolas'
apellido = 'Feliz'

concatenacion = nombre + ' ' + apellido

print(concatenacion[::-1])


# ? escribir una función que encuentre el elemento menor de una lista

def numberoMenor (lista):
  lista.sort()
  print(lista[0])

numberoMenor(lista = [23, 25, 26, 39, 49, 20, 100])

# Respuesta del profesor
                      # todo: Ver el video donde explica como funciona esto

lista2 = [1, 2, 5, 3, 55, -24, -13]

menor = 'init'

for x in lista2:
    if menor == 'init':
        menor = x
    else:
        menor = x if x < menor else menor

print('menor', menor)


# ? escribir una función que devuelva el volumen de una esfera por su radio
# ? 4/3 * pi * r ** 3

def volumen_espefa (radio):
  area = 4/3 * pi * radio ** 3
  area = round(area, 2)
  print(area, 'cm3')

volumen_espefa(6)

# Respuesta del profesor 

def calculaVolumen(r):
    return 4 / 3 * 3.14 * r ** 3

resultado = calculaVolumen(6)
print(resultado)


# ? escribir una función que indique si el usuario es mayor de edad

def mayorDeEdad (edad):
  if edad >= 18 :
    print('Eres mayor de edad')
  else:
    print('Aun eres menor')

mayorDeEdad(26)


# ? escribir una función que indique si un número es par o impar

def parImpar (numero):
  if numero % 2 == 0:
    print('Este es un numero par ;)')
  else: 
    print('Es un numero impar!')

parImpar(26)


# ? escribir una función que indique cuantas vocales tiene una palabra





# ? escribir una aplicación que reciba una cantidad infinita de números hasta
# ? decir basta, luego que devuelva la suma de los números ingresados





# ? escribir una función que reciba nombre y apellido y los vaya agregando a
# ? un archivo






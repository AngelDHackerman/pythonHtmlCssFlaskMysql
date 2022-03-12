
#           # * Leyendo archivos en python

# c = open('./chanchito.txt', 'a')

# # print(c.readline())


#           # * leer lineas 1 a 1

# # print(c.read())

# for x in c:             # ? Asi podemos leer todas las lineas usando el ciclo for
#   print(x)



# c.close()                     # ? Siempre es bueno darle close a los archivos leidos

# # c.write('Agregaremos una nueva linea al nuestro archivo')         # ? Asi agregamos texto al documento

# x = open ('./chanchito.txt', 'r')

# print(x.read())


                    # ? Eliminando archivos y carpetas 

import os

if os.path.exists('chanchito.txt'):
  os.remove('./chanchito.txt')        # * Asi se eliminan los archivos usando python
else: 
  print('El archivo no existe')


if os.path.exists('miCarpeta'):
  os.rmdir('./miCarpeta')
else:
  print('La carpeta no existe')


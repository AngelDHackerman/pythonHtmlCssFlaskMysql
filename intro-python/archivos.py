
          # * Leyendo archivos en python

c = open('./chanchito.txt')

# print(c.read())


          # * leer lineas 1 a 1

print(c.readline())
print(c.readline())
print(c.readline())

for x in c:             # ? Asi podemos leer todas las lineas usando el ciclo for
  print(x)



c.close()                     # ? Siempre es bueno darle close a los archivos leidos






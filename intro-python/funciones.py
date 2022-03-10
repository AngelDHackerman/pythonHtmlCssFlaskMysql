            # ? Funciones

def miFuncion():
  print('Mi primera funcion en python')

# miFuncion()


def imprimeNombre (nombre, apellido): 
  print('El nombre completo es: ', nombre, apellido)

# imprimeNombre('Angel ', 'Hernandez')

          # ? usando parametros variables (como para imprimer una tupla)

def imprimeVarios (*nombre): 
  print('Los datos recibidos son: ', nombre)

# imprimeVarios('Angel', 'Lola', 'Esteban', 'Marco') # Los datos recibidos son:  ('Angel', 'Lola', 'Esteban', 'Marco')


          # ? Pasando argumentos usando los parametros sin importar el orden

def nombreCompleto (apellido, nombre):
  print('El nombre completo es: ', nombre, apellido)

# nombreCompleto(nombre='Angel ', apellido='Hernandez')

def nombreCompleto2 (**kwargs):
  print('El nombre completo es: ', kwargs['nombre'], kwargs['apellido'])

# nombreCompleto2(nombre='Angel ', apellido='Hernandez 2')


          # ? pasando parametros por defecto 

def miFuncion2 (argumento = 'Chanchito feliz'):
  print(argumento)

# miFuncion2('Batman')
# miFuncion2();          

          # ? pasando listas como argumentos

def miFuncionLista (lista): 
  for elemt in lista:
    print (elemt)

# miFuncionLista(['Hola', 'Que', 'hace',])


def concatenaNombres (lista): 
  i = ''
  for elemt in lista:
    i = i + elemt + ' '
  return i

nombres = concatenaNombres(['Hola', 'Que', 'hace',])
print(nombres)








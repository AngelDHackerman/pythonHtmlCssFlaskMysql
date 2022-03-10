            # ? Funciones

def miFuncion():
  print('Mi primera funcion en python')

miFuncion()


def imprimeNombre (nombre, apellido): 
  print('El nombre completo es: ', nombre, apellido)

imprimeNombre('Angel ', 'Hernandez')

          # ? usando parametros variables (como para imprimer una tupla)

def imprimeVarios (*nombre): 
  print('Los datos recibidos son: ', nombre)

imprimeVarios('Angel', 'Lola', 'Esteban', 'Marco') # Los datos recibidos son:  ('Angel', 'Lola', 'Esteban', 'Marco')


          # ? Pasando argumentos usando los parametros sin importar el orden

def nombreCompleto (apellido, nombre):
  print('El nombre completo es: ', nombre, apellido)

# nombreCompleto(nombre='Angel ', apellido='Hernandez')

def nombreCompleto2 (**kwargs):
  print('El nombre completo es: ', kwargs['nombre'], kwargs['apellido'])

nombreCompleto2(nombre='Angel ', apellido='Hernandez 2')














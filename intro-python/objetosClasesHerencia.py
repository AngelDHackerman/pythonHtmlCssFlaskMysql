"""
Las clases, son como los planos de una casa, nos dicen cuantas habitaciones van a tener, y como van a ser construidas.
Las instancias, son las casas construidas usando el plano que creamos con la clase.

"""

          # ? Creando clases en python

class Usuario:
  nombre = 'Felipe'        # * Felipe va a ser el nombre por defecto
  apellido = 'Feliz'


usuario = Usuario()         # * Asi creamos una INSTANCIA. 

print(usuario.nombre)
print(usuario.apellido)


          # ? Clases definidas de mejor manera: 

class Usuario2:
  def __init__(self, nombre, apellido):
    self.nombre = nombre
    self.apellido = apellido
  
alumno = Usuario2('Felipe', 'Feliz')
alumno2 = Usuario2('Chanchito', 'feliz')

print(alumno.nombre, alumno.apellido, alumno2.nombre, alumno2.apellido)


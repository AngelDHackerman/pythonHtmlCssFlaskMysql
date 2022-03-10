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

  def saludo(self):                                     # * asi se crean los metodos
    print('Hola, mi nombre es:', self.nombre, self.apellido)   
  



alumno = Usuario2('Felipe', 'Feliz')

# print(alumno.nombre, alumno.apellido)
# alumno.saludo()

alumno.saludo()
alumno.nombre = 'Juanito'
alumno.saludo()

# del usuario.nombre              # todo:  con la palabra "del" eliminamos el metodo o propiedad que deseamos





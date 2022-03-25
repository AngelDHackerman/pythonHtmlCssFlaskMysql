
# * Asi connectamos python con mysql

import mysql.connector

midb = mysql.connector.connect(
  host='localhost',
  user='chachitofeliz',
  password='holamundo',
  database='prueba'
)

cursor = midb.cursor() # * asi se crea un cursor para hacer consultas sql 

# cursor.execute('select * from Usuario') # ? Esta es la consulta tal cual
sql = 'insert  into Usuario (email, userName, edad) values (%s, %s, %s)'
values = ('micorreo@correo.co.nz', 'nombreusuairo', 45)

cursor.execute('show create table Usuario')

resultado = cursor.fetchall() # ? asi tomamos las consultas hechas y las guardamos en una variable
# resultado = cursor.fetchone() # ? Este devolvera solo el primer elemento que sea encontrado

print(resultado)
            # ? Validando si tenemos el dato en la lista

dato = input('ingrese dato: ') # * Asi se le piden datos al usuario

lista = ['hola', 'mundo', 'chanchito', 'feliz', 'dragones']

if lista.count(dato) > 0: # Cuenta cuantas veces el "dato" esta en la lista, si es mayor a 0 nos valida en true
  print('El dato existe en la lista:', dato)
else:
  print('El dato NO existe :(', dato)


            # ? Validando si tenemos el dato en la lista

# dato = input('ingrese dato: ') # * Asi se le piden datos al usuario

# lista = ['hola', 'mundo', 'chanchito', 'feliz', 'dragones']

# if lista.count(dato) > 0: # Cuenta cuantas veces el "dato" esta en la lista, si es mayor a 0 nos valida en true
#   print('El dato existe en la lista:', dato)
# else:
#   print('El dato NO existe :(', dato)


            # ? Calculadora que suma

primero = input('Ingrese el primer numero: ') # pide el primer numero

try:            # * try va intentar ejecutar el codigo de abajo.
  primero = int(primero) # * Asi se hace el parseInt en python, pasadon strings a numeros.
except:         # * si try falla se ejecuta el codigo de abajo.
  primero = 'no es un numero'

if primero == 'no es un numero': 
  print('Numero no valido, intenta de nuevo')
  exit() # todo: exit hace que se salga del programa


simbolo = input('Ingrese operacion: ') # Pide la operacion a ejecutar 


segundo = input('Ingrese el segundo numero: ') # Pide el segundo numero

try: 
  segundo = int(segundo)
except: 
  segundo = 'no es un numero'

if segundo == 'no es un numero':
  print('Numero no valido, intenta de nuevo')
  exit() # todo: exit hace que se reinicie el ciclo del programa


if simbolo == '+':       # Se ejecuta la operacion elegida en simbolo = input('Ingrese operacion: ')
  print('Suma: ', primero + segundo)
elif simbolo == '-':
  print('Resta: ', primero - segundo)
elif simbolo == '*':
  print('multiplicacion: ', primero * segundo)
elif simbolo == '/':
  print('Division', primero / segundo)
else: 
  print('Operacion NO valida')


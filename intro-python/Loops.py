            # ? Loop while

# i = 0 

# while i < 5: 
#   i += 1
#   if i == 3:      # *lo que esto hace es saltarse la impresion del numero 3.
#     continue      # *Esto hace que continue con la iteracion del ciclo
#   print(i)


            # ? for loop 

# usuarios = ['angel', 'roberto', 'daniel', 'ricardo']

# for usuario in usuarios: # * aqui se usa un for in loop
#   print(usuario)


# usuario = 'Chanchito feliz'

# for char in usuario:      # * Este for in imprime cada caracter del usuario
#   print(char)


# usuarios = ['angel', 'roberto', 'daniel', 'ricardo']

# for usuario in usuarios: 
#   if usuario == 'daniel':
#     break               # * toda vez la condicion se cumple se activa el break y el ciclo se detiene
#   print(usuario)


# usuarios = ['angel', 'roberto', 'daniel', 'ricardo']

# for usuario in usuarios: 
#   if usuario == 'daniel':
#     continue            # * se va a saltar a daniel
#   print(usuario)


# for x in range(3, 30, 3): # * range: primer parametro dice donde comiezna, segundo en donde termina, tercero de cuanto en cuanto debe saltar.
#   print(x)
# else: 
#   print('hemos terminado!')


usuarios = ['angel', 'roberto', 'daniel', 'ricardo']
edades = [24, 25, 26, 35]

for usuario in usuarios:
  for edad in edades:
    print(usuario, edad)
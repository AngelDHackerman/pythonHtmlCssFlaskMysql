import modulos as xs
from camelcase import CamelCase

print(xs.mascotas)
xs.saludo('Angel')

c = CamelCase()
sentence = 'esta oracion necesita camelcase'

camelCased = c.hump(sentence)

print(camelCased)
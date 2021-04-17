from modulos import saludo, mascotas
from camelcase import CamelCase
saludo('ramon')
print(mascotas)

c = CamelCase()

s = 'esta oracion necesita CamelCase!'

camelcased = c.hump(s)
print(camelcased)
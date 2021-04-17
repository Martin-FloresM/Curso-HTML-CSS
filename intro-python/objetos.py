class Usuario:
	def __init__(self, nombre, apellido):
		self.nombre = nombre
		self.apellido = apellido
	def saludo(self):
		print('Hola, mi nombre es ', self.nombre, self.apellido)

class Admin(Usuario):
	def superSaludo(self):
		print('Hola, me llamo ', self.nombre, self.apellido, ' y soy admin')
		

# usuario = Usuario('Felipe', 'Feliz')
# # usuario2 = Usuario('Chanchito', 'Feliz')

# usuario.saludo()
# # usuario2.saludo()
# usuario.nombre = 'Chanchito'
# usuario.saludo()
# # del usuario
# # print(usuario)
# admin = Admin('super', 'Feliz')

# admin.saludo()
# admin.superSaludo()
class Animal:
	def __init__(self, nombre, onomatopeya):
		self.nombre = nombre
		self.onomatopeya = onomatopeya
		
	def saludo(self):
		print('Hola, soy un', self.tipo, 'y mi sonido es el ', self.onomatopeya)

class Gato(Animal):
	tipo  = 'Gato'
	def __init__(self, nombre, onomatopeya):	##extendiendo metodo init de clase padre
		Animal.__init__(self, nombre,onomatopeya)
		print('extencion 1 del init clase padre')
	
class Perro(Animal):
	tipo  = 'Perro'
	def __init__(self, nombre, onomatopeya):
		super().__init__(nombre,onomatopeya)
		print("extencion de clase padre con super()")



class Canario(Animal):
	tipo = 'canario'


gato = Gato('fluffy', 'maullido')
gato.saludo()
perro = Perro('Firulais', 'ladrido')
perro.saludo()
canario = Canario('piolin', 'silvido')
canario.saludo()
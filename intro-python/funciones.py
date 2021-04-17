def  mifuncion():
	print('mi primera funcion.')

# mifuncion()

# def imprimeDato(nombre, apellido):
# 	print('El nombre completo es: ', nombre, apellido)

# imprimeDato('Chanchito', 'Feliz')


def imprimeDato(*nombre):
	print('El nombre completo es: ', nombre)

# imprimeDato('Chanchito', 'Feliz')

def nombreCompleto(nombre, apellido):
	print(nombre, apellido)

# nombreCompleto(nombre='Chanchito', apellido='Feliz')

def nombreCompleto2(**kwargs):
	print(kwargs['nombre'], kwargs['apellido'])

# nombreCompleto2(apellido='Feliz', nombre='Chanchito')

def  mifuncion2(argumento = 'Chanchito'):	## Argumento por defecto 
	print(argumento)

# mifuncion2('batman')
# mifuncion2()	## Cuando la funcion se llama sin argumentos usa los argumentos por defecto


def miFuncionLista(lista):
	for elementos in lista:
		print(elementos)

# miFuncionLista(['Chanchito','Feliz'])

def concatenaNombres(lista):
	i = ''
	for elementos in lista:
		i = i + elementos + ' '
	return i

# nombres = concatenaNombres(['Chanchito','Feliz'])
# print(nombres)


def recursion(i):
	if (i < 1):
		return i
	print(i)
	recursion(i - 1)

recursion(6)
 
### Multiplicar numeros sin usar el *

# a=4
# b=5
# r=0
# for x in range(a):
# 	r += b

# print(r)

### ingresar nombre y apellido e imprimirlos al reves

# nombre = input('ingrese su nombre: ')
# apellido = input('ingrese su apellido: ')

# print(nombre[::-1], apellido[::-1])

## encntrar el menor numero de una lista 

# lista = [1, 2, 6, 89, -5, 10, -15, 20, 3]
# menor=0
# for e in lista:
# 	menor = e if e < menor else menor
# print(menor)

## calcular el volumen de una esfera

def calculoVolumenEsfera(r):
	return 4 / 3 * 3.14 * r**3
resultado = calculoVolumenEsfera(6)
# print(resultado)

## escribir una funcion que indique si el usuario es mayor de edad

class Usuario:
	def __init__(self, edad):
		self.edad = edad

def esMayor(usuario):
	return usuario.edad > 17

usuario = Usuario(45)
usuario2 = Usuario(16)

r1 = esMayor(usuario)
r2 = esMayor(usuario2)
# print(r1, r2)

## escribir una funcion que indique si un numero es par o impar

def parImpar(n):
	return n % 2 == 0

r = parImpar(6)
# print(r)

## escribir una funcion que indique cuantas vocales tiene una palabra

# palabra = 'chAnchItofeliz'
# vocales = 0
# for y in palabra:
# 	x=y.lower()
# 	vocales += 1 if x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u' else 0
# print(vocales)

# ## recibir numeros hasta que el ususario diga basta y sumarlos 
# lista = []
# valor = 0 
# print('Ingrese numeros y para sair digite "basta"')

# while True:
# 	valor = input('Digite el numero: ')
# 	if valor == 'basta':
# 		 break
# 	else:
# 		try:
# 			valor = int(valor)
# 			lista.append(valor)
# 		except:
# 			print('Dato invalido')
# 			exit()
# suma = 0
# for x in lista:
# 	suma += x

# print('La suma total es: ', suma)

## escribir una funcion que reciba nombre y apellido y los agregue a un archivo

def agregaNombreAArchivo(nombre, apellido):
	c = open('nombrecompleto.txt', 'a')
	c.write(nombre + ' ' + apellido + '\n')
	c.close()
agregaNombreAArchivo('Juan', 'Flores')


######~~~~~ INGRESO DE DATOS ~~~~~~~~~~~

# dato = input('ingrese dato: ')

# lista = ['hola', 'mundo', 'chanchito', 'feliz', 'dragones']
# if lista.count(dato) > 0:
# 	print('el dato existe: ', dato)
# else: 
# 	print('el dato no existe',dato)

#### ~~~~~~~~~~~  CALCULADORA ~~~~~~

num1 = input('ingrese el primer numero: ')

try:
	num1 = int(num1)
except:
	num1 = 'chanchito feliz'
if num1=='chanchito feliz':
	print('El valor ingresado no es un entero.')
	exit()

num2 = input('ingrese el segundo numero: ')

try:
	num2 = int(num2)
except:
	num2 = 'chanchito feliz'
if num2=='chanchito feliz':
	print('El valor ingresado no es un entero.')
	exit()
# if num1=='chanchito feliz' or num2=='chnchito feliz' :
# 	print('Has ingresado un dato erroneo, intenta nuevamente')
# else:
simbolo = input('ingrese operacion:  ')
if simbolo=='+':
	print('suma = ',num1+num2)
elif simbolo=='-':
	print('Resta = ',num1-num2)
elif simbolo=='*':
	print('Multiplicacion = ',num1*num2)
elif simbolo=='/':
	print('Division = ',num1/num2)
else:
	print('El simbolo ingresado no es valido.')

#comment
#if 5 > 3:
#    print("5 es mayor que 3")
x = 5
y = 'chanchito feliz'
# print(x,y)
a,b,c = 'lala','lele','zzz'
val1=val2=val3='chanchito feliz'
# print(a,b,c)
# print(val1,val2,val3)
# -------------INTRODUCCION A LISTAS ---------------------

# lista =[1,2,3]
# lista2 = lista.copy()	#.copy duplica la lista en la nueva lista
# lista.append(4) #agrega un elemento a la lista
# lista.clear()   # limpia toda la lista
# print(lista2.count(3)) # count muestra cuantas veces se repite el elemento en ()
# print(lista, lista2)


lista=['hola','soy','juan','pop']
lista.append('canchito triste')
#print(lista)
# lista.pop() #elimina ultimo elemento de la lista
# lista.remove('juan') #elimina un elemneto por su valor
lista.reverse()	#invierte el orden de la lista
lista.sort() # todos los datos deben ser del mismo tipo

# ~~~~~~~~~  TUPLA ~~~~~~~~~~~~~~~

tupla = ('hola', 'mundo', 'somos', 'tupla')
# print(tupla)
# ### la tupla solo tiene metodo index y sort

listaDeTupla= list(tupla)	#pasar tupla a lista
listaDeTupla.append('chanchito')
# print(listaDeTupla)

rango = range(6)	#entregara un rango de 0a6 


#~~~~~~~~~~~~~  DICCIONARIO ~~~~~~~~~~~~~~~

diccionario = {
	"nombre": "chanchito feliz",
	"raza": "persa",
	"edad": 5
}

# print(diccionario)
# print(diccionario['nombre'])
# print(diccionario['raza'])
# print(diccionario.get('nombre'))	#solo obtiene lo del metodo get

diccionario['nombre']= 'Fluffy'
# print(diccionario) 

diccionario['ronronea']= 'si'	#agregar valores al diccionario
# print(diccionario)

###~~~~~  Eliminar del diccionario

# diccionario.pop('ronronea')		#elimina la propiedad dentro del pop
# diccionario.popitem()	#elimina la ultima llave o propiedad agregada
# del diccionario['ronronea']		#elimina la propiedad llamada
diccionario.clear()		#elimina todos los elementos del diccionario

#### ~~~~~ Copiar diccionario

# copiaGatito=diccionario.copy()
# copiaGatito=dict(diccionario)

gatitos={
	"Fluffy":{
		"nombre": "Fluffy",
		"edad": 4
	},
	"Mamba":{
		"nombre": "Black Mamba",
		"edad": 12
	},
}
gatitos ["Fluffy"]["edad"] = 15		#cambiar datos navegndo en los diccionarios concatenados
print(gatitos)

perritos=dict(nombre="chanchito feliz", edad=6)		#crear diccionario con DICT
# print(perritos)

###~~~~~~~~~~~	BOOLEANOS	~~~~~~~~~~`
verdadero = True
falso = False 
# print(verdadero,falso)

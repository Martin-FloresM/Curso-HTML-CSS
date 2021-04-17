# c = open('chanchito.txt', 'w')
# print(c.read())	#leer todo el archivo
# print(c.readline())	#leer una linea a la vez por cada vez que se ejecute el print

# c.write('\n	nueva linea 1111')	##Agregar nueva linea con append
# c.close()

####  para poder visualizar el cambio hay que reabrir el archivo

# n = open('chanchito.txt')
# print(n.read())
# for x in n:
# 	print(x)

## el permiso WRITE borra el archivo y lo escribe de 0


import os ## permite eliminar y crear archivos
# if os.path.exists('chanchito.txt'): 	# verifica la existencia del archivo
# 	os.remove('chanchito.txt')			#elimina el archivo
# else:
# 	print('el archivo no existe')

os.rmdir('micarpeta')	##para eliminar directorios

import mysql.connector

midb = mysql.connector.connect(
	host= 'localhost',
	user= 'root',
	password= 'Jj-1026596645',
	database = 'prueba'
)
cursor = midb.cursor()

#~~~~~~~~~~~~~ Agregar datos e la DB ~~~~~~~~~~

# sql = 'insert into Usuario (email, username, edad) values(%s, %s, %s)'
# values = ('micorreo@correo.co.nz', 'nombreusuario', 45)
# cursor.execute(sql, values)
# midb.commit()

#~~~~~~~~~~~~~~ Actualizar Datos ~~~~~~~~~~
# sql = 'update Usuario set email = %s where id = %s'
# values = ('micorreo@correo.com' , 5)

# cursor.execute(sql, values)
# midb.commit()

#~~~~~~~~~~~~~~ Eliminar registros ~~~~~~~~~~~~

# sql= 'DELETE FROM Usuario WHERE id = %s'
# values= (6,) # Es necesario la  ,_ para que tome los valores de la tupla

# cursor.execute(sql, values)
# midb.commit()
# print(cursor.rowcount)



#~~~~~~ Buscar en db  ~~~~~

cursor.execute('show create table Usuario') # mostrar datos de tabla

cursor.execute('select * from Usuario') #selecciona la tabla
resultado = cursor.fetchall() #trae los datos de la tabla
print(resultado)

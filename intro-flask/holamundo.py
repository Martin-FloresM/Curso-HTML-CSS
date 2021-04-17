from flask import Flask, request, url_for, redirect, render_template
app = Flask(__name__)

import mysql.connector
midb = mysql.connector.connect(
	host="localhost",
	user="root",
	password="Jj-1026596645",
	database="prueba"
)
cursor = midb.cursor(dictionary=True)

@app.route('/')
def index():
	return 'hola mundo'

# Ingresar datos datos desde la url
@app.route('/post/<post_id>',methods=['GET', 'POST'])
def lala(post_id):
	return 'El id del post es: ' + post_id

#metodos HTTP
#GET HOST PUT PATCH DELETE
@app.route('/metodos', methods=['GET', 'POST'])
def lele():
	# if request.method == 'GET':
	# 	return 'El id GET ses: ' + id
	# # elif request.method == 'POST':
	# else:
	# 	return 'El id del POST es: ' + id
	cursor.execute('select * from usuario')
	usuarios = cursor.fetchall()
	# print(usuarios)
	return render_template('lele.html', usuarios=usuarios)

@app.route('/lili', methods=['GET', 'POST'])
def lili():
	print(request.form)
	return 'lilili'

@app.route('/home', methods=['GET'])
def home():
	return(render_template('home.html', mensaje='Hola Mundo'))


@app.route('/crear', methods=['GET', 'POST'])
def crear():
	if request.method == "POST":
		username = request.form['username']
		Email = request.form['Email']
		Edad = request.form['Edad']
		sql = "insert into Usuario (username, email, edad) values(%s, %s, %s)"
		values= (username, Email, Edad)
		cursor.execute(sql, values)
		midb.commit()
		return redirect(url_for('lele'))
	
	return(render_template('crear.html'))
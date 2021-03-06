import pymysql, hashlib
from flask import Flask, render_template, request, url_for, redirect, escape, session
from hashlib import md5
#from flaskext.mysql import MySQL
app = Flask(__name__)
app.secret_key="Samuel Dosado is stupid"
# Make the WSGI interface available at the top level so wfastcgi can get it.
class ServerError(Exception):
   """Base class for other exceptions"""
   pass
wsgi_app = app.wsgi_app
# Connect to the database
def create_connection():
	return pymysql.connect(host='localhost',
							user='root',
							password='13COM',
							db='pythondb',
							charset='utf8mb4',
							cursorclass=pymysql.cursors.DictCursor)

def display_all_records(username, role="admin", Id=0):
	global data
	connection=create_connection()
	try:
		with connection.cursor() as cursor:
			select_sql = "SELECT users.Id As Id,users.Email AS Email,users.FirstName AS FirstName, users.FamilyName As FamilyName,profile.DateOfBirth As DateOfBirth,profile.Photo as Photo FROM users LEFT JOIN profile ON users.Id=profile.UserId"
			if int(Id)>0:
				print(select_sql)
				print(Id)
				select_sql = select_sql+"Where users.ID=" + Id
				val=(int(Id))
				print(select_sql)
				cursor.execute(select_sql)
				data = cursor.fetchone()
				print(data)
			cursor.execute(select_sql)
			data = cursor.fetchall()
			data = list(data)
	finally:
		connection.close()
#display users
@app.route('/')
def hello():
	if session.get('logged_in'):
		username_session=escape(session['username']).capitalize()
		return render_template("index.html", session_user_name=username_session)

	username_session=""
	return render_template("index.html")

# update from form`
@app.route('/add_user', methods=['POST','GET'])
def add_user():
	connection=create_connection()
	if request.method == 'POST':
		form_values = request.form 
		first_name = form_values["firstname"]
		family_name = form_values["familyname"]
		email = form_values["email"]
		password = form_values["password"]
		#hash password
		password = hashlib.md5(password.encode()).hexdigest()
		roleId = 2
		UserName = "Yeet"
		try:
			with connection.cursor() as cursor:
				# Create a new record
				sql = "INSERT INTO `users` (FirstName, FamilyName, Email, UserName, Password, RoleId) VALUES (%s,%s,%s,%s,%s)"
				val=(first_name,family_name,email,password,roleId)
				cursor.execute(sql,(val))
				print("works!")
				#save values in dbase
			connection.commit()
			cursor.close()
		finally:
			return redirect(url_for('hello'))
	return render_template("add_user.html")

# edit from form
@app.route('/edit_record', methods=['POST','GET'])
def edit_user():
	connection=create_connection()
	if request.method == 'POST':
		form_values = request.form 
		first_name = form_values["firstname"]
		family_name = form_values["familyname"]
		email = form_values["email"]
		password = form_values["password"]
		#hash password
		password = hashlib.md5(password.encode()).hexdigest()
		ID = form_values["ID"]
		dob="2001-10-01"
		try:
			with connection.cursor() as cursor:
				# Create a new record
				sql = "UPDATE `users` SET FirstName=%s, FamilyName=%s, Email=%s, DateOfBirth=%s ,Password=%s WHERE `ID`=%s"
				val=(first_name,family_name,email,dob,password,ID)
				cursor.execute(sql,(val))
				#save values in dbase
			connection.commit()
			cursor.close()
		finally:
			return redirect(url_for('hello'))
	try:
		with connection.cursor() as cursor:
			ID = int(request.args.get("id"))
			sql = "SELECT * from `users` WHERE `ID` = %s"
			cursor.execute(sql,(ID))
			data = cursor.fetchall()
	finally:
		connection.commit()
		connection.close()
	return render_template('Edit_user.html', data = data)

# delete from form
@app.route('/delete_record', methods=['POST','GET'])
def delete_user():
	connection=create_connection()
	ID = int(request.args.get("id"))
	print (ID)
	try:
		with connection.cursor() as cursor:
			sql = "SELECT * from `users` WHERE `ID` = %s"
			cursor.execute(sql,(ID))
			data = cursor.fetchall()
			data = list(data)
	finally:
			connection.commit()
	if request.method == 'POST':
		try:
			with connection.cursor() as cursor:
				sql = "DELETE FROM `users` WHERE `ID` = %s"
				cursor.execute(sql,(ID))
		finally:
			connection.commit()
			connection.close()
			return redirect(url_for('hello'))
	print(data)
	return render_template('delete_user.html', data = data)

#admin only view
@app.route('/users')
def users():
	if not session.get('logged_in'):
		return redirect(urlfor('login'))
	else:
		username_session=escape(session['username']).capitalize()
		display_all_records(username_session, "admin")
		connection=create_connection()
		try:
			with connection.cursor() as cursor:
				sql = "SELECT * from `users`"
				cursor.execute(sql)
				data = cursor.fetchall()
				data = list(data)
		finally:
				connection.close()
				print(data)
	return render_template("Users.html", results=data, session_user_name=username_session)

#login
@app.route('/login', methods=["GET","POST"])
def login():
	connection=create_connection()
	if session.get('logged_in'):
		username_session=escape(session['username']).capitalize()
		display_all_records(username_session, "admin",)
		return redirect(url_for('index.html', results = data, session_user_name=username_session))
	error=None
	try:
		with connection.cursor() as cursor:
			if request.method == "POST":
				username_form= request.form['username']
				select_sql='SELECT COUNT(1) FROM users WHERE UserName = %s'
				val=(username_form)
				cursor.execute(select_sql,val)
				#data = cursor.fetchall()

				if not list(cursor.fetchone())[0]:
					raise ServerError('Invalid username')

				password_form = request.form['password']
				select_sql="SELECT Password FROM users WHERE UserName = %s"
				val=(username_form)
				cursor.execute(select_sql,val)
				data = list(cursor.fetchall())
				print(data)
				for row in data:
					print(md5(password_form.encode()).hexdigest())
					if md5(password_form.encode()).hexdigest()==row["Password"]:
						session['username'] = request.form['username']
						session['logged_in'] = True
						return redirect(url_for('hello'))

				raise ServerError('Invalid password')
	except ServerError as e:
		error = str(e)
		session['logged_in']= False

	return render_template('login.html', error=error)

@app.route('/logout')
def logout():
	session.pop('username', None)
	session['logged_in']=False
	return redirect(url_for("hello"))

# Tasks 
# Per assessment AS91902 Document; complex techniques  include creating queries which insert, update or delete to modify data
#so you should add  new routes for edit_user, user_details and delete_user using record ids
# create the html pages needed
# modify database to include an image field which will store the image filename(eg pic.jpg) in database and  implement this functionality in code where applicable


if __name__ == '__main__':
	import os
	HOST = os.environ.get('SERVER_HOST', 'localhost')
	try:
		PORT = int(os.environ.get('SERVER_PORT', '5555'))
	except ValueError:
		PORT = 5555
	app.run(HOST, PORT, debug=True)

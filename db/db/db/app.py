from flask import Flask, render_template, request, url_for, redirect
import pymysql
#from flaskext.mysql import MySQL
app = Flask(__name__)
# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app
# Connect to the database
def create_connection():
    return pymysql.connect(host='localhost',
                             user='root',
                             password='13COM',
                             db='students',
                             charset='utf8mb4'
                             ,cursorclass=pymysql.cursors.DictCursor)

#display users
@app.route('/')
def hello():
    connection=create_connection()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * from `users`"
            cursor.execute(sql)
            data = cursor.fetchall()
            data = list(data)
    finally:
            connection.close()

    return render_template("index.html", results=data)

# update from form
@app.route('/add_user', methods=['POST','GET'])
def update_user():
   connection=create_connection()
   if request.method == 'POST':
         form_values = request.form 
         first_name = form_values["firstname"]
         family_name = form_values["familyname"]
         email = form_values["email"]
         password = form_values["password"]
         dob="2001-10-01"
         try:
            with connection.cursor() as cursor:
                # Create a new record
                sql = "INSERT INTO `users` (FirstName,FamilyName,Email,DateOfBirth,Password) VALUES (%s,%s,%s,%s,%s)"
                val=(first_name,family_name,email,dob,password)
                cursor.execute(sql,(val))
                #save values in dbase
            connection.commit()
            cursor.close()
         finally:
             return redirect(url_for('hello'))
   return render_template("add_user.html")

# edit from form
@app.route('/edit_record', methods=['POST','GET'])
def edit_user():
    if request.method == 'POST':
        form_values = request.form 
        first_name = form_values["firstname"]
        family_name = form_values["familyname"]
        email = form_values["email"]
        password = form_values["password"]
        dob="2001-10-01"
        try:
           with connection.cursor() as cursor:
               # Create a new record
               sql = "UPDATE users (FirstName,FamilyName,Email,DateOfBirth,Password) VALUES (%s,%s,%s,%s,%s) WHERE ="
               val=(first_name,family_name,email,dob,password)
               cursor.execute(sql,(val))
               #save values in dbase
           connection.commit()
           cursor.close()
        finally:
            return redirect(url_for('hello'))
    return render_template('Edit_user.html')

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

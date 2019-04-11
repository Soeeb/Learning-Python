from flask import Flask, render_template, request
import sqlite3, os
app = Flask(__name__)

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app

path = os.getcwd()

@app.route('/')
def main():
    conn = sqlite3.connect(path + 'database.db')
    c = conn.cursor()
    #c.execute("""CREATE TABLE database (
    #            title text,
    #            filename text,
    #            rating inter,
    #            review text
    #            )""")
    #c.execute("INSERT INTO database VALUES ('Avengers','Avengers.jpg',4,'It was a very good movie')")

    c.execute("SELECT * FROM database")
    
    tester = c.fetchone()

    conn.commit()

    conn.close()

    return render_template('index.html', tester = tester)

if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)

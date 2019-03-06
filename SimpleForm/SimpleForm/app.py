from flask import Flask, render_template, request
app = Flask(__name__)

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app

class login(object):
    def __init__(self, fName, lName):
        self.fName = fName
        self.lName = lName

@app.route('/', methods = ["POST", "GET"])
def hello():
    text = request.form
    my_message = ""
    if request.method == "POST":
        my_message = text["input_msg"]
    return render_template("/index.html", my_message = my_message)

if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)

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
    result = ""
    if request.method == "POST":
        num2 = text["input_msg2"]
        num1 = text["input_msg"]
        result = int(num1) + int(num2)
    return render_template("/index.html", my_message = result)

if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)

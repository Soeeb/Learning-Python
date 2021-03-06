from flask import Flask, render_template
app = Flask(__name__)

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app

class Staff:
    def __init__(self, lName, fName, Gender):
        self.lName = fName
        self.fName = lName
        self.Gender = Gender

    def gender_as_word(self):
        if self.Gender == "M":
            return "Male"
        else:
            return "Female"


@app.route('/')
def hello():
    """Renders a sample page."""
    return render_template("/index.html")

@app.route('/simple_demo')
def simple_demo():
    first_name = "Mr"
    last_name = "Jeff"
    return render_template("/simple_demo.html", f_name = first_name, l_name = last_name)

@app.route('/list')
def list_demo ():
    pizzas = ["Margherita", "Pepparoni", "Calzone"]
    return render_template("/list.html", pizza = pizzas)

@app.route('/staff_demo')
def staff_demo ():
    staff = Staff("John", "Jeff", "F")
    return render_template("/staff_demo.html", staff1 = staff)


if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)

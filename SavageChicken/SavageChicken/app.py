from flask import Flask, render_template, request

app = Flask(__name__)

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app
class Image:
        def __init__(self, filename, title):
            self.filename = filename
            self.title = title  
images = []
import os
path = os.getcwd()+"/static/images"
for filename in os.listdir(path):
    images.append(Image(filename, "Savage Chickens, Doug Savage"))

@app.route('/')
def main():
    
    return render_template("index.html", images = images)

@app.route('/rate', methods =["POST","GET"])
def mainRate():
    if request.method == "POST":
        form = request.form

    return render_template("rate.html", imageName = images)

if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT, debug = True)

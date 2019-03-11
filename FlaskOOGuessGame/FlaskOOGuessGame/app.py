from flask import Flask, render_template, request
import random

app = Flask(__name__)
# Make the WSGI interface available at the top level so wfastcgi can get it.

global comp_num, counter
counter = 0
comp_num = random.randint(1,10)
wsgi_app = app.wsgi_app

@app.route('/', methods = ["POST", "GET"])
def guess():
	global comp_num, counter
	message = ""
	if request.method == "POST":
		form = request.form
		counter += 1
		user_guess = int(form["guess"])
		if comp_num == user_guess:
			message = "Well done, you got it"
			return render_template ("/gameOver.html", message = message)
		elif comp_num > user_guess:
			message = "Too Low"
		else:
			message = "Too High"
		if counter == 3:
			message = "You failed"
			return render_template ("/gameOver.html", message = message)
	return render_template("/index.html", message = message)

if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT, debug = True)

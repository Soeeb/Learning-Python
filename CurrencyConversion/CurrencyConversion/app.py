from flask import Flask, render_template, request
import urllib.request, ast
app = Flask(__name__)

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app


@app.route('/', methods = ["POST", "GET"])
def main():
    currency_rates = urllib.request.urlopen("https://api.exchangeratesapi.io/latest?base=NZD").read()
    currency_rates = ast.literal_eval(currency_rates.decode("utf-8"))["rates"]
    con = ""
    country = ""
    form = request.form
    if request.method == "POST":
        con_holder = int(form["currency"])
        exchange = currency_rates[form["country_choice"]]
        con = round(con_holder * exchange,2)
    return render_template("/index.html", message = con, message2 = country, currencies = currency_rates)

if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT, debug = True)

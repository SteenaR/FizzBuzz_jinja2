from flask import Flask, render_template

app = Flask(__name__)

def square(value):
    return (value ** 0.5).is_interger()

app.jinja_env.tests["square"] = square

@app.route("/")
def todo():
    return render_template("fizzbuzz.html")
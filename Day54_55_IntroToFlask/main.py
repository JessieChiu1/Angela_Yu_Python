from flask import Flask

# ==========
# Flask init
# ==========

# __name__ is a special attribute of Python, this denotes the file that is currently being run
# In the context of creating a Flask, "__name__" is used to find the root path for Flask's routing and resource
# location.
# https://docs.python.org/3/library/stdtypes.html?highlight=__name__#special-attributes
# https://docs.python.org/3/library/__main__.html
app = Flask(__name__)


# this will print "main" which is where the Flask app is run from, main.py
# print(__name__)

# ================
# Python Decorator
# ================
# instead of adding tag inside the return statement, you can use other Python decorator to do the same thing.
def make_bold(function):
    def wrapper():
        return f"<strong>{function()}</strong>"
    return wrapper


def make_h1(function):
    def wrapper():
        return f"<h1>{function()}</h1>"
    return wrapper


# =======
# Routing
# =======

# this is just routing
# This is a Python decorators symbol (@)
# The `@app.route("/")` in flask is the python decorator, so the function with html is being wrap by the flask's decorator function in the flask library
@app.route("/")
def hello_world():
    return "<h1>Hello, World!</h1>" \
           "<p>This is a paragraph</p>"


@app.route("/bye")
@make_bold
@make_h1
def bye():
    return "Bye!"


# https://flask.palletsprojects.com/en/1.1.x/quickstart/#variable-rules
@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"Hello {name}, you are number {number}"


# =========================
# Activate the Flask server
# =========================

# This is another popular ways to activate the Flask server
# instead of using the flask command "flask --app main run" in command line
# run the app in debug mode to auto-reload
if __name__ == '__main__':
    app.run(debug=True)

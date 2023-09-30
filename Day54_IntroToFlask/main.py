from flask import Flask

# __name__ is a special attribute of Python, this denotes the file that is currently being run
# In the context of creating a Flask, "__name__" is used to find the root path for Flask's routing and resource
# location.
# https://docs.python.org/3/library/stdtypes.html?highlight=__name__#special-attributes
# https://docs.python.org/3/library/__main__.html
app = Flask(__name__)


# this will print "main" which is where the Flask app is run from, main.py
print(__name__)


# this is just routing
# This is a Python decorators
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


# This is another popular ways to activate the Flask server
# instead of using the flask command "flask --app main run" in command line
if __name__ == '__main__':
    app.run()


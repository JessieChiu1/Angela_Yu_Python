### Creating flask server

`app = Flask(__name__)`

`__name__` is a special attribute of Python, this denotes the file that is currently being run

In the context of creating a Flask, "__name__" is used to find the root path for Flask's routing and resource location.


### How to run flask server

to run the application it is `flask --app {file name} run` 


```bash
flask --app main run
```

Some will add this line to the code to automatically run the server

```
if __name__ == '__main__':
    app.run()
```

### Python Decorators
Decorator is just a function that wraps around another function and gives the other function some functionality

Decorators are often used for tasks like logging, authentication, caching, and more. 

```
def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        function()
    return wrapper_function
    
@delay_decorator
def say_hello():
    print("Hello")
    
 
def say_greeting():
    pinrt("How are you?")   
```

The say_hello function will wait 2 sec before executing because of the `@delay_decorator`

The Say_greeting function will execute immediately

The `@app.route("/")` in flask is the python decorator, so the function with html is being wrap by the flask's decorator function in the flask library
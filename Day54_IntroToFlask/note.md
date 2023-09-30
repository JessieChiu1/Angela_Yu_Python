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
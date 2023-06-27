# Unlimited Positional Arguments
# the function can have as much arguments as you want.
# *args is convention but the important syntax is '*'
# IMPORTANT: the type of the args is a TUPLE!!!
def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum


print(add(4, 5, 2, 12, 523, 23))


# Many Keyword Arguments
# **kwargs is convention but the important syntax is "**"
# The kwargs is a dictionary

def calculate(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)


# Using kwargs in class
# IMPORTANT: The type of the kwargs is a DICTIONARY

class Car:

    def __init__(self, **kwargs):
        # This can work but what if you want the user to have the option to not specific the model/make of the car?
        # self.make = kwargs["make"]
        # self.model = kwargs["model"]
        # this is where you use the .get method
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")
        self.color = kwargs.get("color")
        self.seats = kwargs.get("seats")


my_car = Car(make="Nissan")
print(my_car.seats)

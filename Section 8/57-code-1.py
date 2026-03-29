#57. Decorators in Python
# Wrapper around function

from functools import wraps
def my_decorator(func):

    @wraps(func)
    def wrapper():
        print("Before Function runs")
        func()
        print("AFter function runs")
    return wrapper

@my_decorator
def greet():
    print("Hello from decorators class from chaicode")

greet() 
print(greet.__name__)

#Problem: metadata of the function changes
#Solution:Using built in lib

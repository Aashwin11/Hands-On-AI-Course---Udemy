#58. build a loggin decorator

from functools import wraps

def log_activity(func):
    @wraps(func)
    def wrapper(*args, **kwargs): # whatever args and kwargs are coming, accept it
        print(f"Calling: {func.__name__}")
        result=func(*args,**kwargs)
        print(f"Finished function: {func.__name__}")

        return result
    
    return wrapper

@log_activity
def brew_chai(type, milk="no"):
    print(f"brewing Chai: {type} and milk status: {milk}")

brew_chai("Masala")

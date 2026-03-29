#59. auth decorator

from functools import wraps

def require_admin(func):
    @wraps(func)

    def wrapper(user_rols):
        if user_rols!="admin":
            print(f"Access denied {user_rols}, Only ADMINS")
            return None # Needed for decorators
        else:
            return func(user_rols)
    
    return wrapper

@require_admin
def access_inventory(user):
    print("Access granted to inventory")


access_inventory("admin")
access_inventory("Aniket")
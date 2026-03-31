# Complex try 

def serve_chai(flavor):
    try:
        print(f"Preparing {flavor} of chai...... ")
        if flavor=="unknown":
            raise ValueError("We dont know the flavor")
        
    except ValueError as e:
        print(f"Error: {e}")
    else: #Incase when all goes good
        print(f"CHai is serverd of {flavor}")
    finally: #it will always run , no matter what
        print("Next Customer please")

    
print(serve_chai("masala"))
print(serve_chai("unknown"))
class Base_OutOfIngredientsError(Exception): #Inherited Exception class
    pass

def make_chai(milk,sugar):
    if milk == 0  or sugar==0:
        raise Base_OutOfIngredientsError("Missing Milk or sugar")
    
    print(f"Chai is ready ....")

make_chai(0,1)

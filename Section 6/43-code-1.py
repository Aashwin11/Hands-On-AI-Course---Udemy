#43.Handling Arguments in Function

# chai="Ginger chai"

# def prepare_chai(order):
#     print("Preparing", order)

# prepare_chai(chai)


#Example-2

chai=[1,2,3] #list is mutable
def edit_chai(cup):
    cup[1]=44

edit_chai(chai) # Original property changes
print(chai)


#Example-3 Types of arguments : args -positional parameters and keywordargs (kwargs)

def make_chai(tea,milk,sugar):
    print(F"{tea},{milk},{sugar}")

make_chai("Darjelling","Yes","Low") #positional args

#For kwargs
make_chai(milk="Yes",tea="Mysore",sugar="high")

#Example-3.1

def special_chai(*ingredients,**extras):
    print(f"Ingredients: {ingredients}, Extras:{extras}") 

special_chai("Cinnamon","Cardamom",sweetner="Honey",foam="YES")

# *-> uses args and take n number of parameteres mentioned in the function call
# **-? uses kargs and takes n numer of parameters (variable=value) mentioned in function call and creates tupe when passed to the function

#Example-4

# def chai_menu_order(orders=[]):
#     orders.append("Masala")
#     print(orders)

def chai_menu_order(orders=None): 
    if orders is None:
        order=[]
    print(orders)    

chai_menu_order()
chai_menu_order("Masasla")
chai_menu_order()  
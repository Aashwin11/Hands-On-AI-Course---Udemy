#Scope and Name Resolution in functions

#1.Local Scope
def serve_chai():
    chai_type="Masala" #local scope - validation is just inside method/function
    print(f"Inside function :{chai_type}")

chai_type="Lemon"
serve_chai()
print(f"Outside function: {chai_type}") # if chai_type outside function is commented, the print of outisde function will not recognize the variable and throw error


#2.Enclosing - from outer function if nested
def chai_counter():
    chai_order="ginger" #enclosing scope

    def print_order():
        chai_order="Cardimom"
        print(f"Inside print function: {chai_order}")
    print_order()
    print(f"Outisde print function: {chai_order}")

chai_counter()

chai_order="Tulsi"
print(f"Global Order: {chai_order}")
#3.Global scope - Top level script


#4.Built in - eg. print


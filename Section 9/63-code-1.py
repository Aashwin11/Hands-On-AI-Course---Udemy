#63. Self arguments in python
#Function inside a class is called a Method

class Chaicup:
    size=150 #ml

    # This function is called method
    def describe(self): 
        #self is a reference to all properties defined within class
        return f"A {self.size}ml cup of Chai"
    
cup=Chaicup()
print(cup.describe())
# or directly refering to class

# print(Chaicup.describe())
# we will get error here
# TypeError: Chaicup.describe() missing 1 required positional argument: 'self'
    # We are passing parameter self here for the class method       
    # self can also refer to the object
    # So give the context
        #Object passes refernce , but class does not automatically
    #Solution, pass the object as refernce
print(Chaicup.describe(cup))

cup_two=Chaicup()
cup_two.size=100
print(Chaicup.describe(cup_two))


   
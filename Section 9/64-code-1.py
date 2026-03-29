#64.Constructors and Init in Python

#Init function
    # Process of initialization

class Chaiorder:

    #Before declaring an attribute
    def __init__(self,type_,size):
        #type_ :Type is a functuion that gives type of 
        self.type=type_
        self.size=size

    def summary(self):
        return f"{self.size}ml of cup type:{self.type} Chai"
    

order=Chaiorder("Masala",200)
print(order.summary())

order_two=Chaiorder("Ginger",300)
print(order_two.summary())
        


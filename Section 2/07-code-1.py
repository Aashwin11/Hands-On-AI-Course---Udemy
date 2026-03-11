class Chai:
    def __init__(self,sweetness,milk_level): # Open a factory or method
        self.sweetness=sweetness
        self.mil_level=milk_level

    def sip(self):
        print("Sipping chai")

    def add_sugar(self,amount):
        print("Added sugar")


my_chai=Chai(sweetness=3,milk_level=2)
my_chai.add_sugar(3)

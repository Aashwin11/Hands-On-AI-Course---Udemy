#65. Inheritance and Composition

#Inheritance
class BaseChai:
    def __init__(self,type_):
        self.type=type_

    def prepare(self):
        print(f"Preparing {self.type} Chai.....")

class MasalaChai(BaseChai): #Only use parenthesis for class when there is inheritance
    def add_spices(self):
        print("Adding cardamom, ginger ,cloves")


#Composition
class ChaiShop:
    chai_cls=BaseChai #Hold any of the class SYNTAX OF COMPOSITION< without braces()  

    def __init__(self):
        self.chai=self.chai_cls("Regular")

    def serve(self):
        print(f"Serving {self.chai.type} in the shop")
        self.chai.prepare()


class FancyChaiShop(ChaiShop):
    chai_cls=MasalaChai

#Creating object
shop=ChaiShop()
fancy=FancyChaiShop()
shop.serve()
fancy.serve()
fancy.chai.add_spices()
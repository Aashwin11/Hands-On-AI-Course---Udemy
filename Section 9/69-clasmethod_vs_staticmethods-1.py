#69. Class Method vs Static Method

class BaseOrder:

    def __init__(self,type_,sweetness,size):
        self.type=type_
        self.sweetness=sweetness
        self.size=size

    @classmethod #Classmethod gets cls , not self, it gets whole class reference
    def from_dict(cls, order_data):
        return cls(
            order_data["tea_type"],
            order_data["sweetness"],
            order_data["size"],
        )
    
    @classmethod
    def from_string(cls,order_string):
        tea_type,sweetness,size=order_string.split("-")
        return cls(tea_type,sweetness,size)

class Base2Utils:

    @staticmethod
    def is_valid (size):
        return size in ["Small","Medium","Large"]

#Create object , by utilzing the methods
order1=BaseOrder.from_dict({"tea_type":"masala","sweetness":"medium","size":"small"})
order2=BaseOrder.from_string("ginger-low-small")
order3=BaseOrder("large","low","small")
print(order1.__dict__)
print(order2.__dict__)
print(order3.__dict__)

order4=Base2Utils.is_valid("Small")
print(order4)
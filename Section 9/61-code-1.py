#61. Class and Object Namespace
# Each object possess different property, not overlapping with others
# Each object has its own entity called Namespace

class Chai:
    origin="India" # Variable iinside a class is called Properties

print(f"{Chai.origin}")
Chai.is_hot=True #Add property to a class
print(f"{Chai.is_hot}")


#Creating 2 diff Objects fro Chai class
masala=Chai()
print(f"Coming from object {masala}")
print(masala.origin)
print(masala.is_hot)
masala.is_hot=False

print(f"Did not make is hot of Class false then value: {Chai.is_hot}")
print(f"Made is hot for Object masala false then value: {masala.is_hot}")

#add more property to object masala
masala.flavour="Spicy"
print(f"{masala.flavour}")

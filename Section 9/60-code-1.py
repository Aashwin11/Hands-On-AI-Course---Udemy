#60. OOPs- Class and Object

class Chai: # Class name should be camel
    pass

class Chai_Time:
    pass

print(type(Chai))


ginger_tea=Chai() # Object of Chai Class
print(type(ginger_tea))
print(type(ginger_tea) is Chai)
print(type(Chai) is Chai_Time)
#67. Multiple Inheritance
# Use of Method Resolution Order (MRO)

#Cosnider a class - Class A and another class -Class B , B is inheriting A
#Class C also inherits from Class A
#and then Class D , inherits from Class B  and Class C
#if method is called by D , will it be called by B, C or A

class A:
    label="A: Base Class"

class B(A):
    label="B: Child Class B , inheriting from A"

class C(A):
    label="C: Child Class C,inheriting from A "

class D(B,C): #Whichever class mentioned before will be inherited
    pass

cup=D()
print(f"{cup.label}")
print(f"{D.__mro__}")



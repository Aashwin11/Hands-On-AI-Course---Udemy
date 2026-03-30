#66.Ways to access Base Class
#Code Duplication
    #Explicit Call
    #Method using super()

class BaseClass:

    def __init__(self,type_,strength):
        self.type=type_
        self.strength=strength

# class ChildClass(BaseClass):

#     def __init__(self, type_, strength,spice_level):
#         self.type=type_
#         self.strength=strength
#         self.spice_level=spice_level

        #THis is code duplication

#2nd approach

# class ChildClass(BaseClass):

#     def __init__(self, type_, strength,spice_level):
#         BaseClass.__init__(self,type_,strength)  #This is explicit call
#         self.spice_level=spice_level  

# Using Method super

class ChildClass(BaseClass):

    def __init__(self, type_, strength,spice_level):
        super().__init__(type_, strength)
        self.spice_level=spice_level

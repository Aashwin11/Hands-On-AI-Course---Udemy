# import recipes.flavours
# #SYNTAX: import folder_name.file_name
# print(recipes.flavours.elaichi_chai())

#2nd approach
from chai_business.recipes.flavours import elaichi_chai,ginger_chai
print(ginger_chai())

#3rd approach
from .recipes.flavours import ginger_chai
print(ginger_chai())

#__init__.py -> turns folder into python package, not needed after python 3.3


#62. Attribute shadowing in Python
# Every variable/property inside a class or object also called attribute

class Chai:
    temperature="Hot"
    strength="Strong"

cutting=Chai()
print(f"{cutting.temperature}")

cutting.temperature="Mild"
print(f"Aftering changing: {cutting.temperature}")
print(f"Direct look into the class {Chai.temperature}")


del cutting.temperature
# if object attribute is not available,it falls back to the attribute of the class
print(f"After deleting:{cutting.temperature}")

cutting.cup="small"
print(f"Cup size of cutting : {cutting.cup}")
# Now , since this attribute doesnt exist in the Class, 
#it only exists in the Object cutting, 
# Now if I delete it, waht will be output for that attribute

del cutting.cup
print(f"After delete, Cup size of cutting : {cutting.cup}")

# Gives error: AttributeError: 'Chai' object has no attribute 'cup'

# This is attribute shadowing
sugar_amount=2

print(f"Initial Sugar:{sugar_amount}")
# Memory will create a variable and then point to the value 2

sugar_amount=12
print(f"Middle Sugar:{sugar_amount}")
# value of sugar_amount gets changed 
# THe number never changed, Python created the number and the sugar_amount is pointing to 12 now.
# we are only changing the reference


# Alwyas check the identity


print(f"Id of 2:{id(2)}")
print(f"Id of 12:{id(12)}")
# Initial Sugar:2
# Middle Sugar:12
# Id of 2:108874506900424
# Id of 12:108874506900744


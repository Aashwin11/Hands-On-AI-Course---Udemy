spices={"cardamom","ginger","cinnamon"}
optional={"cloves","ginger","pepper"}

all_spices=spices | optional
print(f"All spices: {all_spices}")

common=spices & optional
print(f"Common spices: {common}")

differences=spices - common
print(f"Only esssential spices: {differences}")

#membership test - check if member exists in a set

print(f"Is existing clove?:{'cloves' in spices}")

#frozen set - unordered collection of unique elements
#List[] - Mutable or Array
#In python its called List

ingredients=["water","milk","black tea"]

ingredients.append("sugar")

print(f"Ingredients are: {ingredients}")
ingredients.remove("water")
print(f"Ingredients are: {ingredients}")

spice_options=["ginger","cardamon"]
chai_ingredients=["water","milk"]

chai_ingredients.extend(spice_options)
print(f"chai ingredients:{chai_ingredients}")

chai_ingredients.insert(2,"clover")
print(f"Chai Ingredients at pos 2: {chai_ingredients}")

last_added= chai_ingredients.pop() # whatever is the last element , it will remove the vlaue from list and emptied from the list
print(f"Last added: {last_added}")
print(f"Chai Ingredients npw: {chai_ingredients}")

chai_ingredients.reverse()
print(f"chai Ingredients reversed in the list: {chai_ingredients}")

chai_ingredients.sort()
print(f"Sorted ingredients: {chai_ingredients}")

sugar_levels=[1,2,3,4,5]
print(f"Max sugar level:{max(sugar_levels)}")
print(f"Min sugar level:{min(sugar_levels)}")


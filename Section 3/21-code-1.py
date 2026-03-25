chai_order=dict(type="Masala Chai", size="large", sugar=2)
print(f"Dictionary order doesnt matter: {chai_order}")

chai_recipe={}
chai_recipe["base"]="black tea"
chai_recipe["liquid"]="milk"

print(f"Value:{chai_recipe['base']}")
print(f"Recipe full: {chai_recipe}")
del chai_recipe['liquid']

print(f"After removing:{chai_recipe}")

print(f"Exits ? : {'sugar' in chai_order}")


chai_order = {"type":"Ginger Chai", "size":"large", "sugar":2, "added":"Ginger"}

# print(f"Chai ORdr keys: {chai_order.keys()}")
# print(f"Chai ORdr values: {chai_order.values()}")
# print(f"Chai ORdr items: {chai_order.items()}")

last_item=chai_order.popitem()
print(f"After last pop: {last_item}")

extra_spice={"spice":"cardamon","added":"Ginger","recipe":"video25"}

chai_recipe.update(extra_spice)
print(f"Updated chai recipe: {chai_recipe}")

chai_zie=chai_order["size"]
print(f"Chai size is: {chai_zie}")

customer_note=chai_order.get("note","no note was given")
print(f"Customer note is:{customer_note}")

#Catching multiple exceptions

def process_Order(item,quantity):
    try:
        price={"masala":20,"cardimon":40}[item] #We have key:value , for the dictionary, we are looking for the item , if we try to extract an item from dictionary based on the value of the item 
        cost=price*quantity

        print(f"Total cost is {cost}")

    except KeyError as k:
        print("Sorrym that chai is not on menu")
    
    except TypeError as t:
        print("quantity must be in number")


process_Order("Ginger",2)
process_Order("masala","two")
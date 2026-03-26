# Handling multiple returns in Python

def make_chai():
    # return "Here is your chai"
    print("here is your chai")

# print(make_chai())
return_value=make_chai()
print(return_value) #Implicitely returns none

#Return 1 value
def idle_chai():
    pass

print(idle_chai()) # -> Gives None  ; Thus , when given nothing , it will return None

def sold_cups():
    return 120

total=sold_cups()
print(total) # Return 1 value



#Return multiple value

def chai_report():
    return 100,20,"everst" #sold, remaining

# sold,remaining=chai_report()
# print(f"Sold:{sold}, Remaining:{remaining}")

sold,remaining,_=chai_report()
print(f"{sold},{remaining},{_}")
# _ -> This doesnt mean it will take n number of returns, it will only take 1 return


#return early from function

def chai_status(cups_left):
    if cups_left ==0:
        return ("Soory, chai over")
    
    return "Chai left here"
    print("chai") # we wont reach here

print(chai_status(0))
print(chai_status(5))
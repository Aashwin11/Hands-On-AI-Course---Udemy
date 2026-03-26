#Types of Function : Lambda, Pure and Impure Function

#Lambda - functions without a name

chai_types=["lighr","kadak","ginger","kadak"]

strong_chai= list(filter(lambda chai:chai!="kadak",chai_types))
print(strong_chai)


#Pure

def pure_chai(cups):
    return cups*10

# no alternations to global scope


#Impure- Not recommended way 

total_chai=0
def impure_chai(cups):
    global total_chai
    total_chai+=12



#Recursive
def recursive(n):
    if n==0:
        return("All chais poured")
    print(f"N:{n}")
    recursive(n-1)

recursive(11)
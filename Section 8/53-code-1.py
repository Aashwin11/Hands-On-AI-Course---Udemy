#53. Generators
# Common terms here  - yield keyword
    # generators help to save memory
    # Sometimes results are not needed immediately
    # Lazy evaluation

#Definiton of generators : same as functions

def servce_chai():
    yield "Cup1: Masala Chai"
    yield "Cup2: Ginger CHai"
    yield "Cup3: Elaichi Chai"


stall=servce_chai()

for cup in stall:
    print(cup)

#Eg: Normal function:

# Normal function
def get_chai_function():
    return ["Cup1","Cup2","Cup3"]

#generator function
def get_chai_generator():
    yield "Cup1"
    yield "Cup2"
    yield "Cup2"

chai_gen=get_chai_generator()
print(chai_gen) #output will be: <generator object get_chai_generator at 0x75448a3d8a90> It just point to the method

# to get output, we need to use method 'next', Next method runs the function once, and see value of it
print(next(chai_gen)) # returns only the 1st value, now method is on paused state and is still in the meory
# if next is called next time again, it will give 2nd result

print(next(chai_gen))  # function resumes exactly where it paused
print(next(chai_gen)) 
print(next(chai_gen)) 
# incase now, once the yield is complete, terminal will give result as :
# Traceback (most recent call last):
#   File "/workspaces/Hands-On-AI-Course---Udemy/Section 8/53-code-1.py", line 41, in <module>
#     print(next(chai_gen)) 
#           ^^^^^^^^^^^^^^
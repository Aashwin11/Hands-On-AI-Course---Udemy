#72. try except else finally

#SYNTAX for graceffuly handling errors

chai_menu={"masala":30, "ginger":40}

try:
    chai_menu["elaichi"] # wrapping this into safe Bubble

except KeyError:
    print("The key tried to acces does not exist")
#IT will give key error
#     chai_menu["elaichi"]
#     ~~~~~~~~~^^^^^^^^^^^
# KeyError: 'elaichi'

print("Hello code") #whole program is crashed
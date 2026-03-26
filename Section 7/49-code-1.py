#List Comprehension

# SYNTAX: [expression for item in iterable if condition]
# Eg:
menu=[
    "Masala",
    "Elaichi",
    "Iced Lemon Tea",
    "Green Tea",
    "Iced Moca late",
    "Ginger"
]
#[expression for item in iterable if condition]
iced_tea=[tea for tea in menu if "Iced" in tea]
print(iced_tea)
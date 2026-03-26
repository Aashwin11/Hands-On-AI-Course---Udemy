# Set Comprehension
#SYNTAX: #{expression for item in iterable if condition} 
    # Expression here changes little

#Eg:

#THis is list
favourite_chais=[
    "Masala Tea",
    "Green Tea",
    "Lemon Tea",
    "Maasala Tea",
    "Elaichi Tea",
    "Green Tea"
]

#Take unique teas only
unique_teas={ chai for chai in favourite_chais}
print(unique_teas)

# Complex example
#Expression issue

recipes={
    "Masala chai":["ginger","cardimom","clove"],
    "Elaichi chai":["cardimom","clove"],
    "Ginger chai":["herb","pepper","clove","ginger"],
}

unique_spices={spice for ingredients in recipes.values() for spice in ingredients}
print(f"Unique spices: {unique_spices}")
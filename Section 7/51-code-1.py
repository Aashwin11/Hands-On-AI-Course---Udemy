# Dictionary Comprehension
#SYNTAX: #{expression for item in iterable if condition} 
    # Expression here is key:value

tea_price_inr={
    "Masala Tea": 40,
    "Green Tea" : 50,
    "Lemon Tea" : 200,
}

tea_prices_dol={ tea:inr/80 for tea,inr in tea_price_inr.items()}

print(tea_prices_dol)
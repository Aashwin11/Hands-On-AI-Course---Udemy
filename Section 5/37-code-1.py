# Walrus operators :=

#General method:
# value=13
# remainder=value %5

# if remainder:
#     print(f"Not completely divisible. remainder is {remainder}")

# Walrus Method:

value=13

if (remainder:=value%5):
        print(f"Not completely divisible. remainder is {remainder}")


# available_sizes=["small","medium","large"]

# if (requsted_size:=input("Enter your size:").lower()) in available_sizes:
#         print(f"Size:{requsted_size} is available")
# else:
#         print(f"Size {requsted_size} is unavailable")


flavours=["masala","ginger","lemon","mint"]
print(f"Available Flavours: {flavours}")

while (flavour:=input("Choose ypur flavour").lower() not in flavours):
        print(f"Sorry, {flavour} is not available")

print(f"YOu choose {flavour} coorectly")
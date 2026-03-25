flavours=["Ginger","Out of stuck","Lemon","Discontinued","Tulsi"]

for f in flavours:
    if f=="Out of Stock":
        continue
    if f=="Discontinued":
        break
    print(f"Discontinued item found")


print(f"Outside loop")
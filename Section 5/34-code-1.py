name=["Alex","Amrtin","Thomas"]
bills=[70,32,45]

for n,b in zip(name,bills,strict=False):
    print(f"{n} paid Rs.{b}")
staff=[("Amit",16),("Zara",18),("Raj",15)]

for name,age in staff:
    if age>=18:
        print(f"{name} is above 18 years")
        break
else:
    print("No one is eligible to manage staff")        
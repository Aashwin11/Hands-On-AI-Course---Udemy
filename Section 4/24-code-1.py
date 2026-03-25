snack=input("Enter preferred value:").lower()
print(f"User said:{snack}")

if snack == "cookie" or snack=="samosa":
    print(f"ORder served:{snack}")
else:
    print(f"{snack} Not available")
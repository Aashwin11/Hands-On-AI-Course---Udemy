is_boiling= True 
print(f"Us Tea boling: {is_boiling}")

stri_count=5

total_actions=stri_count+is_boiling
print(f"Upcasting and make True to 1: {total_actions}")

milk_present=0 #no milk
print(f"Is there milk? {bool(milk_present)}")

milk_present=1 #no milk
print(f"Is there milk? {bool(milk_present)}")

milk_present=11 #no milk
print(f"Is there milk? {bool(milk_present)}")

milk_present="Hitesh" #no milk
print(f"Is there milk? {bool(milk_present)}")

milk_present=None #no milk
print(f"Is there milk? {bool(milk_present)}")

#Logical Operations
#AND , OR, NOT

water_hot=True
tea_added=True

can_serve=water_hot and tea_added
print(f"CAn tea be served: {can_serve}")
# string and index and slicing

#String
chai_type="Ginger Tea"
customer_name="Hitesh"

print(f"Order for {customer_name} :  {chai_type} please !!")

#Indexing
chai_description="Aromatic Tea"
print(f"1st word: {chai_description[0:8]}")
print(f"1st word: {chai_description[0:8:1]}")
print(f"1st word: {chai_description[0:8:2]}") #Every 2nd character
print (f"Last word; {chai_description[10:]}")
print(f"1st word: {chai_description[::-1]}") # To reverse the whole string

lable_text="Chai Spècial"
encoded_label=lable_text.encode("utf-8")
print(f"Non encoded Label: {lable_text}")
print(f"Encoded label:{encoded_label}")
decoded_lable=encoded_label.decode("utf-8")
print(f"Decoded Lable: {decoded_lable}")
#Slicing


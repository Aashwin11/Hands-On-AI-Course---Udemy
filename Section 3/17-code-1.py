#Tuples ()

#Create
masala_spices=("Cardamom","Clove","Cinnamon")

#Extract values | Unpacking
(spice1,spice2,spice3)=masala_spices
print(f"Main ingredients:{spice1},{spice2} & {spice3}")


ginger_ratio, cardamom_ration=2,1
print(f"Ratio of G:C {ginger_ratio}:{cardamom_ration}")
# flip ratio
ginger_ratio, cardamom_ration= cardamom_ration,ginger_ratio
print(f"Ratio of G:C {ginger_ratio}:{cardamom_ration}")

#meo=mbership Testing

print(f"Is ginger is masal Spices? {'ginger' in masala_spices}")
print(f"Is clove is masal Spices? {'clove' in masala_spices}")
print(f"Is clove is masal Spices? {'Clove' in masala_spices}")
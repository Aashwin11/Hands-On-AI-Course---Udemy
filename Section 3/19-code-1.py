# from operator import itm

base_liquid=["water","milk"]

extra_flavour=["ginger"]

#Operator Overloading
full_liquid_mix=base_liquid+extra_flavour
print(f"Liquid mix: {full_liquid_mix}")

Strong_brew=["bloack tea"]*3
print(f"OP of Strong Brew: {Strong_brew}")

Strong_brew=["bloack tea","hard water"]*3
print(f"OP of Strong Brew: {Strong_brew}")

raw_spice_data=bytearray(b"Cinamon")
print(f"Output: {raw_spice_data}")

new_spice_value=raw_spice_data.replace(b"Cina",b"Card")
print(f"Output: {new_spice_value}")

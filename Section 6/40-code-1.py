def get_input():
    print("Getting user input")

def validate():
    print("Validating")

def save_to_db():
    print("Saveed to DB")

def register_user():
    get_input()
    validate()
    save_to_db()
    print("user Reg is complete")

register_user()

# exampl2

def calculate_bill(cups,price):
    return cups*price

print(f"TOtal bill: {calculate_bill(5,3)}")


#example 3

def add_vat(price,vat_rate):
    return price*(100+vat_rate)/100

orders=[100,150,200]
for o in orders:
    print(f"Final amount for {o} order : {add_vat(o,10)}")
order_amout=int(input("Enter order amount:"))
print(f"Order amount:{type(order_amout)}")

delivery_fees= 0 if order_amout > 300 else 30
print(f"total value{order_amout+delivery_fees}")
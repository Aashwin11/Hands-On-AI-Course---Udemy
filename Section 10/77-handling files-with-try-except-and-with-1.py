# try:
#     file=open("order.txt", "w")
#     file.write("Masala chai - 2 cups")
# finally:
#     file.close()

#2nd approach - using new operator with

with open("order2.txt","w") as file:
    file.write("Ginger Tea -4 cups")

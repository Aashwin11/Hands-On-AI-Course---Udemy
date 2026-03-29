#55. Send value to Generator

#2nd use-case of yield in Production
    #yield generates or gives data
    # how come someone send data to yield


def chai_customer():
    print("Welcome !! , what chai woudl you like")
    order=yield  [""]
    while True:
        print(f"Preparing: {order}")
        order=yield

stall=chai_customer()
next(stall) # start of generator

stall.send("Masala chai")
stall.send("Lemon chai")


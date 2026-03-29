#56. Yield from and close the generator

# Sometimes generators do not yield , but borrows value
# We dont want an infinite generator to continue and close

# Working on yield from
def local_chai():
    yield "Masala chai"
    yield "Ginger Chai"

def improted_chai():
    yield "Macha chai"
    yield "Oolong chai"

def full_menu():
    yield from local_chai()  # always execute the function, lamens term: add ()
    yield from improted_chai()

for chai in full_menu():
    print(chai)

# Working on closing the generator

def chai_stall():
    try:
        while True:
            order=yield "Waiting for chai order"
            print(f"Preparing Chai :{order}")

    except:
        print("Stall closed, no more chai")

stall=chai_stall()
next(stall)
stall.send("masala chai")

stall.close() # closes and cleans up memory 


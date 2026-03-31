class InvalidChaiError(Exception): pass

def bill(flavor,cups):
    menu={"masala":20,"ginger":30,"cardimom":40}
    try:
        if flavor not in menu:
            raise InvalidChaiError("That Chai is not available")
        if not isinstance(cups,int):
            raise TypeError("The number of cups must be an integer")
        
        total=menu[flavor]*cups
        print(f"Total bill for {flavor} for {cups} is :Rs.{total}")

    except Exception as e: #Consider the parent Class, not the child class, so both the erros are handled
        print(f"Error:{e}")
    finally:
        print("Thankyou for visiting Chai Code")


bill("mint",2)
bill("masala","two")
bill("ginger",3)
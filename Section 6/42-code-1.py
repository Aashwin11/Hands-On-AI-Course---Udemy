# Non-local vs Global Scope

chai_type="Global chai"

def update_order():
    chai_type="Elaichi"

    def kitchen():
        nonlocal chai_type  # refer just outside scope of current function
        chai_type="Kesar"
        print(f"Value inside kithcen: {chai_type}")

    kitchen()
    print(f"After kithcen update value of chai : {chai_type}")

update_order()



chai_type="Plain"

def front_desk():
    def kithcen():
        global chai_type
        chai_type="Irani"

    kithcen()

front_desk()
print(f"Final global chai:{chai_type}")
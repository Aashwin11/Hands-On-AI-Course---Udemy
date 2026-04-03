import threading
import time

def boil_milk():
    print(f"Boiling milk.....")
    time.sleep(3)
    print(f"Boiling milk complete.....")

def toasting_bun():
    print(f"Toasting Bun.....")
    time.sleep(4)
    print(f"Toeasting bun complete.....")


start=time.time()
t1=threading.Thread(target=boil_milk)
t2=threading.Thread(target=toasting_bun)

t1.start()
t2.start()

t1.join()
t2.join()
end=time.time()

print(f"Completed thread things in {end-start:.2f} secs")
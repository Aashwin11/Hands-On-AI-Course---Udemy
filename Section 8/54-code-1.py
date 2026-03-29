#Infinite Generators
    #used for FAST API and AI
    #used for streams and real time system
    # It drains a lot of memory

def infinite_chai():
    count=1
    while True:
        yield f"Refill count {count}"
        count+=1

refill=infinite_chai()
user_2=infinite_chai()

for _ in range(5):
    print(next(refill))

for _ in range(6):
    print(next(user_2))
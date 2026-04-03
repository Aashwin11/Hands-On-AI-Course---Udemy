#Non shining area of Threads

import threading
import time

def cpu_heavy():
    print(f"crunching some numbers....")
    total=0
    for i in range (10**7):
        total+=i
    
    print("Done")


start=time.time()

threads=[threading.Thread(target=cpu_heavy) for _ in range(3)]
[t.start() for t in threads]
[t.join() for t in threads]    
end=time.time()    
print(f"Completion time {end-start:.2f}")
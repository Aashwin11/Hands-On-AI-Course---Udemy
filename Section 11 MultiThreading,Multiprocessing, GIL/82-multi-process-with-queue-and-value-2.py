#Non shining area of Threads to IMPROVE using Process

from multiprocessing import Process
import threading
import time

def cpu_heavy():
    print(f"crunching some numbers....")
    total=0
    for i in range (10**8):
        total+=i
    
    print("Done")


if __name__=="__main__":
    start=time.time()

    processes=[Process(target=cpu_heavy) for _ in range(3)]
    [p.start() for p in processes]
    [p.join() for p in processes] 
    
    end=time.time()    
    print(f"Completion time {end-start:.2f}")
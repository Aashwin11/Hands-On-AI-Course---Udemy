# Section 11 MultiThreading,Multiprocessing, GIL
#thread and concurrency

#Concurrency - Multiple task at once
#Parallelism - Multiple task at once at the same time,

#Concurrency Example:

#1. Thread Concurrency

import threading
import time

def take_orders():

    for i in range(1,4):
        print(f"Taking order: #{i}..... ")
        time.sleep(2) #1 is second

def brew_chai():
    for i in range(1,4):
        print(f"Brewing chai for order: #{i}....")
        time.sleep(3)


#Create threads
take_order_thread=threading.Thread(target=take_orders) #Thead should have some target, like a function
brew_thread=threading.Thread(target=brew_chai) #Thead should have some target, like a function
#Threads are only created and know the target, we need to invoke

take_order_thread.start()
brew_thread.start()


# wait for both to finish

take_order_thread.join()
brew_thread.join()

print("Process completed")
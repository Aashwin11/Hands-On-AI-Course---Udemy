import asyncio,time
from concurrent.futures import ThreadPoolExecutor #Execute computations asynchronously using threads or processes.
#ThreadPoolExecutor -executes all threads in the pool | similar to asyncio.gather

def check_stocks(item):
    print(f"Checkings {item} in store.....")
    time.sleep(3) # Blocking operation - will block main thread
    return f"{item} stock: 42"
        

async def main():
    loop=asyncio.get_running_loop()   #Return the running event loop. Raise a RuntimeError if there is none.This function is thread-specific.
    with ThreadPoolExecutor() as pool:
        resutl=await loop.run_in_executor(pool,check_stocks,"masala chai") #constantly executes threads
        print(resutl)

asyncio.run(main())
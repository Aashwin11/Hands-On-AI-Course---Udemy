import asyncio
import threading
import time

def background_logger():
    while True:
        time.sleep(1)
        print("Logging system Health.....")


async def fetch():
    await asyncio.sleep(3)
    print("Fetch Order")



threading.Thread(target=background_logger,daemon=True).start()

asyncio.run(fetch())


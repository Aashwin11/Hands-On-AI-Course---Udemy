import asyncio
import time
async def brew(name):
    print(f"Brewing {name} ....")
    await asyncio.sleep(3)
    # time.sleep(3)
    print(f"Brewing {name} complete")

async def main():
    await asyncio.gather(
        brew("Masala chai"),
        brew("Ginger chai"),
        brew("Cardimon Chai")
    ) #Takes couroutines - wraps and schedule them in Event Loop.
    
asyncio.run(main())
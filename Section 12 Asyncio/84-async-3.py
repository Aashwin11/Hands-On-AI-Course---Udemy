import asyncio
import aiohttp # this lib is for async HTTP requests

#Fetch mutliple requests from website : https://httpbin.org/delay/3

async def fetch_url(session,url):
    async with session.get(url) as response: # In async prgrmming, non blocking is acheived by asynci with 
        print(f"Fetched {url} with status {response.status}")


async def main():
    urls=[
        "https://httpbin.org/delay/3"
    ] * 3

    async with aiohttp.ClientSession() as session:
        tasks=[fetch_url (session,url) for url in urls]
        await asyncio.gather(*tasks) # Refernced of asterisk, it passes each task as a seperate arg to gather

asyncio.run(main())
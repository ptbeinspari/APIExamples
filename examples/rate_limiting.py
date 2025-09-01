import asyncio
import aiohttp
from .utils import save_json

async def rate_limited_calls(urls: list, calls_per_second: int) -> None:
    semaphore = asyncio.Semaphore(calls_per_second)
    
    async def rate_limited_fetch(session, url, i):
        async with semaphore:
            await asyncio.sleep(1/calls_per_second)  # Spread requests
            async with session.get(url) as response:
                response.raise_for_status()
                data = await response.json()
                save_json(data, "rate_limiting", f"rate_limit_{i}.json")
                return data
    
    async with aiohttp.ClientSession() as session:
        tasks = [rate_limited_fetch(session, url, i) for i, url in enumerate(urls)]
        results = await asyncio.gather(*tasks)
        
        return results            

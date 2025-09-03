import aiohttp, asyncio
from .utils import save_json



async def fetch_paginated(url: str) -> any:
    all_results = []
    
    async with aiohttp.ClientSession() as session:
        while True:
            async with session.get(f"{url}") as response:
                response.raise_for_status()
                data = await response.json()
                all_results.extend(data.get("results"))
                if not data.get("next"):
                    break
                url = data.get("next")         
    
    save_json(all_results, "pagination", "paginated_posts.json")
    return all_results
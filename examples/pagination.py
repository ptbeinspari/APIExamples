import aiohttp, asyncio
from .utils import save_json


# If API has "next" implemented, async calls will function like sync. If API has "pages" we can construct list
# of URLS and call async, with high concurrency!

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
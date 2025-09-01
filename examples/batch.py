import asyncio
import aiohttp
from .utils import save_json

# Task method
async def fetch_json_and_save(session: aiohttp.ClientSession, base_url: str, id: int) -> dict:
    url = f"{base_url}/{id}"
    async with session.get(url) as response:
        response.raise_for_status()
        data = await response.json()
        save_json(data, "batch",f"item_{id}.json")
        return data

# For all id's in list, perform task
async def batch_fetch_ids(base_url: str, ids: list) -> any:
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_json_and_save(session, base_url, id) for id in ids]
        results = await asyncio.gather(*tasks)
        
        return results
                
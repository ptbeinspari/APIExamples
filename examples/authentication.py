import aiohttp, asyncio
from .utils import save_json

async def basic_auth_call(url: str, username: str, password: str) -> any:
    auth = aiohttp.BasicAuth(username, password)
    async with aiohttp.ClientSession(auth=auth) as session:
        async with session.get(url) as response:
            response.raise_for_status()
            data = await response.json()
            save_json(data, "authentication", "basic_auth_result.json")
            return data

async def oauth_call(url: str, token: str) -> any:
    headers = {"Authorization": f"Bearer {token}"}
    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get(url) as response:
            response.raise_for_status()
            data = await response.json()
            save_json(data, "authentication", "oauth_result.json")
            return data
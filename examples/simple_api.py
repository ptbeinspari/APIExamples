import aiohttp
from .utils import save_json

async def get(url: str, save_as: str) -> any:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            response.raise_for_status()
            data = await response.json()
            save_json(data, "simple_api", save_as)
            return data

async def post(url: str, payload: dict, save_as: str) -> any:
    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=payload) as response:
            response.raise_for_status()
            data = await response.json()
            save_json(data, "simple_api", save_as)
            return data
        






#For comparison
# import requests
# from .utils import save_json

# def get(url: str, save_as: str) -> any:
#     response = requests.get(url)
#     response.raise_for_status()
#     data = response.json()
#     save_json(data, "simple_api", save_as)
#     return data





    
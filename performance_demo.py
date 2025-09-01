
import asyncio
import time
import aiohttp
import requests

async def async_fetch(session: aiohttp.ClientSession, urls: list) -> list:
    tasks = []
    for url in urls:
        tasks.append(session.get(url))
    responses = await asyncio.gather(*tasks)
    return [await resp.json() for resp in responses]

def sync_fetch(urls: list) -> list:
    return [requests.get(url).json() for url in urls]

async def run_performance_comparison(num_requests):
    base_url = "https://jsonplaceholder.typicode.com/todos/"
    urls = [f"{base_url}{i}" for i in range(1, num_requests+1)]
    
    # Async timing
    start = time.perf_counter()
    async with aiohttp.ClientSession() as session:
        results = await async_fetch(session, urls)
    async_time = time.perf_counter() - start
    
    # Sync timing
    start = time.perf_counter()
    results = sync_fetch(urls)
    sync_time = time.perf_counter() - start
    
    return {
        "async_time": async_time,
        "sync_time": sync_time,
        "speedup": sync_time / async_time
    }


if __name__ == "__main__":

    # Example usage - Performance Demo
    # ---------------------------------------------------------------
    print("Running performance comparison demo ----------- (500 requests)...")
    results = asyncio.run(run_performance_comparison(500))
    print(f"Running performance comparison demo ----------- Async: {results['async_time']:.2f}s")
    print(f"Running performance comparison demo ----------- Sync: {results['sync_time']:.2f}s")
    print(f"Running performance comparison demo ----------- Speedup: {results['speedup']:.1f}x")
    # ---------------------------------------------------------------


    

    
    
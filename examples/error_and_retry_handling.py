import aiohttp
from tenacity import retry, retry_if_exception, stop_after_attempt, wait_exponential
from .utils import save_json

# Custom exceptions
class RetryableError(Exception):
    """Indicates an error that should trigger retries"""
    pass

# Status codes that should trigger retries
RETRYABLE_STATUS_CODES = {500, 502, 503, 504, 429}  # Server errors + rate limiting

@retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=2, max=10), retry=retry_if_exception(lambda e: isinstance(e, RetryableError)))
async def robust_api_call(url: str, timeout: int = 10) -> any:
    async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(total=timeout)) as session: # Raises TimeoutError if too long
        async with session.get(url) as response:
            status = response.status
            if status != 200:
                error_msg = f"HTTP {status} error"
                if status in RETRYABLE_STATUS_CODES:
                    raise RetryableError(error_msg)     # Will be retried
                else:
                    raise Exception(error_msg)          # Fails immediately
            
            data = await response.json()
            save_json(data, "error_and_retry_handling", "error_handling_result.json")
            return data
# Copilot Instructions - API Examples Collection

## Project Overview

This repository is an educational collection demonstrating various API interaction patterns in Python using async/await patterns. It serves as a reference implementation for common API scenarios including authentication, rate limiting, pagination, error handling, and performance comparisons.

## Build, Test, and Run Commands

### Installation
```bash
pip install -r requirements.txt
```

### Testing
```bash
# Run all tests with verbose output
pytest -v

# Run a single test file
pytest tests/test_simple_api.py -v

# Run a specific test function
pytest tests/test_simple_api.py::test_get_endpoint -v
```

### Running Examples
```bash
# Run all enabled demos (edit demo.py to enable/disable examples)
python demo.py

# Run performance comparison (async vs sync)
python demo_performance.py

# Run Fabric GraphQL example (requires Azure credentials)
python FabricGraphQLexample.py
```

## Architecture and Module Structure

### Core Pattern: Async-First with aiohttp
- **All examples modules** use `aiohttp` for async HTTP requests, not `requests`
- Functions are defined as `async def` and called with `asyncio.run()` or `await`
- Each module demonstrates one specific API pattern in isolation

### Module Organization
```
examples/
├── simple_api.py           # Basic GET/POST operations
├── authentication.py       # Basic Auth and OAuth/Bearer token patterns
├── rate_limiting.py        # Semaphore-based request rate control
├── pagination.py           # Following 'next' links to fetch all pages
├── batch.py                # Concurrent fetching of multiple IDs
├── error_and_retry_handling.py  # Tenacity-based retry logic
└── utils.py                # Shared save_json helper

tests/
└── test_*.py               # Mirror structure of examples/
```

### Data Persistence Pattern
- All API responses are saved to `data/{module_name}/{filename}.json` via `utils.save_json()`
- The `save_json()` helper automatically creates nested directories
- Each example module saves to its own subfolder (e.g., `data/simple_api/`, `data/batch/`)

### Demo File Pattern
- `demo.py`: Commented examples showing how to use each module. Uncomment sections to run
- Most examples are commented out by default to avoid rate limits during development
- Each example is self-contained and can be run independently

## Key Conventions

### Async Context Managers
Always use async context managers for aiohttp sessions:
```python
async with aiohttp.ClientSession() as session:
    async with session.get(url) as response:
        data = await response.json()
```

### Error Handling with Tenacity
Retries use the `tenacity` library with exponential backoff:
- Custom `RetryableError` exception for retryable errors (5xx, 429)
- Non-retryable errors (4xx except 429) fail immediately
- Pattern: `@retry(stop=stop_after_attempt(3), wait=wait_exponential(...))`

### Rate Limiting Implementation
Use `asyncio.Semaphore` combined with `asyncio.sleep()`:
```python
semaphore = asyncio.Semaphore(calls_per_second)
async with semaphore:
    await asyncio.sleep(1.0/calls_per_second)
    # Make request
```

### Pagination Pattern
Follow `next` URL in responses until None:
```python
while True:
    data = await response.json()
    all_results.extend(data.get("results"))
    if not data.get("next"):
        break
    url = data.get("next")
```

### Batch Processing
Use `asyncio.gather()` to execute multiple coroutines concurrently:
```python
tasks = [fetch_item(session, id) for id in ids]
results = await asyncio.gather(*tasks)
```

## Testing Approach

- Tests use real API endpoints (pokeapi.co, jsonplaceholder.typicode.com)
- Tests are marked with `@pytest.mark.asyncio` for async test execution
- Tests verify both API responses and file persistence
- No mocking - tests make actual HTTP calls to public test APIs

## Special Files

### FabricGraphQLexample.py
- Demonstrates Azure Fabric GraphQL API authentication using OAuth 2.0 client credentials flow
- Requires credentials: `tenant_id`, `client_id`, `client_secret` (stored in keyvault)
- Uses `azure-identity` for token acquisition
- Pattern: Request token → Use bearer token in headers → Execute GraphQL query

### demo_performance.py
- Compares async vs sync performance for large request batches
- Demonstrates the speedup achieved with concurrent async requests
- Default: 1500 requests showing ~10-20x speedup

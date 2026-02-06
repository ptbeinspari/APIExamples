import pytest
import asyncio
from unittest.mock import patch, AsyncMock, Mock
from examples import rate_limiting

@pytest.mark.asyncio
@patch('aiohttp.ClientSession.get')
@patch('asyncio.sleep', new_callable=AsyncMock)
async def test_rate_limiting(mock_sleep, mock_get):
    mock_resp = Mock()
    mock_resp.raise_for_status = Mock()
    mock_resp.json = AsyncMock(return_value={'id': 1})
    mock_get.return_value.__aenter__.return_value = mock_resp

    rate_calls_per_sec = 5 
    num_calls = 20
    
    urls = [f"https://jsonplaceholder.typicode.com/todos/{i}" for i in range(1, num_calls+1)]
    await rate_limiting.rate_limited_calls(urls, rate_calls_per_sec)
    
    assert mock_get.call_count == len(urls)
    assert mock_sleep.call_count == len(urls)

    # Verify sleep duration is approximately 0.2s for 5 req/s
    for call in mock_sleep.call_args_list:
        assert 0.1 <= call.args[0] <= 0.3
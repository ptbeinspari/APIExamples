import pytest
import aiohttp
from unittest.mock import patch, AsyncMock
from tenacity import RetryError
from examples import error_and_retry_handling

@pytest.mark.asyncio
@patch('aiohttp.ClientSession.get')
async def test_error_and_retry_handling_success(mock_get):
    mock_resp = AsyncMock()
    mock_resp.status = 200
    mock_resp.json.return_value = {'data': 'ok'}
    mock_get.return_value.__aenter__.return_value = mock_resp
    
    await error_and_retry_handling.robust_api_call("http://test.com")
    
    assert mock_get.call_count == 1

@pytest.mark.asyncio
@patch('aiohttp.ClientSession.get')
async def test_error_and_retry_handling_retry(mock_get):
    mock_resp = AsyncMock()
    mock_resp.status = 500
    mock_get.return_value.__aenter__.return_value = mock_resp
    
    with pytest.raises(RetryError):
        await error_and_retry_handling.robust_api_call("http://test.com")
    
    assert mock_get.call_count == 3


@pytest.mark.asyncio
@patch('aiohttp.ClientSession.get')
async def test_error_and_retry_handling_no_retry_error(mock_get):
    """Test that non-retryable status codes fail immediately"""
    mock_resp = AsyncMock()
    mock_resp.status = 404  # Not in RETRYABLE_STATUS_CODES
    mock_get.return_value.__aenter__.return_value = mock_resp
    
    with pytest.raises(Exception):
        await error_and_retry_handling.robust_api_call("http://test.com")
    
    # Should fail immediately (1 attempt)
    assert mock_get.call_count == 1
